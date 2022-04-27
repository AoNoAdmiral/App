import React from 'react'
import ImageSlider from './ImageSlider'
import {Data1} from './Data1'

function Home() {
    return (
    <section className="home" id="home">
    <div className="swiper home-slider">
    <ImageSlider props={Data1}/>
    
    <div className="swiper-button-next"></div>
    <div className="swiper-button-prev"></div>
    <div>
        <a className='namẹhome'>GREENHOUSE 1</a>
    </div>
    </div>

</section>
    )
}


export default Home
