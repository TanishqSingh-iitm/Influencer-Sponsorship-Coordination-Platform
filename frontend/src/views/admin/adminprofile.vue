<script setup>
import Topbar from '../../components/Topbar.vue'


</script>

<template>
  <div class="topbar">
    <Topbar />
  </div>
  <div class="profheader">
      <h1>Admin Profile</h1>

    </div>
  <div class="profcontainer">
    <div class="profbody">
      <div class="profimage">
        <img :src="`https://api.dicebear.com/6.x/lorelei/svg?seed=${username}`" alt="Avatar" class="avatar">
        <h3>Administrator</h3>
        <div class="contentbtn">
            <button type="button" class="btn btn-outline-success" @click="Editprofile" >
              <span class="mdi mdi-account-edit"></span> Edit Profile</button>
        </div>
      </div>
      <div class="profcontent">
        <div class="details">
            <div class="namecont">
            <h4><b>Name:</b> {{ name }}</h4> 
        </div>
        <div class="emailcont">
            <h4><b>Username:</b> {{ username }}</h4>
        </div> 
        <div class="emailcont">
            <h4><b>Role:</b> Administrator of CreativeMerge</h4>
        </div>
        <div class="emailcont">
           <h4><b>Email:</b> {{ email }}</h4>
        </div>  
        <div class="emailcont">
            <h4><b>Date Joined:</b> {{ datejoined }}</h4>
        </div>
        <div class="emailcont">
            <h4><b>Last Logged:</b> {{ lastlogged }}</h4>
        </div>
        </div>
        <div class="bio">
            <h4><b>Bio:</b> </h4>
            <h6 style="text-align: justify; margin-left: 10px;">{{ bio }}</h6>
        </div>   
      </div>
  </div>
  </div>
  <div style="background-color: #333; color: white; text-align: center; position: relative; bottom: 0; left: 0; width: 100%; font-family: 'Doto', sans-serif; font-optical-sizing: auto; font-weight: 1000; font-style: normal; font-variation-settings: 'ROND' 100; font-size: 1.1rem; height: 50px;">
  <p align="center" style="margin: 0; line-height: 50px;">© 2024 | © 21F3001516 | Influencer Engagement Sponsor Coordination Platform | © CreativeMerge</p>
</div>
</template>

<script>
import axios from 'axios';
import Editprofilesponsor from '../profiles/editprofilesponsor.vue';
export default {
  name: 'adminprofile',
  data() {
    return {
        username: '',
        userrole: '',
        auth: '',
        email: '',
        datejoined: '',
        lastlogged: '',
        bio: '',
        name: '',
    }
  },
  methods: {
     getdata() {
      console.log('Getting data');
      axios
            .get('http://localhost:5000/adminprofile',
                 {headers: {Authorization: `${this.auth}`}})
            .then((response) => {
                console.log("Response Block",response)
                if(response.status == 200){
                    console.log("Data Fetched Successfully")
                    this.username = response.data.username;
                    this.userrole = response.data.userrole;
                    this.email = response.data.email;
                    this.datejoined = response.data.date_joined;
                    this.lastlogged = response.data.last_login;
                    this.bio = response.data.bio;
                    this.name = response.data.name;
                }
                else{
                    altert(this.response.data.message)
                    console.log("Error in fetching data")
                }
            })
            .catch((error) => {
                console.log(error);
            });
    },
    Editprofile(){
      this.$router.push('/AdminProfileEdit');
    }
  },
  computed: {
    
  },
  watch: {
    
  },
  mounted() {
    
  },
  created() {
      this.username = localStorage.getItem('username');
      this.userrole = localStorage.getItem('userrole');
      this.auth = localStorage.getItem('AuthToken');
      this.getdata();

  }
}
</script>

<style scoped>
.profcontainer {
  display: flex;
  flex-direction: row;
  margin-top: 5px;
  border-color: #5b5a5a;
  border-style: solid;
  border-width: 4px;
  border-radius: 30px;
  width: 85%;
  margin-left: 10%;

}
.profheader {
  display: flex;
  flex-direction: row;
  margin-top: 50px;
  margin-left: 10%;
}


.avatar {
  width: 160px; /* Adjust size as needed */
  height: 160px; /* Adjust size as needed */
  border-radius: 50%;
  object-fit: cover;
  border: #1a1a1a;
  border-width: 5px;
  border-style: solid;

}

.profbody {
  display: flex;
  flex-direction: row;
  justify-content: center;
  width: 100%;
  padding: 10px;
  flex-wrap: wrap;
  
}

.profbody .profimage {
  display: flex;
  flex-direction: Column;
  align-items: center;
  justify-content: center;
  padding: 10px;
  border-right-width: 3px;
  border-right-style: solid;
  border-right-color: #1a1a1a;
  flex-wrap:wrap;
  font-family: cursive;
}

.profbody .profcontent {
  display: flex;
  flex-direction: row;
  padding: 10px;
  flex-wrap:wrap;
  justify-content: space-between;
  width: 84%;
  gap:20px;
  padding: 20px;
}

.profbody .profimage .contentbtn {
  display: flex;
  flex-direction: column;
  flex-wrap:wrap;
  
  width: 100%;
  gap: 20px; 
  justify-content: flex-start;
  justify-items: center;
  justify-self: center;
  padding: 0%;
}

@media (min-width: 450px) and (max-width: 1500px) { 
    .profbody .profimage .contentbtn {
  display: flex;
  flex-direction: row;
  flex-wrap:wrap;
  
  width: 100%;
  gap: 20px; 
  justify-content: flex-start;
  justify-items: center;
  justify-self: center;
  padding: 0%;
}
}

.profbody .namecont {
  display: flex;
  flex-direction: row;
  flex-wrap:wrap;
  
  width: 100%;
  gap: 10px; 
  justify-content: flex-start;
  padding: 0%;
}

.profbody .emailcont {
  display: flex;
  flex-direction: row;
  flex-wrap:wrap;
  
  width: 100%;
  padding: 0%;
}

.profbody .details {
  display: flex;
  flex-direction: column;
  flex-wrap:wrap;
  padding: 0%;
  gap:20px;
  width: 45%;
  justify-content: flex-start;
  
}

.profbody .bio {
  display: flex;
  flex-direction: row;
  flex-wrap:wrap;
  padding: 0%;
  width: 45%;
}

@media (max-width:700px){
    .profbody .profcontent {
  display: flex;
  flex-direction: column;
  padding: 10px;
  flex-wrap:wrap;
  justify-content: space-between;
  width: 84%;
  gap:20px;
  padding: 20px;
 }
 .profbody .details {
  display: flex;
  flex-direction: column;
  flex-wrap:wrap;
  padding: 0%;
  gap:20px;
  width: 100%;
  justify-content: flex-start;
  
}

.profbody .bio {
  display: flex;
  flex-direction: row;
  flex-wrap:wrap;
  padding: 0%;
  width: 100%;
}
}

h4 {
  font-size: 1.5rem;
  font-family: open-sans;
}

@media (max-width: 1560px) {
  .profbody .profimage {
    border-right-width: 0px;
    border-bottom: 3px solid #000000;
    border-width: 100%;
  }
}
</style>