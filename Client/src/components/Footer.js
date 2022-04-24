import React from 'react'
import AboutUs from './Footer/AboutUs'
import Category from './Footer/Category'
import Credit from './Footer/Credit'
import ExtraLink from './Footer/ExtraLink'
import QuickLink from './Footer/QuickLink'
import Share from './Footer/Share'

function Footer() {
    return (
        <section className="footer">

    <div className="box-container">

       <AboutUs/>

        <Category/>

        <QuickLink/>

       <ExtraLink/>

    </div>

    <Share/>

    <Credit/>

</section>
    )
}

export default Footer
