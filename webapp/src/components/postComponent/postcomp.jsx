import React, { Component } from "react";
import "./postcomp.css";

class postcomp extends Component {
  constructor(props) {
    super(props);

    this.state = {
      comment: "",
      commentList: [],
    };
  }

  handleCommentCHange = (event) => {
    this.setState({
      comment: event.target.value,
    });
  };

  handleSubmit = (event) => {
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        message: this.state.comment,
        postId: this.props.id,
      }),
    };
    fetch(
      "https://hackjaipur.herokuapp.com/post/comment/",
      requestOptions
    ).then((response) => response.json());
  };

  componentDidMount() {
    fetch(
      "https://hackjaipur.herokuapp.com/post/comment/?postId=" + this.props.id
    )
      .then((response) => response.json())
      .then((data) => {
        var title = data.results.map((res) => res);
        this.setState({ commentList: title });
      });
  }

  render() {
    return (
      <div>
        <div className="innerpost">
          <div className="row">
            <div className="col-8">
              <h4>{this.props.title}</h4>
              <p>{this.props.body}</p>
            </div>
            <div className="col-4">
              <p>Score: {this.props.score}</p>
            </div>
          </div>
        </div>

        {/* comment */}
        {this.state.commentList.map((post) => (
          <h6>{post.message}</h6>
        ))}

        <form onSubmit={this.handleSubmit}>
          <label>Comment :</label>
          <input
            className="comment_input"
            type="text"
            value={this.state.comment}
            onChange={this.handleCommentCHange}
          />
          <button className="btn btn-primary" type="submit">
            submit
          </button>
        </form>
      </div>
    );
  }
}

export default postcomp;
