import React from "react";
import { BrowserRouter, Redirect, Route } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";
import DogSchedule from "./DogSchedule";
import "./App.css";

export default function App() {

  console.log("rendering App");
  return (
    <BrowserRouter>
      <div className="container-fluid">
        <Route exact path="/dogs/:dogId/schedule">
          <DogSchedule />
        </Route>
      </div>
    </BrowserRouter>
  );
}
