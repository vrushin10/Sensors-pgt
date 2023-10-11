import * as React from "react";
import {
  bullet_detection_data,
  water_quality_data,
} from "../types/water_quality";
// import { Card } from "react-bootstrap"

export const MySensorCard: React.FC<water_quality_data> = (props) => {
  const date = new Date(props.timestamp);
  const formattedDate = new Intl.DateTimeFormat("en-US").format(date);
  return (
    <div className="m-2 max-w-sm  overflow-hidden rounded bg-slate-200  shadow-lg">
      <h1 className="content-center p-6 text-lg font-bold">
        {props.device_id}
      </h1>

      <div className="px-6 py-2">
        <p className="text-base">turbidity : {props.turbidity}</p>
        <p className="text-base">TDS : {props.TDS}</p>
        <p className="text-base">temp : {props.temp}</p>
        <p className="text-base">pH : {props.pH}</p>
        <p className="text-base">Date : {formattedDate}</p>
      </div>
    </div>
  );
};

export const MyBulletCard: React.FC<bullet_detection_data> = (props) => {
  // const date = new Date(props.timestamp);
  // const formattedDate = new Intl.DateTimeFormat("en-US").format(date);
  return (
    <div>
      <div className="m-2 max-w-sm overflow-hidden rounded bg-slate-200 shadow-lg">
        <div className="px-6 py-4">
          <h2>id: {props.vestid}</h2>
          <li>temp : {props.temp}</li>
          <li>heartrate : {props.heartrate}</li>
          <li>lat : {props.lat}</li>
          <li>long : {props.long}</li>
        </div>
      </div>
    </div>
  );
};
