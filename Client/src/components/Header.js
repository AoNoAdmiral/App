import React from 'react'
import Brand from './Header/Brand'
import NavBar from './Header/NavBar'
import Icons from './Header/Icons'
import SearchBox from './Header/SearchBox'

function Header() {
    return (
        <header className="header">
    
    {/*Logo + Ten Thuong Hieu */}
    <Brand/>

    {/*Thanh Dieu Huong */}
   <NavBar/>

   {/*Icon tim kiem, cart, thong tin ca nha */}
   <Icons/>

    {/*Hop tim kiem */}
   <SearchBox/>

</header>
    )
}

export default Header
