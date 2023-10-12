import * as React from "react";
import { MySensorCard, MyBulletCard } from "./Card";
import MyNavbar from "./Navbar";
import {
  bullet_detection_data,
  water_quality_data,
} from "../types/water_quality";
// import { useEffect, useRef } from "react";
import { GETALLFROMDB, GETALLFROMDB_witouturi } from "../worker/dataFetcherservice";
import Mymap from "./Mymap";

// eslint-disable-next-line @typescript-eslint/no-explicit-any
declare type props = any;
declare type statetype = {
  cardprops: water_quality_data[];
  bulletcardprops: bullet_detection_data[];
};
class Dash extends React.Component<props, statetype> {
  // eslint-disable-next-line @typescript-eslint/no-unused-vars

  state: statetype = {
    cardprops: [
      {
        device_id: "2",
        lat: 19.0767253,
        long: 72.9106087,
        pH: 7.8,
        TDS: 100,
        temp: 32,
        timestamp: 90000,
        turbidity: 600,
      },
      {
        device_id: "1",
        lat: 12.12,
        long: 13.13,
        pH: 7.8,
        TDS: 100,
        temp: 32,
        timestamp: 90000,
        turbidity: 600,
      },
    ],
    bulletcardprops: [],
  };

  async componentDidMount() {
    GETALLFROMDB("http://localhost:8000").then((result) => {
      this.setState((states: statetype) => {
        let continains = false;
        result.forEach((x: bullet_detection_data) => {
          continains = states.bulletcardprops.includes(x);
        });
        if (!continains) {
          return { bulletcardprops: states.bulletcardprops.concat(result) };
        } else {
          return { bulletcardprops: states.bulletcardprops };
        }
      });
    });

    // const apiurl = new URL(document.URL);
    // console.log(apiurl.host, "host");
    // console.log(apiurl.hostname, "hostname");

    // GETALLFROMDB_witouturi().then((result) => {
    //   console.log(result,"result");

    //   this.setState((states: statetype) => {
    //         let continains = false;
    //         result.forEach((x: bullet_detection_data) => {
    //           continains = states.bulletcardprops.includes(x);
    //         });
    //         if (!continains) {
    //           return { bulletcardprops: states.bulletcardprops.concat(result) };
    //         } else {
    //           return { bulletcardprops: states.bulletcardprops };
    //         }
    //       });
    // });
    console.log(this.state.bulletcardprops);
    
  }

  render() {
    return (
      <>
        <MyNavbar></MyNavbar>
        <div className=" columns-2">
          <div className="col-span-1">
            <div
              style={{
                display: "flex",
              }}
            >
              {this.state.cardprops.map((card, index) => {
                return <MySensorCard key={index} {...card} />;
              })}
              {/* </div>
            <div
              style={{
                display: "flex",
              }}
            > */}
              {this.state.bulletcardprops.map((card, index) => {
                return <MyBulletCard key={index} {...card} />;
              })}
            </div>
          </div>
          <div className="col-span-2">
            <div className="absolute block h-3/4 w-2/4 rounded p-4">
              <Mymap data={this.state.bulletcardprops} />
            </div>
          </div>
        </div>
      </>
    );
  }
}

export default Dash;
