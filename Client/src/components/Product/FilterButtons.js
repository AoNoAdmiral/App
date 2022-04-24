import React from 'react'

function FilterButtons() {
    return (
        <div className="filter-buttons">
        <div className={'buttons active'}  data-filter="all">all</div>
        <div className={'buttons'} data-filter="arrivals">new arrivals</div>
        <div className={'buttons'} data-filter="featured">featured</div>
        <div className={'buttons'} data-filter="special">special offer</div>
        <div className={'buttons'} data-filter="seller">best seller</div>
        <div className={'buttons'} data-filter="men">Fruit</div>
        <div className={'buttons'} data-filter="female">Vegetables</div>
    </div>
    )
}

export default FilterButtons
