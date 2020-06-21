import React from "react";
import logo from "./logo.svg";
import "./App.css";
import "../node_modules/bootstrap/dist/css/bootstrap.min.css";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import Header from "./components/header/headerComponent";
import HomePage from "./pages/homepage/homepageComponent";
import CreatePost from "./pages/createPost/createpostComponent";
import Groups from "./pages/groups/groupscomponent";
function App() {
  return (
    <div className="App">
      <Header />
      <BrowserRouter>
        <Switch>
          <Route exact path={"/"} component={HomePage} />
          <Route exact path={"/create-post"} component={CreatePost} />
          <Route exact path={"/groups"} component={Groups} />
          <Route exact path={"*"} component={HomePage} />
        </Switch>
      </BrowserRouter>
    </div>
  );
}

export default App;
