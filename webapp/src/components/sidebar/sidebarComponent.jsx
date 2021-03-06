import React, { Component } from "react";
import "./sidebarStyle.css";
import CompBox from "../competitionBox/competitionBoc";

class sidebarComponent extends Component {
  constructor(props) {
    super(props);
    this.state = {
      comp: [],
    };
  }

  componentDidMount() {
    fetch("https://hackjaipur.herokuapp.com/competitions/")
      .then((response) => response.json())
      .then((data) => {
        var title = data.results.map((res) => res);
        this.setState({ comp: title });
      });
  }

  render() {
    return (
      <div>
        <div className="side_border">
          <h2 className="comph2">Competitions</h2>
          <ul>
            {this.state.comp.map((post) => (
              <CompBox
                key={post.id}
                title={post.topic}
                desc={post.desc}
                time={post.time}
                date={post.date}
                link={post.link}
              ></CompBox>
            ))}
          </ul>
        </div>
      </div>
    );
  }
}

export default sidebarComponent;
