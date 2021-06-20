import React, { useEffect, useState } from "react";
import Container from "react-bootstrap/Container";
import Card from "react-bootstrap/Card";
import Button from "react-bootstrap/Button";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Form from "react-bootstrap/Form";
import { Link, useHistory } from "react-router-dom";
import useForm from "react-hook-form";

function FileUploadCard(props) {
  return (
    <Card>
      <Card.Body>
        <Card.Title>{props.title}</Card.Title>
        <Form.Group controlId={props.name}>
          <Form.Label>{props.text}</Form.Label>
          <input
            ref={props.reffunc}
            name={props.name}
            type="file"
            accept=".txt"
          // className="custom-file-input"
          />
        </Form.Group>
      </Card.Body>
    </Card>
  )
}

export default function HomePage() {
  const history = useHistory();
  const { register, handleSubmit } = useForm();

  const onSubmit = (data) => {
    const formData = new FormData();
    formData.append("inputfile", data.inputfile[0]);
    formData.append("outputfile", data.outputfile[0]);

    // for (var pair of formData.entries()) {
    //   console.log(pair[0] + ', ' + pair[1]);
    // }

    (async (formData) => {
      try {
        const response = await fetch("http://localhost:5000", {
          method: "POST",
          body: formData
        });
        const resp = await response.json()

        alert(JSON.stringify(resp));
      } catch (error) {
        console.log(error);
      }
    })(formData);
  };

  return (
    <>
      <Container fluid={true} /* style={{ backgroundColor: "black" }} */>

        <form onSubmit={handleSubmit(onSubmit)}>
          <Row>
            <Col>
              <FileUploadCard
                name="inputfile"
                title="Input File"
                text="Contains all kanji YOU'VE ALREADY learn"
                submittext="upload"
                reffunc={register}>
              </FileUploadCard>
            </Col>
            <Col>
              <FileUploadCard
                name="outputfile"
                title="Output File"
                text="Contains all kanji YOU WANT TO learn"
                submittext="upload"
                reffunc={register}>
              </FileUploadCard>
            </Col>
          </Row>

          <Button variant="primary" type="submit" block className="mt-2">Execute</Button>

        </form>
      </Container>

      <Container style={{ backgroundColor: "black" }}>
        <Row className="mt-3">
          <Col>
            <FileUploadCard
              title="Your Kanji Map Here"
              text="here's your kanjimap"
              submittext="upload">
            </FileUploadCard>
          </Col>
        </Row>
      </Container>
    </>
  );
}
