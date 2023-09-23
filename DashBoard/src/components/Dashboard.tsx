import * as React from "react";
import { MyCard, CardProps } from "./Card";
import MyNavbar from "./Navbar";
// import { useEffect, useRef } from "react";
import Mymap from "./Mymap";

export default function Dashboard() {
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  const [cardprop, setcardprop] = React.useState<CardProps>({
    temp: 32,
    pH: 7.0,
    turbidity: 10,
    TDS: 10,
    timestamp: Date.now(),
    lat: 10.12,
    long: 12.2,
    device_id: "1",
  });

  return (
    <>
      <MyNavbar />
      <MyCard {...cardprop}></MyCard>
      <Mymap />
    </>
  );
}
