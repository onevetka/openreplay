from datetime import timedelta
from textwrap import dedent

import pendulum

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator, ShortCircuitOperator
from airflow.sensors.python import PythonSensor
from decouple import config
import os
_work_dir = os.getcwd()


def false_func():
    return False

def example_airflow_db():
    from airflow.settings import Session
    with Session() as conn:
        cur = conn.execute('SELECT * FROM dag LIMIT 5')
        res = cur.fetchall()
    return res


def example_mlflow(ti):
    import mlflow
    import hashlib
    client = mlflow.MlflowClient()
    models = [model.name for model in client.search_registered_models()]
    print(models)
    projects = ti.xcom_pull(key='project_data').split(' ')
    tenants = ti.xcom_pull(key='tenant_data').split(' ')
    new_projects = list()
    old_projects = list()
    new_tenants = list()
    old_tenants = list()
    for i in range(len(projects)):
        hashed = hashlib.sha256(bytes(f'{projects[i]}-{tenants[i]}'.encode('utf-8'))).hexdigest()
        _model_name = f'{hashed}-RecModel'
        if _model_name in models:
            old_projects.append(projects[i])
            old_tenants.append(tenants[i])
        else:
            new_projects.append(projects[i])
            new_tenants.append(tenants[i])
    ti.xcom_push(key='new_project_data', value=' '.join(new_projects))
    ti.xcom_push(key='new_tenant_data', value=' '.join(new_tenants))
    ti.xcom_push(key='old_project_data', value=' '.join(old_projects))
    ti.xcom_push(key='old_tenant_data', value=' '.join(old_tenants))



def continue_new(ti):
    L = ti.xcom_pull(key='new_project_data')
    if len(L) == 0:
        return False
    else:
        return True


def continue_old(ti):
    L = ti.xcom_pull(key='old_project_data')
    if len(L) == 0:
        return False
    else:
        return True


def my_function():
    l = os.listdir()
    print(l)
    print(f'AWS {config("AWS_ACCESS_KEY_ID", default="NotFound")}')
    return l


def status():
    # SELECT dag_id, execution_date, state FROM airflow.dag_run;
    pass


def get_funtions(ti):
    import sys
    sys.path.insert(1, _work_dir)
    import asyncio
    import os
    os.environ['PG_POOL'] = 'true'
    from utils import pg_client
    asyncio.run(pg_client.init())
    with pg_client.PostgresClient() as conn:
        conn.execute("""SELECT tenant_id, T1.project_id as project_id FROM (
    (SELECT project_id, count(*) as n_events FROM frontend_signals GROUP BY project_id ORDER BY n_events DESC) AS T1
        INNER JOIN (SELECT project_id, tenant_id FROM projects) AS T2 ON T1.project_id = T2.project_id)""")
        res = conn.fetchall()
    projects = list()
    tenants = list()
    for e in res:
        projects.append(str(e['project_id']))
        tenants.append(str(e['tenant_id']))
    asyncio.run(pg_client.terminate())
    #task_instance = kwargs['task_instance']
    #task_instance.xcom_push(key='project_data', value=' '.join(values))
    #ti.xcom_push(key='new_project_data', value=' '.join([]))
    #ti.xcom_push(key='new_tenant_data', value=' '.join([]))
    ti.xcom_push(key='project_data', value=' '.join(projects))
    ti.xcom_push(key='tenant_data', value=' '.join(tenants))
    #XCom.serialize_value(value=' '.join(values), key='project_data', task_id='FirstTest')
    #return res


dag = DAG(
    "first_test",
    default_args={
        "retries": 1,
        "retry_delay": timedelta(minutes=3),
    },
    start_date=pendulum.datetime(2015, 12, 1, tz="UTC"),
    description="My first test",
    schedule=config('crons_train', default='@daily'),
    catchup=False,
)


#assigning the task for our dag to do
with dag:
    split = PythonOperator(
        task_id='Split_Create_and_Retrain',
        provide_context=True,
        python_callable=example_mlflow,
        do_xcom_push=True
    )

    select_vp = PythonOperator(
        task_id='Select_Valid_Projects',
        provide_context=True,
        python_callable=get_funtions,
        do_xcom_push=True
    )

    dag_split1 = ShortCircuitOperator(
        task_id='Create_Condition',
        python_callable=continue_new,
    )

    dag_split2 = ShortCircuitOperator(
        task_id='Retrain_Condition',
        python_callable=false_func,
    )

    new_models = BashOperator(
        task_id='Create_Models',
        bash_command=f"python {_work_dir}/main.py "+"--projects {{task_instance.xcom_pull(task_ids='Split_Create_and_Retrain', key='new_project_data')}} " +
                     "--tenants {{task_instance.xcom_pull(task_ids='Split_Create_and_Retrain', key='new_tenant_data')}}",
    )

    old_models = BashOperator(
        task_id='Retrain_Models',
        bash_command=f"python {_work_dir}/main.py " + "--projects {{task_instance.xcom_pull(task_ids='Split_Create_and_Retrain', key='old_project_data')}} " +
                     "--tenants {{task_instance.xcom_pull(task_ids='Split_Create_and_Retrain', key='old_tenant_data')}}",
    )

    select_vp >> split >> [dag_split1, dag_split2]
    dag_split1 >> new_models
    dag_split2 >> old_models
