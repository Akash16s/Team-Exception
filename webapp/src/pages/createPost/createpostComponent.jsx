import React, { Component } from "react";
import "./createpoststyle.css";
class createpostComponent extends Component {
  constructor(props) {
    super(props);

    this.state = {
      title: "",
      body: "",
      postType: "Coding",
      tags: "",
    };
  }

  titleHandler = (event) => {
    this.setState({
      title: event.target.value,
    });
  };

  titleHandler = (event) => {
    this.setState({
      title: event.target.value,
    });
  };

  bodyHandler = (event) => {
    this.setState({
      body: event.target.value,
    });
  };

  handleTags = (event) => {
    this.setState({
      tags: event.target.value,
    });
  };

  handleSubmit = (event) => {
    console.log(this.state);
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        title: this.state.title,
        body: this.state.body,
        tags: this.state.tags,
      }),
    };
    fetch("https://hackjaipur.herokuapp.com/post/list/", requestOptions).then(
      (response) => {
        console.log(response);
        if (response.status == 400) {
          alert("Your post doesn't follow the guideline");
        }
      }
    );
    event.preventDefault();
  };

  render() {
    return (
      <form className="container jumbotron" onSubmit={this.handleSubmit}>
        <div>
          <label className="label">title :</label>
          <input
            className="input"
            type="text"
            value={this.state.title}
            onChange={this.titleHandler}
          />
        </div>
        <div>
          <label className="label">Body :</label>
          <textarea
            className="input"
            value={this.state.body}
            onChange={this.bodyHandler}
          ></textarea>
        </div>
        <div>
          <label className="label">tags :</label>
          <select
            value={this.state.tags}
            className="input"
            onChange={this.handleTags}
          >
            <option value="react"> React</option>
            <option value="web"> web</option>
            <option value="c++"> C++</option>
            <option value="ML"> Machine Learning</option>
            <option value="python">Python</option>
          </select>
        </div>
        <button className=" postButton btn btn-primary" type="submit">
          submit
        </button>
      </form>
    );
  }
}

export default createpostComponent;
