import pandas as pd
from db.models import DetailedEvent, Event, Session, DATABASE

dtypes_events = {
    'sessionid': "Int64",
    'connectioninformation_downlink': "Int64",
    'connectioninformation_type': "string",
    'consolelog_level': "string",
    'consolelog_value': "string",
    'customevent_name': "string",
    'customevent_payload': "string",
    'jsexception_message': "string",
    'jsexception_name': "string",
    'jsexception_payload': "string",
    'jsexception_metadata': "string",
    'metadata_key': "string",
    'metadata_value': "string",
    'networkrequest_type': "string",
    'networkrequest_method': "string",
    'networkrequest_url': "string",
    'networkrequest_request': "string",
    'networkrequest_response': "string",
    'networkrequest_status': "Int64",
    'networkrequest_timestamp': "Int64",
    'networkrequest_duration': "Int64",
    'mouseclick_id': "Int64",
    'mouseclick_hesitationtime': "Int64",
    'mouseclick_label': "string",
    'pageevent_firstcontentfulpaint': "Int64",
    'pageevent_firstpaint': "Int64",
    'pageevent_messageid': "Int64",
    'pageevent_referrer': "string",
    'pageevent_speedindex': "Int64",
    'pageevent_timestamp': "Int64",
    'pageevent_url': "string",
    'pagerendertiming_timetointeractive': "Int64",
    'pagerendertiming_visuallycomplete': "Int64",
    'integrationevent_timestamp': "Int64",
    'integrationevent_source': "string",
    'integrationevent_name': "string",
    'integrationevent_message': "string",
    'integrationevent_payload': "string",
    'setviewportsize_height': "Int64",
    'setviewportsize_width': "Int64",
    'timestamp_timestamp': "Int64",
    'user_anonymous_id': "string",
    'user_id': "string",
    'issueevent_message_id': "Int64",
    'issueevent_timestamp': "Int64",
    'issueevent_type': "string",
    'issueevent_context_string': "string",
    'issueevent_context': "string",
    'issueevent_payload': "string",
    'customissue_name': "string",
    'customissue_payload': "string",
    'received_at': "Int64",
    'batch_order_number': "Int64"}
dtypes_detailed_events = {
    'sessionid': "Int64",
    'adoptedssreplaceurlbased_sheet_id': "Int64",
    'adoptedssreplaceurlbased_text': "string",
    'adoptedssreplaceurlbased_base_url': "string",
    'adoptedssreplace_sheet_id': "Int64",
    'adoptedssreplace_text': "string",
    'adoptedssinsertruleurlbased_sheet_id': "Int64",
    'adoptedssinsertruleurlbased_rule': "string",
    'adoptedssinsertruleurlbased_index': "Int64",
    'adoptedssinsertruleurlbased_base_url': "string",
    'adoptedssinsertrule_sheet_id': "Int64",
    'adoptedssinsertrule_rule': "string",
    'adoptedssinsertrule_index': "Int64",
    'adoptedssdeleterule_sheet_id': "Int64",
    'adoptedssdeleterule_index': "Int64",
    'adoptedssaddowner_sheet_id': "Int64",
    'adoptedssaddowner_id': "Int64",
    'adoptedssremoveowner_sheet_id': "Int64",
    'adoptedssremoveowner_id': "Int64",
    'clickevent_hesitationtime': "Int64",
    'clickevent_label': "string",
    'clickevent_messageid': "Int64",
    'clickevent_timestamp': "Int64",
    'connectioninformation_downlink': "Int64",
    'connectioninformation_type': "string",
    'consolelog_level': "string",
    'consolelog_value': "string",
    'cpuissue_duration': "Int64",
    'cpuissue_rate': "Int64",
    'cpuissue_timestamp': "Int64",
    'createdocument': 'boolean',
    'createelementnode_id': "Int64",
    'createelementnode_parentid': "Int64",
    'cssdeleterule_index': "Int64",
    'cssdeleterule_stylesheetid': "Int64",
    'cssinsertrule_index': "Int64",
    'cssinsertrule_rule': "string",
    'cssinsertrule_stylesheetid': "Int64",
    'customevent_name': "string",
    'customevent_payload': "string",
    'fetch_duration': "Int64",
    'fetch_method': "string",
    'fetch_request': "string",
    'fetch_response': "string",
    'fetch_status': "Int64",
    'fetch_timestamp': "Int64",
    'fetch_url': "string",
    'graphql_operationkind': "string",
    'graphql_operationname': "string",
    'graphql_response': "string",
    'graphql_variables': "string",
    'inputevent_label': "string",
    'inputevent_messageid': "Int64",
    'inputevent_timestamp': "Int64",
    'inputevent_value': "string",
    'inputevent_valuemasked': 'boolean',
    'inputchange_id': "Int64",
    'inputchange_value': "string",
    'inputchange_value_masked': 'boolean',
    'inputchange_label': "string",
    'inputchange_hesitation_time': "Int64",
    'inputchange_input_duration': "Int64",
    'jsexception_message': "string",
    'jsexception_name': "string",
    'jsexception_payload': "string",
    'jsexception_metadata': "string",
    'memoryissue_duration': "Int64",
    'memoryissue_rate': "Int64",
    'memoryissue_timestamp': "Int64",
    'metadata_key': "string",
    'metadata_value': "string",
    'mobx_payload': "string",
    'mobx_type': "string",
    'mouseclick_id': "Int64",
    'mouseclick_hesitationtime': "Int64",
    'mouseclick_label': "string",
    'mousemove_x': "Int64",
    'mousemove_y': "Int64",
    'movenode_id': "Int64",
    'movenode_index': "Int64",
    'movenode_parentid': "Int64",
    'mousethrashing_timestamp': "Int64",
    'networkrequest_type': "string",
    'networkrequest_method': "string",
    'networkrequest_url': "string",
    'networkrequest_request': "string",
    'networkrequest_response': "string",
    'networkrequest_status': "Int64",
    'networkrequest_timestamp': "Int64",
    'networkrequest_duration': "Int64",
    'ngrx_action': "string",
    'ngrx_duration': "Int64",
    'ngrx_state': "string",
    'otable_key': "string",
    'otable_value': "string",
    'pageevent_domcontentloadedeventend': "Int64",
    'pageevent_domcontentloadedeventstart': "Int64",
    'pageevent_firstcontentfulpaint': "Int64",
    'pageevent_firstpaint': "Int64",
    'pageevent_loaded': 'boolean',
    'pageevent_loadeventend': "Int64",
    'pageevent_loadeventstart': "Int64",
    'pageevent_messageid': "Int64",
    'pageevent_referrer': "string",
    'pageevent_requeststart': "Int64",
    'pageevent_responseend': "Int64",
    'pageevent_responsestart': "Int64",
    'pageevent_speedindex': "Int64",
    'pageevent_timestamp': "Int64",
    'pageevent_url': "string",
    'pageloadtiming_domcontentloadedeventend': "Int64",
    'pageloadtiming_domcontentloadedeventstart': "Int64",
    'pageloadtiming_firstcontentfulpaint': "Int64",
    'pageloadtiming_firstpaint': "Int64",
    'pageloadtiming_loadeventend': "Int64",
    'pageloadtiming_loadeventstart': "Int64",
    'pageloadtiming_requeststart': "Int64",
    'pageloadtiming_responseend': "Int64",
    'pageloadtiming_responsestart': "Int64",
    'pagerendertiming_speedindex': "Int64",
    'pagerendertiming_timetointeractive': "Int64",
    'pagerendertiming_visuallycomplete': "Int64",
    'partitionedmessage_part_no': "Int64",
    'partitionedmessage_part_total': "Int64",
    'performancetrack_frames': "Int64",
    'performancetrack_ticks': "Int64",
    'performancetrack_totaljsheapsize': "Int64",
    'performancetrack_usedjsheapsize': "Int64",
    'performancetrackaggr_avgcpu': "Int64",
    'performancetrackaggr_avgfps': "Int64",
    'performancetrackaggr_avgtotaljsheapsize': "Int64",
    'performancetrackaggr_avgusedjsheapsize': "Int64",
    'performancetrackaggr_maxcpu': "Int64",
    'performancetrackaggr_maxfps': "Int64",
    'performancetrackaggr_maxtotaljsheapsize': "Int64",
    'performancetrackaggr_maxusedjsheapsize': "Int64",
    'performancetrackaggr_mincpu': "Int64",
    'performancetrackaggr_minfps': "Int64",
    'performancetrackaggr_mintotaljsheapsize': "Int64",
    'performancetrackaggr_minusedjsheapsize': "Int64",
    'performancetrackaggr_timestampend': "Int64",
    'performancetrackaggr_timestampstart': "Int64",
    'profiler_args': "string",
    'profiler_duration': "Int64",
    'profiler_name': "string",
    'profiler_result': "string",
    'integrationevent_timestamp': "Int64",
    'integrationevent_source': "string",
    'integrationevent_name': "string",
    'integrationevent_message': "string",
    'integrationevent_payload': "string",
    'rawerrorevent_message': "string",
    'rawerrorevent_name': "string",
    'rawerrorevent_payload': "string",
    'rawerrorevent_source': "string",
    'rawerrorevent_timestamp': "Int64",
    'redux_action': "string",
    'redux_duration': "Int64",
    'redux_state': "string",
    'removenode_id': "Int64",
    'removenodeattribute_id': "Int64",
    'removenodeattribute_name': "string",
    'resourceevent_decodedbodysize': "Int64",
    'resourceevent_duration': "Int64",
    'resourceevent_encodedbodysize': "Int64",
    'resourceevent_headersize': "Int64",
    'resourceevent_messageid': "Int64",
    'resourceevent_method': "string",
    'resourceevent_status': "Int64",
    'resourceevent_success': 'boolean',
    'resourceevent_timestamp': "Int64",
    'resourceevent_ttfb': "Int64",
    'resourceevent_type': "string",
    'resourceevent_url': "string",
    'resourcetiming_timestamp': "Int64",
    'resourcetiming_duration': "Int64",
    'resourcetiming_ttfb': "Int64",
    'resourcetiming_header_size': "Int64",
    'resourcetiming_encoded_body_size': "Int64",
    'resourcetiming_decoded_body_size': "Int64",
    'resourcetiming_url': "string",
    'resourcetiming_initiator': "string",
    'resourcetiming_transferred_size': "Int64",
    'resourcetiming_cached': 'boolean',
    'selectionchange_selection_start': "Int64",
    'selectionchange_selection_end': "Int64",
    'selectionchange_selection': "string",
    'sessiondisconnect': 'boolean',
    'sessiondisconnect_timestamp': "Int64",
    'sessionend_timestamp': "Int64",
    'sessionend_encryption_key': "string",
    'sessionsearch_timestamp': "Int64",
    'sessionsearch_partition': "Int64",
    'sessionstart_projectid': "Int64",
    'sessionstart_revid': "string",
    'sessionstart_timestamp': "Int64",
    'sessionstart_trackerversion': "string",
    'sessionstart_useragent': "string",
    'sessionstart_userbrowser': "string",
    'sessionstart_userbrowserversion': "string",
    'sessionstart_usercountry': "string",
    'sessionstart_userdevice': "string",
    'sessionstart_userdeviceheapsize': "Int64",
    'sessionstart_userdevicememorysize': "Int64",
    'sessionstart_userdevicetype': "string",
    'sessionstart_useros': "string",
    'sessionstart_userosversion': "string",
    'sessionstart_useruuid': "string",
    'setcssdata_data': "Int64",
    'setcssdata_id': "Int64",
    'setinputchecked_checked': "Int64",
    'setinputchecked_id': "Int64",
    'setinputtarget_id': "Int64",
    'setinputtarget_label': "Int64",
    'setinputvalue_id': "Int64",
    'setinputvalue_mask': "Int64",
    'setinputvalue_value': "Int64",
    'setnodeattribute_id': "Int64",
    'setnodeattribute_name': "Int64",
    'setnodeattribute_value': "Int64",
    'setnodedata_data': "Int64",
    'setnodedata_id': "Int64",
    'setnodescroll_id': "Int64",
    'setnodescroll_x': "Int64",
    'setnodescroll_y': "Int64",
    'setpagelocation_navigationstart': "Int64",
    'setpagelocation_referrer': "string",
    'setpagelocation_url': "string",
    'setpagevisibility_hidden': 'boolean',
    'setviewportscroll_x': "Int64",
    'setviewportscroll_y': "Int64",
    'setviewportsize_height': "Int64",
    'setviewportsize_width': "Int64",
    'stateaction_type': "string",
    'stateactionevent_messageid': "Int64",
    'stateactionevent_timestamp': "Int64",
    'stateactionevent_type': "string",
    'timestamp_timestamp': "Int64",
    'unbindnodes_total_removed_percent': "Int64",
    'useranonymousid_id': "string",
    'userid_id': "string",
    'vuex_mutation': "string",
    'vuex_state': "string",
    'loadfontface_parent_id': "Int64",
    'loadfontface_family': "string",
    'loadfontface_source': "string",
    'loadfontface_descriptors': "string",
    'longtasks_timestamp': "Int64",
    'longtasks_duration': "Int64",
    'longtasks_context': "Int64",
    'longtasks_containertype': "Int64",
    'longtasks_containersrc': "string",
    'longtasks_containerid': "string",
    'longtasks_containername': "Int64",
    'setnodeattributedict_id': "Int64",
    'setnodeattributedict_name_key': "Int64",
    'setnodeattributedict_value_key': "Int64",
    'issueevent_message_id': "Int64",
    'issueevent_timestamp': "Int64",
    'issueevent_type': "string",
    'issueevent_context_string': "string",
    'issueevent_context': "string",
    'issueevent_payload': "string",
    'issueevent_url': "string",
    'technicalinfo_type': "string",
    'technicalinfo_value': "string",
    'zustand_mutation': "string",
    'zustand_state': "string",
    'customissue_name': "string",
    'customissue_payload': "string",
    'received_at': "Int64",
    'batch_order_number': "Int64"
}
dtypes_sessions = {'sessionid': "Int64",
                   'user_agent': "string",
                   'user_browser': "string",
                   'user_browser_version': "string",
                   'user_country': "string",
                   'user_device': "string",
                   'user_device_heap_size': "Int64",
                   'user_device_memory_size': "Int64",
                   'user_device_type': "string",
                   'user_os': "string",
                   'user_os_version': "string",
                   'user_uuid': "string",
                   'connection_effective_bandwidth': "Int64",
                   'connection_type': "string",
                   'metadata_key': "string",
                   'metadata_value': "string",
                   'referrer': "string",
                   'user_anonymous_id': "string",
                   'user_id': "string",
                   'session_start_timestamp': "Int64",
                   'session_end_timestamp': "Int64",
                   'session_duration': "Int64",
                   'first_contentful_paint': "Int64",
                   'speed_index': "Int64",
                   'visually_complete': "Int64",
                   'timing_time_to_interactive': "Int64",
                   'avg_cpu': "Int64",
                   'avg_fps': "Int64",
                   'max_cpu': "Int64",
                   'max_fps': "Int64",
                   'max_total_js_heap_size': "Int64",
                   'max_used_js_heap_size': "Int64",
                   'js_exceptions_count': "Int64",
                   'long_tasks_total_duration': "Int64",
                   'long_tasks_max_duration': "Int64",
                   'long_tasks_count': "Int64",
                   'inputs_count': "Int64",
                   'clicks_count': "Int64",
                   'issues_count': "Int64",
                   'issues': "string",
                   'urls_count': "Int64",
                   'urls': "string"}

if DATABASE == 'bigquery':
    dtypes_sessions['urls'] = "string"
    dtypes_sessions['issues'] = "string"

detailed_events_col = []
for col in DetailedEvent.__dict__:
    if not col.startswith('_'):
        detailed_events_col.append(col)

events_col = []
for col in Event.__dict__:
    if not col.startswith('_'):
        events_col.append(col)

sessions_col = []
for col in Session.__dict__:
    if not col.startswith('_'):
        sessions_col.append(col)


def get_df_from_batch(batch, level):
    if level == 'normal':
        df = pd.DataFrame([b.__dict__ for b in batch], columns=events_col)
    if level == 'detailed':
        df = pd.DataFrame([b.__dict__ for b in batch], columns=detailed_events_col)
    if level == 'sessions':
        df = pd.DataFrame([b.__dict__ for b in batch], columns=sessions_col)

    try:
        df = df.drop('_sa_instance_state', axis=1)
    except KeyError:
        pass

    if level == 'normal':
        df = df.astype(dtypes_events)
    if level == 'detailed':
        df['inputevent_value'] = None
        df['customevent_payload'] = None
        df = df.astype(dtypes_detailed_events)
    if level == 'sessions':
        df = df.astype(dtypes_sessions)

    if DATABASE == 'clickhouse' and level == 'sessions':
        df['issues'] = df['issues'].fillna('')
        df['urls'] = df['urls'].fillna('')

    for x in df.columns:
        try:
            if df[x].dtype == "string" or df[x].dtype == "object":
                df[x] = df[x].fillna('')
                df[x] = df[x].str.slice(0, 255)
                df[x] = df[x].str.replace("|", "")
        except TypeError as e:
            print(repr(e))
            if df[x].dtype == 'str':
                df[x] = df[x].str.slice(0, 255)
                df[x] = df[x].str.replace("|", "")
    return df
