import * as React from "react";
import { MyCard, CardProps } from "./Card";
import MyNavbar from "./Navbar";
// import { useEffect, useRef } from "react";
import Mymap from "./Mymap";
import { GETALLFROMDB } from "../worker/dataFetcherservice";
// import { Get_local } from "../worker/dataFetcherservice";
// import { Get_local } from "../worker/dataFetcherservice";

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
  static cardprops2: CardProps = {
    device_id: "2",
    lat: 19.0767253,
    long: 72.9106087,
    pH: 7.8,
    TDS: 100,
    temp: 32,
    timestamp: 90000,
    turbidity: 600,
  };


  async componentDidMount() {
     console.log(await (GETALLFROMDB()));
     
  }
  
  render() {

    return (
      <>
        <MyNavbar></MyNavbar>
        <MyCard {...Dash.cardprops}></MyCard>
        <Mymap data={[Dash.cardprops, Dash.cardprops2]}></Mymap>
      </>
    );
  }
}

export default Dash;
