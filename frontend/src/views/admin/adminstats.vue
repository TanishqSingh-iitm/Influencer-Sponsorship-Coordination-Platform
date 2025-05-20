<script setup>
import Topbar from '../../components/Topbar.vue'
</script>

<template>
  <div>
    <Topbar />
  </div>
  <div class="statsbody">
    <div style="margin-top: 20px;margin-bottom: 20px;" >
            <h2 id="dashb"><span class="mdi mdi-chart-donut-variant"></span> Admin Statistics Dashboard</h2>
    </div>
    <div class="boxed">
        <div class="row1">
            <div class="square blue-gradient"> 
                <h4><span class="mdi mdi-account-group"></span></h4>
                <h4>Total Users</h4> 
                <h5>{{ users }}</h5> 
            </div> 
            <div class="square green-gradient"> 
                <h4><span class="mdi mdi-account-multiple-check"></span></h4>
                <h4>Total Active Users</h4> 
                <h5>{{activeusers}}</h5> 
            </div> 
            <div class="square red-gradient"> 
                <h4><span class="mdi mdi-account-multiple-remove"></span></h4>
                <h4>Total Inactive Users</h4> 
                <h5>{{inactiveusers}}</h5> 
            </div> 
            <div class="square purple-gradient"> 
                <h4><span class="mdi mdi-domain"></span></h4>
                <h4>Total Sponsors</h4> 
                <h5>{{sponsors}}</h5> 
            </div>
            <div class="square orange-gradient"> 
                <h4><span class="mdi mdi-domain-remove"></span></h4>
                <h4>Flagged Sponsors</h4> 
                <h5>{{flaggedsponsors}}</h5> 
            </div> 
       
        </div>
        <div class="row2">
            <div class="square teal-gradient"> 
                <h4><span class="mdi mdi-account"></span></h4>
                <h4>Total Influencers</h4> 
                <h5>{{influencers}}</h5> 
            </div> 
            <div class="square pink-gradient"> 
                <h4><span class="mdi mdi-account-remove"></span></h4>
                <h4>Flagged Influencers</h4> 
                <h5>{{flaggedinfluencers}}</h5> 
            </div> 
            <div class="square yellow-gradient">
                <h4><span class="mdi mdi-book-open-blank-variant"></span></h4> 
                <h4>Total Campaigns</h4> 
                <h5>{{campaigns}}</h5> 
            </div>
            <div class="square coral-gradient"> 
                <h4><span class="mdi mdi-book-open-variant"></span></h4>
                <h4>Completed Campaigns</h4> 
                <h5>{{completedcampaigns}}</h5> 
            </div> 
            <div class="square navy-gradient"> 
                <h4><span class="mdi mdi-cash-multiple"></span></h4>
                <h4>Total Revenue</h4> 
                <h5>&#8377 {{wallet}}</h5> 
            </div>
        </div>
        <div class="row3">
            <div class="square sunset-gradient">
                <h4><span class="mdi mdi-advertisements"></span></h4> 
                <h4>Total Promotions</h4> 
                <h5>{{totalpromotions}}</h5> 
            </div>
            <div class="square magenta-gradient"> 
                <h4><span class="mdi mdi-eye"></span></h4>
                <h4>Audience Reach</h4> 
                <h5>{{audience}}</h5> 
            </div> 
            <div class="square cyan-gradient"> 
                <h4><span class="mdi mdi-face-man-shimmer"></span></h4>
                <h4>Leading Influencer</h4> 
                <h5>{{leadinginfluencer}}</h5> 
            </div>
        </div>
    </div><hr>
    <div class="charts">
        <h2 id="dashb"><span class="mdi mdi-chart-areaspline"></span> Admin Statistics Charts</h2>
        <div class="row1">
           <div class="userpie">
            <Pie :data="useractivitydata" :options="useractivityOptions" />
           </div>  
           <div class="sponsorpie">
            <Doughnut :data="sponsorsdata" :options="sponsorsOptions" />
           </div>
        </div>
        <div class="row2">
            <div class="userpie">
 
            <Doughnut :data="influencerdata" :options="influencerOptions" />
           </div>  
           <div class="sponsorpie">
            <Pie :data="campaigndata" :options="campaignOptions" />
           </div>
        </div>
        <div class="row3">
            <div class="userpie1" >
                    <Bar style="height: 400px;"  :data="campaignvisibilitydata" :options="campaignvisibilityOptions" />
            </div>  
            <div class="sponsorpie1" >
                  <Bar style="height: 400px;"  :data="adsdata" :options="adsOptions" />
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
            wallet: 0,
            users: 0,
            sponsors: 0,
            influencers: 0,
            campaigns: 0,
            inactiveusers: 0,
            activeusers: 0,
            flaggedinfluencers: 0,
            flaggedsponsors: 0,
            completedcampaigns: 0,
            audience: 0,
            leadinginfluencer: '',
            totalpromotions: 0,
            publiccampaigns: 0,
            adclosed: 0,
            adpending: 0,
            adopen: 0,
            adcompleted: 0,
            adrequested: 0,
            adrejected: 0,
            adapproved: 0,
            adnegociated: 0,
            adinprogress: 0,
          
}
    
  },
  methods: {
            getboxeddata(){
                axios
                    .get('http://localhost:5000/admin/statistics', {
                        headers: {
                            'Authorization': this.auth}})
                    .then(response => {
                        console.log(response.data);
                        this.users = response.data.total_users;
                        this.sponsors = response.data.total_sponsors;
                        this.influencers = response.data.total_influencers;
                        this.campaigns = response.data.totalcampaigns;
                        this.inactiveusers = response.data.totalinactiveusers;
                        this.activeusers = response.data.totalactiveusers;
                        this.flaggedinfluencers = response.data.totalflaggedinfluencers;
                        this.flaggedsponsors = response.data.totalflaggedsponsors;
                        this.completedcampaigns = response.data.completedcampaigns;
                        this.audience = response.data.audience;
                        this.leadinginfluencer = response.data.leadinginfluencer;
                        this.totalpromotions = response.data.totalpromotions;
                        this.wallet = response.data.revenue;
                        this.publiccampaigns = response.data.publiccampaign;
                        this.adclosed = response.data.adclosed;
                        this.adpending = response.data.adpending;
                        this.adopen = response.data.adopen;
                        this.adcompleted = response.data.adcompleted;
                        this.adrequested = response.data.adrequested;
                        this.adrejected = response.data.adrejected;
                        this.adapproved = response.data.adapproved;
                        this.adnegociated = response.data.adnegociated;
                        this.adinprogress = response.data.adinprogress;
                        this.totalpromotions = response.data.totalads;
                        this.leadinginfluencer = response.data.topinfluencer;
                    })
                    .catch(error => {
                        console.log(error);
                        alert("Error fetching data");
                    }); 
                },
  },
  computed: {
   
    useractivitydata() { return{ 
                    labels: ['Active Users', 'InActive Users'],
                    datasets: [{ backgroundColor: ['#41B883', '#E46651'], 
                    data: [this.activeusers, this.inactiveusers]}]
            }},
    useractivityOptions(){ return { responsive: true, plugins: { title: { display: true, text: 'User Activity Chart',  
            font: { size: 18 } } } }
        },
    sponsorsdata() { return{ 
                    labels: ['Active Sponsors', 'Flagged Sponsors'],
                    datasets: [{ backgroundColor: ['#FFCE56', '#4BC0C0'], 
                    data: [this.sponsors, this.flaggedsponsors]}]
            }},
    sponsorsOptions(){ return { responsive: true, plugins: { title: { display: true, text: 'Sponsor Activity Chart', font: { size: 18 } } } }
        },
    influencerdata(){ return{ 
                    labels: ['Active Influencers', 'Flagged Influencers'],
                    datasets: [{ backgroundColor: ['#7FDBFF', '#FF9F40'], 
                    data: [this.influencers, this.flaggedinfluencers]}]
            }},
    influencerOptions(){ return { responsive: true, plugins: { title: { display: true, text: 'Influencer Activity Chart', font: { size: 18 } } } }},
    
    campaigndata() { return{ 
                    labels: ['Completed Campaign', 'Pending Campaign'],
                    datasets: [{ label: ['Completed', 'Pending'], backgroundColor: ['#FF6384', '#9966FF'], 
                    data: [this.completedcampaigns, this.campaigns - this.completedcampaigns]}]
            }},
    campaignOptions(){ return { responsive: true, plugins: { title: { display: true, text: 'Campaign Completions Chart', font: { size: 18 } } } }},

    campaignvisibilitydata() { return{ 
                    labels: ['Public Campaign', 'Private Campaign'],
                    datasets: [{ label: ['Public', 'Private'], backgroundColor: ['#8A2BE2', '#00CED1'], 
                    data: [this.publiccampaigns, this.campaigns - this.publiccampaigns]}]
            }},
    campaignvisibilityOptions(){ return { responsive: true, plugins: { title: { display: true, text: 'Campaign Visibility Chart', font: { size: 18 } } } }},
    
    adsdata() { return{ 
                    labels: ['Open', 'Closed','Completed','Requested','Pending','Negociated','Approved','Rejected','InProgress'],
                    datasets: [{ label: ['Open', 'Closed','Completed','Requested','Pending','Negociated','Approved','Rejected','InProgress'], backgroundColor: ['#8A2BE2', '#00CED1','#FF5733','#6A5ACD','#20B2AA','#DC143C','#ADFF2F','#FF69B4','#6495ED'], 
                    data: [this.adopen, this.adclosed, this.adcompleted, this.adrequested, this.adpending, this.adnegociated, this.adapproved, this.adrejected, this.adinprogress]}]
            }},
    adsOptions(){ return { responsive: true, plugins: { title: { display: true, text: 'Ad Requests Status Chart', font: { size: 18 } } } }},



},
  watch: {
    
  },
  mounted() {
    
  },
  created() {
    this.auth = localStorage.getItem('AuthToken');
    this.userrole = localStorage.getItem('userrole');
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