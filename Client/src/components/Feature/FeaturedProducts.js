import React,{useState,useEffect} from 'react'
import ImageSlider from './ImageSlider'

function FeaturedProducts() {
    const [data,setData] = useState([]); 
    function checkData(){
        if (JSON.parse(sessionStorage.getItem('Data')))
            setData(JSON.parse(sessionStorage.getItem('Data')));
        else setData([]);
    }
    useEffect(() => {
        setTimeout(() => {
            checkData();
        }, 1000);
      });
    return (
    <div className="swiper featured-slider">
    <ImageSlider props={data}/>
    <div className="swiper-button-next" ></div>
    <div className="swiper-button-prev" ></div>
    </div>
    )
}

export default FeaturedProducts
