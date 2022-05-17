import cn from 'classnames';
import { Button } from 'UI';
import stl from './table.css';

export default class Table extends React.PureComponent {
  state = { showAll: false };

  onLoadMoreClick = () => {
    this.setState({ showAll: true });
  }

  render() {
    const {
      cols,
      rows = [],
      rowProps,
      rowClass = '',
      small = false,
      compare = false,
      maxHeight = 200,
      onRowClick = null,
      isTemplate,
    } = this.props;
    const { showAll } = this.state;

    return (
      <div className="w-full">
        <div className="flex">
          {
            cols.map(({
              key, title, width,
            }) =>
              <div key={ key } style={ { width } } className={ stl.header }>{ title }</div>)
          }
        </div>
        <div className={ cn(stl.content, "thin-scrollbar") } style={{ maxHeight: maxHeight + 'px'}}>
          { rows.take(showAll ? rows.size : (small ? 3 : 5)).map(row => (
            <div
              className={ cn(rowClass, stl.row, { [stl.small]: small, 'cursor-pointer' : !!onRowClick}) }
              key={ row.key }
              onClick={onRowClick ? (e) => onRowClick(e, row) : () => null}
            >
              { cols.map(({ cellClass = '', className = '', Component, key, toText = t => t, width }) => (
                <div className={ cn(stl.cell, cellClass) } style={{ width }} key={ key }> { Component
                  ? <Component compare={compare} data={ row } { ...rowProps } />
                  : <div className={ cn(stl.text, className) }> { toText(row[ key ]) } </div>
                  }
                </div>
              )) }
            </div>
          )) }
        </div>
        { !isTemplate && rows.size > (small ? 3 : 5) && !showAll &&
            <div className="w-full flex justify-center">
              <Button
                onClick={ this.onLoadMoreClick }
                plain
                small
                className="text-center"
              >
                { rows.size + ' More' }
              </Button>
            </div>
          }
      </div>
    );
  }
}
