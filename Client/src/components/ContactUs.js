import React from 'react'
import GetInTouch from './ContactUs/GetInTouch'
import Heading from './ContactUs/Heading'
import SellerInfo from './ContactUs/SellerInfo'

function ContactUs() {
    return (
        <section className="contact" id="contact">

    <Heading/>

   <SellerInfo/>

    <GetInTouch/>
</section>
    )
}

export default ContactUs
