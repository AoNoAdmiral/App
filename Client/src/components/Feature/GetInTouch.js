import React from 'react'

function check(text) {
    let pattern = /[^0-9-:]/
    let result = pattern.test(text)
    return result
}

function checkFormat(formSettingConfig, formTime) {
    var formElement = document.querySelector(formSettingConfig)
    var inputElement = formElement.querySelector('#temperature')
    if(inputElement){
        var waringFormat1 = formElement.querySelector('#warning1')
        inputElement.onblur = function (){
            if(check(inputElement.value)){
                waringFormat1.innerText = "Vui lòng nhập đúng định dạng aa-bb"
            }
            else if (inputElement.value == ''){
                waringFormat1.innerText = "Vui lòng nhập dòng này"
            }
            else{
                waringFormat1.innerText = ""
            }
        }
    }
    var inputElement2 = formElement.querySelector('#earth')
    if(inputElement2){
        var waringFormat2 = formElement.querySelector('#warning3')
        inputElement2.onblur = function (){
            if(check(inputElement2.value)){
                waringFormat2.innerText = "Vui lòng nhập đúng định dạng aa-bb"
            }
            else if (inputElement2.value == ''){
                waringFormat2.innerText = "Vui lòng nhập dòng này"
            }
            else{
                    waringFormat2.innerText = ""
                }
        }
    }
    var inputElement3 = formElement.querySelector('#humd')
    if(inputElement3){
        var waringFormat3 = formElement.querySelector('#warning2')
        inputElement3.onblur = function (){
            if(check(inputElement3.value)){
                waringFormat3.innerText = "Vui lòng nhập đúng định dạng aa-bb"
            }
            else if (inputElement3.value == ''){
                waringFormat3.innerText = "Vui lòng nhập dòng này"
            }
            else{
                    waringFormat3.innerText = ""
                }
        }
    } 
    var formElement1 = document.querySelector(formTime)
    var inputElement4 = formElement1.querySelector('#time1')
    if(inputElement4){
        var waringFormat4 = formElement1.querySelector('#warning4')
        inputElement4.onblur = function (){
            console.log(inputElement4.value)
            if(check(inputElement4.value)){
                waringFormat4.innerText = "Vui lòng nhập đúng định dạng aa-bb"
            }
            else if (inputElement4.value == ''){
                waringFormat4.innerText = "Vui lòng nhập dòng này"
            }
            else{
                    waringFormat4.innerText = ""
                }
        }
    } 

    var inputElement5 = formElement1.querySelector('#time2')
    if(inputElement5){
        var waringFormat5 = formElement1.querySelector('#warning5')
        inputElement5.onblur = function (){
            if(check(inputElement5.value)){
                waringFormat5.innerText = "Vui lòng nhập đúng định dạng aa-bb"
            }
            else if (inputElement5.value == ''){
                waringFormat5.innerText = "Vui lòng nhập dòng này"
            }
            else{
                    waringFormat5.innerText = ""
                }
        }
    } 
}

function GetInTouch() {
    return (
        <div className="row">

        <form action=""  id="form1">
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
            <input type="submit" value="Lưu" className="btn"  onClick={()=>checkFormat("#form1", "#formTime")}></input>
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
            <input type="submit" value="Lưu" className="btn" onClick={()=>checkFormat("#form1", "#formTime")}></input>
        </form>
    </div>
    )
}

export default GetInTouch