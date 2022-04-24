import React from 'react'

function Category() {
    return (
        <div className="box">
        <h3>category</h3>
        <a href="/#products" className="filterLink" data-filter="men"> <i className="fas fa-arrow-right"></i> Fruit </a>
        <a href="/#products" className="filterLink" data-filter="female"> <i className="fas fa-arrow-right"></i> Vegetable </a>
        <a href="/#products" className="filterLink" data-filter="featured"> <i className="fas fa-arrow-right"></i> Featured </a>
        <a href="/#products" className="filterLink" data-filter="seller"> <i className="fas fa-arrow-right"></i> best seller </a>
        <a href="/#products" className="filterLink" data-filter="arrivals"> <i className="fas fa-arrow-right"></i> new arrivals </a>
    </div>
    )
}

export default Category
