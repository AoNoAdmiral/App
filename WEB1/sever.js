const express = require('express');
const admin = require('firebase-admin');
const bcrypt = require('bcrypt');
const path = require('path');
//firebase admin setup
const fetch = require('node-fetch');


let serviceAccount = require("./btlmtdt-firebase-adminsdk-yv68p-fe100e5c45.json");

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount)
});

let db = admin.firestore();

// aws config
const aws = require('aws-sdk');
const dotenv = require('dotenv');
const { S3 } = require('aws-sdk');

dotenv.config();

// aws parameters
const region ="ap-south-1";
const bucketName = "gym-website1";
const accessKeyId = process.env.AWS_ACCESS_KEY;
const secretAccessKey = process.env.AWS_SECRET_KEY;

aws.config.update({
    region,
    accessKeyId,
    secretAccessKey
})

// init s3 
const s3 = new aws.S3();

//generate image upload link
async function generateUrl(){
    let date = new Date();
    let id = parseInt(Math.random() * 10000000000);

    const imageName = `${id}${date.getTime()}.jpg`;
    const params = ({
        Bucket: bucketName,
        Key: imageName,
        Expires: 300,
        ContentType: 'image/jpeg'
    })
    const uploadUrl = await s3.getSignedUrlPromise('putObject', params);
    return uploadUrl;
}


// declare static path

//intializing express.js
const app = express();
var cors = require('cors')

app.use(cors())
//middlewares
app.use(express.json());

app.post('/test',function(req,res){
    res.header('Access-Control-Allow-Origin',"*");
    res.header('Access-Control-Allow-Methods','GET,PUT,POST,DELETE');
    res.header('Access-Control-Allow-Headers','Content-Type');
    return res.json({'alert': 'invalid number, please enter valid one'})
})

app.post('/signin',(req,res)=>{
    res.header('Access-Control-Allow-Origin',"*");
    res.header('Access-Control-Allow-Methods','GET,PUT,POST,DELETE');
    res.header('Access-Control-Allow-Headers','Content-Type');
    let{email,password} = req.body;

    if(!email.length || !password.length){
        return res.json({'status': 0,'alert' : 'fill your account'});
    }
    db.collection('users').doc(email).get()
    .then(user => {
        if(!user.exists){
            return res.json({'status': 0,'alert': 'log in email does not exists'})
        } else{
            bcrypt.compare(password, user.data().password, (err, result)=>{
                if(result){
                    let data = user.data();
                    return res.json({
                        'status': 1,
                        name: data.name,
                        email: data.email,
                        seller: data.seller,
                    })
                } else{
                    return res.json({'status': 0,'alert': 'password in incorrect'});
                }
            })
        }
    })
})

app.post('/signup',(req,res)=>{
    res.header('Access-Control-Allow-Origin',"*");
    res.header('Access-Control-Allow-Methods','GET,PUT,POST,DELETE');
    res.header('Access-Control-Allow-Headers','Content-Type');
    let { name, email, password,number} = req.body;
    //form validations
    if(name.length < 3){
        return res.json({'status': 0,'alert': 'name must be 3 letters long'});
    } else if(!email.length){
        return res.json({'status': 0,'alert': 'enter your mail'});
    } else if(password.length < 6){
        return res.json({'status': 0,'alert': 'password should be 8 letters long'});
    } else if(!number.length){
        return res.json({'status': 0,'alert': 'enter your phone number'});
    } else if(!Number(number) || number.length < 10){
        return res.json({'status': 0,'alert': 'invalid number, please enter valid one'});
    }

    //store user in db
    db.collection('users').doc(email).get()
    .then(user => {
        if(user.exists){
            return res.json({'status': 0,'alert' : 'email already exists'});
        } else {
            bcrypt.genSalt(10,(err, salt)=>{
               bcrypt.hash(password, salt, (err, hash)=>{
                   req.body.password = hash;
                   db.collection('users').doc(email).set(req.body)
                   .then(data => {
                       res.json({'status': 1,
                           name: req.body.name,
                           email: req.body.email,
                           seller: req.body.seller,
                       })
                   })
               })
            })
        }
    })
})

//routers
//router home
// app.get("/", (req, res) =>{
//     res.sendFile(path.join(staticPath, "index.html"));
// })

// //signup route
// app.get('/signup',(req,res)=>{
//     res.sendFile(path.join(staticPath,"signup.html"))
// })

// app.get('/test',(req,res)=>{
//     return res.json({'alert': 'invalid number, please enter valid one'});
// })

//login router
// app.get('/login', (req,res) => {
//     res.sendFile(path.join(staticPath, "Login.html"));
// })

// app.post('/login', (req,res)=>{
//     let{email,password} = req.body;

//     if(!email.length || !password.length){
//         return res.json({'alert' : 'fill your account'});
//     }
//     db.collection('users').doc(email).get()
//     .then(user => {
//         if(!user.exists){
//             return res.json({'alert': 'log in email does not exists'})
//         } else{
//             bcrypt.compare(password, user.data().password, (err, result)=>{
//                 if(result){
//                     let data = user.data();
//                     return res.json({
//                         name: data.name,
//                         email: data.email,
//                         seller: data.seller,
//                     })
//                 } else{
//                     return res.json({'alert': 'password in incorrect'});
//                 }
//             })
//         }
//     })
// })

// // seller route
// app.get('/seller', (req,res) =>{
//     res.sendFile(path.join(staticPath, "seller.html"));
// })

// app.post('/seller', (req,res)=>{
//     let {name,about,address,number,email}= req.body;
//     if(!name.length||!about.length||!address.length||number.length < 10|| !Number(number)){
//         return res.json({'alert' : 'some info is invalid'});
//     } else {
//         //update user seller status
//         db.collection('sellers').doc(email).set(req.body)
//         .then(data => {
//             db.collection('users').doc(email).update({
//                 seller: true
//             }) .then(data =>{
//                 res.json(true);
//             })
//         })
//     }
// })

// //add add-product
// app.get('/add-product', (req,res) =>{
//     res.sendFile(path.join(staticPath,"addProduct.html"));
// })

// app.get('/add-product/:id', (req,res) =>{
//     res.sendFile(path.join(staticPath,"addProduct.html"));
// })

// //add product
// app.get('/product', (req,res) =>{
//     res.sendFile(path.join(staticPath,"product.html"));
// })


// //get the upload link
// app.get('/s3url',(req,res)=>{
//     generateUrl().then(url => res.json(url));
// })

// // add product
// app.post('/add-product', (req,res)=>{
//     let { name, shortDes,des,images, actualPrice, discount, sellPrice, stock, tags, email, draft , id} = req.body;

//     // validation
//     if(!draft){
//         if(!name.length){
//             return res.json({ 'alert':'enter product name'});
//          } else if(shortDes.length>100 || shortDes.length <10){
//             return res.json({ 'alert':'short description must be between 10 to 100 letters long'});
//          } else if(!des.length){
//             return res.json({ 'alert':'enter detail description about the product'});
//          } else if (!images.length){
//             return res.json({ 'alert':'upload at least one product image'});
//          } else if (!actualPrice.length || !discount.length || !sellPrice.length){
//             return res.json({ 'alert':'you must add pricings'}); 
//          } else if (stock < 10){
//             return res.json({ 'alert':'you should have at least 10kg in stock'});
//          } else if (!tags.length){
//             return res.json({ 'alert':'enter few tags to help ranking your product in search'});
//          }
//     }

//      // add product
//      let docName = id == undefined ? `${name.toLowerCase()}-${Math.floor(Math.random()*5000)}` : id;
//      db.collection('products').doc(docName).set(req.body)
//      .then(data =>{
//          res.json({'product': name});
//      })
//      .catch(err =>{
//          return res.json({'alert': 'some error occured. Try again'});
//      })

// })

//get products
app.post('/get-products',(req, res)=>{
    res.header('Access-Control-Allow-Origin',"*");
    res.header('Access-Control-Allow-Methods','GET,PUT,POST,DELETE');
    res.header('Access-Control-Allow-Headers','Content-Type');
    docRef = db.collection('products')

    docRef.get()
    .then(products =>{
        if(products.empty){
            return res.json('no products');
        }
        let productArr = [];
        products.forEach(item =>{
                let data = item.data();
                data.id =item.id;
                productArr.push(data);
            })
        res.json(productArr);
    })
})

app.post('/addbill',(req, res)=>{
    res.header('Access-Control-Allow-Origin',"*");
    res.header('Access-Control-Allow-Methods','GET,PUT,POST,DELETE');
    res.header('Access-Control-Allow-Headers','Content-Type');
    let { email,order} = req.body;
    x = "order"+Math.floor(Math.random() * 1000);
    db.collection('order').doc(x).set(req.body)
                   .then(data => {
                       res.json({'status': 1})
                   })
})

// app.post('/delete-product', (req,res)=> {
//     let {id} = req.body;
//     db.collection('products').doc(id).delete()
//     .then(data =>{
//         res.json('success');
//     }).catch(err =>{
//         res.json('err');
//     })
// })

// // product page
// app.get('/products/:id', (req,res) =>{
//     res.sendFile(path.join(staticPath,"product.html"));
// })

// //404 router
// app.get('/404', (req,res)=>{
//     res.sendFile(path.join(staticPath, "404.html"));
// })

async function getUser() {
    const response = await fetch("https://io.adafruit.com/api/v2/Airforce/feeds/heat/data", {
        method: 'POST',
            headers: {
                  'Content-Type': 'application/json',
                  'Host': 'io.adafruit.com',
                  'X-AIO-Key':'aio_UGfg4715SOzuHZ5CiEhyKvrMv6ub'
            },
            body: JSON.stringify({
                "datum":{
                    "value":10
                }
            }),
      });
      const movies = await response.json();
      console.log(movies);
}


app.use((req,res)=>{
    console.log("Caught one");
})

app.listen(3005, ()=>{
    console.log('listening on port 3000 .........');
    getUser();
})