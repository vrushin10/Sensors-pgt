import * as React from "react";
// import { Navbar } from "react-bootstrap";
import { MyCard, CardProps } from "./Card";
import MyNavbar from "./Navbar";
import Mymap from "./Map";

export default class Dashboard extends React.Component {
  static cardprop: CardProps = {
  temp: 32,
  pH: 7.0,
  turbidity:10,
  TDS:10,
  timestamp: Date.now(),
  lat:10.12,
  long:12.2,
  device_id:"1"
  };

  render() {
    return (
      <>
        <MyNavbar />
        <MyCard {...Dashboard.cardprop}></MyCard>
        <Mymap ></Mymap>
      </>
    );
  }
}
