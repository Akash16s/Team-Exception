import React from "react";
import "./competitionBox.css";
function competitionBoc(props) {
  return (
    <div className="compBox">
      <a href={props.link}>
        <h3>{props.title}</h3>
      </a>
      <p>{props.desc}</p>
      <strong>{props.time}</strong>
      <br></br>
      <strong>{props.date}</strong>
    </div>
  );
}

export default competitionBoc;
