import React from 'react';
import Header from './components/Header';
import Footer from './components/Footer';
import Home1 from './components/Home1';
import Garden from './components/Garden';
import Feature from './components/Feature';
import Chart from './components/Chart';
const SettingPage = () =>{
    return (
    <div className = "App">
        <Header/>
        <Home1/>
        <Garden/>
        <Chart/>
        <Feature />
        <Footer/>
    </div>
     );
     
}

export default SettingPage;