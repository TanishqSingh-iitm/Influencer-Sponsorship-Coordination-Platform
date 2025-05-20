<script setup>
import Topbar from '../../components/Topbar.vue'
</script>


<template>
  <div>
    <Topbar />
  </div>
  <div style="margin-top:20px">
    <h2 class="display-4 " align="center">Advertisement Request Creation Portal</h2>
  </div>
  <div class="registerform">
    <div class="logoavatar">
    <img src="../../assets/logo.png" alt="logo" class="avatar">
    </div>
    <form >
    <div class="form-group">
        <label for="username" class="form-label" style="font-size: 20px;">
          <span class="mdi mdi-card-bulleted"></span> Ad Title</label>
        <input type="text" name="username" placeholder="Type Ad Name" required class="form-control" style="border-radius: 60px;" v-model="name">
    </div><br>
    <div class="form-group">
        <label for="desc" class="form-label" style="font-size: 20px;"><span class="mdi mdi-text-box"></span> Ad Description / Requirement</label>
        <input type="text" name="desc" placeholder="Type Ad Description" required class="form-control" style="border-radius: 60px;" v-model="description">
    </div><br>
    <div class="form-group">
        <label for="target" class="form-label" style="font-size: 20px;"><span class="mdi mdi-currency-rupee"></span> Ad Amount</label>
        <input type="integer" name="target" placeholder="Type Base amount for Ad" required class="form-control" style="border-radius: 60px;" v-model="target">
    </div><br>
    <div>
        <label for="goal" class="form-label" style="font-size: 20px;">Major Platforms Influencers:</label>
        <p><span class="mdi mdi-youtube" ></span><span class="mdi mdi-instagram"   ></span>
                        <span class="mdi mdi-facebook" ></span><span class="mdi mdi-twitter" ></span>
                        <span class="mdi mdi-at"   ></span><span class="mdi mdi-music-note-outline" ></span>
                        <span class="mdi mdi-twitch" ></span><span class="mdi mdi-kickstarter"   ></span>
                        <span class="mdi mdi-snapchat"  ></span><span class="mdi mdi-linkedin"  ></span></p>
    </div>
    <div class="form-group">
        <label for="industry" class="form-label" style="font-size: 20px;"><span class="mdi mdi-office-building"></span> Ad Preferred Platform</label>
        <input type="text" name="industry" placeholder="Type Platform full name separated with space" required class="form-control" style="border-radius: 60px;" v-model="industry">
    </div><br>
   
    <div class="form-group" align="center">
        <button type="submit" id="submission" class="btn"  align="center" @click.prevent="validateform"><span class="mdi mdi-text-box-plus"></span> Create Campaign Ad
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
  name: 'CreateCampaign',
  data() {
    return {
        name: '',
        description: '',
        target: '',
        auth: '',
        userrole: '',
        industry: '',
        campaignid: '',

    }
  },
  methods: {
    validateform(){
      if(this.name == '' || this.description == '' || this.target == '' || this.industry == ''){
        alert('Please fill all the fields');
      }
      else if(this.target <= 0){
        alert('Ad Amount should be greater than 0');
      }
      else{
        this.createad();
      }
    },
    createad(){
        axios
                .post('http://localhost:5000/sponsor/campaign/'+this.campaignid+'/createad', {
                    title: this.name,
                    description: this.description,
                    amount: this.target,
                    platforms: this.industry                 
                }, {
                    headers: {'Authorization': this.auth}})
                .then((response) => {
                    console.log("Response Block", response);
                    if(response.status == 200){
                        console.log("Campaign Ad Created Successfully");
                        this.name = '';
                        this.description = '';
                        this.target = '';
                        this.industry = '';
                        alert('Campaign Ad Created Successfully');
                        this.$router.go(-1);
                    }
                    else{
                        console.log("Campaign Ad Creation Failed");
                        alert('Campaign Ad Creation Failed! Reason: ' + response.data.message +' Please try again');
                        this.$router.go(-1);
                    }
                })
                .catch((error) => {
                    console.log(error);
                });
      },
  },
  computed: {
    
  },
  watch: {
    
  },
  mounted() {
    
  },
  created() {
    this.auth = localStorage.getItem('AuthToken');
    if (this.auth == null) {
      this.$router.push({ name: 'Login' });
    }
    this.userrole = localStorage.getItem('userrole');
    if (this.userrole != 'Sponsor') {
      this.$router.push({ name: 'Login' });
    }
    this.campaignid = this.$route.params.campaign_id;
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
  flex-direction: column;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
  align-content: center;
  align-self: center;
  margin-top: 50px;
  margin-left: 20px;
  margin-right: 20px;
  justify-content: space-evenly;
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