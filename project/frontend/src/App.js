import React from "react";
import "./App.css";
import Navbar from "./components/Navbar";
import Home from "./components/Home";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Dashboard from "./components/Dashboard";
import AdminDash from "./components/AdminDash";
import RegisterTeacher from "./components/RegisterTeacher";

function App() {
  return (
    <div className="App">
      <Router>
        <Switch>
          <Route exact path="/">
            <Home />
          </Route>
          <Route exact path="/studentdashboard">
            <Navbar />
            <Dashboard />
          </Route>
          <Route exact path="/admindashboard">
            <AdminDash />
          </Route>
          <Route exact path="/registerteacher">
            <RegisterTeacher />
          </Route>
        </Switch>
      </Router>
    </div>
  );
}

export default App;
