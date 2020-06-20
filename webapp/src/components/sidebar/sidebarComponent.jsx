import React, { Component } from "react";
import "./sidebarStyle.css";

class sidebarComponent extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  componentDidMount() {
    fetch("https://hackjaipur.herokuapp.com/post/list/")
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
      });
  }

  render() {
    return (
      <div>
        <div className="row">
          <div className="col-2">
            <div className="side_border">sdsd</div>
          </div>
          <div className="col-10">
            <div className="side_border">sdsd</div>
          </div>
        </div>
      </div>
    );
  }
}

export default sidebarComponent;
