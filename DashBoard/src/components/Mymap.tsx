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

export default function Mymap() {
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  // const iconFeature = new Feature({
  //   geometry: new Point([0, 0]),
  //   name: "Null Island",
  // });
  const iconFeature1 = new Feature({
    geometry: new Point([10, -10]),
    name: "Null Island",
  });

  const iconStyle = new Style({
    image: new Icon({
      anchorXUnits: "fraction",
      anchorYUnits: "pixels",
      src: "vite.svg",
    }),
  });

  // iconFeature.setStyle(iconStyle);
  iconFeature1.setStyle(iconStyle);

  const vectorSource = new VectorSource({
    features: [iconFeature1],
  });

  const vectorLayer = new VectorLayer({
    source: vectorSource,
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
          center: [0, 0],
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
