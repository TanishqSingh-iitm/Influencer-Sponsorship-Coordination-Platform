sponsor<script setup>
import { getDatasetAtEvent } from 'vue-chartjs';
import Topbar from '../../components/Topbar.vue'
</script>

<template>
  <div>
    <Topbar />
  </div>
  <div class="statsbody">
    <div style="margin-top: 20px;margin-bottom: 20px;" >
            <h2 id="dashb"><span class="mdi mdi-newspaper-variant"></span> Campaign Dashboard</h2>
    </div>
    
    <div class="boxed">
      <div class="navigators">
        <div class="statistics">
            <div class="prog">
              <h6 for="progress">Campaign Progress:</h6>
            <div class="progress" role="progressbar" aria-label="Animated striped example" :aria-valuenow="campaignprogress" aria-valuemin="0" aria-valuemax="100">
              <div class="progress-bar progress-bar-striped progress-bar-animated bg-info" :style="{ width: campaignprogress + '%' }">{{ campaignprogress }}%</div>
            </div>
            </div>
        <div class="row1">
            <div class="square blue-gradient"> 
                <h4><span class="mdi mdi-bullseye-arrow"></span></h4>
                <h4>Target</h4> 
                <p>{{campaigntarget}}</p> 
            </div> 
            <div class="square green-gradient"> 
                <h4><span class="mdi mdi-bullseye"></span></h4>
                <h4>Current</h4> 
                <p>{{campaigncurrent}}</p> 
            </div> 
            <div class="square red-gradient"> 
                <h4><span class="mdi mdi-cash"></span></h4>
                <h4>Budget</h4> 
                <p>&#8377{{campaignbudget}}</p> 
            </div> 
            <div class="square purple-gradient"> 
                <h4><span class="mdi mdi-list-status"></span></h4>
                <h4>Status</h4> 
                <p>{{ campaignstatus }}</p> 
            </div>
            <div class="square orange-gradient"> 
                <h4><span class="mdi mdi-star"></span></h4>
                <h4>DaysLeft</h4> 
                <p>{{campaignduration}}</p> 
            </div>
            
            <div class="square teal-gradient"> 
                <h4><span class="mdi mdi-eye"></span></h4>
                <h4>Visibility</h4> 
                <p>{{campaignvisibility}}</p> 
            </div>  
            <div class="buttons" v-if="campaignstatus!='Completed'">
        <button type="submit" class="btn btn-success" style="font-size:20px; border-radius:20px;"  @click="paymentpage()" v-if="campaignstatus=='Pending'">
        <span class="mdi mdi-cash-plus"></span>
                                  Add Money
        </button>
        <button class="btn btn-warning" style="font-size:20px; border-radius:20px; pointer-events: none;" v-if="campaignstatus=='Flagged'">This Campaign is Flagged</button>
        <button type="button" class="btn btn-danger" style="border-radius: 20px;font-size:20px;" @click="openReportModal" v-if="campaignstatus!='Completed'"><span class="mdi mdi-comment-alert"></span> Report</button>
      </div>
            </div>
            <div class="prog">
              <h6 for="progress">Campaign Duration Completed:</h6>
            <div class="progress" role="progressbar" aria-label="Animated striped example" :aria-valuenow="campaigncompletion" aria-valuemin="0" aria-valuemax="100">
              <div class="progress-bar progress-bar-striped progress-bar-animated bg-success" :style="{ width: campaigncompletion + '%' }">{{ campaigncompletion }}%</div>
            </div> </div>
          </div>
      </div>
    </div>
    <div class="campaigndetails">
        <div class="detailsrow1">
          <h4><b>Campaign Title:</b> {{ campaigntitle }}</h4>
          <h4><b>Campaign Sponsor:</b> {{ campaignsponsor }}</h4>
        </div>
        <div class="detailsrow2">
          <h4><b>Campaign Start Date:</b> {{ campaignstartdate }}</h4>
          <h4><b>Campaign End Date:</b> {{ campaignenddate }}</h4>
        </div>
        <div class="detailsrow3">
          <h4><b>Related Industry:</b> {{ campaignindustry }}</h4>
          <h4><b>Related Niche:</b> {{ campaignniche }}</h4>
        </div>
        <h4 style="text-align: justify;"><b>Description:</b> {{ campaigndescription }}</h4>
        <h4 style="text-align: justify;"><b>Goal:</b> {{ campaigngoal }}</h4>
    </div>
  </div>
  <div class="addsbody">
    <div class="addsheads">
      <h2 id="dashh"><span class="mdi mdi-newspaper-variant"></span> Advertisements</h2>
      <button type="button" class="btn btn-success" style="border-radius: 20px;font-size:20px;" @click="createad(campaign_id)" v-if="campaignstatus=='Pending'"><span class="mdi mdi-plus"></span> Add Advertisement</button>
    </div>
    <div class="activesponsor" v-if="ads.length>0">
        <div class="heading">
              <h2>Campaign Ads</h2>
        </div>
        <section class="table__body" >
            <table>
                <thead>
                    <tr>
                        <th> S.No </th>
                        <th> Title </th>
                        <th> Ad Amount Base &#8377 </th>
                        <th> Ad Amount Final &#8377 </th>
                        <th> Preferred Platforms </th>
                        <th> Date Created </th>
                        <th> Ad Campaign </th>
                        <th> Status </th>
                       
                        <th> Actions </th>
                    </tr>
                </thead>
                <tbody>
                  <tr v-for="(ad, index) in ads" :key="ads.id">
                      <td>{{ index + 1}}</td>
                      <td>{{ ad.title }}</td>
                      <td>&#8377 {{ ad.baseprice }}</td>
                      <td>&#8377 {{ ad.negociatedprice }}</td>
                      <td><span class="mdi mdi-youtube" v-if="ad.preferedplatforms.youtube" ></span><span class="mdi mdi-instagram"  v-if="ad.preferedplatforms.instagram" ></span>
					<span class="mdi mdi-facebook" v-if="ad.preferedplatforms.facebook" ></span><span class="mdi mdi-twitter"  v-if="ad.preferedplatforms.twitter" ></span>
					<span class="mdi mdi-at"  v-if="ad.preferedplatforms.thread"  ></span><span class="mdi mdi-music-note-outline"  v-if="ad.preferedplatforms.tiktok" ></span>
					<span class="mdi mdi-twitch"  v-if="ad.preferedplatforms.twitch" ></span><span class="mdi mdi-kickstarter"  v-if="ad.preferedplatforms.kick" ></span>
					<span class="mdi mdi-snapchat"  v-if="ad.preferedplatforms.snapchat"  ></span><span class="mdi mdi-linkedin"  v-if="ad.preferedplatforms.linkedin" ></span></td>
                      <td>{{ ad.date_created }}</td>
                      <td>{{ ad.campaign }}</td>
                      <td><span class="badge badge-pill" :style="getStatusStyle(ad.status)" style="margin-left: 10px;">{{ ad.status }}</span></td>
                      <td id="actions">
                        <button type="button" class="btn btn-primary" style="border-radius: 10px; font-size: 15px;" @click="openModal(ad)" v-tooltip.bottom="'View Ad'"><span class="mdi mdi-advertisements"></span></button>
		                    <button type="button" class="btn btn-warning" style="border-radius: 10px;font-size:15px;"v-tooltip.bottom="'Edit Ad'" @click="editads(ad.id)" v-if="adcheck2(ad.status)"><span class="mdi mdi-comment-edit"></span></button>
		                    <button type="button" class="btn btn-danger" style="border-radius: 10px;font-size:15px;"v-tooltip.bottom="'Delete Ad Permanently'" @click="deleteads(ad.id)" v-if="adcheck2(ad.status)"><span class="mdi mdi-delete-forever"></span></button>
		                    <button type="button" class="btn btn-success" style="border-radius: 10px;font-size:15px;"v-tooltip.bottom="'Hire Influencer'" v-if="adcheck(ad.status)" @click="hireinfluencer(campaign_id,ad.id)"><span class="mdi mdi-account-supervisor"></span></button>
                      </td>
                  </tr>
                </tbody>
            </table>
        </section>
        <div class="totals" align="right">
          <span class="badge badge-pill" style="border-radius:30px;background:rgb(0, 88, 150)"> Total Campaign Ads: {{ ads.length }}</span>
        </div>
      </div>
  </div>
  <!-- Modal -->
   <div v-if="ads.length>0">
   <div class="modal fade" id="adModal" tabindex="-1" aria-labelledby="adModalLabel" aria-hidden="true"> 
    <div class="modal-dialog"> <div class="modal-content"> <div class="modal-header"> 
      <h1 class="modal-title fs-5" id="adModalLabel">{{ selectedAd.title }}</h1> 
      <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button> 
      </div> <div class="modal-body"> <p><strong>Base Price:</strong> &#8377 {{ selectedAd.baseprice }}</p> 
      <p><strong>Negotiated Price:</strong> &#8377 {{ selectedAd.negociatedprice }}</p> 
      <p><strong>Preferred Platforms:</strong></p> 
      <p ><span class="mdi mdi-youtube" v-if="selectedAd.preferedplatforms.youtube" ></span><span class="mdi mdi-instagram"  v-if="selectedAd.preferedplatforms.instagram" ></span>
          <span class="mdi mdi-facebook" v-if="selectedAd.preferedplatforms.facebook" ></span><span class="mdi mdi-twitter"  v-if="selectedAd.preferedplatforms.twitter" ></span>
          <span class="mdi mdi-at"  v-if="selectedAd.preferedplatforms.thread"  ></span><span class="mdi mdi-music-note-outline"  v-if="selectedAd.preferedplatforms.tiktok" ></span>
          <span class="mdi mdi-twitch"  v-if="selectedAd.preferedplatforms.twitch" ></span><span class="mdi mdi-kickstarter"  v-if="selectedAd.preferedplatforms.kick" ></span>
          <span class="mdi mdi-snapchat"  v-if="selectedAd.preferedplatforms.snapchat"  ></span><span class="mdi mdi-linkedin"  v-if="selectedAd.preferedplatforms.linkedin" ></span></p>
      <p><strong>Date Created:</strong> {{ selectedAd.date_created }}</p> 
      <p><strong>Campaign:</strong> {{ selectedAd.campaign }}</p> 
      <p><strong>Status:</strong> {{ selectedAd.status }}</p>
      <p style="text-align: justify;"><strong>Description:</strong> {{ selectedAd.description }}</p> 
      </div> <div class="modal-footer"> 
        <button type="button" class="btn btn-dark" data-bs-dismiss="modal">Close</button> 
        </div>
         </div> 
         </div> 
         </div>
</div> 
<!-- Report Modal --> 
<div class="modal fade" id="reportModal" tabindex="-1" aria-labelledby="reportModalLabel" aria-hidden="true"> 
  <div class="modal-dialog"> 
    <div class="modal-content"> 
      <div class="modal-header"> 
        <h1 class="modal-title fs-5" id="reportModalLabel">Report Campaign</h1> 
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
import axios from 'axios';
export default {
  name: 'Campaign',
  data() {
    return {
          auth: '',
          campaign_id: '',
          userrole: '',
          campaigntitle: '',
          campaigndescription: '',
          campaigntarget: 0,
          campaigncurrent: 0,
          campaignbudget: 0,
          campaignstatus: '',
          campaignratings: '',
          campaignprogress: 0,
          campaignstartdate: '',
          campaignenddate: '',
          campaignsponsor: '',
          campaignindustry: '',
          campaignniche: '',
          campaigngoal: '',
          campaignvisibility: '',
          ads:[],
          selectedAd: {preferedplatforms: {}},
          reportReason: '', 
          reportDetails: '',
         reportIssue: '', 
         reportReasonError: '',
          reportDetailsError: '', 
          reportIssueError: '',
          campaigncompletion: 0,
          campaignduration: 0
    }
  },
  methods: {
          paymentpage(){
            this.$router.push({ name: 'PaymentPage', params: { campaign_id: this.campaign_id } });
          },
          getdata(){
            axios
                .get('http://localhost:5000/sponsor/campaign/'+this.campaign_id+'/view', {
                    headers: {
                        'Authorization': this.auth}})
                .then(response => {
                    console.log(response);
                    this.campaigntitle = response.data.title;
                    this.campaigndescription = response.data.description;
                    this.campaigntarget = response.data.target;
                    this.campaigncurrent = response.data.current;
                    this.campaignbudget = response.data.budget;
                    this.campaignstatus = response.data.status;
                    this.campaignratings = response.data.rating;
                    this.campaignprogress = response.data.progress;
                    this.campaignstartdate = response.data.start_date;
                    this.campaignenddate = response.data.end_date;
                    this.campaignsponsor = response.data.sponsor;
                    this.campaignindustry = response.data.related_industry;
                    this.campaignniche = response.data.related_niche;
                    this.campaigngoal = response.data.goal;
                    this.campaignvisibility = response.data.visibility;
                    this.campaigncompletion = response.data.campaign_completion;
                    this.campaignduration = response.data.campaign_duration;
                })
                .catch(error => {
                    console.log(error);
                });
              },
              createad(id){
                this.$router.push({ name: 'CreateAdPage', params: { campaign_id: id } });
              },
          getads(){
            axios
                .get('http://localhost:5000/campaign/'+this.campaign_id+'/ads', {
                    headers: {
                        'Authorization': this.auth}})
                .then(response => {
                    console.log(response);
                    this.ads = response.data;
                })
                .catch(error => {
                    console.log(error);
                });
              },
              getStatusStyle(status) { const styles = { Open: 'background:rgb(0, 88, 150);', Approved: 'background:rgb(76, 175, 80);', Rejected: 'background:rgb(244, 67, 54);', Requested: 'background:rgb(255, 152, 0);', 'In Progress': 'background:rgb(33, 150, 243);', Completed: 'background:rgb(0, 128, 128);', Pending: 'background:rgb(128, 0, 128);', Negotiated: 'background:rgb(184, 134, 11);', Closed:'background:rgb(0,0,0)' }; return styles[status] || ''; },
              openModal(ad) { 
                this.selectedAd = ad; 
                const modal = new bootstrap.Modal(document.getElementById('adModal')); 
                modal.show(); },
          editads(id){
            this.$router.push({ name: 'EditAdPage', params: { Ad_id: id } });
          },
          deleteads(id){
            axios
                .delete('http://localhost:5000/ad/'+id+'/delete', {
                    headers: {
                        'Authorization': this.auth}})
                .then(response => {
                    console.log(response);
                    if(response.status == 200){
                        alert("Ad Deleted Successfully");}
                    if(response.status == 202){
                        alert("Ad Deletion Failed Reason: "+ response.data.message);}
                    this.$router.go(0);
                })
                .catch(error => {
                    alert("Ad Deletion Failed Reason: "+ error.response.data.message);
                    console.log(error);
                });},
          adcheck(x){
            if(x=='Closed'||x=='Completed'||x=='Requested'||x=='Approved'){
              return false;
            }
            else{
              return true;
            }
          },
          checkstatus(){
            if(this.campaignstatus=='Completed' || this.campaignstatus=='Flagged'){
              return false;
            }
            else{
              return true;
            }
          },
          hireinfluencer(id1,id2){
            this.$router.push({ name: 'HireInfluencerPage', params: { campaign_id: id1, Ad_id: id2 } });
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
        axios.post('http://localhost:5000/campaign/'+ this.campaign_id +'/report', {
          issue: this.reportIssue,
          reason: this.reportReason,
          details: this.reportDetails
        }, { headers: { 'Authorization': this.auth } })
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
      adcheck2(x){
        if(x=='Closed'||x=='Completed'||x=='Approved'){
          return false;
        }
        else{
          return true;
        }
      }
  },
  computed: {
    
  },
  watch: {
    
  },
  mounted() {
    
  },
  created() {
      this.auth = localStorage.getItem('AuthToken');
      this.campaign_id = this.$route.params.campaign_id;
      if (this.auth == null) {
        this.$router.push({ name: 'Login' });
      }
      this.userrole = localStorage.getItem('userrole');
      this.getdata();
      this.getads();
  }
}
</script>

<style scoped>

.activesponsor {
  display: flex;
  flex-direction: column;
  gap: 10px;
  border: 2px ;
  border-radius: 30px;
  padding: 10px;
  flex-wrap: wrap;
  width: 100%;
}

.activesponsor .heading {
  display: flex;
  flex-direction: row;
  flex: 0 1;
  border-radius: 30px;
  padding: 10px;
  flex-wrap: wrap;

}
.table__body {
  display: flex;
  gap: 10px;
  border-radius: 30px;
  flex-wrap: wrap;
  overflow: auto;
  width: 100%;
  overflow: overlay;
  background-color: #fffb;

    margin: .8rem auto;
    border-radius: .6rem;

}
.table__body::-webkit-scrollbar{
    width: 0.5rem;
    height: 0.5rem;
}

.table__body::-webkit-scrollbar-thumb{
    border-radius: .5rem;
    background-color: #0004;
    visibility: hidden;
}

.table__body:hover::-webkit-scrollbar-thumb{ 
    visibility: visible;
}
#actions{
  display: flex;
  flex-direction: row;
  max-width: fit-content;
  gap: 12px;
}
table {
  width: 100%;
  table-layout: auto;
}

table, th, td {
  border-collapse: collapse;
  text-align: left;
  padding: 1rem;
  min-width: 140px;
}

@media (max-width: 1000px) {
  table td{
    min-width:150px;
    min-height: 10vh;
  }
  #actions{
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    margin-right: 0px;
    gap: 5px;
  }
}

thead th {
    position: sticky;
    top: 0;
    left: 0;
    background-color: #d5d1defe;
    cursor: pointer;
    text-transform: capitalize;
    font-weight: bold;
}

tbody tr:nth-child(even) {
    background-color: #0000000b;
}

tbody tr {
    --delay: .1s;
    transition: .5s ease-in-out var(--delay), background-color 0s;
}

tbody tr.hide {
    opacity: 0;
    transform: translateX(100%);
}

tbody tr:hover {
    background-color: #fff6 !important;
}

tbody tr td,
tbody tr td p,
tbody tr td img {
    transition: .2s ease-in-out;
}

tbody tr.hide td,
tbody tr.hide td p {
    padding: 0;
    font: 0 / 0 sans-serif;
    transition: .2s ease-in-out .5s;
}

tbody tr.hide td img {
    width: 0;
    height: 0;
    transition: .2s ease-in-out .5s;
}


.statsbody {
  margin-top: 25px;
  display: flex;
  flex-direction: column;
  width: 80%;
  border: 5px solid #000000;
  align-self: center;
  border-radius: 20px;
  margin-bottom: 40px;
  background-color: #f9f9f9; 
}

.addsbody .adsbody{
  margin-top: 10px;
  display: flex;
  flex-direction: row;
  gap:20px;
  width: 100%;
  border-radius: 20px;
  margin-bottom: 40px;
  padding: 30px;
}


.statsbody .campaigndetails {
  display: flex;
  flex-direction: column;
  width: 100%;
  border-radius: 20px;
  background-color: #f9f9f9;
  padding: 30px;
  padding-left: 40px;
  padding-right: 40px;
  
  flex-wrap:wrap;
}

.addsbody .addsheads {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 15px;
  padding: 20px;
}

.addsbody {
  margin-top: 10px;
  display: flex;
  flex-direction: column;
  width: 80%;
  border: 5px solid #000000;
  align-self: center;
  border-radius: 20px;
  margin-bottom: 40px;
  background-color: #f9f9f9; 
}

b{
  color: #000000;
}

.campaigndetails .detailsrow1 {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 15px;
}

.campaigndetails .detailsrow2 {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 15px;
}

.campaigndetails .detailsrow3 {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  gap: 15px;
  justify-content: space-between;
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
    flex-direction: row;
    gap: 15px; 
}

.statsbody .boxed .buttons {
    align-self: center;
    display: flex;
    flex-direction: column;
    justify-self: right;
    gap: 15px;
    padding: 20px;
    align-items: right;

    border-radius: 20px; 
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); 
    background-color: #f9f9f9; 
}



.statsbody .boxed .navigators { 
    display: flex; 
    flex-direction: row; 
    gap: 15px; 
    width: 100%; 
    padding: 20px; 
    flex-wrap: wrap;
    border-radius: 20px; 
    background-color: #f9f9f9; 
}

.statsbody .boxed .navigators .statistics { 
    display: flex; 
    flex-direction: column; 
    gap: 15px; 
    padding: 20px; 
    border-radius: 20px; 
    width: 80%;
    flex: 1 auto;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); 
    background-color: #f9f9f9; 
}

.progress {
    width: 100%;
    align-self: center;
    border-radius: 20px;
}

.statsbody .boxed .row1 {
    display: flex; 
    flex-direction: row;
    flex-wrap: wrap; 
    gap: 25px; 
    justify-content: center;
    align-items: center;
    align-content: center;


}



.square { 
    width: 120px; 
    height: 120px; 
    display: flex; 
    flex-direction: column; 
    justify-content: center; 
    align-items: center; 
    color: white; 
    border-radius: 10px; 
    padding: 65px; 
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




</style>