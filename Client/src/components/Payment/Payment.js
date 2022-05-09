import React,{useState,useEffect} from 'react'
import {Data,Shipping} from './Data'
import axios from 'axios';
function Setting() {
    const [count, setCount] = useState(JSON.parse(sessionStorage.getItem("Order")));
    const [total, setTotal] = useState(0);
    const [note, setNote] = useState("");
    const [address, setAddress] = useState("");
    const [POP,setPOP]=useState(0);
    const [ad1, set1] = useState("");
    const [ad2, set2] = useState("");
    const [ad3, set3] = useState("");
    let listItem = []
    let listnumber = []
    function changeRoot(event){
        setNote(event.target.value);
    }
    function changeAdd(event){
        setAddress(event.target.value);
    }
    function change1(event){
      set1(event.target.value);
  }
  function change2(event){
    set2(event.target.value);
}
function change3(event){
  set3(event.target.value);
}
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
      function buyItem(props){
        var x = JSON.parse(sessionStorage.getItem('Order'))
        for(const a in x){
            let com = JSON.parse(x[a])
          if (com[1] === props[1] ){
            com[4]++;
            x[a] = JSON.stringify(com)
            sessionStorage.setItem('Order',JSON.stringify(x));
            return;
          }
        }
        x.push(JSON.stringify({1:props[1],2:props[2],3:props[3],4:1}));
        sessionStorage.setItem('Order',JSON.stringify(x));  
      }
      function lowerItem(props){
        var x = JSON.parse(sessionStorage.getItem('Order'))
        for(const a in x){
            let com = JSON.parse(x[a])
          if (com[1] === props[1] ){
            com[4]--;
            if (com[4]!=0){
            x[a] = JSON.stringify(com)
            sessionStorage.setItem('Order',JSON.stringify(x));}
            else removeItem(props);
            return;
          }
        }
        x.push(JSON.stringify({1:props[1],2:props[2],3:props[3],4:1}));
        sessionStorage.setItem('Order',JSON.stringify(x));  
      }
    function submit(){
      axios.post("http://localhost:3000/addbill", {
        email: sessionStorage.getItem('email'),
        order:JSON.parse(sessionStorage.getItem('Order'))
      })
      .then(function (response) {
        if(response.data.status==1)
          window.location = "/";
      })
      .catch(function (error) {
        console.log(error);
      });
    }
    return (
    <section class="cart">
    <div class="cart_left">
        <div class="row">
            <span class="rowTitle">Shopping cart</span>
        </div>
        {count.map((item)=>{
            let props=JSON.parse(item);
            return (
        <div class="cart_items">
            <img src={props[2]} alt=""/>
            <div class="cart_items_details">
                <div class="cart_items_details-top">
                    <span class="items_name">{props[1]}</span>
                    <span class="closeIcon" id="closeIcon">
                        <i class="fas fa-times" onClick={()=>removeItem(props)}></i>
                    </span>
                </div>
                <div class="cart_items_details-bottom">
                    <span class="cart_items_details-price">{props[3].toLocaleString()} VND</span>
                    <div class="controls">
                        <button class="minusIcon" type="button" onClick={()=>lowerItem(props)}>-</button>
                        <span class="count" id="count">{props[4]}</span>
                        <button class="plusIcon"  type="button" onClick={()=>buyItem(props)}>+</button>
                    </div>
                </div>
            </div>
        </div>)})}
    <div class="cartPromoDiv">
            <form>
            <input type="text" id="fname" name="fname" width="50%"  placeholder="Note" onChange={changeRoot}/>
            </form>
        </div>
    </div>
    <div class="cart_right">
        <div class="row1">
            <span class="rowTitle">Shopping cart</span>
        </div>
        <div class="row">
            <span class="rowTitle">Sub total</span>
            <span class="rowAmount">{total.toLocaleString()} VND</span>
        </div>
        <div class="row">
            <span class="rowTitle">Shipping</span>
            <span class="rowAmount">{(20000).toLocaleString()} VND</span>
        </div>
        <div class="row2">
            <span class="rowTitle">Total</span>
            <span class="rowAmount">{(total+20000).toLocaleString()} VND</span>
        </div>
        <div class="btn">
            <button type="button" onClick={()=>setPOP(1)}>Checkout</button>
        </div>
    </div>
    <div class={POP?"left apply-form":"hide left apply-form"}>
        <form action="#" class="Setting">
        <span class="closeIcon" className="closecon" onClick={()=>setPOP(0)}>
            <i class="fas fa-times"></i>
        </span>
          <div class="form-inner">
            <div class="form-group">
              <label for="">SỐ THẺ</label>
              <input type="text" placeholder="9404 3202 5794 3749" id="" onChange={change1}/>
            </div>
            <div class="form-group">
                <label for="">TÊN IN TRÊN THẺ</label>
                <input type="text" placeholder="NGUYEN VAN A" id="" onChange={change2}/>
            </div>
            <div class="form-group">
                <label for="">NGÀY PHÁT HÀNH</label>
                <input type="text" placeholder="05/14" id="" onChange={change3}/>
              </div>
            <div class="form-group">
              <label for="">ĐỊA CHỈ NHẬN HÀNG</label>
              <input type="text" placeholder="132/20 LÝ THƯỜNG KIỆT....." id="my_field" onChange={changeAdd}/>
            </div>
          </div>
          <button class="submit-btn1" id="apply-form-btn" onClick={()=>submit()}>Confirm</button>
        </form>
      </div>
</section>
    )
}



export default Setting