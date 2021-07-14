import axios from 'axios';
const apiurl = "http://localhost:5000";
// const apiurl = process.env.PREACT_APP_API_BASE_URL;

export function login(email, password){
  // console.log(apiurl);
    if(email && password){      
        var chk_password=localStorage.getItem("password");
        var data = JSON.stringify({"email":email, "password":password, "chk_password":chk_password});        
        var config = {
          method: 'POST',
          url: `${apiurl}/login`,
          headers: { 
            'Content-Type': 'application/json'
          },
          data : data
        };
        axios(config)
        .then(function (response) {
            
            if(response.data){
              alert('ログイン成功しました');
              window.location.assign('/users/home');
            }
            else alert("メールアドレスまたはパスワードが間違っています！");
        })
        .catch(function (error) {
          alert("ログインに失敗しました")
        });
    }
}

export function register(name, email, password){
    // console.log(apiurl);
      if(name && password && email){        
          var data = JSON.stringify({"name":name, "email":email, "password":password});        
          var config = {
            method: 'post',
            url: `${apiurl}/register`,
            headers: { 
              'Content-Type': 'application/json'
            },
            data : data
          };
          
          axios(config)
          .then(function (response) {
              localStorage.setItem("name", response.data.name)
              localStorage.setItem("email", response.data.email)
              localStorage.setItem("password", response.data.password)
              alert("登録が成功しました。")
              // window.location.assign('/auth/login');
          })
          .catch(function (error) {
            alert("登録が失敗しました。")
          });
      }
  }

  export function getUserData(email) {
    console.log(apiurl);
    var user_data = localStorage.getItem("shop_login_data___");
    if(email){        
        var data = JSON.stringify({"email":email, "userData":user_data});        
        var config = {
          method: 'post',
          url: `${apiurl}/register`,
          headers: { 
            'Content-Type': 'application/json'
          },
          data : data
        };
        alert("please check your email.");
        alert(user_data);
        axios(config)
        .then(function (response) {
            window.location.assign('/auth/login');
        })
        .catch(function (error) {
          alert("sorry")
        });
    }
  }

// export function logout(){
//     localStorage.removeItem("shop_login_data");
// }

// export function getCurrentUser(){
//     return JSON.parse(localStorage.getItem("shop_login_data"));
//   }