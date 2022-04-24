import React,{useState} from 'react'
import axios from 'axios';
export default function Login(){
    const [loginState,setLogin]=useState(0)
    const [loginEmail, setEmail] = useState("");
    const [loginPW, setPw] = useState("");
    const [loginName, set1] = useState("");
    const [loginPhone, set2] = useState("");
    const [loginEmail2, set3] = useState("");
    const [loginPW2, set4] = useState("");
    function onChangeUsername(event){
      setEmail(event.target.value);
    }
    function showAlert(msg){
      let alertBox = document.querySelector('.alert-box');
      let alertMsg = document.querySelector('.alert-msg');
      alertMsg.innerHTML = msg;
      alertBox.classList.add('show');
      setTimeout(()=>{
          alertBox.classList.remove('show');
      },3000);
    }
    function onChangePW(event){
      setPw(event.target.value);
    }
    function onChange1(event){
      set1(event.target.value);
    }
    function onChange2(event){
      set2(event.target.value);
    }
    function onChange3(event){
      set3(event.target.value);
    }
    function onChange4(event){
      set4(event.target.value);
    }
    function createsubmit(){
        axios.post("http://localhost:3000/signup", {
          name: loginName,
          email: loginEmail2,
          password: loginPW2,
          number: loginPhone
        })
        .then(function (response) {
          if(response.data.status == 0)
            showAlert(response.data.alert)
          else{
            sessionStorage.setItem('email',loginEmail); 
            window.location = "/";
        }
        })
        .catch(function (error) {
          console.log(error);
        });
    }
    function login(){
      axios.post("http://localhost:3000/signin", {
        email: loginEmail,
        password: loginPW,
      })
      .then(function (response) {
        if(response.data.status == 0)
          showAlert(response.data.alert)
        else{
          sessionStorage.setItem('email',loginEmail); 
          window.location = "/";
        }
      })
      .catch(function (error) {
        console.log(error);
      });
  }
    return(
        <div className="Page">
        <img src="images/loader.gif" className="loader" alt=""/>
    
        <div className="alert-box">
            <img src="https://i.imgur.com/7kl9riE.jpg" className="alert-img" alt=""/>
            <p className="alert-msg">Error message</p>
        </div>

        <div className="signup">
            <span className="or">Or</span>
            <div className="left1">
                {loginState===0?
                <div>
                <form> 
                    <div className="form-inner">
                        <div className="form-group">
                            {/* <label for="">Email address</label> */}
                            <input type="text" className="INPUS" placeholder="Enter your Email" onChange={onChangeUsername} name="email" />
                        </div>
                        <div className="form-group">
                            {/* <label for="">Password</label> */}
                            <input type="password" placeholder="Enter your password" onChange={onChangePW} name="password" />
                        </div>
                    </div>
                    <p className="remember"><input type="checkbox" /> <span>Remember me</span></p>
                    <p className="member"> New user? <a onClick={()=>setLogin(1)}>Create an account</a></p>
                </form> <button className="submit-btn1" onClick={()=>login()}>Log in</button> </div>:""
                }
                {loginState===1?<div>
                <form>
                <div class="form-inner">
                <div class="form-group">
                    <label for="">Name</label>
                    <input type="text" className="INPUS" placeholder="Enter your name" autocomplete="off" name="name" onChange={onChange1}/>
                </div>
                <div class="form-group">
                    <label for="">Phone</label>
                    <input type="text" className="INPUS" placeholder="Enter your phone" autocomplete="off" name="number" onChange={onChange2}/>
                </div>
                <div class="form-group">
                    <label for="">Email address</label>
                    <input type="email" className="INPUS" placeholder="Enter your email" autocomplete="off" name="email"  onChange={onChange3}/>
                </div>
                <div class="form-group">
                    <label for="">Password</label>
                    <input type="password" className="INPUS" placeholder="Create your password" autocomplete="off" name="password"  onChange={onChange4}/>
                </div>
                </div>
                <p class="remember">
                    <input type="checkbox" /> <span>Remember me</span>
                </p>
                <p class="member"> Are you a member ? <a onClick={()=>setLogin(0)}>Login now</a></p>
                </form><button class="submit-btn" onClick={()=>createsubmit()}>Create an account</button></div>:""
                }
            </div>
            <div className="right">
              <ul>
                <li className="facebook">
                  <a href="#" onClick={()=>alert(loginEmail)}>
                  <i className="fas fa-user" aria-hidden="true"></i>
                    <span>Connect with facebook</span>
                  </a>
                </li>
                <li className="twitter">
                  <a href="#">
                  <i className="fas fa-user" aria-hidden="true"></i>
                    <span>Connect with twitter</span>
                  </a>
                </li>
                <li className="google">
                  <a href="#">
                    <i className="fas fa-user" aria-hidden="true"></i>
                    <span>Connect with google</span>
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </div>
    
        )
}