<script setup>
import Topbar from '../../components/Topbar.vue'
</script>

<template>
  <div>
    <Topbar />
  </div>
  <div style="margin-top:20px">
    <h2 class="display-4 " align="center">Admin Edit Profile Portal</h2>
  </div>
  <div class="registerform">
    <div class="logoavatar">
    <img src="../../assets/logo.png" alt="logo" class="avatar">
    </div>
    <form >
      <div class="form-group">
        <label for="name" class="form-label" style="font-size: 20px;"><span class="mdi mdi-card-text"></span> Name</label>
        <input type="text" name="name" placeholder="Type your New Name" required class="form-control" style="border-radius: 60px;" v-model="name">
    </div><br>
      <div class="form-group">
        <label for="password" class="form-label" style="font-size: 20px;"><span class="mdi mdi-form-textbox-password"></span> Password</label>
        <input type="password" name="password" placeholder="Type your new password" required class="form-control" style="border-radius: 60px;" v-model="password">
    </div><br>
    <div class="form-group">
        <label for="confirm_password" class="form-label" style="font-size: 20px;"><span class="mdi mdi-form-textbox-password"></span> Confirm Password</label>
        <input type="password" name="confirm_password" placeholder="Retype your new password" required class="form-control" style="border-radius: 60px;" v-model="confirm_password">
    </div><br>
    <div class="form-group">
        <label for="Info" class="form-label" style="font-size: 20px;"><span class="mdi mdi-information-variant-circle"></span> Additonal Info</label>
        <input type="text" name="Info" placeholder="Type your Bio (OPTIONAL)" class="form-control" style="border-radius: 60px;" v-model="addinfo">
    </div><br>
    <div class="form-group" align="center">
        <button type="submit" id="submission" class="btn"  align="center" @click.prevent="validateform"><span class="mdi mdi-pencil"></span> Edit Profile 
         </button>
    </div>
</form>
  </div>
  <div style="background-color: #333; color: white; text-align: center; position: relative; bottom: 0; left: 0; width: 100%; font-family: 'Doto', sans-serif; font-optical-sizing: auto; font-weight: 1000; font-style: normal; font-variation-settings: 'ROND' 100; font-size: 1.1rem; height: 50px;">
  <p align="center" style="margin: 0; line-height: 50px;">© 2024 | © 21F3001516 | Influencer Engagement Sponsor Coordination Platform | © CreativeMerge</p>
</div>


</template>

<script>
import axios from 'axios';
export default {
  name: '',
  data() {
    return {
      name: '',
      password: '',
      confirm_password: '',
      addinfo: '',
      auth:'' ,
      username: '',
      validation:false
    }
  },
  methods: {
    validateform() {
      if (this.password != this.confirm_password) {
        alert("Password and Confirm Password do not match");
      }
      else if (this.name == '' || this.password == '' || this.confirm_password == '') {
        alert("Please fill in all the fields");
      }
      else {
        this.senddata();
      }
    },
    senddata(){
      axios
                .post('http://localhost:5000/adminprofile/edit', {
                    password: this.password,
                    confirm_password: this.confirm_password,
                    name: this.name,
                    role: "Admin",
                    bio: this.addinfo,
                 
                }, {headers: {Authorization: this.auth}})
                .then((response) => {
                    console.log("Response Block", response);
                    if(response.status == 200){
                        console.log("Admin Profile Edit Successfull");
                        this.password = null,
                        this.confirm_password = null,
                        this.name = null,
                        this.addinfo = null,
                        alert('Admin Profile Edited Successfully!');
                        this.$router.push('/AdminProfile');
                    }
                    else{
                        console.log("Admin Profile Edit Failed");
                        alert('Admin Pofile Edit Failed! Reason: ' + response.data.message +' Please try again');
                    }
                })
                .catch((error) => {
                    console.log(error);
                });
    }
  },
  computed: {
    
  },
  watch: {
    
  },
  mounted() {
    
  },
  created() {
          this.auth = localStorage.getItem('AuthToken'); 
          this.username = localStorage.getItem('username');
          
  }
}
</script>

<style scoped>
.footer {
        background-color: #333;
        color: #fff;
        text-align: center;
        padding: 10px 0;
        bottom: 0;
        width: 100%;
    }
.registerform {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
  align-content: center;
  flex-direction: column;
  align-self: center;
  margin-top: 50px;
  justify-content: space-evenly;
  max-width: 700px;
  border-color: rgb(27, 28, 28);
  border-style: solid;
  border-radius: 30px;
  background-color: #e8e8e8;
  padding-left: 30px;
  padding-right: 30px;
  padding-bottom: 30px;
  margin-bottom: 20px;
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
</style>