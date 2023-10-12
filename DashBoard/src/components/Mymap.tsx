import { useEffect, useRef } from "react";
import "ol/ol.css";
import { Map } from "ol";
import Feature from "ol/Feature";
import Point from "ol/geom/Point";
import View from "ol/View";
import { Icon, Style } from "ol/style";
import { BingMaps, Vector as VectorSource } from "ol/source";
import { Tile as TileLayer, Vector as VectorLayer } from "ol/layer";
import { fromLonLat } from "ol/proj";
import { bullet_detection_data } from "../types/water_quality";

export declare type mapProps = {
  data: bullet_detection_data[];
};

export default function Mymap(props: mapProps) {
  const freatures: Feature<Point>[] = [];
  const data = props.data;
  for (let index = 0; index < data.length; index++) {
    const prop = data[index];
    const iconFeature = new Feature({
      geometry: new Point(fromLonLat([prop.long, prop.lat])),
      id: prop.vestid,
    });
    iconFeature.setStyle(
      new Style({
        image: new Icon({
          src: "./assests/untitled.svg",
          height: 25,
        }),
      }),
    );
    freatures.push(iconFeature);
  }

  const vectorLayer = new VectorLayer({
    source: new VectorSource({
      features: freatures,
    }),
  });

  const rasterLayer = new TileLayer({
    source: new BingMaps({
      key: "Auy4QBkmzCKysMRGoQZSbrRFPv2CC0MYAXRDxOHRRXH9IYv2DV6kVyStMGeQ_PWL",
      imagerySet: "Aerial",
    }),
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
      <div className="relative h-full w-full bg-white" ref={mapRef}></div>
    </>
  );
}
