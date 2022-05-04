import React, { useRef, useState, useEffect } from 'react'
import { LineChart, Line, CartesianGrid, XAxis, YAxis, Tooltip } from 'recharts';
import axios from 'axios';

function handleData(data){
  var time = []
  for (const x in data){
    var name1 = data[x][0].split('T')
    name1 = name1[1].slice(0, -4)
    time.push({
      name: name1,
      uv: data[x][1]
    })
  }
  return time
}

function Chart() {

  const [dataEarth, setDataEarth] = useState(null)
  const [dataHeat, setDataHeat] = useState(null)
  const [dataHumd, setDataHumd] = useState(null)

  // lay data chart
  axios.get("https://io.adafruit.com/api/v2/Airforce/feeds/earth/data/chart?", {
  }, {
    headers: {
      'Content-Type': 'application/json',
      'X-AIO-Key': sessionStorage.getItem('key')
    }
  })
    .then(function (response) {
      var a = handleData(response.data.data)
      setDataEarth(a)
    });
    axios.get("https://io.adafruit.com/api/v2/Airforce/feeds/humd/data/chart?", {
    }, {
      headers: {
        'Content-Type': 'application/json',
        'X-AIO-Key': sessionStorage.getItem('key')
      }
    })
      .then(function (response) {
        console.log(response.data.data)
        var a = handleData(response.data.data)
        setDataHumd(a)
      });
    axios.get("https://io.adafruit.com/api/v2/Airforce/feeds/heat/data/chart?", {
    }, {
      headers: {
        'Content-Type': 'application/json',
        'X-AIO-Key': sessionStorage.getItem('key')
      }
    })
      .then(function (response) {
        var a = handleData(response.data.data)
        setDataHeat(a)
      });
  setInterval(() => {
    axios.get("https://io.adafruit.com/api/v2/Airforce/feeds/heat/data/chart?", {
    }, {
      headers: {
        'Content-Type': 'application/json',
        'X-AIO-Key': sessionStorage.getItem('key')
      }
    })
      .then(function (response) {
        var a = handleData(response.data.data)
        setDataHeat(a)
      });
    }, 30000);

    setInterval(() => {
    axios.get("https://io.adafruit.com/api/v2/Airforce/feeds/humd/data/chart?", {
    }, {
      headers: {
        'Content-Type': 'application/json',
        'X-AIO-Key': sessionStorage.getItem('key')
      }
    })
      .then(function (response) {
        console.log(response.data.data)
        var a = handleData(response.data.data)
        setDataHumd(a)
      });
    }, 30000);

    setInterval(() => {
    axios.get("https://io.adafruit.com/api/v2/Airforce/feeds/earth/data/chart?", {
    }, {
      headers: {
        'Content-Type': 'application/json',
        'X-AIO-Key': sessionStorage.getItem('key')
      }
    })
      .then(function (response) {
        var a = handleData(response.data.data)
        setDataEarth(a)
      });
    }, 30000);

  return (

    
    <section className="contact" id="contact">
      <h1 className="heading"> <span>Chart</span> Heat </h1>
      <LineChart width={1300} height={400} data={dataHeat} margin={{ top: 5, right: 100, bottom: 5, left: 0 }}>
        <Line type="monotone" dataKey="uv" stroke="#8884d8" />
        <CartesianGrid stroke="#ccc" strokeDasharray="5 5" />
        <XAxis dataKey="name" />
        <YAxis />
        <Tooltip />
      </LineChart>
      <h1 className="heading"> <span>Chart</span> Humid </h1>
      <LineChart width={1300} height={400} data={dataHumd} margin={{ top: 5, right: 100, bottom: 5, left: 0 }}>
        <Line type="monotone" dataKey="uv" stroke="#8884d8" />
        <CartesianGrid stroke="#ccc" strokeDasharray="5 5" />
        <XAxis dataKey="name" />
        <YAxis />
        <Tooltip />
      </LineChart>
      <h1 className="heading"> <span>Chart</span> Earth </h1>
      <LineChart width={1300} height={400} data={dataEarth} margin={{ top: 5, right: 100, bottom: 5, left: 0 }}>
        <Line type="monotone" dataKey="uv" stroke="#8884d8" />
        <CartesianGrid stroke="#ccc" strokeDasharray="5 5" />
        <XAxis dataKey="name" />
        <YAxis />
        <Tooltip />
      </LineChart>
    </section>
  )
}

export default Chart