<script setup>
import axios from 'axios';
import Topbar from '../../components/Topbar.vue'
</script>

<template>
  <div>
    <Topbar />
  </div>
    <div style="margin-top: 30px;margin-bottom: 20px; align-self: center;" >
              <h2><span class="mdi mdi-view-dashboard"></span> Sponsors Dashboard</h2>
    </div>
  <div class="dashboard">
      <div class="activesponsor" v-if="Sponsorlistactive.length>0">
        <div class="heading">
              <h2>Active Sponsors</h2>
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
                        <th> Data Joined </th>
                        <th> Status </th>
                        <th> Reported </th>
                        <th> Actions </th>
                    </tr>
                </thead>
                <tbody>
                  <tr v-for="(sponsoract, index) in Sponsorlistactive" :key="sponsoract.id">
                      <td>{{ index + 1}}</td>
                      <td>{{ sponsoract.name }}</td>
                      <td>@ {{ sponsoract.username }}</td>
                      <td>{{ sponsoract.email }}</td>
                      <td>{{ sponsoract.industry }}</td>
                      <td>{{ sponsoract.date_joined }}</td>
                      <td>{{ sponsoract.status }}</td>
                      <td>{{ sponsoract.reported }}</td>
                      <td id="actions">
                          <button type="submit" class="btn btn-primary"  style="font-size:15px; border-radius:10px;" @click="viewprofile(sponsoract.id)" v-tooltip.top="'View Profile'">
                            <span class="mdi mdi-view-quilt"></span>
                              </button>
                          <button type="submit" class="btn btn-warning"  style="font-size:15px; border-radius:10px;" @click="flagsponsor(sponsoract.id)" v-tooltip.top="'Flag Sponsor'">
                            <span class="mdi mdi-flag-variant"></span>
                              </button>
                          <button type="submit" class="btn btn-danger"  style="font-size:15px; border-radius:10px;" @click="deactivatesponsor(sponsoract.id)" v-tooltip.top="'Deactivate Sponsor'">
                            <span class="mdi mdi-account-off"></span>   
                              </button>
                          <button v-if="sponsoract.reported>0" type="submit" class="btn btn-info"  style="font-size:15px; border-radius:10px;" @click="readreport(sponsoract.id)" v-tooltip.top="'Read Reports'">
                            <span class="mdi mdi-comment-alert"></span>
                            </button>
                      </td>
                  </tr>
                </tbody>
            </table>
        </section>
        <div class="totals" align="right">
          <span class="badge badge-pill" style="border-radius:30px;background:rgb(0, 88, 150)"> Total Active Sponsors: {{Sponsorlistactive.length}}</span>
        </div>
      </div>
      <div class="inactivesponsor" v-if="Sponsorlistinactive.length>0">
          <div class="heading">
              <h2>Inactive Sponsors</h2>
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
                        <th> Data Joined </th>
                        <th> Status </th>
                        <th> Reported </th>
                        <th> Actions </th>
                    </tr>
                </thead>
                <tbody>
                  <tr v-for="(sponsorinact, index) in Sponsorlistinactive" :key="sponsorinact.id">
                      <td>{{ index + 1}}</td>
                      <td>{{ sponsorinact.name }}</td>
                      <td>@ {{ sponsorinact.username }}</td>
                      <td>{{ sponsorinact.email }}</td>
                      <td>{{ sponsorinact.industry }}</td>
                      <td>{{ sponsorinact.date_joined }}</td>
                      <td>{{ sponsorinact.status }}</td>
                      <td>{{ sponsorinact.reported }}</td>
                      <td id="actions">
                          <button type="submit" class="btn btn-primary"  style="font-size:15px; border-radius:10px;" @click="viewprofile(sponsorinact.id)" v-tooltip.top="'View Profile'">
                            <span class="mdi mdi-view-quilt"></span>
                              </button>
                          <button type="submit" class="btn btn-warning"  style="font-size:15px; border-radius:10px; " @click="flagsponsor(sponsorinact.id)" v-tooltip.top="'Flag Sponsor'">
                            <span class="mdi mdi-flag-variant"></span>
                              </button>
                          <button type="submit" class="btn btn-success"  style="font-size:15px; border-radius:10px;" @click.prevent="activatesponsor(sponsorinact.id)" v-tooltip.top="'Activate Sponsor'">
                            <span class="mdi mdi-account-reactivate"></span>
                              </button>
                              <button v-if="sponsorinact.reported>0"  type="submit" class="btn btn-info"  style="font-size:15px; border-radius:10px;" @click="readreport(sponsorinact.id)" v-tooltip.top="'Read Reports'">
                            <span class="mdi mdi-comment-alert"></span>
                            </button>
                      </td>
                  </tr>
                </tbody>
            </table>
        </section>
        <div class="totals" align="right">
          <span class="badge badge-pill" style="border-radius:30px;background:rgb(0, 88, 150)"> Total Inactive Sponsors: {{Sponsorlistinactive.length}}</span>
        </div>
      </div>
      <div class="flaggedsponsors" v-if="Sponsorlistflagged.length>0">
        <div class="heading">
              <h2>Flagged Sponsors</h2>
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
                        <th> Data Joined </th>
                        <th> Status </th>
                        <th> Reported </th>
                        <th> Actions </th>
                    </tr>
                </thead>
                <tbody>
                  <tr v-for="(sponsorflag, index) in Sponsorlistflagged" :key="sponsorflag.id">
                      <td>{{ index + 1}}</td>
                      <td>{{ sponsorflag.name }}</td>
                      <td>@ {{ sponsorflag.username }}</td>
                      <td>{{ sponsorflag.email }}</td>
                      <td>{{ sponsorflag.industry }}</td>
                      <td>{{ sponsorflag.date_joined }}</td>
                      <td>{{ sponsorflag.status }}</td>
                      <td>{{ sponsorflag.reported }}</td>
                      <td id="actions">
                          <button type="submit" class="btn btn-primary"  style="font-size:15px; border-radius:10px;" @click="viewprofile(sponsorflag.id)" v-tooltip.top="'View Profile'">
                            <span class="mdi mdi-view-quilt"></span>
                              </button>
                          <button type="submit" class="btn btn-success"  style="font-size:15px; border-radius:10px; " @click="unflagsponsor(sponsorflag.id)" v-tooltip.top="'UnFlag Sponsor'">
                            <span class="mdi mdi-flag-variant-off"></span>
                              </button>
                              <button v-if="sponsorflag.reported>0" type="submit" class="btn btn-info"  style="font-size:15px; border-radius:10px;" @click="readreport(sponsorflag.id)" v-tooltip.top="'Read Reports'">
                          <span class="mdi mdi-comment-alert"></span> 
                            </button>
                      </td>
                  </tr>
                </tbody>
            </table>
        </section>
        <div class="totals" align="right">
          <span class="badge badge-pill" style="border-radius:30px;background:rgb(0, 88, 150)"> Total Flagged Sponsors: {{Sponsorlistflagged.length}}</span>
        </div>
      </div>
  </div>
  <div style="background-color: #333; color: white; text-align: center; position: relative; bottom: 0; left: 0; width: 100%; font-family: 'Doto', sans-serif; font-optical-sizing: auto; font-weight: 1000; font-style: normal; font-variation-settings: 'ROND' 100; font-size: 1.1rem; height: 50px;">
  <p align="center" style="margin: 0; line-height: 50px;">© 2024 | © 21F3001516 | Influencer Engagement Sponsor Coordination Platform | © CreativeMerge</p>
</div>
</template>

<script>
export default {
  name: '',
  data() {
    return {
          Sponsorlistactive: [],
          Sponsorlistinactive: [],
          Sponsorlistflagged: [],
          auth:'',
          username:'',
          sponser_id:null,

    }
  },
  methods: {
        getdatalists(){
          axios 
            .get('http://localhost:5000/admin/sponsordashboard',
                 {headers: {Authorization: this.auth}})
            .then((response) => {
                this.Sponsorlistactive = response.data.active;
                this.Sponsorlistinactive = response.data.inactive;
                this.Sponsorlistflagged = response.data.flagged;
              })
            .catch((error) => {
                console.log(error);
            });

        },
        flagsponsor(sponsor_id){
          axios 
          .post('http://localhost:5000/admin/sponsordashboard/'+sponsor_id+'/flag',{},
                 {headers: {Authorization: this.auth}})
            .then((response) => {
                console.log("Response Block",response)
                this.$router.go(0);
              })
            .catch((error) => {
                console.log(error);
            });
        },
        unflagsponsor(sponsor_id){
          axios 
          .post('http://localhost:5000/admin/sponsordashboard/'+sponsor_id+'/unflag',
                {} ,{headers: {Authorization: this.auth}})
            .then((response) => {
                console.log("Response Block",response)
                this.$router.go(0);
              })
            .catch((error) => {
                console.log(error);
            });
        },
        activatesponsor(sponsor_id){
          axios 
          .post('http://localhost:5000/admin/sponsordashboard/'+sponsor_id+'/activate',{},
                 {headers: {Authorization: this.auth}})
            .then((response) => {
                console.log("Response Block",response)
                this.$router.go(0);
              })
            .catch((error) => {
                console.log(error);
            });
        },
        deactivatesponsor(sponsor_id){
          axios 
          .post('http://localhost:5000/admin/sponsordashboard/'+sponsor_id+'/deactivate',{},
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
            this.$router.push({name: 'SponsorProfilePublicPage', params: {users_id: userids}});
          },
          readreport(userids){
            this.$router.push({name: 'AdminReportsPage', params: {users_id: userids}});
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
  gap: 25px;
}
table {
  width: 100%;
  table-layout: auto;
}

table, th, td {
  border-collapse: collapse;
  text-align: left;
  padding: 1rem;
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
