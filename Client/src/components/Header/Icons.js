import React,{useState,useEffect } from 'react'
import {Data} from './Data'
import axios from 'axios';
function Icons() {
    const styleObj = {
        marginLeft:0
    }
    function login(){
      window.location = "/login";
  }
  function logout(){
    sessionStorage.setItem('email',"");
    window.location = "/login";
}
    return (
      sessionStorage.getItem('email')==""?
    <div>
    <div className="icons" id="here">
        <div id="menu-btn" className="fas fa-bars"></div>
        <div id="search-btn" className="fas fa-search"></div>
        <a id="login-btn" className="fas fa-user"></a>
        <div className="login-form">
          <h3 className="total"> HELLO</h3>
          <a onClick={()=>login()} style={styleObj} className="header__menu-link btn btn--border btn--rounded buttom"> LOG IN</a>
        </div>
    </div>
    <form action="" className="search-form">
        <input type="search" name="" placeholder="search here..." id="search-box"></input>
        <label for="search-box" className="fas fa-search"></label>
    </form>
    </div>:

    <div>
    <div className="icons" id="here">
        <div id="menu-btn" className="fas fa-bars"></div>
        <div id="search-btn" className="fas fa-search"></div>
        <div id="login-btn" className="fas fa-user"></div>
        <div className="login-form">
          <h3 className="total"> HELLO {sessionStorage.getItem('email')}</h3>
          <a onClick={()=>logout()} style={styleObj} className="header__menu-link btn btn--border btn--rounded buttom"> LOG OUT</a>
        </div>
    </div>
    <form action="" className="search-form">
        <input type="search" name="" placeholder="search here..." id="search-box"></input>
        <label for="search-box" className="fas fa-search"></label>
    </form>
    </div>
    
    )
}

export default Icons