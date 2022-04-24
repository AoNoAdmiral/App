import { useState } from "react"
export default function Popup(props,num,trigger,setTrigger, lol, setLoL, c, setC){
  function buyItem(props,index){
    var x = JSON.parse(sessionStorage.getItem('Order'))
    for(const a in x){
        let com = JSON.parse(x[a])
      if (com[1] === props[1]){
        com[4]++;
        x[a] = JSON.stringify(com)
        sessionStorage.setItem('Order',JSON.stringify(x));
        return;
      }
    }
    x.push(JSON.stringify({1:props[1],2:props[2],3:props[3],4:1}));
    sessionStorage.setItem('Order',JSON.stringify(x));
    setTrigger(-1);
  }
    return( (trigger === num )?
        <section class="product-details on">
        <span class="closeIcon" id="closeIcon" onClick={()=>{setTrigger(-1); setC(0);}}>
            <i class="fas fa-times"></i>
        </span>
        <img class="image-slider" src={lol}></img>
        <div class="details">
          <h2 class="product-brand">{props[1]}</h2>
          <div class="scroll-object">
          <p class="product-short-des">{props[9]}</p>
          </div>
          <span class="product-price">PRICE: {props[3].toLocaleString()}</span>
          {/* <span class="product-actual-price">{props[4]}</span>
          <span class="product-discount"> {props[5]}</span> */}
          <button class="btn cart-btn" onClick={()=>buyItem(props,c)}>add to cart</button>
        </div>
    </section>:        
    <section class="product-details off">
        <span class="closeIcon" id="closeIcon" onClick={()=>{setTrigger(-1); setC(0);}}>
            <i class="fas fa-times"></i>
        </span>
        <img class="image-slider" src={lol}></img>
        <div class="details">
          <h2 class="product-brand">{props[1]}</h2>
          <div class="scroll-object">
          <p class="product-short-des">{props[9]}</p>
          </div>
          <span class="product-price">PRICE: {props[3].toLocaleString()}</span>
          {/* <span class="product-actual-price">{props[4]}</span>
          <span class="product-discount"> {props[5]}</span> */}
          <button class="btn cart-btn" onClick={()=>buyItem(props,c)}>add to cart</button>
        </div>
    </section>
    )
}