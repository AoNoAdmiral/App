import React from 'react';
import Banner from './components/Banner';
import Home from './components/Home';
import Header from './components/Header';
import Product from './components/Product';
import Deal from './components/Deal';
import Feature from './components/Feature';
import Review from './components/Review';
import ContactUs from './components/ContactUs';
import Blog from './components/Blog';
import Footer from './components/Footer';
import axios from 'axios';
import {products} from './components/Product/Data';
const Mainpage = () =>{
    try {
        // console.log(JSON.parse(JSON.stringify(products)))
        // const localData = [];
        // for (let i = 0; i < products.length; i++) {
        //     localData.push(JSON.stringify(products[i]))
        // }
        // sessionStorage.setItem('Data',JSON.stringify(localData))
    //     let size = [];
    //     let loz = [];
    const localData = [];
    axios.post("http://localhost:3000/get-products", {

      })
      .then(function (response) {
        console.log(response['data'])
        for (let i = 0; i < response['data'].length; i++) {
            localData.push(JSON.stringify(response['data'][i]))
        }
        sessionStorage.setItem('Data',JSON.stringify(localData))
      })
      .catch(function (error) {
        console.log(error);
      });
        // const response = axios.get("http://localhost:3000/get-products").then(
        //     (res) => {
        //         console.log(1)
        //     }
        //     )
    //             for(const x in res.data.products){
    //                 const res2 = axios.get("http://localhost:3000/productitem/"+res.data.products[x]['id']).then( (ans)=>{
    //                     size = []
    //                     loz = []
    //                     for(const y in ans.data.productItems){
    //                         size.push(ans.data.productItems[y]['size'])
    //                         loz.push(ans.data.productItems[y]['img'])
    //                     }
    //                     localData.push(JSON.stringify({"0":res.data.products[x]['id'],"1":res.data.products[x]['name'],"2":res.data.products[x]['img'],"3":res.data.products[x]['price'],"5":"(50)","6":res.data.products[x]['feature'],"7":res.data.products[x]['description'],"8":JSON.stringify(size),"9":JSON.stringify(loz)}));
    //                 });  
    //             }
    //             // sessionStorage.setItem('Data',JSON.stringify(localData))
    //             setTimeout(()=>sessionStorage.setItem('Data',JSON.stringify(localData)),4000)
    //         })
    //         setTimeout(()=>sessionStorage.setItem('Data',JSON.stringify(localData)),4000)
      } catch (error) {
        console.log(error);
    }
    sessionStorage.setItem('Order',JSON.stringify([]));
    return (    
    <div className = "App">
        <Header/>
        <Home/>
        <Banner/>
        {/* <Product/> */}
        <Deal/>
        <Feature/>
        <Review/>
        <ContactUs/>
        <Blog/>
        <Footer/>
    </div>
     );
     
}

export default Mainpage;