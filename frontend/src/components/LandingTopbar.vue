<script setup>

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
          <button type="button" class="btn" style="margin-right: 10px; margin-bottom: 10px;" id="login" @click="Login"><span class="mdi mdi-login"></span> Login</button>

        </li>
        <li class="nav-item" >
          <button type="button" class="btn btn-success" style="margin-right: 10px;" @click="Register"><span class="mdi mdi-account-plus"></span> Register</button>
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
  name: 'LandingTopbar',
  methods: {
    smoothScroll(id) {
      document.body.click();
      document.querySelector(id).scrollIntoView({
        behavior: 'smooth'
      });
    },
    Login(){
      this.$router.push('/login');
    },
    Register(){
      this.$router.push('/Register');
    }
  },
  created() {
    if (localStorage.getItem('AuthToken')) {
      alert('You are already logged in. Redirecting you to the dashboard.');
      this.$router.push('/dashboard');
    }
  },


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
  margin-bottom: 5px;
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



#login {
  border: none;
  border-radius: 5px;
  font-size: 1rem;
  font-weight: 700;
  cursor: pointer;
  transition: buttoncolor 0.3s;
}

#login:hover {
  background-color: rgb(139, 64, 253, 0.1);
  color: #0f0f0f;
  border-radius: 10%;
}

.navbar-nav { 
  margin-left: auto; /* Align nav items to the right */
}


</style>