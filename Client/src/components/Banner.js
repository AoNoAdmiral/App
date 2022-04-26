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
                <p class="sale-user-detail">Khu vườn đang trồng các loại hoa quả....</p>

                <div class="sale-user-detail">  
                
                <i class="fas fa-temperature-high">   :30</i>
                
                <i class="fas fa-cloud">   :30</i>
               
                <i class="fas fa-water">   :30</i>
                </div>
              

              </div>
              <div class="sale-user-right">
                <div class="banner__sale-buynow">
                  <a href="/payment" class="header__menu-link btn btn--border btn--rounded">
                  Visit Now
                </a>
                </div>
              </div>            
          </div>
        </div>
        <div class="sale2">
          <div class="card">
            <img src="https://images.pexels.com/photos/736779/pexels-photo-736779.jpeg?cs=srgb&dl=pexels-iconcom-736779.jpg&fm=jpg" alt="" class="card-imgage"/>            
              <div class="sale-user-left">
                <h4 class="sale-user-name">GREENHOUSE 2</h4>
                <p class="sale-user-detail">Khu vườn đang trồng các loại hoa quả....</p>

                <div class="sale-user-detail">  

                <i class="fas fa-temperature-high">   :30</i>

                <i class="fas fa-cloud">   :30</i>

                <i class="fas fa-water">   :30</i>
                </div>
              </div>
              <div class="sale-user-right">
                <div class="banner__sale-buynow">
                  <a href="#" class="header__menu-link btn btn--border btn--rounded">
                  Visit Now
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
