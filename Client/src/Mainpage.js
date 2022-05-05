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

  if (!sessionStorage.getItem('email')) {
    sessionStorage.setItem('email', "");
  }
  if (!sessionStorage.getItem('list')) {
    sessionStorage.setItem('list', JSON.stringify([]));
  }
  try {
    sessionStorage.setItem('key', "aio_mAPX55I3pBbA0eth8HqaPulwtCyO");
  }
  catch {

  }

    return (
    <div className="App">
      <Header />
      <Home />
      <Banner />
      <Deal />
      <Feature />
      <Review />
      <ContactUs />
      <Blog />
      <Footer />
    </div>
  );

}

export default Mainpage;