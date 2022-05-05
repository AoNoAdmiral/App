import React,{useState,useEffect} from 'react'
import axios from 'axios'; 
function Banner() {
  const [dataHeat, setDataHeat] = useState("")
  const [dataHumd, setDataHumd] = useState("")
  const [dataEarth, setDataEarth] = useState("")
  let data = JSON.parse(sessionStorage.getItem('list'));
  if (JSON.parse(sessionStorage.getItem('list'))!=[]){
    let data = JSON.parse(sessionStorage.getItem('list'))
    console.log(data)
    data.forEach(x =>{
        axios.get("https://io.adafruit.com/api/v2/"+x['ID']+"/feeds/heat/data?limit=1", {
          }, {
            headers: {
              'Content-Type': 'application/json',
              'X-AIO-Key': x['Key']
            }
          })
        .then(function (response) {
          setDataHeat(response.data[0]['value'])
        });
        axios.get("https://io.adafruit.com/api/v2/"+x['ID']+"/feeds/humd/data?limit=1", {
          }, {
            headers: {
              'Content-Type': 'application/json',
              'X-AIO-Key': x['Key']
            }
          })
        .then(function (response) {
          setDataHumd(response.data[0]['value'])
        });
        axios.get("https://io.adafruit.com/api/v2/"+x['ID']+"/feeds/earth/data?limit=1", {
          }, {
            headers: {
              'Content-Type': 'application/json',
              'X-AIO-Key': x['Key']
            }
          })
          .then(function (response) {
            setDataEarth(response.data[0]['value'])
          });
        })
      }

  setInterval(() => {
    axios.get("https://io.adafruit.com/api/v2/Airforce/feeds/heat/data?limit=1", {
    }, {
      headers: {
        'Content-Type': 'application/json',
        'X-AIO-Key': sessionStorage.getItem('key')
      }
    })
  .then(function (response) {
    setDataHeat(response.data[0]['value'])
  });
  axios.get("https://io.adafruit.com/api/v2/Airforce/feeds/humd/data?limit=1", {
    }, {
      headers: {
        'Content-Type': 'application/json',
        'X-AIO-Key': sessionStorage.getItem('key')
      }
    })
  .then(function (response) {
    setDataHumd(response.data[0]['value'])
  });
  axios.get("https://io.adafruit.com/api/v2/Airforce/feeds/earth/data?limit=1", {
    }, {
      headers: {
        'Content-Type': 'application/json',
        'X-AIO-Key': sessionStorage.getItem('key')
      }
    })
    .then(function (response) {
      setDataEarth(response.data[0]['value'])
    });
    }, 30000);

    return (
        <section className="banner-container">   
        <div class="sale">
          {data.map(function(x,index){
            return(
              <div class="sale1">
              <div class="card">
                <img src="https://images.pexels.com/photos/2886937/pexels-photo-2886937.jpeg?cs=srgb&dl=pexels-mark-stebnicki-2886937.jpg&fm=jpg" alt="" class="card-imgage"/>            
                  <div class="sale-user-left">
                    <h4 class="sale-user-name">GREENHOUSE {index+1}</h4>
                    <p class="sale-user-detail">Khu vườn đang trồng các loại hoa quả....</p>
    
                    <div class="sale-user-detail">  
                    
                    <i class="fas fa-temperature-high">   :{dataHeat}</i>
                    
                    <i class="fas fa-cloud">   :{dataHumd}</i>
                   
                    <i class="fas fa-water">   :{dataEarth}</i>
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
            )
          })

          }
        
        {/* <div class="sale2">
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
        </div> */}
          </div>


        </section>
    )
}

export default Banner
