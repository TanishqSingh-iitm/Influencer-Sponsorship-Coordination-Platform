<script setup>
import Topbar from '../../components/Topbar.vue'
</script>


<template>
  <div>
    <Topbar />
  </div>
  <div style="margin-top:20px">
    <h2 class="display-4 " align="center">Campaign Edit Portal</h2>
  </div>
  <div class="registerform">
    <div class="logoavatar">
    <img src="../../assets/logo.png" alt="logo" class="avatar">
    </div>
    <form >
    <div class="form-group">
        <label for="username" class="form-label" style="font-size: 20px;">
          <span class="mdi mdi-card-bulleted"></span> Campaign Name</label>
        <input type="text" name="username" placeholder="Type Campaign Name" required class="form-control" style="border-radius: 60px;" v-model="name">
    </div><br>
    <div class="form-group">
        <label for="desc" class="form-label" style="font-size: 20px;"><span class="mdi mdi-text-box"></span> Campaign Description</label>
        <input type="text" name="desc" placeholder="Type Campaign Description" required class="form-control" style="border-radius: 60px;" v-model="description">
    </div><br>
    <div class="form-group">
        <label for="target" class="form-label" style="font-size: 20px;"><span class="mdi mdi-eye"></span> Campaign Target Reach</label>
        <input type="integer" name="target" placeholder="Type Target Reach (in No like 10000)" required class="form-control" style="border-radius: 60px;" v-model="target">
    </div><br>
    <div class="form-group">
        <label for="goal" class="form-label" style="font-size: 20px;"><span class="mdi mdi-card-text"></span> Campaign Goals</label>
        <input type="text" name="goal" placeholder="Type Campaign Goals" required class="form-control" style="border-radius: 60px;" v-model="goal">
    </div><br>
    <div class="form-group">
        <label for="industry" class="form-label" style="font-size: 20px;"><span class="mdi mdi-office-building"></span> Campaign Related Industry</label>
        <input type="text" name="industry" placeholder="Type Campaign Goals" required class="form-control" style="border-radius: 60px;" v-model="industry">
    </div><br>
    <div class="form-group">
        <label for="niche" class="form-label" style="font-size: 20px;"><span class="mdi mdi-play-network"></span> Campaign Related Niche</label>
        <input type="text" name="niche" placeholder="Type Campaign Goals" required class="form-control" style="border-radius: 60px;" v-model="niche">
    </div><br>
    <div class="form-group">
        <label for="Info" class="form-label" style="font-size: 20px;">
          <span class="mdi mdi-monitor-eye"></span> Campaign visibility:
        </label>
        <div style="font-size: 20px;">
          <label style="margin-right: 10px;">
            <input type="radio" value="Public" v-model="accessType" /> Public Campaign
          </label>
          <label>
            <input type="radio" value="Private" v-model="accessType" /> Private Campaign
          </label>
        </div>
      </div><br>
    <div class="form-group">
        <label for="startdate" class="form-label" style="font-size: 25px;"><span class="mdi mdi-calendar-start"></span> Campaign Start Date:</label>
        <input type="date" name="startdate" id="availdate" required  class="form-control" style="border-radius:60px" v-model="startdate">
    </div><br>
    <div class="form-group">
        <label for="enddate" class="form-label" style="font-size: 25px;"><span class="mdi mdi-calendar-end"></span> Campaign End Date:</label>
        <input type="date" name="enddate" id="availdate" required  class="form-control" style="border-radius:60px" v-model="enddate">
    </div><br>
    
    <div class="form-group" align="center">
        <button type="submit" id="submission" class="btn"  align="center" @click.prevent="validateform"><span class="mdi mdi-text-box-plus"></span> Create Campaign
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
  name: 'EditCampaign',
  data() {
    return {
        accessType: 'Private',
        name: '',
        description: '',
        target: '',
        goal: '',
        startdate: '',
        enddate: '',
        auth: '',
        userrole: '',
        industry: '',
        niche: '',
        campaignid: ''

    }
  },
  methods: {
    validateform(){
      if(this.name == '' || this.description == '' || this.target == ''  || this.startdate == '' || this.enddate == '' || this.industry == '' || this.niche == ''){
        alert('Please fill all the fields');
      }
      else if(this.startdate >= this.enddate){
        alert('Start Date cannot be greater than or Equal End Date');
      }
      else if(this.target <= 0){
        alert('Target Reach should be greater than 0');
      }
      else if(this.accessType == ''){
        alert('Please select the Campaign Visibility');
      }
      else{
        this.createcampaign();
      }
    },
    getcampaign(){
        axios
                .get('http://localhost:5000/sponsor/campaign/'+this.campaignid, {
                    headers: {'Authorization': this.auth}})
                .then((response) => {
                    console.log("Response Block", response);
                    if(response.status == 200){
                        console.log("Campaign Retrieved Successfully");
                        this.name = response.data.title;
                        this.description = response.data.description;
                        this.target = response.data.target;
                        this.goal = response.data.goal;
                        this.startdate = response.data.start_date;
                        this.enddate = response.data.end_date;
                        this.accessType = response.data.visibility;
                        this.industry = response.data.related_industry;
                        this.niche = response.data.related_niche;
                    }
                    else{
                        console.log("Campaign Retrieval Failed");
                        alert('Campaign Retrieval Failed! Reason: ' + response.data.message +' Please try again');
                    }
                })
                .catch((error) => {
                    console.log(error);
                });
      },
    createcampaign(){
        axios
                .put('http://localhost:5000/sponsor/campaign/'+this.campaignid, {
                    name: this.name,
                    description: this.description,
                    target: this.target,
                    goal: this.goal,
                    startdate: this.startdate,
                    enddate: this.enddate,
                    accessType: this.accessType,
                    niche: this.niche,
                    industry: this.industry                 
                }, {
                    headers: {'Authorization': this.auth}})
                .then((response) => {
                    console.log("Response Block", response);
                    if(response.status == 200){
                        console.log("Campaign Edited Successfully");
                        this.name = '';
                        this.description = '';
                        this.target = '';
                        this.goal = '';
                        this.startdate = '';
                        this.enddate = '';
                        this.accessType = 'Private';
                        this.industry = '';
                        this.niche = '';
                        alert('Campaign Edited Successfully');
                        this.$router.push('/SponsorDashboard');
                    }
                    else{
                        console.log("Campaign Creation Failed");
                        alert('Campaign Edit Failed! Reason: ' + response.data.message +' Please try again');
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
    this.campaignid = this.$route.params.campaign_id;
    this.auth = localStorage.getItem('AuthToken');
    if (this.auth == null) {
      this.$router.push({ name: 'Login' });
    }
    this.userrole = localStorage.getItem('userrole');
    if (this.userrole != 'Sponsor') {
      alert('You are not authorized to view this page');
      this.$router.push({ name: 'Login' });
    }
    this.getcampaign();
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