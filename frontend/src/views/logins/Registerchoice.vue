<script setup>
import LandingTopbar from '../../components/LandingTopbar.vue'
</script>
<template>
<div>
  <LandingTopbar />
</div>
<div class="registeroptions">
<div class="sponsors">
    <div class="card">
        <div class="card-info">
            <img id="logospon" width="100" height="100" src="https://img.icons8.com/external-wanicon-lineal-color-wanicon/100/external-sponsored-digital-content-wanicon-lineal-color-wanicon.png" alt="Sponsor"/>
            <h3 style="opacity: 1 !important;">Register as Sponsor</h3>
            <button class="button" id="ChooseSpon" @click="Spon"><span class="mdi mdi-domain"></span> Register Sponsor</button>
        </div>
    </div>
</div>

<div class="influencers">
    <div class="card">
        <div class="card-info">
            <img id="logoinflu" width="100" height="100" src="https://img.icons8.com/external-wanicon-lineal-color-wanicon/100/external-influencer-marketing-strategy-wanicon-lineal-color-wanicon.png" alt="Influencer"/>
            <h3>Register as Influencer</h3>
            <button class="button" id="ChooseInflu" @click="Influ"><span class="mdi mdi-account-tie"></span> Register Influencer</button>
        </div>
    </div>
</div>
</div>

<div style="background-color: #333; color: white; text-align: center; position: relative; bottom: 0; left: 0; width: 100%; font-family: 'Doto', sans-serif; font-optical-sizing: auto; font-weight: 1000; font-style: normal; font-variation-settings: 'ROND' 100; font-size: 1.1rem; height: 50px;">
  <p align="center" style="margin: 0; line-height: 50px;">© 2024 | © 21F3001516 | Influencer Engagement Sponsor Coordination Platform | © CreativeMerge</p>
</div>


</template>
<script>
export default {
  name: 'Registerchoice',
  methods: {
    Spon(){
      this.$router.push('/Registersponsor');
    },
    Influ(){
      this.$router.push('/Registerinfluencer');
    }
  }
}




</script>
<style scoped>
/* From Uiverse.io by alexruix */ 
.registeroptions {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
  margin-top: 50px;
  justify-content: space-evenly;
  margin-bottom: 260px;
}

#logospon {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
}

#logoinflu {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
}

.card {
 --background: linear-gradient(to left, #f7ba2b 0%, #ea5358 100%);
 width: 300px;
 height: 354px;
 padding: 5px;
 border-radius: 1rem;
 overflow: visible;
 background: #f7ba2b;
 background: var(--background);
 position: relative;
 z-index: 1;
 margin-top: 25px;
}

.card::after {
 position: absolute;
 content: "";
 top: 30px;
 left: 0;
 right: 0;
 z-index: -1;
 height: 100%;
 width: 100%;
 transform: scale(0.8);
 filter: blur(25px);
 background: #f7ba2b;
 background: var(--background);
 transition: opacity .5s;
}

.card-info {
 --color: #ffffff;
 background: var(--color);
 color: var(--color);
 display: flex;
 justify-content: center;
 align-items: center;
 flex-direction: column;
 gap: 3rem;
 width: 100%;
 height: 100%;
 overflow: visible;
 border-radius: .7rem;
}

.card .title {
 font-weight: bold;
 letter-spacing: .1em;
}

.card-info h3 { 
    color: #1e1c1c;
    opacity: 1 !important; 
    font-family: sans-serif;
    font-size: 1.7rem;
}
.footer {
        background-color: #333;
        color: #fff;
        text-align: center;
        padding: 10px 0;
        bottom: 0;
        width: 100%;
    }
/*Hover*/
.card:hover::after {
 opacity: 0;
}

.card:hover .card-info {
 color: #f7ba2b;
 transition: color 1s;
}


/* From Uiverse.io by suda-code */ 
button{
  padding: 12.5px 30px;
  border: 0;
  border-radius: 100px;
  background-color: #2ba8fb;
  color: #ffffff;
  font-weight: Bold;
  transition: all 0.5s;
  -webkit-transition: all 0.5s;
}

button:hover {
  background-color: #6fc5ff;
  box-shadow: 0 0 20px #6fc5ff50;
  transform: scale(1.1);
}

button:active {
  background-color: #3d94cf;
  transition: all 0.25s;
  -webkit-transition: all 0.25s;
  box-shadow: none;
  transform: scale(0.98);
}



</style>