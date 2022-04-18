import React from "react";
import "../style/Dashboard.css";
import { useHistory } from "react-router-dom";
import { useState } from "react";
import ClassCard from "../components/Classcard";

function Dashboard() {
  const [classes, setClasses] = useState([
    { creatorName: "Rahim", creatorPhoto: "", name: "Business", id: "101" },
    { creatorName: "Karim", creatorPhoto: "", name: "Math", id: "102" },
    { creatorName: "Mofiz", creatorPhoto: "", name: "Sociology", id: "103" },
  ]);
  const history = useHistory();

  return (
    <div className="dashboard">
      {classes?.length === 0 ? (
        <div className="dashboard__404">
          No classes found! Join or create one!
        </div>
      ) : (
        <div className="dashboard__classContainer">
          {classes.map((individualClass) => (
            <ClassCard
              creatorName={individualClass.creatorName}
              creatorPhoto={individualClass.creatorPhoto}
              name={individualClass.name}
              id={individualClass.id}
              style={{ marginRight: 30, marginBottom: 30 }}
            />
          ))}
        </div>
      )}
    </div>
  );
}
export default Dashboard;
