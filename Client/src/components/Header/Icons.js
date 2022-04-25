import React,{useState,useEffect } from 'react'
import {Data} from './Data'
import axios from 'axios';
function Icons() {
    function switchPay(){
      if (Object.keys(JSON.parse(sessionStorage.getItem('Order'))).length===0) alert("Please choose at least 1 item")
      else  window.location = "/payment";
    }
    const styleObj = {
        marginLeft:0
    }
    const [count, setCount] = useState(JSON.parse(sessionStorage.getItem("Order")));
    const [total, setTotal] = useState(0);
    function calcTotal(){
      var x = JSON.parse(sessionStorage.getItem('Order'))
      var y = 0;
      for(const a in x){
          let com = JSON.parse(x[a])
        y += com[3]*com[4];
      }
      setTotal(y);
    }
    useEffect(() => {
      setTimeout(() => {
        setCount(JSON.parse(sessionStorage.getItem("Order")));
      }, 1000);
    });
    useEffect(() => {
      setTimeout(() => {
        calcTotal();
      }, 1000);
    });
    function removeItem(props){
      var x = JSON.parse(sessionStorage.getItem('Order'))
      for(const a in x){
          let com = JSON.parse(x[a])
        if (com[1] === props[1]){
          x.splice(a,1);
          sessionStorage.setItem('Order',JSON.stringify(x));
          return;
        }
      }
      return;
    }
    return (
    <div>
    <div className="icons" id="here">
        <div id="menu-btn" className="fas fa-bars"></div>
        <div id="search-btn" className="fas fa-search" onClick={()=>test()}></div>
        <a id="login-btn" href="/login" className="fas fa-user"></a>
    </div>

    </div>
    
    )
}

export default Icons