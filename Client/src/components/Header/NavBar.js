import React from 'react'

function NavBar() {
    return (
        <nav className="navbar">
        <a href="\">home</a>
        <a href="#banner">Our Garden</a>
        <a href="#featured">Action</a>
        {/* <a href="#review">review</a> */}
        <a href="#contact">Contact Us</a>
        <a href="#blogs">Blogs</a>
    </nav>
    )
}

export default NavBar
