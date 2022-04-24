import React from 'react'

function Banner() {
    return (
        <section className="banner-container">

        <div className="banner">
            <img src="image/shop_banner_img1.jpg" alt=""/> 
            <div className="content">
                <span>special offer</span>
                <h3>upto 50% off</h3>
                <a href="/#products" data-filter="special" className="filterLink btn">shop now</a>
            </div>
        </div>
        
        <div className="banner">
            <img src="image/shop_banner_img2.jpg" alt=""/>
            <div className="content">
                <span>special offer</span>
                <h3>upto 50% off</h3>
                <a href="/#products" data-filter="special" className="filterLink btn">shop now</a>
            </div>
        </div>
        
        </section>
    )
}

export default Banner
