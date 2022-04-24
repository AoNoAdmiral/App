import React,{useState} from 'react'
function toggleFlag(index){
    let x = document.querySelectorAll(`.flag-${index}`)
    let a = 0;
    x.forEach(item=> {
        a ++;
        item.classList.toggle('active');
    }
    )
}
const ImageSlider = ({props}) => {
    function buyItem(props,index){
        if (!sessionStorage.getItem('id')){
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
        x.push(JSON.stringify({1:props[1],2:props[2],3:props[3],4:1}));
        sessionStorage.setItem('Order',JSON.stringify(x));  
    }
    return(
        <div className="swiper-wrapper">
            {props.map((x,index)=>{
                let data= JSON.parse(x);
            return(
            <div className="swiper-slide slide">
            <div>
                <div className="icons">
                    <a className="fas fa-shopping-cart" onClick={()=>buyItem(data,0)}></a>
                    <a className = {`flag-${index} fas fa-heart heart`} onClick={ ()=> toggleFlag(index) }></a>
                    <a href="#products" className="fas fa-eye"></a>
                </div>
                <div className="image">
                    <img src={data[2]} alt=""/>
                </div>
                <div className="content">
                    <h3>{data[1]}</h3>
                        <div className="price">
                            <div className="amount">{data[3]} VND</div>
                            {/* <div className="cut">{data[4]}</div>
                            <div className="offer">{data[5]}</div> */}
                        </div>
                        <div className="stars">
                            <i className="fas fa-star"></i>
                            <i className="fas fa-star"></i>
                            <i className="fas fa-star"></i>
                            <i className="fas fa-star"></i>
                            <i className="far fa-star"></i>
                            <span>{data[5]}</span>
                        </div>
                </div>
            </div>
            </div>
            )})}
        </div>
    )
}
export default ImageSlider
