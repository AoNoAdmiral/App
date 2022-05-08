import React,{useState,useEffect} from 'react'
import axios from 'axios'; 
function Garden() {
  const [dataHeat, setDataHeat] = useState("")
  const [dataHumd, setDataHumd] = useState("")
  const [dataEarth, setDataEarth] = useState("")
  const [dataWater, setDataWater] = useState(0)
  let data = JSON.parse(sessionStorage.getItem('list'));
        axios.get("https://io.adafruit.com/api/v2/Airforce/feeds/heat/data?limit=1", {
          }, {
            headers: {
              'Content-Type': 'application/json',
              'X-AIO-Key':  sessionStorage.getItem('key')
            }
          })
        .then(function (response) {
          setDataHeat(response.data[0]['value'])
        });
        axios.get("https://io.adafruit.com/api/v2/Airforce/feeds/humd/data?limit=1", {
          }, {
            headers: {
              'Content-Type': 'application/json',
              'X-AIO-Key':  sessionStorage.getItem('key')
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

  setInterval(() => {
    axios.get("https://io.adafruit.com/api/v2/Airforce/feeds/heat/data?limit=1", {
    }, {
      headers: {
        'Content-Type': 'application/json',
        'X-AIO-Key': sessionStorage.getItem('key')
      }
    })
  .then(function (response) {
    console.log(response.data[0]['value'])
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
    axios.get("https://io.adafruit.com/api/v2/Airforce/feeds/watering/data?limit=1", {
    }, {
      headers: {
        'Content-Type': 'application/json',
        'X-AIO-Key': sessionStorage.getItem('key')
      }
    })
    .then(function (response) {
      setDataWater(response.data[0]['value'])
    });
    }, 5000);
    return (
<section className="bestseller" id="garden">
    <div class="bestseller__name">
          <h2 class="name">Properties</h2>
          <p class="line__name"></p>
    </div>

    <div class="container">
          <ul class="bestseller__list">
            <li class="bestseller__item">
              <img src="https://i.imgur.com/fFhEhfl.png" alt="" class="bestseller__image" />
              <h3 class="bestseller__name">TEMPERATURE</h3>
              <a href="product.html" data-filter="mango-188" class="bestseller__details">
               <i class="fas fa-temperature-high">   :{dataHeat} °C</i>
              </a>
            </li>
            <li class="bestseller__item">
              <img src="https://i.imgur.com/0YjERwC.png" alt="" class="bestseller__image" />
              <h3 class="bestseller__name">AIR HUMIDITY</h3>
              <a href="product.html" data-filter="lemon-4094" class="bestseller__details">
              <i class="fas fa-cloud">   :{dataHumd} %</i>
              </a>
            </li>
            <li class="bestseller__item">
              <img src="https://i.imgur.com/VLfKuTT.png" alt="" class="bestseller__image" />
              <h3 class="bestseller__name">EARTH HUMIDITY</h3>
              <a href="product.html" data-filter="coconut-2989" class="bestseller__details">
              <i class="fas fa-water">   :{dataEarth} %</i>
              </a>
            </li>
            <li class="bestseller__item">
              <img src="https://i.imgur.com/H0hPPmf.png" alt="" class="bestseller__image" />
              <h3 class="bestseller__name">WATERING</h3>
              <a href="product.html" data-filter="tangerines-274" class="bestseller__details">
              <i class="fas fa-water">   :{dataWater==1?"ON":"OFF"}</i>
              </a>
            </li>
          </ul>
        </div>
    
</section>
    )
}

export default Garden