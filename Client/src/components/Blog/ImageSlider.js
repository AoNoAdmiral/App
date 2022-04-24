import React,{useState} from 'react'

const ImageSlider = ({props}) => {
    return(
        <div className="swiper-wrapper">
            {props.map((props)=>{
            return(
            <div className="swiper-slide slide">
              <div >
                <div className="image">
                    <img src={props.img} alt=""/>
                </div>
                <div className="content">
                    <h3>{props.title}</h3>
                    <p>{props.Para}</p>
                    <a href="#" className="btn">read more</a>
                    <div className="icons">
                        <a href="#"> <i className="fas fa-calendar"></i> {props.Time} </a>
                        <a href="#"> <i className="fas fa-user"></i> by {props.User} </a>
                    </div>
                </div>
                </div>
            </div>
            )})}
        </div>
    )
}
export default ImageSlider