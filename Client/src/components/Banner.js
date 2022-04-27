import React from 'react'

function Banner() {
    return (
        <section className="banner-container">

          <div class="sale">
          <div class="sale1">
          <div class="card">
            <img src="https://images.pexels.com/photos/2886937/pexels-photo-2886937.jpeg?cs=srgb&dl=pexels-mark-stebnicki-2886937.jpg&fm=jpg" alt="" class="card-imgage"/>            
              <div class="sale-user-left">
                <h4 class="sale-user-name">GREENHOUSE 1</h4>
                <i class="fa-temperature">30 ĐỘ</i>

              </div>
              <div class="sale-user-right">
                <div class="banner__sale-buynow">
                  <a href="#" class="header__menu-link btn btn--border btn--rounded">
                  Buy Now
                </a>
                </div>
              </div>            
          </div>
        </div>
        <div class="sale2">
          <div class="card">
            <img src="https://images.pexels.com/photos/736779/pexels-photo-736779.jpeg?cs=srgb&dl=pexels-iconcom-736779.jpg&fm=jpg" alt="" class="card-imgage"/>            
              <div class="sale-user-left">
                <h4 class="sale-user-name">LIME</h4>
                <p class="sale-user-detail">There are several species of citrus trees whose fruits are called limes</p>
              </div>
              <div class="sale-user-right">
                <div class="banner__sale-buynow">
                  <a href="#" class="header__menu-link btn btn--border btn--rounded">
                  Buy Now
                </a>
                </div>
              </div>            
          </div>
        </div>
          </div>


        </section>
    )
}

export default Banner
