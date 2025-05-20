<script setup>
import axios from 'axios';
import Topbar from '../../components/Topbar.vue'
</script>

<template>
  <div>
    <Topbar />
  </div>
    <div style="margin-top: 30px;margin-bottom: 20px; align-self: center;" >
              <h2><span class="mdi mdi-view-dashboard"></span> Influencer's Dashboard</h2>
    </div>
  <div class="dashboard">
      <div class="activesponsor" v-if="Influencerlistactive.length>0">
        <div class="heading">
              <h2>Active Influencers</h2>
        </div>
        <section class="table__body">
            <table>
                <thead>
                    <tr>
                        <th> S.No </th>
                        <th> Name </th>
                        <th> Username </th>
                        <th> Email </th>
                        <th> Industry </th>
                        <th> Niche</th>
                        <th> Platforms</th>
                        <th> Reach</th>
                        <th> Data Joined </th>
                        <th> Status </th>
                        <th> Reported </th>
                        <th> Actions </th>
                    </tr>
                </thead>
                <tbody>
                  <tr v-for="(influenceract, index) in Influencerlistactive" :key="influenceract.id">
                      <td>{{ index + 1}}</td>
                      <td>{{ influenceract.name }}</td>
                      <td>@ {{ influenceract.username }}</td>
                      <td>{{ influenceract.email }}</td>
                      <td>{{ influenceract.industry }}</td>
                      <td>{{ influenceract.niche }}</td>
                      <td><span class="mdi mdi-youtube" v-if="influenceract.yt" ></span><span class="mdi mdi-instagram"  v-if="influenceract.insta" ></span>
                        <span class="mdi mdi-facebook" v-if="influenceract.fb" ></span><span class="mdi mdi-twitter"  v-if="influenceract.twitter" ></span>
                        <span class="mdi mdi-at"  v-if="influenceract.thread"  ></span><span class="mdi mdi-music-note-outline"  v-if="influenceract.tiktok" ></span>
                        <span class="mdi mdi-twitch"  v-if="influenceract.twitch" ></span><span class="mdi mdi-kickstarter"  v-if="influenceract.kick" ></span>
                        <span class="mdi mdi-snapchat"  v-if="influenceract.snapchat"  ></span><span class="mdi mdi-linkedin"  v-if="influenceract.linkedin" ></span>
                      </td>
                      <td>{{ influenceract.totalreach }}</td>
                      <td>{{ influenceract.date_joined }}</td>
                      <td>{{ influenceract.status }}</td>
                      <td>{{ influenceract.reported }}</td>
                      <td id="actions">
                          <button type="submit" class="btn btn-primary"  style="font-size:15px; border-radius:10px;" @click="viewprofile(influenceract.id)" v-tooltip.top="'View Profile'">
                            <span class="mdi mdi-view-quilt"></span>
                              </button>
                          <button type="submit" class="btn btn-warning"  style="font-size:15px; border-radius:10px;" @click="flaginfluencer(influenceract.id)" v-tooltip.top="'Flag Influencer'">
                            <span class="mdi mdi-flag-variant"></span>
                              </button>
                          <button type="submit" class="btn btn-danger"  style="font-size:15px; border-radius:10px;" @click="deactivateinfluencer(influenceract.id)" v-tooltip.top="'Deactivate Account'">
                            <span class="mdi mdi-account-off"></span>
                              </button>
                          <button v-if="influenceract.avg_rating>0" type="submit" class="btn btn-info"  style="font-size:15px; border-radius:10px;" @click="readreviews(influenceract.id)" v-tooltip.top="'Read Reviews'">
                            <span class="mdi mdi-comment-text-multiple"></span>
                          </button>
                          <button v-if="influenceract.reported>0" type="submit" class="btn btn-dark"  style="font-size:15px; border-radius:10px;" @click="readreport(influenceract.id)" v-tooltip.top="'Read Reports'">
                            <span class="mdi mdi-comment-alert"></span>
                          </button>
                      </td>
                  </tr>
                </tbody>
            </table>
        </section>
        <div class="totals" align="right">
          <span class="badge badge-pill" style="border-radius:30px;background:rgb(0, 88, 150)"> Total Active Influencers: {{Influencerlistactive.length}}</span>
        </div>
      </div>
      <div class="inactivesponsor" v-if="Influencerlistinactive.length>0">
          <div class="heading">
              <h2>Inactive Influencers</h2>
          </div>
          <section class="table__body">
            <table>
                <thead>
                    <tr>
                        <th> S.No </th>
                        <th> Name </th>
                        <th> Username </th>
                        <th> Email </th>
                        <th> Industry </th>
                        <th> Niche</th>
                        <th> Platforms</th>
                        <th> Reach</th>
                        <th> Data Joined </th>
                        <th> Status </th>
                        <th> Reported </th>
                        <th> Actions </th>
                    </tr>
                </thead>
                <tbody>
                  <tr v-for="(influencerinact, index) in Influencerlistinactive" :key="influencerinact.id">
                      <td>{{ index + 1}}</td>
                      <td>{{ influencerinact.name }}</td>
                      <td>@ {{ influencerinact.username }}</td>
                      <td>{{ influencerinact.email }}</td>
                      <td>{{ influencerinact.industry }}</td>
                        <td>{{ influencerinact.niche }}</td>
                      <td><span class="mdi mdi-youtube" v-if="influencerinact.yt" ></span><span class="mdi mdi-instagram"  v-if="influencerinact.insta" ></span>
                        <span class="mdi mdi-facebook" v-if="influencerinact.fb" ></span><span class="mdi mdi-twitter"  v-if="influencerinact.twitter" ></span>
                        <span class="mdi mdi-at"  v-if="influencerinact.thread"  ></span><span class="mdi mdi-music-note-outline"  v-if="influencerinact.tiktok" ></span>
                        <span class="mdi mdi-twitch"  v-if="influencerinact.twitch" ></span><span class="mdi mdi-kickstarter"  v-if="influencerinact.kick" ></span>
                        <span class="mdi mdi-snapchat"  v-if="influencerinact.snapchat"  ></span><span class="mdi mdi-linkedin"  v-if="influencerinact.linkedin" ></span>
                      </td>
                      <td>{{ influencerinact.totalreach }}</td>
                      <td>{{ influencerinact.date_joined }}</td>
                      <td>{{ influencerinact.status }}</td>
                      <td>{{ influencerinact.reported }}</td>
                      <td id="actions">
                          <button type="submit" class="btn btn-primary"  style="font-size:15px; border-radius:10px;" @click="viewprofile(influencerinact.id)" v-tooltip.top="'View Profile'">
                            <span class="mdi mdi-view-quilt"></span>
                              </button>
                          <button type="submit" class="btn btn-warning"  style="font-size:15px; border-radius:10px; " @click="flaginfluencer(influencerinact.id)" v-tooltip.top="'Flag Influencer'">
                            <span class="mdi mdi-flag-variant"></span>
                              </button>
                          <button type="submit" class="btn btn-success"  style="font-size:15px; border-radius:10px;" @click.prevent="activateinfluencer(influencerinact.id)" v-tooltip.top="'Activate Account'">
                            <span class="mdi mdi-account-reactivate"></span>
                              </button>
                              <button v-if="influencerinact.reported>0" type="submit" class="btn btn-dark"  style="font-size:15px; border-radius:10px;" @click="readreport(influencerinact.id)" v-tooltip.top="'Read Reports'">
                            <span class="mdi mdi-comment-alert"></span>
                          </button>
                      </td>
                  </tr>
                </tbody>
            </table>
        </section>
        <div class="totals" align="right">
          <span class="badge badge-pill" style="border-radius:30px;background:rgb(0, 88, 150)"> Total Inactive Influencers: {{Influencerlistinactive.length}}</span>
        </div>
      </div>
      <div class="flaggedsponsors" v-if="Influencerlistflagged.length>0">
        <div class="heading">
              <h2>Flagged Influencers</h2>
          </div>
          <section class="table__body">
            <table>
                <thead>
                    <tr>
                        <th> S.No </th>
                        <th> Name </th>
                        <th> Username </th>
                        <th> Email </th>
                        <th> Industry </th>
                        <th> Niche</th>
                        <th> Platforms</th>
                        <th> Reach</th>
                        <th> Data Joined </th>
                        <th> Status </th>
                        <th> Reported </th>
                        <th> Actions </th>
                    </tr>
                </thead>
                <tbody>
                  <tr v-for="(influencerflag, index) in Influencerlistflagged" :key="influencerflag.id">
                      <td>{{ index + 1}}</td>
                      <td>{{ influencerflag.name }}</td>
                      <td>@ {{ influencerflag.username }}</td>
                      <td>{{ influencerflag.email }}</td>
                      <td>{{ influencerflag.industry }}</td>
                      <td>{{ influencerflag.niche }}</td>
                      <td><span class="mdi mdi-youtube" v-if="influencerflag.yt" ></span><span class="mdi mdi-instagram"  v-if="influencerflag.insta" ></span>
                        <span class="mdi mdi-facebook" v-if="influencerflag.fb" ></span><span class="mdi mdi-twitter"  v-if="influencerflag.twitter" ></span>
                        <span class="mdi mdi-at"  v-if="influencerflag.thread"  ></span><span class="mdi mdi-music-note-outline"  v-if="influencerflag.tiktok" ></span>
                        <span class="mdi mdi-twitch"  v-if="influencerflag.twitch" ></span><span class="mdi mdi-kickstarter"  v-if="influencerflag.kick" ></span>
                        <span class="mdi mdi-snapchat"  v-if="influencerflag.snapchat"  ></span><span class="mdi mdi-linkedin"  v-if="influencerflag.linkedin" ></span>
                      </td>
                      <td>{{ influencerflag.totalreach }}</td>
                      <td>{{ influencerflag.date_joined }}</td>
                      <td>{{ influencerflag.status }}</td>
                      <td>{{ influencerflag.reported }}</td>
                      <td id="actions">
                          <button type="submit" class="btn btn-primary"  style="font-size:15px; border-radius:10px;" @click="viewprofile(influencerflag.id)" v-tooltip.top="'View Profile'">
                            <span class="mdi mdi-view-quilt"></span>
                              </button>
                          <button type="submit" class="btn btn-success"  style="font-size:15px; border-radius:10px; " @click="unflaginfluencer(influencerflag.id)" v-tooltip.top="'UnFlag Influencer'">
                            <span class="mdi mdi-flag-variant-off"></span>
                              </button>
                          <button v-if="influencerflag.avg_rating>0"  type="submit" class="btn btn-info"  style="font-size:15px; border-radius:10px;" @click="readreviews(influenceract.id)" v-tooltip.top="'Read Reviews'">
                            <span class="mdi mdi-comment-text-multiple"></span>
                          </button>
                          <button v-if="influencerflag.reported>0" type="submit" class="btn btn-dark"  style="font-size:15px; border-radius:10px;" @click="readreport(influencerflag.id)" v-tooltip.top="'Read Reports'">
                            <span class="mdi mdi-comment-alert"></span>
                          </button>
                      </td>
                  </tr>
                </tbody>
            </table>
        </section>
        <div class="totals" align="right">
          <span class="badge badge-pill" style="border-radius:30px;background:rgb(0, 88, 150)"> Total Flagged Influencers: {{Influencerlistflagged.length}}</span>
        </div>
      </div>
  </div>
  <div style="background-color: #333; color: white; text-align: center; position: relative; bottom: 0; left: 0; width: 100%; font-family: 'Doto', sans-serif; font-optical-sizing: auto; font-weight: 1000; font-style: normal; font-variation-settings: 'ROND' 100; font-size: 1.1rem; height: 50px;">
  <p align="center" style="margin: 0; line-height: 50px;">© 2024 | © 21EJCCS821,826,854 | Influencer Engagement Sponsor Coordination Platform | © CreativeMerge</p>
</div>
</template>

<script>
export default {
  name: '',
  data() {
    return {
          Influencerlistactive: [],
          Influencerlistinactive: [],
          Influencerlistflagged: [],
          auth:'',
          username:'',
          influencer_id:null,

    }
  },
  methods: {
        getdatalists(){
          axios 
            .get('http://localhost:5000/admin/influencerdashboard',
                 {headers: {Authorization: this.auth}})
            .then((response) => {
                console.log("Response Block",response);
                this.Influencerlistactive = response.data.active;
                this.Influencerlistinactive = response.data.inactive;
                this.Influencerlistflagged = response.data.flagged;
              })
            .catch((error) => {
                console.log(error);
            });

        },
        flaginfluencer(influencer_id){
          axios 
          .post('http://localhost:5000/admin/influencerdashboard/'+influencer_id+'/flag',{},
                 {headers: {Authorization: this.auth}})
            .then((response) => {
                console.log("Response Block",response)
                this.$router.go(0);
              })
            .catch((error) => {
                console.log(error);
            });
        },
        unflaginfluencer(influencer_id){
          axios 
          .post('http://localhost:5000/admin/influencerdashboard/'+influencer_id+'/unflag',
                {} ,{headers: {Authorization: this.auth}})
            .then((response) => {
                console.log("Response Block",response)
                this.$router.go(0);
              })
            .catch((error) => {
                console.log(error);
            });
        },
        activateinfluencer(influencer_id){
          axios 
          .post('http://localhost:5000/admin/influencerdashboard/'+influencer_id+'/activate',{},
                 {headers: {Authorization: this.auth}})
            .then((response) => {
                console.log("Response Block",response)
                this.$router.go(0);
              })
            .catch((error) => {
                console.log(error);
            });
        },
        deactivateinfluencer(influencer_id){
          axios 
          .post('http://localhost:5000/admin/influencerdashboard/'+influencer_id+'/deactivate',{},
                 {headers: {Authorization: this.auth}})
            .then((response) => {
                console.log("Response Block",response)
                this.$router.go(0);
              })
            .catch((error) => {
                console.log(error);
            });
        },
        viewprofile(userids){
            this.$router.push({name: 'InfluencerProfilePublicPage', params: {users_id: userids}});
          },
          readreport(userids){
            this.$router.push({name: 'AdminReportsPage', params: {users_id: userids}});
          },
          readreviews(userids){
            this.$router.push({name: 'AdminUserReviewsPage', params: {users_id: userids}});
          }
  },
  computed: {
    
  },
  watch: {
    
  },
  mounted() {
    
  },
  created(){
    this.auth = localStorage.getItem('AuthToken');
    this.getdatalists();
  }
}
</script>


<style scoped>
/* Existing styles */

.dashboard {
  display: flex;
  flex-wrap: wrap;
  flex-direction: column;
  gap: 50px;
  margin: 0 10%;
  border: 5px solid #5b5a5a;
  border-radius: 30px;
  
  
  padding: 10px;
  width: 80%;
  margin-bottom: 20px;
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
  min-width: 300px;
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
  gap: 15px;
}
table {
  width: 100%;
  table-layout: auto;
}

table, th, td {
  border-collapse: collapse;
  text-align: left;
  padding: 1rem;
  min-width: 120px;
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
    background-color: rgba(217, 217, 217, 0.4) !important;
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
