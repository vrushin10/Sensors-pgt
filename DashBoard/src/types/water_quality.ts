export declare type  water_quality_node = {
    device_id: string,
    installation_date:number,
    last_reported:number,
} 

export declare type  water_quality_data = {
    device_id: string,
    lat: number,
    long: number,
    pH: number,
    TDS: number,
    temp: number,
    turbidity: number,
    timestamp: number,
} 