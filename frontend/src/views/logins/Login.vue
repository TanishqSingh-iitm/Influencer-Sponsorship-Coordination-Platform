<script setup>
import LandingTopbar from '../../components/LandingTopbar.vue'
</script>

<template>
<div class="navig">
<LandingTopbar />
</div>
<div class="login">
<div> 
    <h1 align="center" style="font-family: cursive;"> Welcome To CreativeMerge</h1>
    <h2 class="display-5" align="center">Login Portal</h2>
</div>
</div>
<div class="container" >
    <div class="logoavatar">
    <img src="../../assets/logo.png" alt="logo" class="avatar">
    </div>
    <form>
        <div class="form-group" style="margin-bottom: 10px;">
           
            <label for="username" class="form-label" style="font-size: 25px;"><span class="mdi mdi-account"></span> UserName </label> 
            <input type="text" name="username" pattern="[a-zA-Z0-9_]+|[^@]+@[^@]+\.[a-zA-Z]{2,}" placeholder="Enter your Username/Email" required class="form-control" style="border-radius: 60px; font-size: 15px;" v-model="username">
        </div>
        <div class="form-group" style="margin-bottom: 10px;">
            <label for="password" class="form-label" style="font-size: 25px;"><span class="mdi mdi-form-textbox-password"></span> Password</label>
            <input type="password" name="password" placeholder="Enter your Password" required class="form-control" style="border-radius: 60px;" v-model="password">
        </div><br>
        <button type="submit" id="submission" class="btn" style=" "  @click.prevent="validateform">Sign In <span class="mdi mdi-login"></span></button>
    </form>
</div>
<div style="background-color: #333; color: white; text-align: center; position: relative; bottom: 0; left: 0; width: 100%; font-family: 'Doto', sans-serif; font-optical-sizing: auto; font-weight: 1000; font-style: normal; font-variation-settings: 'ROND' 100; font-size: 1.1rem; height: 50px;">
  <p align="center" style="margin: 0; line-height: 50px;">© 2024 | © 21F3001516 | Influencer Engagement Sponsor Coordination Platform | © CreativeMerge</p>
</div>
</template>


<script>
import axios from 'axios';
export default {
    name: 'Login',
    data() {

        return {
            username: null,
            password: null
        }
    },
    methods: {
        printonconsole() {
           console.log(this.username);
           console.log(this.password);
    },
    validateform() {
        if (this.username == null || this.password == null){
            console.log("Please fill all the fields");
            alert('Please fill all the fields');
        }
        else{
            this.login();
        }
    },
    login() {
        axios
            .post('http://localhost:5000/signin', {
                text: this.username,
                password: this.password
            })
            .then((response) => {
                console.log("Response Block",response)
                if(response.status == 200){
                    console.log("Login Successfull");
                    localStorage.setItem('AuthToken', response.data.authToken);
                    localStorage.setItem('userrole', response.data.Role);
                    localStorage.setItem('userid', response.data.id);
                    localStorage.setItem('username', response.data.username);
                    localStorage.setItem('profilepic', response.data.Profilepic);
                    this.username = null,
                    this.password = null,
                    alert('Login Successfull! Welcome to CreativeMerge');
                    if(response.data.Role == 'Admin'){
                        this.$router.push('/AdminStats');
                    }
                    else if(response.data.Role == 'Influencer'){
                        this.$router.push('/influencerhome');
                    }
                    else if(response.data.Role == 'Sponsor'){
                        this.$router.push('/sponsorhome');
                    }
                    else{
                        this.$router.push('/');}
                }
                else{
                    console.log("Login Failed");
                    alert('Login Failed! Reason: '+ response.data.message + ' Please try again');

                }
            })
            .catch((error) => {
                console.log(error);
            });
            }
    }

}

</script>
<style>
.footer {
        background-color: #333;
        color: #fff;
        text-align: center;
        padding: 10px 0;
        bottom: 0;
        width: 100%;
    }
.login {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    flex-direction: column;
    margin:20px;
}
.container {
    justify-content: center;
    justify-items: center;
    width: 100%;
    max-width: 350px;
    padding-bottom: 25px;
    padding-left: 25px;
    padding-right: 25px;
    padding-top: 5px;
    flex-direction: column;
    border-style: solid;
    border-radius: 30px;
    background-color: #f0f0f0;
    margin-bottom: 110px;
}
#submission {
  background-color: blueviolet;
  color:aliceblue; 
  border-radius: 30px; 
  align-content: center;
  align-items: center;
  font-size: 20px;
  color: #fff;
  outline: none;
  align-self: center;
  border: none;
  width: 100%;
  cursor: pointer;
}
#submission:hover {
    background-color: #4CAF50;
}
.logoavatar {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    flex-direction: column;
    margin-top: 20px;
}
.avatar {
    width: 100px; /* Adjust size as needed */
    height: 100px; /* Adjust size as needed */
    border-radius: 50%;
    object-fit:fill;
    margin-bottom: 5px;
}
</style>