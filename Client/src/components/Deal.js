import React from 'react'

function Deal() {
    return (
        <section className="deal">

    <div className="image">
        <img src="image/tranding_img.png" alt=""/>
    </div>

    <div className="content">
        <span>Have a good day!</span>
        <h3>The weather is very nice today</h3>
        <p>The seeds are growing very well</p>
        <a href="/#products" className="filterLink btn" data-filter="special">Visit now</a>
    </div>

</section>
    )
}

export default Deal
