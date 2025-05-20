<script setup>
import Topbar from '../../components/Topbar.vue'
</script>

<template>
  <div>
    <Topbar />
  </div>
  <div style="margin-top:20px">
    <h2 class="display-4 " align="center">Sponsor Profile Edit Portal</h2>
  </div>
  <div class="registerform">
    <div class="logoavatar">
    <img src="../../assets/logo.png" alt="logo" class="avatar">
    </div>
    <form >
    <div class="form-group">
        <label for="username" class="form-label" style="font-size: 20px;">
            <span class="mdi mdi-account"></span> Username</label>
        <input type="text" name="username" placeholder="Type your Username" required class="form-control" style="border-radius: 60px;" v-model="username">
    </div><br>
    <div class="form-group">
        <label for="password" class="form-label" style="font-size: 20px;"><span class="mdi mdi-form-textbox-password"></span> Password</label>
        <input type="password" name="password" placeholder="Type your password" required class="form-control" style="border-radius: 60px;" v-model="password">
    </div><br>
    <div class="form-group">
        <label for="confirm_password" class="form-label" style="font-size: 20px;"><span class="mdi mdi-form-textbox-password"></span> Confirm Password</label>
        <input type="password" name="confirm_password" placeholder="Retype your password" required class="form-control" style="border-radius: 60px;" v-model="confirm_password">
    </div><br>
    <div class="form-group">
        <label for="name" class="form-label" style="font-size: 20px;"><span class="mdi mdi-card-text"></span> Company Name / Individual Name</label>
        <input type="text" name="name" placeholder="Type Company Name / Individual Name" required class="form-control" style="border-radius: 60px;" v-model="name">
    </div><br>
    <div class="form-group">
        <label for="email" class="form-label" style="font-size: 20px;"><span class="mdi mdi-email"></span> Sponsor E-mail</label>
        <input type="text" name="email" placeholder="Type your Email address (OPTIONAL)" class="form-control" style="border-radius: 60px;" v-model="email">
    </div><br>
    <div class="form-group">
        <label for="industry" class="form-label" style="font-size: 20px;"><span class="mdi mdi-domain"></span> Sponsor Industry</label>
        <input type="text" name="industry" placeholder="Type your Working Industry" required class="form-control" style="border-radius: 60px;" v-model="industry">
    </div><br>
    <div class="form-group">
        <label for="website" class="form-label" style="font-size: 20px;"><span class="mdi mdi-web"></span> Sponsor Website</label>
        <input type="text" name="website" placeholder="Type your Website (OPTIONAL)" class="form-control" style="border-radius: 60px;" v-model="site">
    </div><br>
    <div class="form-group">
        <label for="Info" class="form-label" style="font-size: 20px;"><span class="mdi mdi-information-variant-circle"></span> Additonal Info</label>
        <input type="text" name="Info" placeholder="Type your Additional Information (OPTIONAL)" class="form-control" style="border-radius: 60px;" v-model="addinfo">
    </div><br>
    <div class="form-group"><br>
        <input type="checkbox" class="form-check-input" name="isterms" id="isterms" style="margin-top:5px; margin-right: 10px;" v-model="profpic">
        <label class="form-check-label" for="isterms" style="font-size: 15px; margin-bottom:5px"> Have Profile Pic</label>
    </div><br>
    <label for="Info" class="form-label" style="font-size: 20px;"><span class="mdi mdi-cloud-upload"></span> Upload Profile Pic</label>
    <div class="input-group mb-3" >
            <input type="file" class="form-control" id="inputGroupFile02" style="border-top-left-radius: 60px; border-bottom-left-radius: 60px;" :disabled="!profpic" @change="addImage">
            <label class="input-group-text" for="inputGroupFile02" style="border-top-right-radius: 60px; border-bottom-right-radius: 60px;" ><span class="mdi mdi-upload"></span> Upload</label>
    </div>
    <div class="form-group"><br>
        <input type="checkbox" class="form-check-input" name="isterms" id="isterms" style="margin-top:5px; margin-right: 10px;" v-model="isterms">
        <label class="form-check-label" for="isterms" style="font-size: 15px; margin-bottom:5px"> I accept <router-link to="/Sponsor_Terms" style="margin-right: 20px;"> Terms & Conditions and Privacy Policy.</router-link></label>
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
  name: 'ProfileEditSponsor',
  data() {
    return {
      username: '',
      password: '',
      confirm_password: '',
      name: '',
      email: '',
      industry: '',
      site: '',
      addinfo: '',
      isterms: false,
      profpic: false,
      role: 'Sponsor',
      Image: null,
    }
  },
  methods: {
      validateform(){
        if(this.username == '' || this.password == '' || this.confirm_password == '' || this.name == '' || this.isterms == false || this.industry == '' ){
          alert("Please fill all the fields and accept the terms and conditions");
    
        }
        else if(this.password != this.confirm_password){
          alert("Password and Confirm Password does not match");
        }
        else{
          this.signup();
          this.uploadimg();
        }
      },
      signup(){
        axios
                .post('http://localhost:5000/sponsorprofile/edit/'+this.user_id, {
                    username: this.username,
                    password: this.password,
                    confirm_password: this.confirm_password,
                    name: this.name,
                    email: this.email,
                    isterms: this.isterms,
                    role: "Sponsor",
                    industry: this.industry,
                    site: this.site,
                    addinfo: this.addinfo,
                    profpic: this.profpic,
                 
                }, {
                    headers: {'Authorization': this.auth}})
                .then((response) => {
                    console.log("Response Block", response);
                    if(response.status == 200){
                        console.log("Profile Edit Successfull");
                        localStorage.setItem('username', this.username);
                        this.username = null,
                        this.password = null,
                        this.confirm_password = null,
                        this.name = null,
                        this.email = null,
                        this.isterms = false,
                        this.industry = null,
                        this.site = null,
                        this.addinfo = null,
                        this.profpic = false,
                        alert('Profile Updated Successfully');
                        this.$router.push('/SponsorProfile');
                    }
                    else{
                        console.log("Profile Edit Failed");
                        alert('Profile Edit Failed! Reason: ' + response.data.message +' Please try again');
                    }
                })
                .catch((error) => {
                    console.log(error);
                });
      },
      addImage(event){
        this.Image = event.target.files[0];
      },
      uploadimg(){
        let formData = new FormData();
        formData.append('file', this.Image);
        formData.append('username', this.username);
        formData.append('role', this.role);
        formData.append('profpic', this.profpic);
        axios.post('http://localhost:5000/uploadprofpic', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        });
      }

  },
  computed: {
    
  },
  watch: {
      profpic(){
        if(!this.profpic){
          Image= null;
        }
      }
  },
  mounted() {
    
  },
  created() {
      this.username1 = localStorage.getItem('username');
      this.auth = localStorage.getItem('AuthToken');
      this.user_id = localStorage.getItem('userid');
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
  align-self: center;
  margin-top: 50px;
  justify-content: space-evenly;
  max-width: 450px;
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