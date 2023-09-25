import { useEffect, useRef } from "react";
import "./styles.css";
import "ol/ol.css";
import { Map } from "ol";
import Feature from "ol/Feature";
import Point from "ol/geom/Point";
import View from "ol/View";
import { Icon, Style } from "ol/style";
import { OSM, Vector as VectorSource } from "ol/source";
import { Tile as TileLayer, Vector as VectorLayer } from "ol/layer";
import { fromLonLat } from "ol/proj";
import { water_quality_data } from "../types/water_quality";

export declare type mapProps = {
  data: water_quality_data[];
};

export default function Mymap(props: mapProps) {
  const freatures: Feature<Point>[] = [];
  const data = props.data;
  for (let index = 0; index < data.length; index++) {
    const prop = data[index];
    const iconFeature = new Feature({
      geometry: new Point(fromLonLat([prop.long, prop.lat])),
      id: prop.device_id,
    });
    iconFeature.setStyle(
      new Style({
        image: new Icon({
          src: "untitled.svg",
          height: 30,
        }),
      })
    );
    freatures.push(iconFeature);
  }

  const vectorLayer = new VectorLayer({
    source: new VectorSource({
      features: freatures,
    }),
  });

  const rasterLayer = new TileLayer({
    source: new OSM(),
  });

  function useMap() {
    const mapRef = useRef<Map>();
    if (!mapRef.current) {
      mapRef.current = new Map({
        target: "map",
        layers: [rasterLayer, vectorLayer],
        view: new View({
          center: [10, 10],
          zoom: 2,
        }),
      });
    }
    return mapRef.current;
  }

  const mapRef = useRef<HTMLDivElement>(null);
  const map = useMap();

  useEffect(() => {
    if (mapRef.current) {
      map.setTarget(mapRef.current);
      map.updateSize();
    }
  }, [map]);

  return (
    <>
      <div className="map-container">
        <div id="map" ref={mapRef}></div>
      </div>
    </>
  );
}
