import React from 'react';
import Mainpage from './Mainpage.js'
import SearchPage from './SearchPage.js'
import SettingPage from './SettingPage.js'
import axios from 'axios';
import { Route, BrowserRouter as Router, Routes } from "react-router-dom"
const App = () =>{
    return (
        
        <Router>
            <Routes>
                <Route path="/" element={<Mainpage/>}/>
                <Route path="/login" element={<SearchPage/>}/>
                <Route path="/Setting" element={<SettingPage/>}/>
            </Routes>
        </Router>
     );
     
}

export default App;

