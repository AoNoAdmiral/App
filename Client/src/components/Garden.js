import React from 'react'

function Garden() {
    return (
<section className="bestseller" id="garden">
    <div class="bestseller__name">
          <h2 class="name">Properties</h2>
          <p class="line__name"></p>
    </div>

    <div class="container">
          <ul class="bestseller__list">
            <li class="bestseller__item">
              <img src="https://i.pinimg.com/564x/94/e7/c6/94e7c6c46ff8a1a2a002f3b17c332573.jpg" alt="" class="bestseller__image" />
              <h3 class="bestseller__name">TEMPERATURE</h3>
              <a href="product.html" data-filter="mango-188" class="bestseller__details">
               <i class="fas fa-temperature-high">   :30</i>
              </a>
            </li>
            <li class="bestseller__item">
              <img src="https://i.pinimg.com/564x/94/e7/c6/94e7c6c46ff8a1a2a002f3b17c332573.jpg" alt="" class="bestseller__image" />
              <h3 class="bestseller__name">TEMPERATURE</h3>
              <a href="product.html" data-filter="lemon-4094" class="bestseller__details">
              <i class="fas fa-cloud">   :30</i>
              </a>
            </li>
            <li class="bestseller__item">
              <img src="https://i.pinimg.com/564x/94/e7/c6/94e7c6c46ff8a1a2a002f3b17c332573.jpg" alt="" class="bestseller__image" />
              <h3 class="bestseller__name">TEMPERATURE</h3>
              <a href="product.html" data-filter="coconut-2989" class="bestseller__details">
              <i class="fas fa-water">   :30</i>
              </a>
            </li>
            <li class="bestseller__item">
              <img src="https://i.pinimg.com/564x/94/e7/c6/94e7c6c46ff8a1a2a002f3b17c332573.jpg" alt="" class="bestseller__image" />
              <h3 class="bestseller__name">TEMPERATURE</h3>
              <a href="product.html" data-filter="tangerines-274" class="bestseller__details">
              <i class="fas fa-water">   :30</i>
              </a>
            </li>
          </ul>
        </div>
    
</section>
    )
}

export default Garden