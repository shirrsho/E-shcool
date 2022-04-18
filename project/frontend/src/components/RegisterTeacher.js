import React from "react";
import { Button, FloatingLabel } from "react-bootstrap";
import { Form } from "react-bootstrap";
import "../style/RegisterTeacher.css";

function RegisterTeacher() {
  return (
    <div className="main">
      <FloatingLabel controlId="floatingInput" label="Name">
        <Form.Control className="box" type="text" placeholder="name" />
      </FloatingLabel>

      <FloatingLabel
        controlId="floatingInput"
        label="Email address"
        className="mb-3"
      >
        <Form.Control
          className="box"
          type="email"
          placeholder="name@example.com"
        />
      </FloatingLabel>
      <FloatingLabel controlId="floatingPassword" label="Password">
        <Form.Control className="box" type="password" placeholder="Password" />
      </FloatingLabel>
      <Button id="butt">Add Teacher</Button>
    </div>
  );
}

export default RegisterTeacher;
