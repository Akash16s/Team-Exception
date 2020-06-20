import React, { Component } from "react";
import "./posthandler.css";
import PostComp from "../postComponent/postcomp";

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
            {this.state.posts.map((post) => (
              <PostComp
                key={post.id}
                id={post.id}
                title={post.title}
                body={post.body}
                type={post.postType}
                date={post.creationDate}
                tags={post.tags}
                score={post.score}
              />
            ))}
          </ul>
        </div>
      </div>
    );
  }
}

export default postHandler;
