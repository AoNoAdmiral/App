import React from 'react';
import Mainpage from './Mainpage.js'
import SearchPage from './SearchPage.js'
import PaymentPage from './PaymentPage.js'
import axios from 'axios';
import { Route, BrowserRouter as Router, Routes } from "react-router-dom"
const App = () =>{
    return (
        
        <Router>
            <Routes>
                <Route path="/" element={<Mainpage/>}/>
                <Route path="/login" element={<SearchPage/>}/>
                <Route path="/payment" element={<PaymentPage/>}/>
            </Routes>
        </Router>
     );
     
}

export default App;

