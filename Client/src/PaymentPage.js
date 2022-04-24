import React from 'react';
import Header from './components/Header';
import Footer from './components/Footer';
import Payment from './components/Payment/Payment'
const PaymentPage = () =>{
    return (
    <div className = "App">
        <Header/>
        <Payment/>
        <Footer/>
    </div>
     );
     
}

export default PaymentPage;