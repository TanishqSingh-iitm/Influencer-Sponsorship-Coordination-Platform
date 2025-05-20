<script setup>
import { computed} from 'vue';
import { onMounted } from 'vue'; 
import { useRouter } from 'vue-router';

const auth = localStorage.getItem('AuthToken');
const username = localStorage.getItem('username');
const role = localStorage.getItem('userrole');
const profilepic = localStorage.getItem('profilepic');
const userid = localStorage.getItem('userid');
const imgsrc = computed(() => {
  if (profilepic) {
    if (role === 'Sponsor') {
      return new URL(`../../../backend/Images/SponsorImg/${username}.png`, import.meta.url).href;
    }
    else if (role === 'Influencer') {
      return new URL(`../../../backend/Images/InfluencerImg/${username}.png`, import.meta.url).href;
    }
    else{
      return new URL(`https://api.dicebear.com/6.x/micah/svg?seed=${username}`);
    }
  }
  return new URL(`https://api.dicebear.com/6.x/micah/svg?seed=${username}`);
});

const router = useRouter(); 
const checkAuthAndRedirect = () => { 
  if (!auth || !role || !username || !userid) { 
    alert('You have been logged out. Redirecting to login page.'); 
    router.push('/login'); 
  } else { 
    console.log('All authentication details are present.'); 
  } 
}; 
onMounted(() => { 
  checkAuthAndRedirect(); 
});

</script>

<template>
<div class="landnav">
<nav class="navbar navbar-expand-lg" id="landnavi">
  <div class="container-fluid">
    <img src="../assets/logo.png" class="avatar" alt="User Avatar" /> 
    <h2 class="appname">CreativeMerge</h2> 
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavDropdown" align="center">
      <ul class="navbar-nav">
        <li class="nav-item" >
          <button type="button" class="btn" style="margin-right: 2px; margin-top: 5px;" id="btn-nav" @click="home" v-if="hasAuthToken_Influencer"><span class="mdi mdi-home"></span> Home</button>
          <button type="button" class="btn" style="margin-right: 2px; margin-top: 5px;" id="btn-nav" @click="home" v-if="hasAuthToken_Sponsor"><span class="mdi mdi-home"></span> Home</button>
        </li>
        <li class="nav-item" >
          <button type="button" class="btn" style="margin-right: 2px; margin-top: 5px;" id="btn-nav" @click="adminstats" v-if="hasAuthToken_Admin"><span class="mdi mdi-chart-bar-stacked"></span> Statistics</button>
          <button type="button" class="btn" style="margin-right: 2px; margin-top: 5px;" id="btn-nav" @click="sponsorstats" v-if="hasAuthToken_Sponsor"><span class="mdi mdi-chart-waterfall"></span> Statistics</button>
          <button type="button" class="btn" style="margin-right: 2px; margin-top: 5px;" id="btn-nav" @click="influencerstats" v-if="hasAuthToken_Influencer"><span class="mdi mdi-chart-timeline"></span> Statistics</button>
        </li>
        <li class="nav-item" >
          <button type="button" class="btn" style="margin-right: 5px; margin-top: 5px;" id="btn-nav" @click="admincampaign" v-if="hasAuthToken_Admin"><span class="mdi mdi-monitor-dashboard"></span> Campaign Dashboard</button> 
        </li>
        <li class="nav-item" >
          <button type="button" class="btn" style="margin-right: 2px; margin-top: 5px;" id="btn-nav" @click="adminsponsor" v-if="hasAuthToken_Admin"><span class="mdi mdi-tablet-dashboard"></span> Sponsor Dashboard</button>
          <button type="button" class="btn" style="margin-right: 2px; margin-top: 5px;" id="btn-nav" @click="sponsordash" v-if="hasAuthToken_Sponsor"><span class="mdi mdi-monitor-dashboard"></span> Sponsor Dashboard</button>
          <button type="button" class="btn" style="margin-right: 2px; margin-top: 5px;" id="btn-nav" @click="influencerdash" v-if="hasAuthToken_Influencer"><span class="mdi mdi-monitor-dashboard"></span> Influencer Dashboard</button>
        </li>
        <li class="nav-item" >
          <button type="button" class="btn" style="margin-right: 5px; margin-top: 5px;" id="btn-nav" @click="admininfluencer" v-if="hasAuthToken_Admin"><span class="mdi mdi-monitor-account"></span> Influencer Dashboard</button>
          <button type="button" class="btn" style="margin-right: 5px; margin-top: 5px;" id="btn-nav" @click="adrequestdash" v-if="hasAuthToken_Sponsor"><span class="mdi mdi-clipboard-list"></span> Ad Requests Dashboard</button>  
        </li>
        <li class="nav-item" >
          <button type="button" class="btn" style="margin-right: 5px; margin-top: 5px;" id="btn-nav" @click="wallet" v-if="hasAuthToken_Influencer"><span class="mdi mdi-wallet"></span> wallet</button>
          <button type="button" class="btn" style="margin-right: 5px; margin-top: 5px;" id="btn-nav" @click="wallet" v-if="hasAuthToken_Admin"><span class="mdi mdi-wallet"></span> wallet</button>
          <button type="button" class="btn" style="margin-right: 5px; margin-top: 5px;" id="btn-nav" @click="wallet" v-if="hasAuthToken_Sponsor"><span class="mdi mdi-wallet"></span> Wallet</button>   
        </li>
        <li class="nav-item dropdown"> 
          <a class="nav-link dropdown-toggle" role="button" data-bs-toggle="dropdown" aria-expanded="false" id="avat"> 
            <img v-bind:src="imgsrc"   id="prof" alt="User Avatar" /> 
          </a> 
          <ul class="dropdown-menu dropdown-menu-end">  
            <li>
                <span class="name">{{ username }}</span> 
                <span class="userrole" v-if="hasAuthToken_Admin">Administrator</span>
                <span class="userrole" v-if="hasAuthToken_Sponsor">Sponsor</span> 
                <span class="userrole" v-if="hasAuthToken_Influencer">Influencer</span>  
            </li>
          
            <hr>
            <li>
              <a class="dropdown-item" @click="profile"><span class="mdi mdi-card-account-details"></span> Profile</a>
            </li> 
            <li>
              <a class="dropdown-item" href="#"><span class="mdi mdi-theme-light-dark"></span>Theme</a>
            </li>
            <hr>
            <li>
              <button type="button" class="btn"  id="loginout" @click="Logout" style="display:block; justify-self: center;"><span class="mdi mdi-logout"></span> Sign Out</button>
            </li> 
          </ul> 
        </li>
      </ul>
    </div>
  </div>
</nav>
</div>
</template>

<script>
import Login from '@/views/logins/Login.vue';
import axios from 'axios';
import { RouterLink } from 'vue-router';

export default {
  name: 'Topbar',
  data() {
    return {
        
      
    }
  },
  methods: {
    smoothScroll(id) {
      document.body.click();
      document.querySelector(id).scrollIntoView({
        behavior: 'smooth'
      });
    },
    Logout(){
      localStorage.removeItem('AuthToken');
      localStorage.removeItem('username');
      localStorage.removeItem('userrole');
      localStorage.removeItem('profilepic');
      localStorage.removeItem('userid');
      alert('You have been logged out Successfully');
      this.$router.push('/login');
    },
    hasAuthToken(){
      return !!auth;
    },
    profile(){
      if(localStorage.getItem('userrole') === 'Sponsor'){
        this.$router.push('/SponsorProfile');
      }
      else if(localStorage.getItem('userrole') === 'Influencer'){
        this.$router.push('/InfluencerProfile');
      }
      else{
        this.$router.push('/AdminProfile');
      }
    },
    adminsponsor(){
      if(localStorage.getItem('userrole') === 'Admin'){
            this.$router.push('/AdminSponsorDash');}
        else{
            alert('You are not authorized to view this page');

        }
    },
    admininfluencer(){
      if(localStorage.getItem('userrole') === 'Admin'){
            this.$router.push('/AdminInfluencerDash');}
        else{
            alert('You are not authorized to view this page');

        }
    },
    admincampaign(){
      if(localStorage.getItem('userrole') === 'Admin'){
            this.$router.push('/AdminCampaignDash');}
        else{
            alert('You are not authorized to view this page');

        }
    },
    adminstats(){
      if(localStorage.getItem('userrole') === 'Admin'){
            this.$router.push('/AdminStats');}
      else{
            alert('You are not authorized to view this page');

        }
    },
    sponsordash(){
      if(localStorage.getItem('userrole') === 'Sponsor'){
            this.$router.push('/SponsorDashboard');}
      else{
            alert('You are not authorized to view this page');

        }
    },
    wallet(){
      if(localStorage.getItem('AuthToken')=='' || localStorage.getItem('AuthToken')==null){
        alert('You need to login to view this page');
        this.$router.push('/login');
      }
      else{
        this.$router.push('/wallet');
      }
    },
    sponsorstats(){
      if(localStorage.getItem('userrole') === 'Sponsor'){
            this.$router.push('/SponsorStats');}
      else{
            alert('You are not authorized to view this page');

        }
    },
    home(){
      if(localStorage.getItem('userrole') === 'Sponsor'){
            this.$router.push('/sponsorhome');}
      else if(localStorage.getItem('userrole') === 'Influencer'){
            this.$router.push('/influencerhome');}
      else{
        alert('You are not authorized to view this page');
        this.$router.go(-1);
      }
    },
    adrequestdash(){
      if(localStorage.getItem('userrole') === 'Sponsor'){
            this.$router.push('/AdRequestDash');}
      else{
            alert('You are not authorized to view this page');

        }
    },
    influencerdash(){
      if(localStorage.getItem('userrole') === 'Influencer'){
            this.$router.push('/InfluencerDash');}
      else{
            alert('You are not authorized to view this page');

        }
    },
    influencerstats(){
      if(localStorage.getItem('userrole') === 'Influencer'){
            this.$router.push('/InfluencerStats');}
      else{
            alert('You are not authorized to view this page');

        }
    },
    
  },
  computed:{
    
    hasAuthToken_Sponsor(){
      return localStorage.getItem('userrole') === 'Sponsor';
    },
    hasAuthToken_Influencer(){
      return localStorage.getItem('userrole') === 'Influencer';
    },
    hasAuthToken_Admin(){
      return localStorage.getItem('userrole') === 'Admin';
    },
    
   
  },
  watch:{
    
  },
  created() {
  
  
    

  }

}
</script>

<style scoped>

.landnav {
  background-color: #1574d4;
  width: 100%;
}
#landnavi {
  background-color: #dadbdc;
  color: #000;
  width: 100%;
 
}
.avatar {
  width: 50px; /* Adjust size as needed */
  height: 50px; /* Adjust size as needed */
  border-radius: 50%;
  object-fit: cover;
}

#prof {
  width: 35px; /* Adjust size as needed */
  height: 35px; /* Adjust size as needed */
  border-radius: 50%;
  object-fit: cover;
}

.user-info {
    display: block;
}

.name {
    justify-self: center;
    display: block;
    font-size: 0.875rem; /* Equivalent to text-sm */
    color: #1F2937; /* Equivalent to text-gray-900 */
    font-weight: bold;
    font-family: cursive;
    
}

.email {
    justify-self: center;
    display: block;
    font-size: 0.875rem; /* Equivalent to text-sm */
    color: #6B7280; /* Equivalent to text-gray-500 */
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis; /* Equivalent to truncate */
    font-family: cursive;
}

.userrole{
  justify-self: center;
  display: block;
  font-size: 0.875rem; /* Equivalent to text-sm */
  color: #6B7280; /* Equivalent to text-gray-500 */
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis; /* Equivalent to truncate */
  font-family: cursive;
}

/* For dark mode */
body.dark .name {
    color: #FFFFFF; /* Equivalent to text-white */
}

body.dark .email {
    color: #9CA3AF; /* Equivalent to text-gray-400 */
}




@keyframes blink { 
  0% { opacity: 1; } 
  50% { opacity: 0.3; } 
  100% { opacity: 1; } 
}

@keyframes blink-color { 
  0% { color: #ff69b4; } 
  25% { color: #ff4500; } /* Orange Red */ 
  50% { color: #1e90ff; } /* Dodger Blue */ 
  75% { color: #32cd32; } /* Lime Green */ 
  100% { color: #ff69b4; } 
}



.appname {
  margin-left: 10px;
  font-family: "Doto", sans-serif;
  font-optical-sizing: auto;
  font-weight: 1000;
  font-style: normal;
  font-variation-settings:
    "ROND" 100;
  font-size: 2rem;
  animation: blink 10s ease-in-out infinite;
}

#btn-nav {
  border: none;
  border-radius: 5px;
  font-size: 1rem;
  font-weight: 700;
  cursor: pointer;
  transition: buttoncolor 0.3s;
}

#btn-nav:hover {
  background-color: rgb(139, 64, 253, 0.1);
  color: #0f0f0f;
  border-radius: 5%;
}

#loginout {
  border: none;
  border-radius: 5px;
  font-size: 1rem;
  font-weight: 700;
  cursor: pointer;
  transition: buttoncolor 0.3s;
}

#loginout:hover {
  background-color: rgb(139, 64, 253, 0.1);
  color: #0f0f0f;
  border-radius: 10%;
}

.navbar-nav { 
  margin-left: auto; /* Align nav items to the right */
}

#avat:hover{
  cursor: pointer;
  background-color: #dadbdc;

}


</style>