import React from 'react'
import FilterButtons from './Product/FilterButtons'
import Heading from './Product/Heading'
import ProductItems from './Product/ProductItems'

function Product() {
    return (
        <section className="products" id="products">

    <Heading/>

    <FilterButtons/>

    <ProductItems/>

</section>
    )
}

export default Product
