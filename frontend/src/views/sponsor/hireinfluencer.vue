<script setup>
import Topbar from '../../components/Topbar.vue'
</script>

<template>
  <div>
    <Topbar />
  </div>
  <div style="margin-top: 30px;margin-bottom: 20px; align-self: center;" >
              <h1><span class="mdi mdi-account-group"></span> Hire Industry Influencer</h1>
    </div> 
    <div class="searchbar">
            <select class="btn btn-outline-primary" v-model="selectedOption" id="searchOption" > 
                <option value="" disabled selected>Select Option</option>
                <option value="sponsorName">Influencer Name</option> 
                <option value="rating">Rating</option> 
                <option value="relatedNiche">Niche</option> 
                <option value="followers">Followers</option>  
            </select>
            <input type="text" class="btn btn-outline-info" v-model="searchKeyword"  placeholder="Enter search keyword / No for followers_ratings greater than equal " />
            <button id="clear" class="btn btn-outline-danger" @click="clearSearch" ><span class="mdi mdi-backspace-reverse" ></span> Clear</button>
    </div><hr>
  <div class="homebody">
        <div class="showcase" v-if="filteredinfluencers.length>0">
            <div class="card border-info mb-3" v-for="influencer in filteredinfluencers" :key="influencer.id">
                <div class="card-header bg-transparent border-info" style="text-align: justify; display: flex; justify-content: space-between;">
                    <b>Influencer</b>
                    <b>@{{ influencer.username }}</b>
                </div>
                <img :src="`https://api.dicebear.com/6.x/micah/svg?seed=${influencer.username}`" class="card-img-top avatar" :alt="`Image of ${influencer.name}`" style="align-self: center;margin-top: 8px;">
                <div class="card-body text">
                        <h5 class="card-title"><strong>Name:</strong> {{ influencer.name }}</h5>
                        <h5 class="card-text"><strong>Platforms:</strong> <span class="mdi mdi-youtube" v-if="influencer.yt" ></span><span class="mdi mdi-instagram"  v-if="influencer.insta" ></span>
                        <span class="mdi mdi-facebook" v-if="influencer.fb" ></span><span class="mdi mdi-twitter"  v-if="influencer.twitter" ></span>
                        <span class="mdi mdi-at"  v-if="influencer.thread"  ></span><span class="mdi mdi-music-note-outline"  v-if="influencer.tiktok" ></span>
                        <span class="mdi mdi-twitch"  v-if="influencer.twitch" ></span><span class="mdi mdi-kickstarter"  v-if="influencer.kick" ></span>
                        <span class="mdi mdi-snapchat"  v-if="influencer.snapchat"  ></span><span class="mdi mdi-linkedin"  v-if="influencer.linkedin" ></span></h5>
                        <h5 class="card-text"><strong>Industry:</strong> {{ influencer.industry }}</h5>
                        <h5 class="card-text"><strong>Niche:</strong> {{ influencer.niche }}</h5>
                        <h5 class="card-text"><strong>Email:</strong> {{ influencer.email }}</h5>
                        <h5 class="card-text"><strong>Followers:</strong> {{ influencer.totalreach }}</h5>
                        <h5 class="card-text" style="display: flex; gap:10px"><strong>Influencer Rating:</strong> <Rating v-model="influencer.avg_rating" readonly /></h5>
                    </div>
                <div class="card-footer bg-transparent border-info" style="display: flex; gap:20px; justify-content: space-evenly;">
                    <button class="btn btn-primary" @click="requestinfluencer(influencer.id)"><span class="mdi mdi-near-me"></span> Hire Influencer</button>
                    <button class="btn btn-success" @click="viewinfluencer(influencer.id)"><span class="mdi mdi-card-account-details"></span> View Influencer</button>
                </div>
            </div>
        </div>
        <dir>
            <h3 v-if="filteredinfluencers.length === 0" style="text-align: center; margin-top: 20px;">No Industry Influencers Found</h3>
        </dir>
  </div>

  <div style="background-color: #333; color: white; text-align: center; position: relative; bottom: 0; left: 0; width: 100%; font-family: 'Doto', sans-serif; font-optical-sizing: auto; font-weight: 1000; font-style: normal; font-variation-settings: 'ROND' 100; font-size: 1.1rem; height: 50px;">
  <p align="center" style="margin: 0; line-height: 50px;">© 2024 | © 21F3001516 | Influencer Engagement Sponsor Coordination Platform | © CreativeMerge</p>
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
        influencers: [],
        auth:'',
        username: '',
        userrole:'',
        campaignid: '',
        adid:''
    }
  },
  methods: {
        getcampaigns() {
            axios
            .get('http://localhost:5000/sponsor/'+this.campaignid+'/hireinfluencer', {
                headers: {
                    Authorization: `${this.auth}`
                }
            })
            .then(response => {
                console.log(response);
                this.influencers = response.data;
            })
            .catch(error => {
                console.log(error);
            });
        },
        viewCampaign(id) {
            this.$router.push({ name: 'ViewCampaignPublicPage', params: { campaign_id: id } });
        },
        viewinfluencer(id) {
            this.$router.push({ name: 'InfluencerProfilePublicPage', params: { users_id: id } });
        },
        clearSearch() { this.selectedOption = ''; this.searchKeyword = '';},submitSearch() {console.log('Search submitted'); },
       requestinfluencer(id){
            axios
            .post('http://localhost:5000/sponsor/'+this.adid+'/hireinfluencer/'+id,{} ,{
                headers: {
                    Authorization: `${this.auth}`
                }
            })
            .then(response => {
                console.log(response);
                this.$router.go(-1);
            })
            .catch(error => {
                console.log(error);
            });
       }
  },
  computed: {
    filteredinfluencers() {
    if (!this.selectedOption || !this.searchKeyword) {
        return this.influencers;
    }

    const searchLower = this.searchKeyword.toLowerCase();
    
    if (this.selectedOption === 'sponsorName' && this.searchKeyword) {
        return this.influencers.filter((influencer) => {
            return influencer.name.toLowerCase().includes(searchLower);
        });
    }

    if (this.selectedOption === 'rating' && this.searchKeyword) {
        const searchNumber = parseFloat(this.searchKeyword);
        return this.influencers.filter((influencer) => {
            return influencer.avg_rating >= searchNumber;
        });
    }

    if (this.selectedOption === 'relatedNiche' && this.searchKeyword) {
        return this.influencers.filter((influencer) => {
            return influencer.niche.toLowerCase().includes(searchLower);
        });
    }

    if (this.selectedOption === 'followers' && this.searchKeyword) {
        const searchNumber = parseInt(this.searchKeyword, 10);
        return this.influencers.filter((influencer) => {
            return influencer.reach >= searchNumber;
        });
    }

    return this.influencers; // Return all influencers if no filters match
}
  },
  watch: {
    
  },
  mounted() {
    
  },
    created() {
        this.auth = localStorage.getItem('AuthToken');
        this.username = localStorage.getItem('username');
        this.userrole = localStorage.getItem('userrole');
        this.campaignid = this.$route.params.campaign_id;
        this.adid = this.$route.params.Ad_id;
        this.getcampaigns();
    }
}
</script>

<style scoped>

.homebody {
  display: flex;
  height: 100vh;
  flex-direction: column;
  flex-wrap: wrap;
  width:80%;
  align-self: center;
  margin-top:10px;
  padding: 20px;


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
    flex-wrap: wrap;
    justify-content: space-evenly;
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