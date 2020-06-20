import React from "react";
import "./postcomp.css";

function postcomp(props) {
  console.log(props);
  return (
    <div>
      <div className="innerpost">
        <div className="row">
          <div className="col-8">
            <h4>{props.title}</h4>
            <p>{props.body}</p>
          </div>
          <div className="col-4">
            <p>Score: {props.score}</p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default postcomp;
