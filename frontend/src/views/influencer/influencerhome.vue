<script setup>
import Topbar from '../../components/Topbar.vue'
</script>

<template>
  <div>
    <Topbar />
  </div>
  <div style="margin-top: 30px;margin-bottom: 20px; align-self: center;" >
              <h1><span class="mdi mdi-home-variant"></span>Influencer Home</h1>
    </div>
    <div class="searchbar">
            <select class="btn btn-outline-primary" v-model="selectedOption" id="searchOption" > 
                <option value="" disabled selected>Select Option</option>
                <option value="sponsorName">Sponsor Name</option> 
                <option value="campaignTitle">Campaign Title</option> 
                <option value="relatedNiche">Related Niche</option> 
                <option value="relatedIndustry">Related Industry</option> 
            </select>
            <input type="text" class="btn btn-outline-info" v-model="searchKeyword"  placeholder="Enter search keyword" />
            <button id="clear" class="btn btn-outline-danger" @click="clearSearch" ><span class="mdi mdi-backspace-reverse" ></span> Clear</button>
    </div><hr>
  <div class="homebody">
        <div class="showcase" v-if="flagged==false">
            <div class="card border-info mb-3" v-for="campaign in filteredCampaigns" :key="campaign.id">
                <div class="card-header bg-transparent border-info" style="text-align: justify;"><b>Advertisement Campaign</b></div>
                    <div class="card-body text">
                        <h5 class="card-title"><strong>Title:</strong> {{ campaign.title }}</h5>
                        <h5 class="card-text"><strong>Started On:</strong> {{ campaign.start_date }}</h5>
                        <h5 class="card-text"><strong>Ending On:</strong> {{ campaign.end_date }}</h5>
                        <h5 class="card-text"><strong>Sponsor:</strong> {{ campaign.sponsor }}</h5>
                        <h5 class="card-text"><strong>Industry:</strong> {{ campaign.related_industry }}</h5>
                        <h5 class="card-text"><strong>Niche:</strong> {{ campaign.related_niche }}</h5>
                        <h5 class="card-text"><strong>Duration Complete:</strong> {{ campaign.campaign_completion }}%</h5>
                    </div>
                <div class="card-footer bg-transparent border-info" style="display: flex; gap:20px; justify-content: space-evenly;">
                    <button class="btn btn-primary" @click="viewCampaign(campaign.id)"><span class="mdi mdi-newspaper-variant"></span> View Campaign</button>
                    <button class="btn btn-success" @click="viewsponsor(campaign.sponsor_id)"><span class="mdi mdi-card-account-details"></span> View Sponsor</button>
                </div>
            </div>
        </div>
        <div v-if="filteredCampaigns.length === 0 && flagged==false" style="text-align: center; margin-top: 20px;">
            <h3>No Public Campaigns found</h3>
        </div>
        <div v-if="flagged==true"  style="text-align: center; margin-top: 20px;">
            <h3>Your Account is Flagged By Admin.<br> For quries contact at: Admin@CreativeMerge.com</h3>
        </div>
  </div>
  <div class="footer" style="background-color: #333; color: white; text-align: center; position: relative; justify-content: center; left: 0; width: 100%; font-family: 'Doto', sans-serif; font-optical-sizing: auto; font-weight: 1000; font-style: normal; font-variation-settings: 'ROND' 100; font-size: 1.1rem;">
  <p align="center">© 2024 | © 21F3001516 | Influencer Engagement Sponsor Coordination Platform | © CreativeMerge</p>
</div>

</template>

<script>
import axios from 'axios';
export default {
  name: 'InfluencerHome',
  data() {
    return {
        selectedOption: '',
        searchKeyword: '',
        campaigns: [],
        auth:'',
        username: '',
        userrole:'',
        campaignid: '',
        flagged: false
    }
  },
  methods: {
        getcampaigns() {
            axios
            .get('http://localhost:5000/influencer/home', {
                headers: {
                    Authorization: `${this.auth}`
                }
            })
            .then(response => {
                console.log(response);
                this.campaigns = response.data.data;
                this.flagged = response.data.flag;
            })
            .catch(error => {
                console.log(error);
            });
        },
        viewCampaign(id) {
            this.$router.push({ name: 'ViewCampaignPublicPage', params: { campaign_id: id } });
        },
        viewsponsor(id) {
            this.$router.push({ name: 'SponsorProfilePublicPage', params: { users_id: id } });
        },
        clearSearch() { this.selectedOption = ''; this.searchKeyword = '';},submitSearch() {console.log('Search submitted'); },

  },
  computed: {
    filteredCampaigns() { 
        if (!this.selectedOption || !this.searchKeyword) { 
            return this.campaigns; }
        if(this.selectedOption === 'sponsorName' && this.searchKeyword) { 
            return this.campaigns.filter((campaign) => { return campaign.sponsor.toLowerCase().includes(this.searchKeyword.toLowerCase()); }); }
        if(this.selectedOption === 'campaignTitle' && this.searchKeyword) {
            return this.campaigns.filter((campaign) => { return campaign.title.toLowerCase().includes(this.searchKeyword.toLowerCase()); }); }
        if(this.selectedOption === 'relatedNiche' && this.searchKeyword) {
            return this.campaigns.filter((campaign) => { return campaign.related_niche.toLowerCase().includes(this.searchKeyword.toLowerCase()); }); }
        if(this.selectedOption === 'relatedIndustry' && this.searchKeyword) {
            return this.campaigns.filter((campaign) => { return campaign.related_industry.toLowerCase().includes(this.searchKeyword.toLowerCase()); }); }
        
          },
  },
  watch: {
    
  },
  mounted() {
    
  },
    created() {
        this.auth = localStorage.getItem('AuthToken');
        this.username = localStorage.getItem('username');
        this.userrole = localStorage.getItem('userrole');

        this.getcampaigns();
    }
}
</script>

<style scoped>

.homebody {
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
  width:80%;
  align-self: center;
  margin-top:10px;
  padding: 20px;
  min-height: 80vh;

}

.searchbar {
  display: flex;
  justify-content: center;
  flex-direction: row;
  width:100%;
  align-self: start;
  padding: 20px;
}

.showcase {
    display: flex;
    align-self: center;
    gap:20px;
}




select {
  width: 20%;
  border-top-left-radius: 20px; border-bottom-left-radius: 20px; border-top-right-radius: 0px; border-bottom-right-radius: 0px;
}

input {
  width: 40%;
  border-top-left-radius: 0px; border-bottom-left-radius: 0px; border-top-right-radius: 0px; border-bottom-right-radius: 0px;
}

#submit, #clear {
 width: 10%;

}

#submit {
  border-top-left-radius: 0px; border-bottom-left-radius: 0px; border-top-right-radius: 0px; border-bottom-right-radius: 0px;
}

#clear {
  border-top-left-radius: 0px; border-bottom-left-radius: 0px; border-top-right-radius: 20px; border-bottom-right-radius: 20px;}

hr {
  margin-top: 20px;
}

@media (max-width:1000px){
    .showcase {
        flex-direction: column;
        flex-wrap: wrap;
        width:100%
    }
    .homebody {
        display: flex;
        flex-direction: column;
    }
   .card {
       width: 100%;
   }
}

@media (max-width:770px){
    .searchbar {
        flex-direction: column;
        flex-wrap: wrap;
        width:100%;
        align-self: center;
        padding: 20px;
        align-items: center;
    }
    select {
  width: 100%;
  border-top-left-radius: 7px; border-bottom-left-radius: 7px; border-top-right-radius: 7px; border-bottom-right-radius: 7px;
}

input {
  width: 100%;
  border-top-left-radius: 7px; border-bottom-left-radius: 7px; border-top-right-radius: 7px; border-bottom-right-radius: 7px;
}

#submit, #clear {
 width: 100%; border-top-left-radius: 7px; border-bottom-left-radius: 7px; border-top-right-radius: 7px; border-bottom-right-radius: 7px;
}

hr {
  margin-top: 20px;
}
}

</style>