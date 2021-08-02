import React from "react";
import { BrowserRouter, Redirect, Route } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";
import DogSchedule from "./DogSchedule";
import "./App.css";
import DemoCal from "./DEMO-use-calendar";
import DemoBigCal from "./DEMO-BigCalendar";
import { MyMonthlyCalendar } from "./DEMO-zack";



export default function App() {

  console.log("rendering App");
  return (
    <BrowserRouter>
      <div className="container-fluid">
        <Route exact path="/dogs/:dogId/schedule">
          <DogSchedule />
          <DemoCal />
          {/* <DemoBigCal />*/}
          {/* <MyMonthlyCalendar /> */}
          

          
        </Route>
      </div>
    </BrowserRouter>
  );
}
