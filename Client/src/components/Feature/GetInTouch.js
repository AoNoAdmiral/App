import React,{useState,useEffect} from 'react'
import axios from 'axios'


function check(text) {
    let pattern = /[^0-9-:]/
    let result = pattern.test(text)
    return result
}

function checkFormat(formSettingConfig, formTime) {
    var formElement = document.querySelector(formSettingConfig)
    var inputElement = formElement.querySelector('#temperature')
    if (inputElement) {
        var waringFormat1 = formElement.querySelector('#warning1')
        inputElement.onblur = function () {
            if (check(inputElement.value)) {
                waringFormat1.innerText = "Vui lòng nhập đúng định dạng aa-bb"
            }
            else if (inputElement.value == '') {
                waringFormat1.innerText = "Vui lòng nhập dòng này"
            }
            else {
                waringFormat1.innerText = ""
            }
        }
    }
    var inputElement2 = formElement.querySelector('#earth')
    if (inputElement2) {
        var waringFormat2 = formElement.querySelector('#warning3')
        inputElement2.onblur = function () {
            if (check(inputElement2.value)) {
                waringFormat2.innerText = "Vui lòng nhập đúng định dạng aa-bb"
            }
            else if (inputElement2.value == '') {
                waringFormat2.innerText = "Vui lòng nhập dòng này"
            }
            else {
                waringFormat2.innerText = ""
            }
        }
    }
    var inputElement3 = formElement.querySelector('#humd')
    if (inputElement3) {
        var waringFormat3 = formElement.querySelector('#warning2')
        inputElement3.onblur = function () {
            if (check(inputElement3.value)) {
                waringFormat3.innerText = "Vui lòng nhập đúng định dạng aa-bb"
            }
            else if (inputElement3.value == '') {
                waringFormat3.innerText = "Vui lòng nhập dòng này"
            }
            else {
                waringFormat3.innerText = ""
            }
        }
    }
    var formElement1 = document.querySelector(formTime)
    var inputElement4 = formElement1.querySelector('#time1')
    if (inputElement4) {
        var waringFormat4 = formElement1.querySelector('#warning4')
        inputElement4.onblur = function () {
            console.log(inputElement4.value)
            if (check(inputElement4.value)) {
                waringFormat4.innerText = "Vui lòng nhập đúng định dạng aa-bb"
            }
            else if (inputElement4.value == '') {
                waringFormat4.innerText = "Vui lòng nhập dòng này"
            }
            else {
                waringFormat4.innerText = ""
            }
        }
    }

    var inputElement5 = formElement1.querySelector('#time2')
    if (inputElement5) {
        var waringFormat5 = formElement1.querySelector('#warning5')
        inputElement5.onblur = function () {
            if (check(inputElement5.value)) {
                waringFormat5.innerText = "Vui lòng nhập đúng định dạng aa-bb"
            }
            else if (inputElement5.value == '') {
                waringFormat5.innerText = "Vui lòng nhập dòng này"
            }
            else {
                waringFormat5.innerText = ""
            }
        }
    }
}

function handleInputConfigSetting(){
    checkFormat("#form1", "#formTime");
    var heat = 0
    var humd = 0
    var earth = 0
    if(document.getElementById("humd").value){
        humd = document.getElementById("humd").value
    }
    console.log(humd)
    if(document.getElementById("temperature").value){
        heat = document.getElementById("temperature").value
    }
    if(document.getElementById("earth").value){
        earth = document.getElementById("earth").value
    }
    // update Tuoi nuoc ( Doi watering qua conditionheat/humd/earth va value thanh gia tri tuong ung)
    axios.post("https://io.adafruit.com/api/v2/Airforce/feeds/conditionalhumd/data",{
           "datum":{
               "value":humd
               }
    },{             
    headers: {
      'Content-Type': 'application/json',
      'X-AIO-Key':sessionStorage.getItem('key')
    }
  })

    axios.post("https://io.adafruit.com/api/v2/Airforce/feeds/conditionheat/data",{
           "datum":{
               "value":heat
               }
    },{             
    headers: {
      'Content-Type': 'application/json',
      'X-AIO-Key':sessionStorage.getItem('key')
    }
  })

    axios.post("https://io.adafruit.com/api/v2/Airforce/feeds/conditionalearth/data",{
           "datum":{
               "value":earth
               }
    },{             
    headers: {
      'Content-Type': 'application/json',
      'X-AIO-Key':sessionStorage.getItem('key')
    }
  })
  
}

function handleInputWateringTime(){
    checkFormat("#form1", "#formTime");
    var time1 = 0
    var time2 = 0
    if(document.getElementById("time1").value){
        time1 = document.getElementById("time1").value
    }
    if(document.getElementById("time2").value){
        time2 = document.getElementById("time2").value
    }
   
    // update Tuoi nuoc ( Doi watering qua conditionheat/humd/earth va value thanh gia tri tuong ung)
    axios.post("https://io.adafruit.com/api/v2/Airforce/feeds/mark1/data",{
           "datum":{
               "value":time1
               }
    },{             
    headers: {
      'Content-Type': 'application/json',
      'X-AIO-Key':sessionStorage.getItem('key')
    }
  })

    axios.post("https://io.adafruit.com/api/v2/Airforce/feeds/mark2/data",{
           "datum":{
               "value":time2
               }
    },{             
    headers: {
      'Content-Type': 'application/json',
      'X-AIO-Key':sessionStorage.getItem('key')
    }
  })

}

function GetInTouch() {

    const [conditionalHumd, setConditionalHumd] = useState("");
    const [conditionHeat, setConditionHeat] = useState("");
    const [conditionalEarth, setConditionalEarth] = useState("");
    // // lay data dk
    
    useEffect(() => {
        axios.get("https://io.adafruit.com/api/v2/Airforce/feeds/conditionheat/data?limit=1").then((response) => {
            setConditionHeat(response.data[0]['value']);
            document.getElementById("temperature").value = response.data[0]['value'];
        });
        }, []);

    useEffect(() => {
        axios.get("https://io.adafruit.com/api/v2/Airforce/feeds/conditionalearth/data?limit=1").then((response) => {
            setConditionalEarth(response.data[0]['value']);
            document.getElementById("earth").value = response.data[0]['value'];
        });
        }, []);

    useEffect(() => {
        axios.get("https://io.adafruit.com/api/v2/Airforce/feeds/conditionalhumd/data?limit=1").then((response) => {
            setConditionalHumd(response.data[0]['value']);
            document.getElementById("humd").value = response.data[0]['value'];
        });
        }, []);

    useEffect(() => {
            axios.get("https://io.adafruit.com/api/v2/Airforce/feeds/mark1/data?limit=1").then((response) => {
                document.getElementById("time1").value = response.data[0]['value'];
            });
            }, []);

    useEffect(() => {
                axios.get("https://io.adafruit.com/api/v2/Airforce/feeds/mark2/data?limit=1").then((response) => {
                    document.getElementById("time2").value = response.data[0]['value'];
                });
                }, []);        
        return (
        <div className="row">

            <form action="" id="form1">
                <h3 className="centerH3">Thông số nhà kính</h3>
                <div className="inputBox">
                    <label className="labelSetting">Nhiệt độ (Đơn vị: 0c):</label>
                    <input type="text" placeholder="Ex: 20-25" id="temperature"></input>
                </div>
                <span className="waringFormat" id="warning1"></span>
                <div className="inputBox">
                    <label className="labelSetting">Độ ẩm không khí (Đơn vị: %):</label>
                    <input type="text" placeholder="Ex: 20-25" id="humd"></input>
                </div>
                <span className="waringFormat" id="warning2"></span>
                <div className="inputBox">
                    <label className="labelSetting">Độ ẩm của đất (Đơn vị: %):</label>
                    <input type="text" placeholder="Ex: 20-25" id="earth"></input>
                </div>
                <span className="waringFormat" id="warning3"></span>
                <input type="button" value="Lưu" className="btn" onClick={() => handleInputConfigSetting()}></input>
            </form>

            <form action="" id="formTime">
                <h3 className="centerH3">Thời gian tự động tưới nước</h3>
                <div className="inputBox">
                    <label className="labelSetting">Thời gian tưới nước 1:</label>
                    <input type="text" placeholder="Ex: 7:25" id="time1"></input>
                </div>
                <span className="waringFormat" id="warning4"></span>
                <div className="inputBox">
                    <label className="labelSetting">Thời gian tưới nước 2:</label>
                    <input type="text" placeholder="Ex: 7:25" id="time2"></input>
                </div>
                <span className="waringFormat" id="warning5"></span>
                <input type="button" value="Lưu" className="btn" onClick={() => handleInputWateringTime()}></input>
            </form>
        </div>
    )
}

export default GetInTouch
