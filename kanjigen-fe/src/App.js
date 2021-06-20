import React from "react";
import { BrowserRouter as Router, Route } from "react-router-dom";
import Switch from "react-bootstrap/cjs/Switch";
import GeneralPage from "./Pages/GeneralPage";
import HomePage from "./Pages/HomePage/HomePage";
import Error404Page from "./Pages/Error404Page/Error404Page";

export default function App() {
  return (
    <>
      <Router>
        <Switch className="h-100 w-100 pl-0">

          <Route path="/">
            <GeneralPage title="Homepage">
              <HomePage />
            </GeneralPage>
          </Route>


          <Route path="/404">
            <GeneralPage title="Error 404">
              <Error404Page />
            </GeneralPage>
          </Route>
        </Switch>
      </Router>
    </>

  );
}
