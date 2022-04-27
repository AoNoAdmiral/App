import React from 'react'

function Category() {
    return (
        <div className="box">
        <h3>Garden House</h3>
        <a href="/#products" className="filterLink" data-filter="Garden 1"> <i className="fas fa-arrow-right"></i> Garden 1 </a>
        <a href="/#products" className="filterLink" data-filter="Garden 2"> <i className="fas fa-arrow-right"></i> Garden 2 </a>
        <a href="/#products" className="filterLink" data-filter="Garden 3"> <i className="fas fa-arrow-right"></i> Garden 3 </a>
        <a href="/#products" className="filterLink" data-filter="Garden 4"> <i className="fas fa-arrow-right"></i> Garden 4 </a>
        <a href="/#products" className="filterLink" data-filter="Garden 5"> <i className="fas fa-arrow-right"></i> Garden 5 </a>
    </div>
    )
}

export default Category
