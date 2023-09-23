import * as React from "react";
import { MyCard, CardProps } from "./Card";
import MyNavbar from "./Navbar";
// import { useEffect, useRef } from "react";
import Mymap from "./Mymap";

class Dash extends React.Component {
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  static cardprops: CardProps = {
    device_id: "1",
    lat: 12.12,
    long: 13.13,
    pH: 7.8,
    TDS: 100,
    temp: 32,
    timestamp: 90000,
    turbidity: 600,
  };

  render() {
    return (
      <>
        <MyNavbar></MyNavbar>
        <MyCard {...Dash.cardprops}></MyCard>
        <Mymap></Mymap>
      </>
    );
  }
}

export default Dash;
