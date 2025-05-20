<script setup>
import Topbar from '../../components/Topbar.vue'
import { computed } from 'vue';

</script>

<template>
  <div>
    <Topbar />
  </div>
  <div class="profbody" align="center">
    <div class="contents">
        <h1 style="border-bottom: 5px solid #000000; width: 100%; padding: 5px;">Influencer Profile</h1>
        <div>
            <h3>Personal Information</h3>
            <div class="name">
                <h4><b>Name:</b> {{ name }}</h4>
            </div>
            <div class="usernamei">
                <h4><b>Username:</b> {{ Username }}</h4>
            </div>
            <div class="email">
                <h4><b>Email:</b> {{ email }}</h4>
            </div>
            <div class="industry">
                <h4><b>Industry:</b> {{industry}}</h4>
            </div>
            <div class="niche">
                <h4><b>Niche:</b> {{niche}}</h4>
            </div>
            <div class="datejoined">
                <h4><b>Date Joined:</b> {{datejoined}}</h4>
            </div>
            <div class="bio">
                <h4><b>Bio:</b></h4>
                <h5 style="text-align: justify;">{{ bio }}</h5>
            </div>
            
        </div>

    </div>
    
    <div class="profimage">
      
        <img :src="imgsrc" alt="Avatar" class="avatar">
        
        <h4 style="font-family: Doto; font-weight: 900; font-variation-settings:ROND 100; font-optical-sizing: auto;">@ {{Username}}</h4>
        <h4 style="font-family: cursive;"><b>{{ name }}</b></h4>
        <h5><b>Influencer</b></h5>
        
        <div class="contentbtn">
          <label for="rating" style="font-weight: bold;">Rating:<Rating id="rating" v-model="value"  readonly /></label>
        </div>
        <h5><span class="mdi mdi-monitor-cellphone-star"></span><b> Social Presence</b></h5>
        <div class="social">
            <div class="row1">
                <button type="button" class="btn btn-outline-danger"  v-tooltip.top="'Youtube'" v-if=" isyt " @click="yt"><span class="mdi mdi-youtube"></span> {{ ytfollowers }} Followers</button>
                <button type="button" class="btn btn-outline-info"  v-tooltip.top="'Instagram'" id="instabtn" style="color: #C13584; border-color: #C13584;" v-if=" isinsta " @click="insta"><span class="mdi mdi-instagram"></span> {{ instafollowers }} Followers</button>
                <button type="button" class="btn btn-outline-primary"  v-tooltip.top="'Facebook'" v-if="isfb " @click="fb" ><span class="mdi mdi-facebook" ></span> {{fbfollowers}} Followers</button>
                <button type="button" class="btn btn-outline-info"  v-tooltip.top="'Twitter / X'" v-if="isx " @click="xt" ><span class="mdi mdi-twitter" ></span> {{xfollowers}} Followers</button>
                <button type="button" class="btn btn-outline-secondary"  v-tooltip.top="'Threads'" v-if=" isthread" @click="thr"><span class="mdi mdi-at" ></span> {{threadfollowers}} Followers</button>
                <button type="button" class="btn btn-outline-dark"  v-tooltip.top="'TikTok'" style="color: #C13564; border-color: #C13584;" v-if=" istik" @click="tik"><span class="mdi mdi-music-note-outline"></span> {{ tikfollowers }} Followers</button>
                <button type="button" class="btn btn-outline-info"  v-tooltip.top="'Twitch'" id="twitchbtn" style="color: #9146FF; border-color: #9146FF;" v-if="istwitch " @click="twi"><span class="mdi mdi-twitch"></span> {{twitchfollowers}} Followers</button>
                <button type="button" class="btn btn-outline-success"  v-tooltip.top="'Kick'" v-if="iskick " @click="ki"><span class="mdi mdi-kickstarter" ></span> {{kickfollowers}} Followers</button>
                <button type="button" class="btn btn-outline-warning"  v-tooltip.top="'Snapchat'" style="font-weight: 500;"  v-if="issnap " @click="snap"><span class="mdi mdi-snapchat" ></span> {{snapfollowers}} Followers</button>
                <button type="button" class="btn btn-outline-info"  v-tooltip.top="'LinkedIn'" id="linkedbtn" style="color: #0A66C2; border-color: #0A66C2;" v-if=" islinked" @click="lin"><span class="mdi mdi-linkedin"></span> {{linkedfollowers}} Followers</button>

            </div>
            
            <div class="row2">
              <h5 style="align-content: center; justify-content: center;"><span class="mdi mdi-monitor-eye"></span> <b>Total Reach: </b><button class="btn btn-success" style="margin-left:20px ; pointer-events: none;" ><span class="mdi mdi-eye" ></span> {{ totalreach }}</button></h5> 
              <button type="button" class="btn btn-danger" style="font-weight: 500;" @click="openReportModal"><span class="mdi mdi-flag-variant"></span> Report Influencer</button>
            </div>
        </div>
    </div>

  </div>


<div>
  <Footer />
</div>

<!-- Report Modal --> 
<div class="modal fade" id="reportModal" tabindex="-1" aria-labelledby="reportModalLabel" aria-hidden="true"> 
  <div class="modal-dialog"> 
    <div class="modal-content"> 
      <div class="modal-header"> 
        <h1 class="modal-title fs-5" id="reportModalLabel">Report User</h1> 
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button> </div> 
        <div class="modal-body"> 
          <form> <div class="mb-3"> 
            <label for="report-reason" class="col-form-label">Reason:</label> 
            <select class="form-control" id="report-reason" v-model="reportReason"> 
              <option value="">Select a reason</option> 
              <option value="spam">Spam</option> 
              <option value="abuse">Abuse</option> 
              <option value="inappropriate">Inappropriate Content</option> 
              <option value="other">Other</option> </select> 
              <div v-if="reportReasonError" class="text-danger">{{ reportReasonError }}</div> 
            </div><div class="mb-3"> <label for="issue-description" class="col-form-label">Issue:</label> <textarea class="form-control" id="issue-description" v-model="reportIssue"></textarea> <div v-if="reportIssueError" class="text-danger">{{ reportIssueError }}</div> </div> 
            <div class="mb-3"> <label for="report-details" class="col-form-label">Details:</label> 
              <textarea class="form-control" id="report-details" v-model="reportDetails"></textarea> 
              <div v-if="reportDetailsError" class="text-danger">{{ reportDetailsError }}</div> </div> 
            </form> </div> <div class="modal-footer"> 
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button> 
              <button type="button" class="btn btn-primary" @click="validateReportForm">Submit Report</button> 
            </div> 
          </div> 
        </div>
      </div>

      <div style="background-color: #333; color: white; text-align: center; position: relative; bottom: 0; left: 0; width: 100%; font-family: 'Doto', sans-serif; font-optical-sizing: auto; font-weight: 1000; font-style: normal; font-variation-settings: 'ROND' 100; font-size: 1.1rem; height: 50px;">
  <p align="center" style="margin: 0; line-height: 50px;">© 2024 | © 21F3001516 | Influencer Engagement Sponsor Coordination Platform | © CreativeMerge</p>
</div>
</template>

<script>

import Rating from 'primevue/rating';
import Footer from '@/components/Footer.vue';
import axios from 'axios';

export default {
  name: 'InfluencerProfilePrivate',
  data() {
    return {
        value: 0,
        user_id: '',
        token: '',
        Username: '',
        name: '',
        email: '',
        industry: '',
        profilespic: false,
        niche: '',
        bio: '',
        role: 'Influencer',
        datejoined: '',
        lastloged: '',
        isyt: false,
        isinsta: false,
        isx: false,
        isthread: false,
        isfb: false,
        istik: false,
        iskick: false,
        istwitch: false,
        issnap: false,
        islinked: false,
        ytfollowers: '',
        ytlink: '',
        instafollowers: '',
        instalink: '',
        xfollowers: '',
        xlink: '',
        threadfollowers: '',
        threadlink: '',
        fbfollowers: '',
        tikfollowers: '',
        kickfollowers: '',
        twitchfollowers: '',
        snapfollowers: '',
        linkedfollowers: '',
        ytlink: '',
        instalink: '',
        xlink: '',
        threadlink: '',
        fblink: '',
        tiklink: '',
        kicklink: '',
        twitchlink: '',
        snaplink: '',
        linkedlink: '',
        reportReason: '', 
          reportDetails: '',
         reportIssue: '', 
         reportReasonError: '',
          reportDetailsError: '', 
          reportIssueError: ''
    }
  },
  methods: {
    getdata(){
      axios
            .get('http://localhost:5000/influencerprofile/' + this.user_id,
                 {headers: {Authorization: `${this.token}`}})
            .then((response) => {
                console.log("Response Block",response)
                if(response.status == 200){
                    console.log("Data Fetched Successfully")
                    this.Username = response.data.username;
                    this.name = response.data.name;
                    this.email = response.data.email;
                    this.bio = response.data.bio;
                    this.industry = response.data.industry;
                    this.niche = response.data.niche;
                    this.datejoined = response.data.date_joined;
                    this.lastloged = response.data.last_login;
                    this.isyt = response.data.youtube;
                    this.isinsta = response.data.instagram;
                    this.isx = response.data.twitter;
                    this.isthread = response.data.thread;
                    this.isfb = response.data.facebook;
                    this.istik = response.data.tiktok;
                    this.iskick = response.data.kick;
                    this.istwitch = response.data.twitch;
                    this.issnap = response.data.snapchat;
                    this.islinked = response.data.linkedin;
                    this.ytfollowers = response.data.youtubefollowers;
                    this.ytlink = response.data.youtubelink;
                    this.instafollowers = response.data.instagramfollowers;
                    this.instalink = response.data.instagramlink;
                    this.xfollowers = response.data.twitterfollowers;
                    this.xlink = response.data.twitterlink;
                    this.threadfollowers = response.data.threadfollowers;
                    this.threadlink = response.data.threadlink;
                    this.fbfollowers = response.data.facebookfollowers;
                    this.fblink = response.data.facebooklink;
                    this.tikfollowers = response.data.tiktokfollowers;
                    this.tiklink = response.data.tiktoklink;
                    this.kickfollowers = response.data.kickfollowers;
                    this.kicklink = response.data.kicklink;
                    this.twitchfollowers = response.data.twitchfollowers;
                    this.twitchlink = response.data.twitchlink;
                    this.snapfollowers = response.data.snapchatfollowers;
                    this.snaplink = response.data.snapchatlink;
                    this.linkedfollowers = response.data.linkedinfollowers;
                    this.linkedlink = response.data.linkedinlink;
                    this.totalreach = response.data.totalreach;
                    this.profilespic = response.data.profilepic;
                    this.value = response.data.rating;
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



    yt() { 
      if (this.ytlink) { 
        window.location.href = this.ytlink; 
      } 
      else { 
        alert('Link not available'); 
      } 
    },
    insta() { 
      if (this.instalink) { 
        window.location.href = this.instalink; 
      } 
      else { 
        alert('Link not available'); 
      } 
    },
    fb() { 
      if (this.fblink) { 
        window.location.href = this.fblink; 
      } 
      else { 
        alert('Link not available'); 
      } 
    },
    tik() { 
      if (this.tiklink) { 
        window.location.href = this.tiklink; 
      } 
      else { 
        alert('Link not available'); 
      } 
    },
    snap() { 
      if (this.snaplink) { 
        window.location.href = this.snaplink; 
      } 
      else { 
        alert('Link not available'); 
      } 
    },
    thr() { 
      if (this.threadlink) { 
        window.location.href = this.threadlink; 
      } 
      else { 
        alert('Link not available'); 
      } 
    },
    lin() { 
      if (this.linkedlink) { 
        window.location.href = this.linkedlink; 
      } 
      else { 
        alert('Link not available'); 
      } 
    },
    twi() { 
      if (this.twitchlink) { 
        window.location.href = this.twitchlink; 
      } 
      else { 
        alert('Link not available'); 
      } 
    },
    xt() { 
      if (this.xlink) { 
        window.location.href = this.xlink; 
      } 
      else { 
        alert('Link not available'); 
      } 
    },
    ki() { 
      if (this.kicklink) { 
        window.location.href = this.kicklink; 
      } 
      else { 
        alert('Link not available'); 
      } 
    },
    openReportModal() { 
      const modal = new bootstrap.Modal(document.getElementById('reportModal')); modal.show(); 
    },
    validateReportForm() { 
      this.reportReasonError = ''; 
      this.reportDetailsError = ''; 
      this.reportIssueError = ''; 
      let valid = true; if (!this.reportReason) 
      { this.reportReasonError = 'Please select a reason for reporting.'; 
      valid = false; }
      if (!this.reportIssue) { this.reportIssueError = 'Please provide an issue description.'; valid = false; }
      if (!this.reportDetails) { 
        this.reportDetailsError = 'Please provide details for your report.';
         valid = false; } 
      if (valid) { this.submitReport(); } }, 
    
      submitReport() { 
        axios.post('http://localhost:5000/influencer/'+ this.user_id +'/report', {
          issue: this.reportIssue,
          reason: this.reportReason,
          details: this.reportDetails
        }, { headers: { 'Authorization': this.token } })
        .then((response) => { 
          console.log(response); 
          alert('Report submitted successfully!'); 
          this.reportIssue = '';
          this.reportReason = '';
          this.reportDetails = ''; 
          document.getElementById('reportModal').classList.remove('show'); 
          document.getElementById('reportModal').style.display = 'none'; 
          document.getElementsByClassName('modal-backdrop')[0].remove();
          
        })
        .catch((error) => { 
          console.log(error); 
          alert('An error occurred while submitting your report. Please try again later.'); 
        });
      },
  },
  computed: {
    imgsrc(){
      if(this.profilespic == true) {
        return new URL(`../../../../backend/Images/InfluencerImg/${this.Username}.png`, import.meta.url).href;
    }
      else{
      return new URL(`https://api.dicebear.com/6.x/micah/svg?seed=${this.Username}`);
    }}
  },
  watch: {
    
  },
  mounted() {
    
  },
  created() {
    this.user_id = this.$route.params.users_id;
    this.token = localStorage.getItem('AuthToken');
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
  flex-wrap: wrap;
  width: 55%;
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
  width: 45%;
  border-left: 5px solid #000000;
  flex-wrap: wrap;
  gap: 15px;
  padding: 10px;
  background-color: #000000e5;
  color: #ededed;
  border-top-right-radius: 25px;
  border-bottom-right-radius: 25px;
  flex: 1 1 auto;
  min-height: 100%;
}

.avatar {
  width: 160px; /* Adjust size as needed */
  height: 160px; /* Adjust size as needed */
  border-radius: 50%;
  object-fit: cover;
  border: #e3e3e3;
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
  }
}

.profbody .profimage .contentbtn {
  display: flex;
  flex-direction: row;
  flex-wrap:wrap;
  margin :2px;
  width: 100%;
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
  flex-direction: column;
  flex-wrap: wrap;
  gap: 10px;
  justify-content: space-evenly;
  padding: 10px;
  align-content: center;
}


/* Twitch button active state */
#twitchbtn:active {
  color: #ffffff;
  border-color: #6441A4;
}

/* LinkedIn button active state */
#linkedbtn:active {
  color: #ffffff;
  border-color: #0077B5;
}

/* Instagram button active state */
#instabtn:active {
  color: #ffffff;
  border-color: #C13584;
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
  text-align: flex-start;

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