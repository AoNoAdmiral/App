import React from 'react'
import FeaturedProducts from './Feature/FeaturedProducts'
import Heading from './Feature/Heading'
import GetInTouch from './Feature/GetInTouch'

function Feature() {
    return (
        <section className="featured" id="featured">

    <Heading/>

    <FeaturedProducts/>
   <section className="contact" id="contact">

    <GetInTouch></GetInTouch>
        </section>
</section>
    )
}

export default Feature
