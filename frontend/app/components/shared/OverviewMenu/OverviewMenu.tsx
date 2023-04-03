import React from 'react';
import { SideMenuitem } from 'UI';
import { connect } from 'react-redux';
import { setActiveTab } from 'Duck/search';
import { withRouter, RouteComponentProps } from 'react-router-dom';
import { sessions, fflags, withSiteId } from "App/routes";

interface Props {
  setActiveTab: (tab: any) => void;
  activeTab: string;
  isEnterprise: boolean;
}
function OverviewMenu(props: Props & RouteComponentProps) {
  // @ts-ignore
  const { activeTab, isEnterprise, history, match: { params: { siteId } }, location } = props;

  return (
    <div className={"flex flex-col gap-2 w-full"}>
      <div className="w-full">
        <SideMenuitem
          active={activeTab === 'all'}
          id="menu-sessions"
          title="Sessions"
          iconName="play-circle-bold"
          onClick={() => {
            props.setActiveTab({ type: 'all' })
            !location.pathname.includes(sessions()) && history.push(withSiteId(sessions(), siteId))
          }}
        />
      </div>
      <div className="w-full">
        <SideMenuitem
          active={activeTab === 'bookmark'}
          id="menu-bookmarks"
          title={`${isEnterprise ? 'Vault' : 'Bookmarks'}`}
          iconName={ isEnterprise ? "safe" : "star" }
          onClick={() => {
            props.setActiveTab({ type: 'bookmark' })
            !location.pathname.includes(sessions()) && history.push(withSiteId(sessions(), siteId))
          }}
        />
      </div>
      <div className="w-full">
        <SideMenuitem
          active={activeTab === 'notes'}
          id="menu-notes"
          title="Notes"
          iconName="stickies"
          onClick={() => {
            props.setActiveTab({ type: 'notes' })
            !location.pathname.includes(sessions()) && history.push(withSiteId(sessions(), siteId))
          }}
        />
      </div>
      <div className="w-full">
        <SideMenuitem
          active={activeTab === 'flags'}
          id="menu-flags"
          title="Feature Flags"
          iconName="toggles"
          onClick={() => {
            props.setActiveTab({ type: 'flags' })
            !location.pathname.includes(fflags()) && history.push(withSiteId(fflags(), siteId))
          }}
        />
      </div>
    </div>
  );
}

export default connect((state: any) => ({
    activeTab: state.getIn(['search', 'activeTab', 'type']),
    isEnterprise: state.getIn(['user', 'account', 'edition']) === 'ee',
}), { setActiveTab })(withRouter(OverviewMenu));
