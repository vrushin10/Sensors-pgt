import * as React from "react";
// import { Navbar } from "react-bootstrap";
import { MyCard, CardProps } from "./Card";
import MyNavbar from "./Navbar";

export default class Dashboard extends React.Component {
  static cardprop: CardProps = {
    temp: 35,
    isShot: false,
    heartRate: 90,
    lat: 12.56,
    long: 12.56,
  };

  render() {
    return (
      <>
        <MyNavbar />
        <MyCard {...Dashboard.cardprop}></MyCard>
      </>
    );
  }
}
