import * as React from "react";
import { Card } from "react-bootstrap";
// import { Card } from "react-bootstrap"

export interface CardProps {
  temp: number;
  pH: number;
  turbidity: number;
  TDS: number;
  timestamp: number;
  lat: number;
  long: number;
  device_id: string;
}

export const MyCard: React.FC<CardProps> = (props) => {
  const date = new Date(props.timestamp);
  const formattedDate = new Intl.DateTimeFormat("en-US").format(date);
  return (
    <div>
      <Card style={{ width: "18rem", margin: "2rem" }}>
        <Card.Body>
          <Card.Title>id: {props.device_id}</Card.Title>
          <Card.Text>
            <div>temp : {props.temp}</div>
            <div>turbidity : {props.turbidity}</div>
            <div>pH : {props.pH}</div>
            <div>TDS : {props.TDS}</div>
            <div>time: {formattedDate}</div>
          </Card.Text>
        </Card.Body>
      </Card>
    </div>
  );
};
