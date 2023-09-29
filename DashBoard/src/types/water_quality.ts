import { z, ZodArray } from "zod";

export const water_quality_node_zod = z.object({
  device_id: z.string(),
  installation_date: z.number(),
  last_reported: z.number(),
});

export const water_quality_data_zod = z.object({
  device_id: z.string(),
  lat: z.number(),
  long: z.number(),
  pH: z.number(),
  TDS: z.number(),
  temp: z.number(),
  turbidity: z.number(),
  timestamp: z.number(),
});

export const array_water_quality_data_zod: ZodArray<
  typeof water_quality_data_zod
> = z.array(water_quality_data_zod);

export declare type water_quality_node = {
  device_id: string;
  installation_date: number;
  last_reported: number;
};

export declare type water_quality_data = {
  device_id: string;
  lat: number;
  long: number;
  pH: number;
  TDS: number;
  temp: number;
  turbidity: number;
  timestamp: number;
};

export declare type bullet_detection_data = {
  vestid: string;
  bullet_detected: boolean;
  lat: number;
  long: number;
  temp: number;
  heartrate: number;
  timestamp: number;
};

export const bullet_detection_data_zod = z.object({
  vestid: z.string(),
  bullet_detected: z.boolean(),
  lat: z.number(),
  long: z.number(),
  temp: z.number(),
  heartrate: z.number(),
  timestamp: z.number(),
});

export const array_bullet_detection_data_zod: ZodArray<
  typeof bullet_detection_data_zod
> = z.array(bullet_detection_data_zod);
