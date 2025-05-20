<script setup>
import Topbar from '../../components/Topbar.vue'
</script>

<template>
  <div>
    <Topbar />
  </div>
  <div class="statsbody">
    <div style="margin-top: 20px;margin-bottom: 20px;" >
            <h2 id="dashb"><span class="mdi mdi-chart-donut-variant"></span> {{ username }} Statistics Dashboard</h2>
    </div>
    <div class="boxed">
        <div class="row1">
            <div class="square blue-gradient"> 
                <h4><span class="mdi mdi-newspaper-variant"></span></h4>
                <h4>Total Ad Requests</h4> 
                <h5>{{ adtotal }}</h5> 
            </div> 
            <div class="square green-gradient"> 
                <h4><span class="mdi mdi-newspaper-variant-outline"></span></h4>
                <h4>Completed Requests</h4> 
                <h5>{{adcompleted}}</h5> 
            </div> 
            <div class="square red-gradient"> 
                <h4><span class="mdi mdi-cash-register"></span></h4>
                <h4>Total Revenue</h4> 
                <h5>&#8377 {{amount}}</h5> 
            </div> 
            <div class="square purple-gradient"> 
                <h4><span class="mdi mdi-account-group"></span></h4>
                <h4> Total Followers</h4> 
                <h5>{{follower}}</h5> 
            </div>
            <div class="square orange-gradient"> 
                <h4><span class="mdi mdi-receipt-text-check"></span></h4>
                <h4>Approved Ad Requests</h4> 
                <h5>{{adapproved}}</h5> 
            </div> 
       
        </div>
    </div>
       <hr>
    <div class="charts">
        <h2 id="dashb"><span class="mdi mdi-chart-areaspline"></span> {{username}} Statistics Charts</h2>
        <div class="row1">
           <div class="userpie">
            <Pie :data="useractivitydata" :options="useractivityOptions" />
           </div>  
           <div class="sponsorpie">
            <Doughnut :data="sponsorsdata" :options="sponsorsOptions" />
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
import Chart from 'chart.js/auto';
import { Bar } from 'vue-chartjs'
import { Pie } from 'vue-chartjs'
import { Doughnut } from 'vue-chartjs' 
import { Chart as ChartJS, Title, Tooltip, Legend, ArcElement, CategoryScale, LinearScale } from 'chart.js'  
ChartJS.register(Title, Tooltip, Legend, ArcElement, CategoryScale, LinearScale)

export default {
  name: 'AdminStats',
  components: {
  Pie,Bar
      
  },
  data() {
    return {
            auth: '',
            userrole: '',
            username: '',
            amount: 0,
            adapproved: 0,
            adcompleted: 0,
            adrejected: 0,
            adtotal: 0,
            follower:'',
}
    
  },
  methods: {
            getboxeddata(){
                axios
                    .get('http://localhost:5000/influencer/stats', {
                        headers: {
                            'Authorization': this.auth}})
                    .then(response => {
                        console.log(response.data);
                        this.amount = response.data.revenue;
                        this.adapproved = response.data.approved_ad_requests;
                        this.adcompleted = response.data.completed_ad_requests;
                        this.adrejected = response.data.rejected;
                        this.adtotal = response.data.total_ad_requests;
                        this.follower = response.data.totalfollowers;
                    })
                    .catch(error => {
                        console.log(error);
                        alert("Error fetching data");
                    }); 
                },
  },
  computed: {
   
    useractivitydata() { return{ 
                    labels: ['Completed Ad Requests', 'Incomplete Ad Requests'],
                    datasets: [{ backgroundColor: ['#41B883','#8A2BE2'], 
                    data: [this.adcompleted, this.adtotal-this.adcompleted-this.adrejected]}]
            }},
    useractivityOptions(){ return { responsive: true, plugins: { title: { display: true, text: 'Ad Request Completion Chart',  
            font: { size: 18 } } } }
        },
    sponsorsdata() { return{ 
                    labels: ['Approved Ad Requests', 'Rejected Ad Requests'],
                    datasets: [{ backgroundColor: ['#FFCE56', '#4BC0C0'], 
                    data: [this.adapproved, this.adrejected]}]
            }},
    sponsorsOptions(){ return { responsive: true, plugins: { title: { display: true, text: 'Ad Request Approval Ratio Chart', font: { size: 18 } } } }
        },




},
  watch: {
    
  },
  mounted() {
    
  },
  created() {
    this.auth = localStorage.getItem('AuthToken');
    this.userrole = localStorage.getItem('userrole');
    this.username = localStorage.getItem('username');
    this.userid = localStorage.getItem('userid');
    this.getboxeddata();
  }
}
</script>

<style scoped>
.statsbody {
  margin-top: 25px;
  display: flex;
  flex-direction: column;
  width: 80%;
  border: 5px solid #000000;
  align-self: center;
    border-radius: 20px;
  margin-bottom: 40px;
}

.charts {
  display: flex;
  flex-direction: column;
  width: 95%;
  border: 5px solid #000000;
  align-self: center;
  border-radius: 20px;
  background-color: #f9f9f9;
  padding: 20px;
  justify-content: space-evenly;
  margin-bottom: 25px;
}


.charts .row1 {
  display: flex;
  flex-direction: row;
  width: 100%;
  flex-wrap: wrap;
  justify-content: space-evenly;
  align-self: center;
  padding: 20px;

}

.charts .row2 {
  display: flex;
  flex-direction: row;
  width: 100%;
  flex-wrap: wrap;
  justify-content: space-evenly;
  padding: 20px;

}

.charts .row3 {
  display: flex;
  flex-direction: row;
  width: 100%;
  flex-wrap: wrap;
  justify-content: space-evenly;
  padding: 20px;
  
}

.userpie {
  width: 48%;
  display: flex;
  flex-direction: row;
  height:500px;
}

.sponsorpie {
  width: 48%;
  display: flex;
  flex-direction: row;
  height:500px;
}

.userpie1 {
  width: 48%;
  display: flex;
  
}

.sponsorpie1 {
  width: 48%;
  display: flex;
  
}


@media screen and (max-width: 600px) {
  .userpie {
    width: 100%;
    display: flex;
    flex-direction: row;
    width: 100%;
  }
  .sponsorpie {
    width: 100%;
    display: flex;
    flex-direction: row;
    width: 100%;}
}


#dashb {
  
  font-weight: bold;
  color: #000000;
  text-align: center;
  border-bottom: 3px solid #000000;
    padding-bottom: 10px;
}

.statsbody .boxed { 
    display: flex; 
    flex-wrap: wrap;
    justify-content: space-evenly; 
    gap: 15px; 
} 

.statsbody .boxed .row1 {
    display: flex; 
    flex-direction: row;
    justify-content: space-evenly;
    flex-wrap: wrap; 
    gap: 15px; 
    justify-content: center; 
    margin-top: 20px; 
}

.statsbody .boxed .row2 {
    display: flex; 
    flex-direction: row;
    justify-content: space-evenly;
    flex-wrap: wrap; 
    gap:15px; 
    justify-content: center; 
    margin-top: 20px; 
}

.statsbody .boxed .row3 {
    display: flex; 
    flex-direction: row;
    justify-content: space-evenly;
    flex-wrap: wrap; 
    gap: 15px; 
    justify-content: center; 
    margin-top: 20px; 
}

.square { 
    width: 185px; 
    height: 180px; 
    display: flex; 
    flex-direction: column; 
    justify-content: center; 
    align-items: center; 
    color: white; 
    border-radius: 10px; 
    padding: 20px; 
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); 
    text-align: center; 
} 
    
.blue-gradient { 
    background: linear-gradient(45deg, #2196F3, #21CBF3); 
} 

.green-gradient { 
    background: linear-gradient(45deg, #4CAF50, #8BC34A); 
} 

.red-gradient { 
    background: linear-gradient(45deg, #F44336, #E57373); 
} 

.purple-gradient {
     background: linear-gradient(45deg, #9C27B0, #BA68C8); 
     }

.orange-gradient { 
    background: linear-gradient(45deg, #FF5722, #FF9800);
} 

.teal-gradient { 
    background: linear-gradient(45deg, #009688, #4DB6AC); 
} 

.pink-gradient { 
    background: linear-gradient(45deg, #E91E63, #F48FB1); 
} 
.yellow-gradient { 
    background: linear-gradient(45deg, #FFD700, #FFC107);
}

.coral-gradient { 
    background: linear-gradient(45deg, #5df9a6, #00b84a); 
}

.navy-gradient { 
    background: linear-gradient(45deg, #000080, #0000CD);
}

.sunset-gradient { background: linear-gradient(45deg, #FF7E5F, #FEB47B); /* Sunset orange and light pink */ color: white; }

.magenta-gradient {
  background: linear-gradient(45deg, #ff00ff, #ff33cc); /* Magenta and Deep Pink */
  color: white;
}

.cyan-gradient {
  background: linear-gradient(45deg, #00FFFF, #00BFFF); /* Cyan and Deep Sky Blue */
  color: rgb(242, 242, 242); /* Black text for better visibility */
}




</style>