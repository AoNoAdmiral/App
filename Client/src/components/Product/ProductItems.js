import React,{useState,useEffect} from 'react'
import {products} from './Data.js'
import axios from 'axios';
import Popup from './Popup.js'
function toggleFlag(index){
    let x = document.querySelectorAll(`.flag-${index}`)
    let a = 0;
    x.forEach(item=> {
        a ++;
        item.classList.toggle('active');
    }
    )
}
function ProductItems() {
    function buyItem(props,index){
        if (!sessionStorage.getItem('email')){
            window.location = "/login";
            return;
        }
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
        x.push(JSON.stringify({0:index,1:props[1],2:props[2],3:props[3],4:1}));
        sessionStorage.setItem('Order',JSON.stringify(x));  
    }
    const [Popple,setPopple] = useState(-1);
    const [data,setData] = useState([]); 
    const [Page,setPage] = useState([]); 
    const [stop,setStop] = useState(0);
    const [b,setB] = useState(1);
    const [c,setC] = useState(0);
    const [Pnumber,setP] = useState([]);
    const [num,setNum] = useState(0);
    function checkData(){
        if (stop===1)
            return;
        if (JSON.parse(sessionStorage.getItem('Data'))){
            setData(JSON.parse(sessionStorage.getItem('Data')));
            createPage('all');
            setStop(1);
        }
        else setData([]);
    }
    function createPage(dataFilter){
        let x = [];
        let k = [];
        let index = -1;
        let maxSize = 6;
        let current = 0;
        let text = "";
        for (let i = 0; i < data.length; i++) {
            if(JSON.parse(data[i])[7].indexOf(dataFilter) > -1  || dataFilter == 'all'){
                if(current % maxSize ==0){
                    x.push ([]);
                    index++;
                    k.push(index+1);
                }
                x[index].push(data[i]);
                current++;
            }
        }
        setP(k);
        setPage(x);
    }
    function pick(x){
        setNum(x);
    }
    useEffect(() => {
        setTimeout(() => {
            checkData();
        }, 500);
      });
    let filterBtn = document.querySelectorAll('.filter-buttons .buttons');
    filterBtn.forEach(button =>{
        button.onclick = () =>{
          filterBtn.forEach(btn => btn.classList.remove('active'));
          button.classList.add('active');
          let dataFilter = button.getAttribute('data-filter');
          createPage(dataFilter);
          pick(0);
        };
      });
      
    return (
        <div className="box-container">
        {
            Page.map(function(data,ind){

                return(
                    (ind === num )?<div className="Page1">
                    {data.map(function(ex,index){
                        let props = JSON.parse(ex);
                        return(
                        <div className="box" data-item={props[7]}>
                        <div className="icons">
                            <a className="fas fa-shopping-cart" onClick={()=>buyItem(props,index)}></a>
                            <a className = {`flag-${index} fas fa-heart heart`} onClick={ ()=> toggleFlag(index) }></a>
                            <a className="fas fa-eye" onClick={()=>{setPopple(index); setB(props[2])}}></a>
                        </div>
                        <div className="image">
                            <img src={props[2]} alt=""/>
                        </div>
                        <div className="content">
                            <h3>{props[1]}</h3>
                            <div className="price">
                                <div className="amount">{props[3]} VND</div>
                            </div>
                        </div>
                        {Popup(props,Popple,index,setPopple,b,setB,c,setC)}
                        </div>
                        )
                    })}
                    </div>:"")
            })
        }
        <div className="bbb">
        <div id="pagination">
        {   
            Pnumber.map(function(ex,index){
                if(ex==1)
                return(
                    <a class={num===index?"active":""} onClick={()=>pick(index)}>{ex}</a>
                );
                else
                return(
                    <a class={num===index?"active":""} onClick={()=>pick(index)}>{ex}</a>
                );
            })
        }
        </div>
        </div>
        </div>
    );
}


export default ProductItems
