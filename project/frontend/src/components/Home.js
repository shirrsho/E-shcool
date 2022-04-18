import React from "react";
import "../style/Home.css";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

const Home = () => {
  return (
    <div className="home">
      <div className="home__container">
        <img
          src="https://upload.wikimedia.org/wikipedia/commons/5/59/Google_Classroom_Logo.png"
          alt="Google Classroom Image"
          className="home__image"
        />
        <button className="home__login">Login with Google</button>
      </div>
    </div>
  );
};

export default Home;
