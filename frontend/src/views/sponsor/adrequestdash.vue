<script setup>
import Topbar from '../../components/Topbar.vue'

</script>

<template>
  <div>
    <Topbar />
  </div>
  <div style="margin-top: 30px;margin-bottom: 20px; align-self: center;" >
              <h1><span class="mdi mdi-view-dashboard"></span> Sponsor Dashboard</h1>
    </div>
    <div class="dashboard">
      <div class="sponsornav">
        <h2 id="xyz">Advertisement Requests:</h2>
        
      </div>
      
      <div class="activesponsor" v-if="activecampaigns.length>0">
        <div class="heading">
              <h2>Approved Requests</h2>
        </div>
        <section class="table__body" >
            <table>
                <thead>
                    <tr>
                        <th> S.No </th>
                        <th> Ad Title </th>
                        <th> Influencer </th>
                        <th> Campaign Title </th>
                        <th> NegociatedPrice &#8377 </th>
                        <th> Ad Status </th>
                        <th> Date Requested </th>
                        <th> Granted On</th>
                        <th> Finish By </th>
                        <th> Actions </th>
                    </tr>
                </thead>
                <tbody>
                  <tr v-for="(actcamp, index) in activecampaigns" :key="activecampaigns.id">
                      <td>{{ index + 1}}</td>
                      <td>{{ actcamp.ad_title }}</td>
                      <td>{{ actcamp.user_name }}</td>
                      <td>{{ actcamp.campaign_title }}</td>
                      <td>&#8377 {{ actcamp.negociatedprice }}</td>
                      <td>{{ actcamp.ad_status }}</td>
                      <td>{{ actcamp.date_created }}</td>
                      <td>{{ actcamp.granted_at }}</td>
                      <td>{{ actcamp.finish_by }}</td>
                      <td id="actions">
                          <button type="submit" class="btn btn-primary"   style="font-size:15px; border-radius:10px;" @click="viewcampaign(actcamp.campaignid)" v-tooltip.top="'View Campaign'">
                            <span class="mdi mdi-newspaper"></span>
                              </button>
                          <button type="submit" class="btn btn-info"  style="font-size:15px; border-radius:10px;" @click="messageinfluencer(actcamp.id)" v-tooltip.top="'Message Influencer'">                         
                            <span class="mdi mdi-cellphone-message"></span>
                              </button>
                          <button type="submit" class="btn btn-primary"  style="font-size:15px; border-radius:10px;" @click="finishcampaign(actcamp.id)" v-tooltip.top="'View Influencer'">
                            <span class="mdi mdi-badge-account-horizontal"></span>
                          </button>
                          <button type="submit" class="btn btn-primary"  style="font-size:15px; border-radius:10px;" @click="openModal(actcamp.ad_id)" v-tooltip.top="'View Ad'">
                            <span class="mdi mdi-advertisements"></span>
                          </button>
                      </td>
                  </tr>
                </tbody>
            </table>
        </section>
        <div class="totals" align="right">
          <span class="badge badge-pill" style="border-radius:30px;background:rgb(0, 88, 150)"> Total Approved Requests: {{ activecampaigns.length }} </span>
        </div>
      </div>
      <div class="inactivesponsor" v-if="inactivecampaigns.length>0" >
          <div class="heading">
              <h2>Requested Requests</h2>
          </div>
          <section class="table__body">
            <table>
              <thead>
                    <tr>
                        <th> S.No </th>
                        <th> Ad Title </th>
                        <th> Influencer </th>
                        <th> Campaign Title </th>
                        <th> NegociatedPrice &#8377 </th>
                        <th> Ad Status </th>
                        <th> Date Requested </th>
                        <th> Actions </th>
                    </tr>
                </thead>
                <tbody>
                  <tr v-for="(inactcamp, index) in inactivecampaigns" :key="inactivecampaigns.id">
                      <td>{{ index + 1}}</td>
                      <td>{{ inactcamp.ad_title }}</td>
                      <td>{{ inactcamp.user_name }}</td>
                      <td>{{ inactcamp.campaign_title }}</td>
                      <td>&#8377 {{ inactcamp.negociatedprice }}</td>
                      <td>{{ inactcamp.ad_status }}</td>
                      <td>{{ inactcamp.date_created }}</td>
                      <td id="actions">
                        <button type="submit" class="btn btn-primary"   style="font-size:15px; border-radius:10px;" @click="viewcampaign(inactcamp.campaignid)" v-tooltip.top="'View Campaign'">
                            <span class="mdi mdi-newspaper"></span>
                              </button>
                          <button type="submit" class="btn btn-info"  style="font-size:15px; border-radius:10px;" @click="messageinfluencer(inactcamp.id)" v-tooltip.top="'Negociate Request'">                         
                            <span class="mdi mdi-cellphone-message"></span>
                              </button>
                          <button type="submit" class="btn btn-success" v-if="inactcamp.requested_byinfluencer" style="font-size:15px; border-radius:10px;" @click="approverequest(inactcamp.id)" v-tooltip.top="'Approve Request'">
                            <span class="mdi mdi-tooltip-check"></span>
                          </button>
                          <button type="submit" class="btn btn-danger" v-if="inactcamp.requested_byinfluencer"  style="font-size:15px; border-radius:10px;" @click="rejectrequest(inactcamp.id)" v-tooltip.top="'Reject Request'">
                            <span class="mdi mdi-tooltip-remove"></span>
                          </button>
                          <button type="submit" class="btn btn-danger" v-if="inactcamp.requested_bysponsor" style="font-size:15px; border-radius:10px;" @click="removerequest(inactcamp.id)" v-tooltip.top="'Remove Request'">
                            <span class="mdi mdi-tooltip-remove"></span>
                          </button>
                          <button type="submit" class="btn btn-primary"  style="font-size:15px; border-radius:10px;" @click="viewinfluencer(inactcamp.user_id)" v-tooltip.top="'View Influencer'">
                            <span class="mdi mdi-badge-account-horizontal"></span>
                          </button>
                      </td>
                  </tr>
                </tbody>
            </table>
        </section>
        <div class="totals" align="right">
          <span class="badge badge-pill" style="border-radius:30px;background:rgb(0, 88, 150)"> Total Requested Requests: {{ inactivecampaigns.length }} </span>
        </div>
      </div>
      <div class="inactivesponsor"  v-if="completecampaigns.length>0">
          <div class="heading">
              <h2>Completed Requests</h2>
          </div>
          <section class="table__body">
            <table>
              <thead>
                    <tr>
                      <th> S.No </th>
                        <th> Ad Title </th>
                        <th> Influencer </th>
                        <th> Campaign Title </th>
                        <th> NegociatedPrice &#8377 </th>
                        <th> Ad Status </th>
                        <th> Date Requested </th>
                        <th> Granted On</th>
                        <th> Finish By </th>
                        <th> Actions </th>
                    </tr>
                </thead>
                <tbody>
                  <tr v-for="(compcamp, index) in completecampaigns" :key="completecampaigns.id">
                      <td>{{ index + 1}}</td>
                      <td>{{ compcamp.ad_title }}</td>
                      <td>{{ compcamp.user_name }}</td>
                      <td>{{ compcamp.campaign_title }}</td>
                      <td>&#8377 {{ compcamp.negociatedprice }}</td>
                      <td>{{ compcamp.ad_status }}</td>
                      <td>{{ compcamp.date_created }}</td>
                      <td>{{ compcamp.granted_at }}</td>
                      <td>{{ compcamp.finish_by }}</td>
                      <td id="actions">
                          <button type="submit" class="btn btn-primary" data-bs-toggle="tooltip" data-bs-placement="top" data-bs-title="Tooltip on top" style="font-size:15px; border-radius:10px;" @click="viewcampaign(compcamp.campaignid)" v-tooltip.top="'View Campaign'">
                            <span class="mdi mdi-newspaper"></span>
                              </button>
                              <button type="submit" class="btn btn-info"  style="font-size:15px; border-radius:10px;" @click="openModal(compcamp.ad_id)" v-tooltip.top="'View Ad'">
                            <span class="mdi mdi-advertisements"></span>
                          </button>
                          <button type="submit" class="btn btn-success"  style="font-size:15px; border-radius:10px;" @click="openReportModal(compcamp.user_id)" v-tooltip.top="'Rate Influencer'">
                            <span class="mdi mdi-message-draw"></span>
                          </button>
                      </td>
                  </tr>
                </tbody>
            </table>
        </section>
        <div class="totals" align="right">
          <span class="badge badge-pill" style="border-radius:30px;background:rgb(0, 88, 150)"> Total Completed Requests: {{ completecampaigns.length }} </span>
        </div>
      </div>
      
      <div class="inactivesponsor"  v-if="rejected.length>0">
          <div class="heading">
              <h2>Rejected Requests</h2>
          </div>
          <section class="table__body">
            <table>
              <thead>
                    <tr>
                        <th> S.No </th>
                        <th> Ad Title </th>
                        <th> Influencer </th>
                        <th> Campaign Title </th>
                        <th> NegociatedPrice &#8377 </th>
                        <th> Ad Request Status</th>
                        <th> Date Requested </th>
                        <th> Actions </th>
                    </tr>
                </thead>
                <tbody>
                  <tr v-for="(rejad, index) in rejected" :key="rejad.id">
                      <td>{{ index + 1}}</td>
                      <td>{{ rejad.ad_title }}</td>
                      <td>{{ rejad.user_name }}</td>
                      <td>{{ rejad.campaign_title }}</td>
                      <td>&#8377 {{ rejad.negociatedprice }}</td>
                        <td>{{ rejad.status }}</td>
                      <td>{{ rejad.date_created }}</td>
                      <td id="actions">
                          <button type="submit" class="btn btn-primary" data-bs-toggle="tooltip" data-bs-placement="top" data-bs-title="Tooltip on top" style="font-size:15px; border-radius:10px;" @click="viewcampaign(rejad.campaignid)" v-tooltip.top="'View Campaign'">
                            <span class="mdi mdi-newspaper"></span>
                            </button></td>
                  </tr>
                </tbody>
            </table>
        </section>
        <div class="totals" align="right">
          <span class="badge badge-pill" style="border-radius:30px;background:rgb(0, 88, 150)"> Total Rejected Requests: {{ rejected.length }} </span>
        </div>
      </div>


  </div>

  <div>
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

<div class="modal fade" id="reportModal" tabindex="-1" aria-labelledby="reportModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="reportModalLabel">Rate Influencer</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <form>
          <div class="mb-3">
            <label for="report-reason" class="col-form-label">Rating:</label>
            <select class="form-control" id="report-reason" v-model="rating">
              <option value="" selected>Select a rating</option>
              <option value="1">1 Star</option>
              <option value="2">2 Stars</option>
              <option value="3">3 Stars</option>
              <option value="4">4 Stars</option>
              <option value="5">5 Stars</option>
            </select>
            <div v-if="reportReasonError" class="text-danger">{{ reportReasonError }}</div>
          </div>
          <div class="mb-3">
            <label for="report-details" class="col-form-label">Review:</label>
            <textarea class="form-control" id="report-details" v-model="reviews"></textarea>
            <div v-if="reportDetailsError" class="text-danger">{{ reportDetailsError }}</div>
          </div>
        </form>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary" @click="validateReportForm">Submit Review</button>
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
  name: 'SponsorDashboard',
  data() {
    return {
        auth: '',
        role: '',
        activecampaigns: [],
        inactivecampaigns: [],
        completecampaigns: [],
        rejected:[],
        user_id: '',
        tooltipVisible: false,
        selectedAd:{preferedplatforms: {}},
        rating: 0,
        reviews: '',
        reportReasonError: '',
        reportDetailsError: '',
        selecteduser:'',

    }
  },
  methods: {
          getdata() {
            axios 
            .get('http://localhost:5000/sponsor/'+ this.user_id +'/adrequests',
                 {headers: {Authorization: this.auth}})
            .then((response) => {
                console.log(response);
                this.activecampaigns = response.data.approved;
                this.inactivecampaigns = response.data.requests;
                this.completecampaigns = response.data.completed;
                this.rejected = response.data.rejected;
              })
            .catch((error) => {
                console.log(error);
            });
            },
          
          approverequest(id){
            axios
            .put('http://localhost:5000/adrequest/'+id+'/approve',{},
                 {headers: {Authorization: this.auth}})
            .then((response) => {
                console.log(response);
                alert('Ad Request Approved Successfully');
                this.$router.go(0);
              })
            .catch((error) => {
                alert('Ad Request Approval Failed! Reason: ' + response.data.message +' Please try again');
                console.log(error);
            });
          },
          rejectrequest(id){
            axios
            .put('http://localhost:5000/adrequest/'+id+'/reject',{},
                 {headers: {Authorization: this.auth}})
            .then((response) => {
                console.log(response);
                alert('Ad Request Rejected Successfully');
                this.$router.go(0);
              })
            .catch((error) => {
                alert('Ad Request Rejected Failed! Reason: ' + response.data.message +' Please try again');
                console.log(error);
            });
          },
          removerequest(id){
            axios
            .delete('http://localhost:5000/adrequest/'+id+'/remove',
                 {headers: {Authorization: this.auth}})
            .then((response) => {
                console.log(response);
                if(response.status == 200){
                alert('Request Removed Successfully');
                this.$router.go(0);}
                else{
                  alert('Request Removal Failed! Reason: ' + response.data.message +' Please try again');
                  this.$router.go(0);
                }
              })
            .catch((error) => {
                alert('Request Removal Failed! Reason: ' + response.data.message +' Please try again');
                console.log(error);
            });
          },
          viewcampaign(id){
            this.$router.push({ name: 'ViewCampaignPage', params: { campaign_id: id } });
          },
          viewinfluencer(id){
            this.$router.push({ name:'InfluencerProfilePublicPage', params: { users_id:id } })
          },
          getad(id){
            axios
            .get('http://localhost:5000/influencer/ad/'+id,
                 {headers: {Authorization: this.auth}})
            .then((response) => {
                console.log(response);
                this.selectedAd = response.data;
              })
            .catch((error) => {
                console.log(error);
            });
          },
          openModal(id) {
                this.getad(id); 
                const modal = new bootstrap.Modal(document.getElementById('adModal')); 
                modal.show(); },
          
          openReportModal(id) {
                  this.selecteduser = id; 
                  const modal = new bootstrap.Modal(document.getElementById('reportModal')); 
                  modal.show(); }, 
                  
          validateReportForm() { 
            this.reportReasonError = ''; 
            this.reportDetailsError = ''; 
            let valid = true; 
            if (!this.rating) { 
              this.reportReasonError = 'Please select a rating.'; 
              valid = false; } 
            if (!this.reviews) { 
              this.reportDetailsError = 'Please provide a review.'; 
              valid = false; } 
            if (valid) { 
              this.submitReport(); } 
            }, 
            
            submitReport() { 
              axios
              .post('http://localhost:5000/sponsor/rateinfluencer', 
              { rating: this.rating, 
                review: this.reviews,
                influencer_id: this.selecteduser
              
              }, 
              { headers: { 'Authorization': this.auth } }) 
              .then((response) => { console.log(response); 
                alert('Review submitted successfully!');
                 this.rating = ''; this.reviews = ''; 
                 document.getElementById('reportModal').classList.remove('show');
                  document.getElementById('reportModal').style.display = 'none';
                   document.getElementsByClassName('modal-backdrop')[0].remove(); }) 
                   .catch((error) => { console.log(error); alert('An error occurred while submitting your review. Please try again later.');

                    });
                   },
            messageinfluencer(id){
              this.$router.push({ name: 'SponsorNegociationMessagePage', params: { request_id: id } });
            },


  },
  computed: {

  },
  watch: {
    
  },
  mounted() {
    
  },
  created() {
   
    this.auth = localStorage.getItem('AuthToken');
    this.role = localStorage.getItem('userrole');
    this.user_id = localStorage.getItem('userid');
    if (this.auth == null) {
      this.$router.push({ name: 'Login' });
    }
    if (this.role != 'Sponsor') {
      this.$router.push({ name: 'Login' });
    }
    this.getdata();
  }
}
</script>

<style scoped>
.dashboard {
  display: flex;
  flex-wrap: wrap;
  flex-direction: column;
  gap: 40px;
  margin: 0 10%;
  border: 5px solid #5b5a5a;
  border-radius: 30px;
  
  
  padding: 10px;
  width: 80%;
  margin-bottom: 20px;
}

.dashboard .sponsornav {
  display: flex;
  flex-direction: row;
  gap: 10px;
  border: 2px ;
  border-radius: 30px;
  padding: 10px;
  flex-wrap: wrap;
  width: 100%;
  align-self: right;
  justify-content: flex-end;
}

.dashboard .sponsornav h2 {
  display: flex;
  flex-direction: row;
  margin-right: auto;
}

.dashboard .activesponsor .heading {
  display: flex;
  flex-direction: row;
  flex: 0 1;
  border-radius: 30px;
  padding: 10px;
  flex-wrap: wrap;

}

.dashboard .activesponsor {
  display: flex;
  flex-direction: column;
  gap: 10px;
  border: 2px ;
  border-radius: 30px;
  padding: 10px;
  flex-wrap: wrap;
  width: 100%;
}

.dashboard .activesponsor .heading {
  display: flex;
  flex-direction: row;
  flex: 0 1;
  border-radius: 30px;
  padding: 10px;
  flex-wrap: wrap;

}

.dashboard .inactivesponsor {
  display: flex;
  flex-direction: column;
  gap: 10px;
  border: 2px ;
  border-radius: 30px;
  padding: 10px;
  flex-wrap: wrap;
  width: 100%;
}

.dashboard .flaggedsponsors {
  display: flex;
  flex-direction: column;
  gap: 10px;
  border: 2px;
  border-radius: 30px;
  padding: 10px;
  flex-wrap: wrap;
  width: 100%;
}




.dashboard .table__body {
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

.dashboard .inactivesponsor .table__body {
  display: flex;
  gap: 20px;
  border-radius: 30px;
  flex-wrap: wrap;
  overflow-x: auto;
  width: 100%;
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
  min-width: 200px;
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





</style>