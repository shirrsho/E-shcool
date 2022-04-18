import React from "react";
import { Card } from "react-bootstrap";
import { useHistory } from "react-router-dom";
import "../style/AdminDash.css";

function AdminDash() {
  const history = useHistory();
  function registerTeacher() {
    history.push("/registerteacher");
  }
  return (
    <div className="container">
      <Card
        class="card"
        border="info"
        style={{ width: "18rem", margin: "20px" }}
        onClick={registerTeacher}
      >
        <Card.Body>
          <h1>Register Teacher</h1>
        </Card.Body>
      </Card>
      <Card
        class="card"
        border="info"
        style={{ width: "18rem", margin: "20px" }}
      >
        <Card.Body>
          <h1>Create course</h1>
        </Card.Body>
      </Card>
      <Card
        class="card"
        border="info"
        style={{ width: "18rem", margin: "20px" }}
      >
        <Card.Body>
          <h1>Add notice</h1>
        </Card.Body>
      </Card>
      <Card
        class="card"
        border="info"
        style={{ width: "18rem", margin: "20px" }}
      >
        <Card.Body>
          <h1>Verify Students</h1>
        </Card.Body>
      </Card>
      <Card
        class="card"
        border="info"
        style={{ width: "18rem", margin: "20px" }}
      >
        <Card.Body>
          <h1>Course Operations</h1>
        </Card.Body>
      </Card>
    </div>
  );
}
export default AdminDash;
