import React, { Component } from "react";
import "./groupsstyle.css";
import CompBox from "../../components/competitionBox/competitionBoc";

class groupscomponent extends Component {
  constructor(props) {
    super(props);

    this.state = {
      comp: [],
      groups: [],
    };
  }

  componentDidMount() {
    fetch("https://hackjaipur.herokuapp.com/competitions/")
      .then((response) => response.json())
      .then((data) => {
        var title = data.results.map((res) => res);
        this.setState({ comp: title });
      });

    fetch("https://hackjaipur.herokuapp.com/groups/")
      .then((response) => response.json())
      .then((data) => {
        var title = data.results.map((res) => res);
        this.setState({ groups: title });
      });
  }

  render() {
    return (
      <div>
        <div className="row">
          <div className="col-3">
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
          <div className="col-9">
            <h1>Groups</h1>
            <ul>
              {this.state.groups.map((post) => (
                <div className="groups">
                  <a href="#">
                    <h1>{post.title}</h1>
                  </a>
                  <p>{post.description}</p>
                </div>
              ))}
            </ul>
          </div>
        </div>
      </div>
    );
  }
}

export default groupscomponent;
