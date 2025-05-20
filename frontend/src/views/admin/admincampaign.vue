<script setup>
import Topbar from '../../components/Topbar.vue'

</script>

<template>
  <div>
    <Topbar />
  </div>
  <div style="margin-top: 30px;margin-bottom: 20px; align-self: center;" >
              <h1><span class="mdi mdi-view-dashboard"></span> Campaigns Dashboard</h1>
    </div>
    <div class="dashboard">
      <div class="sponsornav">
        <h2 id="xyz">Advertisement Campaigns:</h2>
      </div>
      
      <div class="activesponsor" v-if="activecampaigns.length>0">
        <div class="heading">
              <h2>Active Campaigns</h2>
        </div>
        <section class="table__body" >
            <table>
                <thead>
                    <tr>
                        <th> S.No </th>
                        <th> Title </th>
                        <th> Start Date </th>
                        <th> End Date </th>
                        <th> Budget &#8377 </th>
                        <th> Target Reach </th>
                        <th> Activity </th>
                        <th> Status </th>
                        <th> Visibility </th>
                        <th> Progress %</th>
                        <th> Date Created </th>
                        <th> Actions </th>
                    </tr>
                </thead>
                <tbody>
                  <tr v-for="(actcamp, index) in activecampaigns" :key="activecampaigns.id">
                      <td>{{ index + 1}}</td>
                      <td>{{ actcamp.title }}</td>
                      <td>{{ actcamp.start_date }}</td>
                      <td>{{ actcamp.end_date }}</td>
                      <td>&#8377 {{ actcamp.budget }}</td>
                      <td>{{ actcamp.target }}</td>
                      <td v-if="actcamp.active"> Active</td>
                      <td v-if="!actcamp.active">Inactive</td>
                      <td>{{ actcamp.status }}</td>
                      <td>{{ actcamp.visibility }}</td>
                      <td><Knob v-model="actcamp.progress"  readonly :size="50" valueColor="Lime"  /></td>
                      <td>{{ actcamp.date_created }}</td>
                      <td id="actions">
                          <button type="submit" class="btn btn-primary"   style="font-size:15px; border-radius:10px;" @click="viewcampaign(actcamp.id)" v-tooltip.top="'View Campaign'">
                            <span class="mdi mdi-newspaper"></span>
                              </button>
                          <button type="submit" class="btn btn-warning"  style="font-size:15px; border-radius:10px;" @click="flagcampaign(actcamp.id)" v-tooltip.top="'Flag Campaign'">
                            <span class="mdi mdi-flag-variant"></span>
                          </button>
                          <button type="submit" class="btn btn-dark"  style="font-size:15px; border-radius:10px;" @click="readreport(actcamp.id)" v-tooltip.top="'Read Reports'">
                            <span class="mdi mdi-comment-alert"></span>
                          </button>
                      </td>
                  </tr>
                </tbody>
            </table>
        </section>
        <div class="totals" align="right">
          <span class="badge badge-pill" style="border-radius:30px;background:rgb(0, 88, 150)"> Total Active Campaigns: {{ activecampaigns.length }}</span>
        </div>
      </div>
      <div class="inactivesponsor" v-if="inactivecampaigns.length>0">
          <div class="heading">
              <h2>Flagged Campaigns</h2>
          </div>
          <section class="table__body">
            <table>
              <thead>
                    <tr>
                        <th> S.No </th>
                        <th> Title </th>
                        <th> Start Date </th>
                        <th> End Date </th>
                        <th> Budget &#8377</th>
                        <th> Target Reach </th>
                        <th> Activity </th>
                        <th> Status </th>
                        <th> Visibility </th>
                        <th> Progress %</th>
                        <th> Date Created </th>
                        <th> Actions </th>
                    </tr>
                </thead>
                <tbody>
                  <tr v-for="(inactcamp, index) in inactivecampaigns" :key="inactivecampaigns.id">
                      <td>{{ index + 1}}</td>
                      <td>{{ inactcamp.title }}</td>
                      <td>{{ inactcamp.start_date }}</td>
                      <td>{{ inactcamp.end_date }}</td>
                      <td>&#8377 {{ inactcamp.budget }}</td>
                      <td>{{ inactcamp.target }}</td>
                        <td v-if="inactcamp.active"> Active</td>
                        <td v-if="!inactcamp.active">Inactive</td>
                      <td>{{ inactcamp.status }}</td>
                      <td>{{ inactcamp.visibility }}</td>
                      <td><Knob v-model="inactcamp.progress"  readonly :size="50" valueColor="Lime"  /></td>
                      <td>{{ inactcamp.date_created }}</td>
                      <td id="actions">
                          <button type="submit" class="btn btn-primary"  style="font-size:15px; border-radius:10px;" @click="viewcampaign(inactcamp.id)" v-tooltip.top="'View Campaign'">
                            <span class="mdi mdi-newspaper"></span>
                              </button>
                          <button type="submit" class="btn btn-success"  style="font-size:15px; border-radius:10px;" @click="unflagcampaign(inactcamp.id)" v-tooltip.top="'Flag Campaign'">
                            <span class="mdi mdi-flag-variant-off"></span>
                          </button>
                          <button type="submit" class="btn btn-dark"  style="font-size:15px; border-radius:10px;" @click="readreport(inactcamp.id)" v-tooltip.top="'Read Reports'">
                            <span class="mdi mdi-comment-alert"></span>
                          </button>
                      </td>
                  </tr>
                </tbody>
            </table>
        </section>
        <div class="totals" align="right">
          <span class="badge badge-pill" style="border-radius:30px;background:rgb(0, 88, 150)"> Total Flagged Campaigns: {{ inactivecampaigns.length }} </span>
        </div>
      </div>
      <div class="inactivesponsor" v-if="completecampaigns.length>0" >
          <div class="heading">
              <h2>Completed Campaigns</h2>
          </div>
          <section class="table__body">
            <table>
              <thead>
                    <tr>
                        <th> S.No </th>
                        <th> Title </th>
                        <th> Start Date </th>
                        <th> End Date </th>
                        <th> Budget &#8377</th>
                        <th> Target Reach </th>
                        <th> Activity </th>
                        <th> Status </th>
                        <th> Visibility </th>
                        <th> Progress %</th>
                        <th> Date Created </th>
                        <th> Actions </th>
                    </tr>
                </thead>
                <tbody>
                  <tr v-for="(compcamp, index) in completecampaigns" :key="completecampaigns.id">
                      <td>{{ index + 1}}</td>
                      <td>{{ compcamp.title }}</td>
                      <td>{{ compcamp.start_date }}</td>
                      <td>{{ compcamp.end_date }}</td>
                      <td>&#8377 {{ compcamp.budget }}</td>
                      <td>{{ compcamp.target }}</td>
                      <td v-if="compcamp.active"> Active</td>
                      <td v-if="!compcamp.active">Inactive</td>
                      <td>{{ compcamp.status }}</td>
                      <td>{{ compcamp.visibility }}</td>
                      <td><Knob v-model="compcamp.progress"  readonly :size="50" valueColor="Lime"  /></td>
                      <td>{{ compcamp.date_created }}</td>
                      <td id="actions">
                          <button type="submit" class="btn btn-primary" data-bs-toggle="tooltip" data-bs-placement="top" data-bs-title="Tooltip on top" style="font-size:15px; border-radius:10px;" @click="viewcampaign(compcamp.id)" v-tooltip.top="'View Campaign'">
                            <span class="mdi mdi-newspaper"></span>
                              </button>
                      </td>
                  </tr>
                </tbody>
            </table>
        </section>
        <div class="totals" align="right">
          <span class="badge badge-pill" style="border-radius:30px;background:rgb(0, 88, 150)"> Total Completed Campaigns: {{ completecampaigns.length }}  </span>
        </div>
      </div>
    
  </div>
  <div style="background-color: #333; color: white; text-align: center; position: relative; bottom: 0; left: 0; width: 100%; font-family: 'Doto', sans-serif; font-optical-sizing: auto; font-weight: 1000; font-style: normal; font-variation-settings: 'ROND' 100; font-size: 1.1rem; height: 50px;">
  <p align="center" style="margin: 0; line-height: 50px;">© 2024 | © 21EJCCS821,826,854 | Influencer Engagement Sponsor Coordination Platform | © CreativeMerge</p>
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
        user_id: '',
        tooltipVisible: false
    }
  },
  methods: {
          getdata() {
            axios 
            .get('http://localhost:5000/admin/campaigns',
                 {headers: {Authorization: this.auth}})
            .then((response) => {
                console.log(response);
                this.activecampaigns = response.data.campaigns;
                this.inactivecampaigns = response.data.flaggedcampaign;
                this.completecampaigns = response.data.completed;
              })
            .catch((error) => {
                console.log(error);
            });
            },
          flagcampaign(id){
            axios
            .post('http://localhost:5000/admin/campaigns/'+id+'/flag',{},
                 {headers: {Authorization: this.auth}})
            .then((response) => {
                console.log(response);
                alert('Campaign Flagged Successfully');
                this.$router.go(0);
              })
            .catch((error) => {
                alert('Campaign Flagging Failed! Reason: ' + response.data.message +' Please try again');
                console.log(error);
            });
          },
          unflagcampaign(id){
            axios
            .post('http://localhost:5000/admin/campaigns/'+id+'/unflag',{},
                 {headers: {Authorization: this.auth}})
            .then((response) => {
                console.log(response);
                alert('Campaign Un Flagged Successfully');
                this.$router.go(0);
              })
            .catch((error) => {
                alert('Campaign Unflagging Failed! Reason: ' + response.data.message +' Please try again');
                console.log(error);
            });
          },
          readreports(id){
            axios
            .put('http://localhost:5000/sponsor/campaign/'+id+'/complete',{},
                 {headers: {Authorization: this.auth}})
            .then((response) => {
                console.log(response);
                alert('Campaign Finished Successfully');
                this.$router.go(0);
              })
            .catch((error) => {
                alert('Campaign Finishing Failed! Reason: ' + response.data.message +' Please try again');
                console.log(error);
            });
          },
          viewcampaign(id){
            this.$router.push({ name: 'ViewCampaignPublicPage', params: { campaign_id: id } });
          },
          readreport(userids){
            this.$router.push({name: 'AdminReportsCampaignPage', params: {campaign_id: userids}});
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
      this.$router.push({ name: 'LoginPage' });
    }
    if (this.role != 'Admin') {
      this.$router.push({ name: 'LoginPage' });
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





</style>