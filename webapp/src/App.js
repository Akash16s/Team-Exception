import React from "react";
import logo from "./logo.svg";
import "./App.css";
import "../node_modules/bootstrap/dist/css/bootstrap.min.css";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import Header from "./components/header/headerComponent";
import HomePage from "./pages/homepage/homepageComponent";
function App() {
  return (
    <div className="App">
      <Header />
      <BrowserRouter>
        <Switch>
          <Route exact path={"/"} component={HomePage} />
          {/* <Route exact path={"*"} component={NotFound} /> */}
        </Switch>
      </BrowserRouter>
    </div>
  );
}

export default App;
