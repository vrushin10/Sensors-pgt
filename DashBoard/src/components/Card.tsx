import * as React from "react";
import { Card } from "react-bootstrap";
// import { Card } from "react-bootstrap"

export interface CardProps {
  temp: number;
  isShot: boolean;
  heartRate: number;
  lat: number;
  long: number;
}

export const MyCard: React.FC<CardProps> = (props) => {
  return (
    <div>
      <Card style={{ width: "18rem", margin: "2rem" }}>
        <Card.Body>
          <Card.Title>
            Hello, {props.temp} {props.heartRate} {props.isShot} !
          </Card.Title>
          <Card.Text>
            Some quick example text to build on the card title and make up the
            bulk of the card's content.
          </Card.Text>
        </Card.Body>
      </Card>
    </div>
  );
};
