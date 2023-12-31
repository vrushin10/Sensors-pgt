import axios from "axios";
// import {z,ZodArray} from "zod"
import {
  array_bullet_detection_data_zod,
  bullet_detection_data,
} from "../types/water_quality";



export async function GETALLFROMDB(api:string): Promise<bullet_detection_data[]> {
  // eslint-disable-next-line no-useless-catch
  try {
    
    const response = await axios.get(api +"/firebase");
    const output = array_bullet_detection_data_zod.parse(response.data) as bullet_detection_data[];
    return output;
  } catch (error) {
    throw error
  }
}
export async function GETALLFROMDB_witouturi(): Promise<bullet_detection_data[]> {
  // eslint-disable-next-line no-useless-catch
  try {
    const response = await axios.get("/firebase");
    const output = array_bullet_detection_data_zod.parse(response.data) as bullet_detection_data[];
    return output;
  } catch (error) {
    throw error
  }
}

export async function fetchDataFromApi(): Promise<
  bullet_detection_data[] | unknown
> {
  try {
    const response = (await axios.get("http://localhost:8000/firebase")).data;
    return array_bullet_detection_data_zod.parse(
      response
    ) as bullet_detection_data[];
  } catch (error) {
    return error;
  }
}
