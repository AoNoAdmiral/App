import React,{useEffect} from 'react';
import Banner from './components/Banner';
import Home from './components/Home';
import Header from './components/Header';
import Product from './components/Product';
import Deal from './components/Deal';
import Feature from './components/Feature';
import Review from './components/Review';
import ContactUs from './components/ContactUs';
import Blog from './components/Blog';
import Footer from './components/Footer';
import axios from 'axios';
import {products} from './components/Product/Data';

const Mainpage = () =>{
  // update Tuoi nuoc ( Doi watering qua conditionheat/humd/earth va value thanh gia tri tuong ung)
//   axios.post("https://io.adafruit.com/api/v2/Airforce/feeds/watering/data",{
//          "datum":{
//              "value":1
//              }
//   },{             
//   headers: {
//     'Content-Type': 'application/json',
//     'Host': 'io.adafruit.com',
//     'X-AIO-Key':sessionStorage.getItem('key')
//   }
// })
// .then(function (response) {
//    
// })
    if(!sessionStorage.getItem('email')){
      sessionStorage.setItem('email',"");
    }
    try {
    sessionStorage.setItem('key',"aio_Xhym94eulsCijNPlpzAbm3MkFOGz")
    const localData = [];
    // lay data chart
    axios.get("https://io.adafruit.com/api/v2/Airforce/feeds/heat/data/chart?hours=24&resolution=15",{
    },{             
    headers: {
      'Content-Type': 'application/json',
      'Host': 'io.adafruit.com',
      'X-AIO-Key':sessionStorage.getItem('key')
    }
  })
  .then(function (response) {
     
  })
  axios.get("https://io.adafruit.com/api/v2/Airforce/feeds/humd/data/chart?hours=24&resolution=15",{
    },{             
    headers: {
      'Content-Type': 'application/json',
      'Host': 'io.adafruit.com',
      'X-AIO-Key':sessionStorage.getItem('key')
    }
  })
  .then(function (response) {
     
  })
  axios.get("https://io.adafruit.com/api/v2/Airforce/feeds/earthhumd/data/chart?hours=24&resolution=15",{
    },{             
    headers: {
      'Content-Type': 'application/json',
      'Host': 'io.adafruit.com',
      'X-AIO-Key':sessionStorage.getItem('key')
    }
  })
  .then(function (response) {
     
  })
  // lay data dk
  axios.get("https://io.adafruit.com/api/v2/Airforce/feeds/conditionalhumd/data?limit=1",{
    },{             
    headers: {
      'Content-Type': 'application/json',
      'Host': 'io.adafruit.com',
      'X-AIO-Key':sessionStorage.getItem('key')
    }
  })
  .then(function (response) {
     
  })
  axios.get("https://io.adafruit.com/api/v2/Airforce/feeds/conditionheat/data?limit=1",{
    },{             
    headers: {
      'Content-Type': 'application/json',
      'Host': 'io.adafruit.com',
      'X-AIO-Key':sessionStorage.getItem('key')
    }
  })
  .then(function (response) {
     
  })
  axios.get("https://io.adafruit.com/api/v2/Airforce/feeds/conditionalearth/data?limit=1",{
    },{             
    headers: {
      'Content-Type': 'application/json',
      'Host': 'io.adafruit.com',
      'X-AIO-Key':sessionStorage.getItem('key')
    }
  })
  .then(function (response) {
     
  })
      } catch (error) {
        console.log(error);
    }
    // lay data current
    function checkData(){
      axios.get("https://io.adafruit.com/api/v2/Airforce/feeds/heat/data?limit=1",{
      },{             
      headers: {
        'Content-Type': 'application/json',
        'Host': 'io.adafruit.com',
        'X-AIO-Key':sessionStorage.getItem('key')
      }
    })
    .then(function (response) {
       
    })
    }
    setInterval(() => {
      checkData();
    }, 3000);
    function checkData2(){
      axios.get("https://io.adafruit.com/api/v2/Airforce/feeds/humd/data?limit=1",{
      },{             
      headers: {
        'Content-Type': 'application/json',
        'Host': 'io.adafruit.com',
        'X-AIO-Key':sessionStorage.getItem('key')
      }
    })
    .then(function (response) {
       
    })
    }
    setInterval(() => {
      checkData2();
    }, 3000);
    function checkData3(){
      axios.get("https://io.adafruit.com/api/v2/Airforce/feeds/earthhumd/data?limit=1",{
      },{             
      headers: {
        'Content-Type': 'application/json',
        'Host': 'io.adafruit.com',
        'X-AIO-Key':sessionStorage.getItem('key')
      }
    })
    .then(function (response) {
       
    })
    }
    setInterval(() => {
      checkData3();
    }, 3000);

    function checkData4(){
      axios.get("https://io.adafruit.com/api/v2/Airforce/feeds/watering/data?limit=1",{
      },{             
      headers: {
        'Content-Type': 'application/json',
        'Host': 'io.adafruit.com',
        'X-AIO-Key':sessionStorage.getItem('key')
      }
    })
    .then(function (response) {
       
    })
    }
    setInterval(() => {
      checkData4();
    }, 3000);
    sessionStorage.setItem('Order',JSON.stringify([]));
    return (    
    <div className = "App">
        <Header/>
        <Home/>
        <Banner/>
        <Product/>
        <Deal/>
        <Feature/>
        <Review/>
        <ContactUs/>
        <Blog/>
        <Footer/>
    </div>
     );
     
}

export default Mainpage;