import React, { Component } from "react";
import "./posthandler.css";

class postHandler extends Component {
  constructor(props) {
    super(props);

    this.state = {
      posts: [],
    };
  }

  componentDidMount() {
    fetch("https://hackjaipur.herokuapp.com/post/list")
      .then((response) => response.json())
      .then((data) => {
        var title = data.results.map((res) => res);
        this.setState({ posts: title });
      });
  }

  render() {
    return (
      <div>
        <div className="posts">
          <h2 className="">Latest Posts</h2>
          <ul>
            {/* {this.state.comp.map((post) => (
              <CompBox
                key={post.id}
                title={post.topic}
                desc={post.desc}
                time={post.time}
                date={post.date}
                link={post.link}
              ></CompBox>
            ))} */}
          </ul>
        </div>
      </div>
    );
  }
}

export default postHandler;
