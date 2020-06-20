import React, { Component } from "react";
import SideBar from "../../components/sidebar/sidebarComponent";
import PostHandler from "../../components/postHandler/postHandler";
class homepageComponent extends Component {
  render() {
    return (
      <div>
        <div className="row">
          <div className="col-3">
            <SideBar />
          </div>
          <div className="col-9">
            <PostHandler />
          </div>
        </div>
      </div>
    );
  }
}

export default homepageComponent;
