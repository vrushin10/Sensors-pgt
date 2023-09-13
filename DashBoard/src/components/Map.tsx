// import * as React from "react";
import Map, { Marker } from "react-map-gl/maplibre";

export default function Mymap() {
  return (
    <Map
      initialViewState={{
        longitude: -100,
        latitude: 40,
        zoom: 3.5,
      }}
      mapStyle="https://api.maptiler.com/maps/streets/style.json?key=get_your_own_key"
    >
      <Marker longitude={-100} latitude={40} anchor="bottom">
        <img src="./pngaaa.com-4863990.png" />
      </Marker>
    </Map>
  );
}
