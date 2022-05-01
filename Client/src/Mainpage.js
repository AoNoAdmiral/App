import React, { useEffect } from 'react';
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
import { products } from './components/Product/Data';
import Chart from './components/Chart';
const Mainpage = () => {
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

  // })
  if (!sessionStorage.getItem('email')) {
    sessionStorage.setItem('email', "");
  }
  try {
    sessionStorage.setItem('key', "aio_Hncl31kfAQrNu1qyRmoTruGYqp6M");
  }
  catch {

  }
    // lay data chart
  //     'Content-Type': 'application/json',
  //     'Host': 'io.adafruit.com',
  //     'X-AIO-Key':sessionStorage.getItem('key')
  //   }
  // })
  // .then(function (response) {

  // })
  // // lay data dk
  // axios.get("https://io.adafruit.com/api/v2/Airforce/feeds/conditionalhumd/data?limit=1",{
  //   },{             
  //   headers: {
  //     'Content-Type': 'application/json',
  //     'Host': 'io.adafruit.com',
  //     'X-AIO-Key':sessionStorage.getItem('key')
  //   }
  // })
  // .then(function (response) {

  // })
  // axios.get("https://io.adafruit.com/api/v2/Airforce/feeds/conditionheat/data?limit=1",{
  //   },{             
  //   headers: {
  //     'Content-Type': 'application/json',
  //     'Host': 'io.adafruit.com',
  //     'X-AIO-Key':sessionStorage.getItem('key')
  //   }
  // })
  // .then(function (response) {

  // })
  // axios.get("https://io.adafruit.com/api/v2/Airforce/feeds/conditionalearth/data?limit=1",{
  //   },{             
  //   headers: {
  //     'Content-Type': 'application/json',
  //     'Host': 'io.adafruit.com',
  //     'X-AIO-Key':sessionStorage.getItem('key')
  //   }
  // })
  // .then(function (response) {

  // })
  //   const localData = [];
  //   axios.post("http://localhost:3000/get-products", {

  //     })
  //     .then(function (response) {
  //       console.log(response['data'])
  //       for (let i = 0; i < response['data'].length; i++) {
  //           localData.push(JSON.stringify(response['data'][i]))
  //       }
  //       sessionStorage.setItem('Data',JSON.stringify(localData))
  //     })
  //     .catch(function (error) {
  //       console.log(error);
  //     });
  //     } catch (error) {
  //       console.log(error);
  //   }
  //   // lay data current
  //   function checkData(){
  //     axios.get("https://io.adafruit.com/api/v2/Airforce/feeds/heat/data?limit=1",{
  //     },{             
  //     headers: {
  //       'Content-Type': 'application/json',
  //       'Host': 'io.adafruit.com',
  //       'X-AIO-Key':sessionStorage.getItem('key')
  //     }
  //   })
  //   .then(function (response) {
  //     //  console.log(response)
  //   })
  //   }
  //   setInterval(() => {
  //     checkData();
  //   }, 3000);
  //   function checkData2(){
  //     axios.get("https://io.adafruit.com/api/v2/Airforce/feeds/humd/data?limit=1",{
  //     },{             
  //     headers: {
  //       'Content-Type': 'application/json',
  //       'Host': 'io.adafruit.com',
  //       'X-AIO-Key':sessionStorage.getItem('key')
  //     }
  //   })
  //   .then(function (response) {

  //   })
  //   }
  //   setInterval(() => {
  //     checkData2();
  //   }, 3000);
  //   function checkData3(){
  //     axios.get("https://io.adafruit.com/api/v2/Airforce/feeds/earthhumd/data?limit=1",{
  //     },{             
  //     headers: {
  //       'Content-Type': 'application/json',
  //       'Host': 'io.adafruit.com',
  //       'X-AIO-Key':sessionStorage.getItem('key')
  //     }
  //   })
  //   .then(function (response) {

  //   })
  //   }
  //   setInterval(() => {
  //     checkData3();
  //   }, 3000);

  //   function checkData4(){
  //     axios.get("https://io.adafruit.com/api/v2/Airforce/feeds/watering/data?limit=1",{
  //     },{             
  //     headers: {
  //       'Content-Type': 'application/json',
  //       'Host': 'io.adafruit.com',
  //       'X-AIO-Key':sessionStorage.getItem('key')
  //     }
  //   })
  //   .then(function (response) {

  //   })
  //   }
  //   setInterval(() => {
  //     checkData4();
  //   }, 3000);
    // sessionStorage.setItem('Order',JSON.stringify([]));
    return (
    <div className="App">
      <Header />
      <Home />
      <Banner />
      <Deal />
      {/* <Chart/> */}
      <Feature />
      <Review />
      <ContactUs />
      <Blog />
      <Footer />
    </div>
  );

}

export default Mainpage;