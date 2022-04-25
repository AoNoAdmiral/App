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
var cors = require('cors');
const { time } = require('console');

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

async function getUser() {
    // const response = await fetch("https://io.adafruit.com/api/v2/Airforce/feeds/heat/data", {
    //     method: 'POST',
    //         headers: {
    //               'Content-Type': 'application/json',
    //               'Host': 'io.adafruit.com',
    //               'X-AIO-Key':'aio_UGfg4715SOzuHZ5CiEhyKvrMv6ub'
    //         },
    //         body: JSON.stringify({
    //             "datum":{
    //                 "value":10
    //             }
    //         }),
    //   });
    const response = await fetch("https://io.adafruit.com/api/v2/Airforce/feeds/heat/data?limit=1", {
        method: 'GET',
            headers: {
                  'Content-Type': 'application/json',
                  'Host': 'io.adafruit.com',
                  'X-AIO-Key':'aio_UGfg4715SOzuHZ5CiEhyKvrMv6ub'
            }
      });
      const movies = await response.json();
    return movies[0]['value']
}

async function getUser2() {
    const response = await fetch("https://io.adafruit.com/api/v2/Airforce/feeds/heat/data", {
        method: 'GET',
            headers: {
                  'Content-Type': 'application/json',
                  'Host': 'io.adafruit.com',
                  'X-AIO-Key':'aio_UGfg4715SOzuHZ5CiEhyKvrMv6ub'
            }
      });
    const movies = await response.json();
    const response2 = await fetch("https://io.adafruit.com/api/v2/Airforce/feeds/earthhumd/data", {
        method: 'GET',
            headers: {
                  'Content-Type': 'application/json',
                  'Host': 'io.adafruit.com',
                  'X-AIO-Key':'aio_UGfg4715SOzuHZ5CiEhyKvrMv6ub'
            }
      });
    const movies2 = await response2.json();
    const response3 = await fetch("https://io.adafruit.com/api/v2/Airforce/feeds/humd/data", {
        method: 'GET',
            headers: {
                  'Content-Type': 'application/json',
                  'Host': 'io.adafruit.com',
                  'X-AIO-Key':'aio_UGfg4715SOzuHZ5CiEhyKvrMv6ub'
            }
      });
    const movies3 = await response3.json();
}

//routers
//router home
app.get("/current", (req, res) =>{
    const x = getX();
})

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

app.use((req,res)=>{
    console.log("Caught one");
})

app.listen(3005, ()=>{
    console.log('listening on port 3000 .........');
})