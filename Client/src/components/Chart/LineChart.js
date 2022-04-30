import React, {useState, useEffect} from "react";
import { Line, Bar } from "react-chartjs-2";
import axios from "axios";

function LineChart(chartData){

    // const [data, setData] = useState(0)

    // useEffect(() => {
    //     axios.get("https://io.adafruit.com/api/v2/Airforce/feeds/heat/data/chart?hours=24&resolution=15").then((response) => {
    //         setData(response.data);
    //     });
    //     }, []);
    // console.log(data)
    return (
        <Bar data={chartData}/>
    )
}

export default LineChart
