<script setup>
import Topbar from '../../components/Topbar.vue'
import Footer from '@/components/Footer.vue';
import { computed } from 'vue';
const username = localStorage.getItem('username');
const profilepic = localStorage.getItem('profilepic');
const imgsrc = computed(() => {
  if (!!profilepic) {
    if (profilepic === 'true') {
        return new URL(`../../../../backend/Images/SponsorImg/${username}.png`, import.meta.url).href;
    }
    else{
      return new URL(`https://api.dicebear.com/6.x/lorelei/svg?seed=${username}`);
    }
}
  else{
      return new URL(`https://api.dicebear.com/6.x/lorelei/svg?seed=${username}`);
    }
  }
);
</script>

<template>
  <div>
    <Topbar />
  </div>
  <div class="profbody" align="center">
    <div class="profimage">
      
      <img :src="imgsrc" alt="Avatar" class="avatar">
      
      <h4 style="font-family: Doto; font-weight: 900; font-variation-settings:ROND 100; font-optical-sizing: auto;">@ {{username1}}</h4>
      <h4 style="font-family: cursive;"><b>{{ name }}</b></h4>
      <h5>Sponsor</h5>
      
      <div class="contentbtn">
          <button type="button" class="btn btn-warning" @click="editprofile"><span class="mdi mdi-account-edit"></span> Edit Profile</button>
          <button type="button" class="btn btn-success" @click="publicprofile(user_id)"><span class="mdi mdi-account-eye"></span> Public Profile</button>
          <button type="button" class="btn btn-danger" @click="deleteprofile"><span class="mdi mdi-delete-forever"></span> Delete Profile</button>
          <button type="button" class="btn btn-primary" @click="website"><span class="mdi mdi-web"></span> Website</button>
      </div><br>
      <div class="social">
          <div class="row2">
              
          </div>
      </div>
  </div>
    
    <div class="contents">
        <h1 style="border-bottom: 5px solid #000000; width: 100%; padding: 5px;">Sponsor Profile</h1>
        <div>
            <h3>Personal Information</h3>
            <div class="name">
                <h4><b>Name: </b>{{ name }}</h4>
            </div>
            <div class="usernamei">
                <h4><b>Username: </b>{{ username1 }}</h4>
            </div>
            <div class="email">
                <h4><b>Email: </b>{{ email }}</h4>
            </div>
            <div class="industry">
                 <h4 v-if="site.length>0"><b>Website: </b>{{site}}</h4>
                <h4 v-if="site.length==0"><b>Website: </b>No Site Given</h4>
            </div>
            <div class="industry">
                <h4><b>Industry: </b>{{industry}}</h4>
            </div>
            <div class="datejoined">
                <h4><b>Date Joined: </b>{{datejoined}}</h4>
            </div>
            <div class="lastloged">
                <h4><b>Last Logged In: </b>{{lastloged}}</h4>
            </div>
            <div class="bio">
                <h4><b>Company Info:</b> </h4>
                <p v-if="addinfo.length>0" style="text-align: justify; font-size: larger;">{{ addinfo }}</p>
                <p v-if="addinfo.length==0" style="text-align: justify;font-size: larger;"> No Info available Yet</p>
            </div>
        </div>
    </div>
  </div>
  <div style="background-color: #333; color: white; text-align: center; position: relative; bottom: 0; left: 0; width: 100%; font-family: 'Doto', sans-serif; font-optical-sizing: auto; font-weight: 1000; font-style: normal; font-variation-settings: 'ROND' 100; font-size: 1.1rem; height: 50px;">
  <p align="center" style="margin: 0; line-height: 50px;">© 2024 | © 21EJCCS821,826,854 | Influencer Engagement Sponsor Coordination Platform | © CreativeMerge</p>
</div>

</template>

<script>
import axios from 'axios';
export default {
  name: 'SponsorProfile',
  data() {
    return {
          user_id:'',
          username1:'',
          auth:'',
          name:'',
          email:'',
          industry:'',
          site:'',
          addinfo:'',
          datejoined:'',
          lastloged:'',
          userids:'',
    }
  },
  methods: {
          getdata(){
            axios
            .get('http://localhost:5000/sponsorprofile/'+this.user_id, {
              headers: {
                'Authorization': this.auth
              }
            })
            .then((response) => {
              console.log("Response Block", response);
              this.name = response.data.name;
              this.email = response.data.email;
              this.industry = response.data.industry;
              this.site = response.data.site;
              this.addinfo = response.data.bio;
              this.datejoined = response.data.date_joined;
              this.lastloged = response.data.last_login;
            })
            .catch((error) => {
              console.log("Error Block", error);
            });
          },
          publicprofile(userids){
            this.$router.push({name: 'SponsorProfilePublicPage', params: {users_id: userids}});
          },
          editprofile(){
            this.$router.push('/EditSponsorProfile');
          },
          deleteprofile(){
            this.$router.push('/DeleteSponsorProfile');
          },
          website() { 
      if (this.site) { 
        window.location.href = this.site; 
      } 
      else { 
        alert('Link not available'); 
      } 
    },
  },
  computed: {
    
  },
  watch: {
    
  },
  mounted() {
    
  },
  created() {
      this.username1 = localStorage.getItem('username');
      this.auth = localStorage.getItem('AuthToken');
      this.user_id = localStorage.getItem('userid');
      this.getdata();

  }
}
</script>

<style scoped>



.profheader {
  text-align: center;
  margin-top: 20px;
}

.profbody {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  margin-top: 20px;
  width: 80%;
  border-width: 5px;
  border-style: solid;
  border-color: #000000;
  height: auto; /* Allow height to adjust */
  flex-wrap: wrap-reverse; /* Enable wrapping */
  margin-left: 10%;
  background-color: rgb(230, 230, 230);
  border-radius: 30px;
  margin-bottom: 25px;

  
}

.profbody .contents {
  display: flex;
  flex-direction: column;
  align-self: flex-end;
  flex-wrap: wrap-reverse;
  width: 75%;
  padding: 10px;
  gap: 10px;
  justify-content: space-evenly;
  flex: 1 1 auto;
  font-family: 'Times New Roman', Times, serif;
}

.profbody .profimage {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 25%;
  border-right: 5px solid #000000;
  flex-wrap: wrap;
  gap: 15px;
  padding: 10px;
  background-color: #000000e5;
  color: #ededed;
  border-top-left-radius: 25px;
  border-bottom-left-radius: 25px;
  flex: 1 1 auto;
  height: stretch;

}

.avatar {
  width: 160px; /* Adjust size as needed */
  height: 160px; /* Adjust size as needed */
  border-radius: 50%;
  object-fit: cover;
  border: #e8e7e7;
  border-width: 5px;
  border-style: solid;
  background-color: azure
}

/* Media query for screen sizes below 650px */
@media (max-width: 820px) {
  .profbody {
    flex-direction: column;
    width: 90%;
    margin-left: 5%; /* Adjust margin for smaller screens */
    justify-content: center;
    align-items: center;
    justify-items: center;
  }
  
  .profbody .contents {
    width: 100%;
    margin-bottom: 10px; /* Add margin between wrapped elements */
    order:2;
  }

  .profbody .profimage {
    width: 100%;
    border-width: 0px;
    order:1;
    border-bottom: 3px solid #000000;
    border-top-right-radius: 25px;
    border-top-left-radius: 25px;
    border-bottom-right-radius: 0px;
    border-bottom-left-radius: 0px;
  }
}

.profbody .profimage .contentbtn {
  display: flex;
  flex-direction: column;
  flex-wrap:wrap;
  margin :2px;
  width: 80%;
  gap: 20px; 
  justify-content: space-evenly;
  justify-items: center;
  justify-self: center;
  padding: 0%;
}

@media (min-width: 820px) and (max-width: 1500px) { 
    .profbody .profimage .contentbtn {
  display: flex;
  flex-direction: row;
  flex-wrap:wrap;
  
  width: 100%;
  gap: 20px; 
  justify-content: center;
  justify-items: center;
  justify-self: center;
  padding: 0%;

}
}

.profbody .social {
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
  width: 100%;
  gap: 20px;
  justify-content: space-around;
  
}

.profbody .social .row1 {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  gap: 15px;
  justify-content: space-around;
  padding: 10px;
  
}

.profbody .social .row1 button {
  
  gap: 5px;
  justify-content: center;
  align-items: center;
  flex: 1 1  auto;
  min-width: 100px;
  max-width: 187px;
}

.profbody .social .row2 {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  gap: 15px;
  justify-content: space-around;
  padding: 10px;
}



.profbody .contents .name {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  gap: 10px;
  padding: 10px;
}

.profbody .contents .usernamei {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  gap: 10px;
  padding: 10px;
}

.profbody .contents .email {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  gap: 10px;
  padding: 10px;
}

.profbody .contents .industry {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  gap: 10px;
  padding: 10px;
}

.profbody .contents .niche {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  gap: 10px;
  padding: 10px;
}

.profbody .contents .datejoined {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  gap: 10px;
  padding: 10px;
}

.profbody .contents .lastloged {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  gap: 10px;
  padding: 10px;
}

.profbody .contents .bio {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  gap: 10px;
  padding: 10px;
}


</style>