<script setup>
import Topbar from '../../components/Topbar.vue'

</script>

<template>
  <div>
    <Topbar />
  </div>
  <div class="dash">
        <div class="chats">  
            
          <div class="inactivesponsor">
          <div class="heading" style="display: flex; justify-content: space-between;">
              <h2>Chat Messages</h2>
              <button class="btn btn-primary" @click="refresh" style="border-radius: 20px;"><span class="mdi mdi-refresh"></span> Refresh</button>
          </div>
          <section class="table__body">
            <table>
              <thead>
                    <tr>
                        <th> Msg No.</th>
                        <th> Time Sent</th>
                        <th> Sender </th>
                        <th> Message </th>
                    </tr>
                </thead>
                <tbody>
                  <tr v-for="(message, index) in messages" :key="message.id">
                      <td>{{ index+1 }}</td>
                      <td>{{ message.date_created}}</td>
                      <td v-if="checkname(message.sender_name)" > You </td>
                      <td v-else> {{ message.sender_name }} </td>
                      <td>{{ message.message }}</td>
                  </tr>
                </tbody>
            </table>
        </section>
        
      </div>
      <div class="form" style="display: flex; flex-direction: column; gap: 10px; ">
        <div class="totals" align="left">
          <span class="badge badge-pill" style="border-radius:30px;background:rgb(0, 88, 150)"> Total Messages: {{ messages.length }} </span>
        </div>
        <div class="input-group mb-3">
        <label for="message" style="margin-right: 14px; margin-top: 5px;">Message:</label>
        <input type="text" class="form-control" placeholder="Enter Your Message" aria-label="Enter your Message" aria-describedby="button-addon2" v-model="message"  style="border-top-left-radius: 10px; border-bottom-left-radius: 10px;">
        <button class="btn btn-primary" type="button" id="button-addon2" @click="sendmessage" ><span class="mdi mdi-send"></span> Send</button>
        </div>
      </div>
        </div>
        <div class="negociations">
          <div class="negociationcont">
            <h3><strong>Job Details</strong></h3>
            <h5><strong>Job Title:</strong> {{ ad.title }}</h5>
            <h5 style="text-align: justify;"><strong>Job Description:</strong> {{ ad.description }}</h5>
            <h5><strong>Job Campaign:</strong> {{ ad.campaign }}</h5>
            <h5><strong>Job Amount Offered:</strong> &#8377{{ ad.baseprice }}</h5>
            <h5><strong>Job Preferred Platforms:</strong></h5>
            <h5><span class="mdi mdi-youtube" v-if="ad.preferedplatforms.youtube" ></span><span class="mdi mdi-instagram"  v-if="ad.preferedplatforms.instagram" ></span>
          <span class="mdi mdi-facebook" v-if="ad.preferedplatforms.facebook" ></span><span class="mdi mdi-twitter"  v-if="ad.preferedplatforms.twitter" ></span>
          <span class="mdi mdi-at"  v-if="ad.preferedplatforms.thread"  ></span><span class="mdi mdi-music-note-outline"  v-if="ad.preferedplatforms.tiktok" ></span>
          <span class="mdi mdi-twitch"  v-if="ad.preferedplatforms.twitch" ></span><span class="mdi mdi-kickstarter"  v-if="ad.preferedplatforms.kick" ></span>
          <span class="mdi mdi-snapchat"  v-if="ad.preferedplatforms.snapchat"  ></span><span class="mdi mdi-linkedin"  v-if="ad.preferedplatforms.linkedin" ></span></h5>
            <h5><strong>Job Created On:</strong> {{ ad.date_created }}</h5>
            <h5><strong>Job Status:</strong> {{ ad.status }}</h5>
            <h5><strong>Job Negociated Amount:</strong> <u>&#8377 {{ ad.negociatedprice }}</u></h5>
            <h6 v-if="ad.status!='Approved'"> Negociation Amount:</h6>
            <div class="input-group mb-3" v-if="ad.status!='Approved'">
                 
                  <span class="input-group-text">&#8377</span>
                  <input type="text" class="form-control" aria-label="Dollar amount (with dot and two decimal places)" placeholder="Enter Your Negociation Amount" v-model="price">
            </div>
            <div id="actions" v-if="ad.status!='Approved'">
                        <button type="button" class="btn btn-primary" style="border-radius: 10px; font-size: 15px;" v-tooltip.bottom="'Send Negociation'" @click="sendnegociation"><span class="mdi mdi-cash-fast"></span> Negociate</button>
		                    <button type="button" class="btn btn-success" style="border-radius: 10px;font-size:15px;"v-tooltip.bottom="'Accept Negociation'" @click="approverequest" ><span class="mdi mdi-cash-check"></span> Accept</button>
		                    <button type="button" class="btn btn-danger" style="border-radius: 10px;font-size:15px;"v-tooltip.bottom="'Reject Negociation'" @click="rejectrequest" ><span class="mdi mdi-cash-off"></span> Reject</button>
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
  name: 'NegociationSponsor',
  data() {
    return {
      messages: [ ],
        auth:'',
        username: '',
        userid: '',
        message: '',
        jobid: '',
        ad: {},
        adrequest: {},
        price: '',
  };
    
  },
  methods: {
    getmessages(){
      axios
          .get('http://localhost:5000/influencer/'+this.jobid+'/chats',{
              headers: { Authorization: this.auth }})
          .then(response => {
              console.log(response.data);
              this.messages = response.data;
              this.messages = response.data;
              if(response.status == 202){
                alert('Error: '+ response.data.message);
                this.$router.push('/InfluencerDash');
              }
          })
          .catch(error => {
              console.log(error);
          });
    },
    sendmessage(){
      axios
          .post('http://localhost:5000/influencer/'+this.jobid+'/chats',{
              message: this.message,
              sender: this.userid,
          },{
              headers: { Authorization: this.auth }})
          .then(response => {
              if(response.status == 200){
                  alert('Message Sent');
                  this.message = '';
                  this.getmessages();
              }
              else{
                  alert('Message not sent');
              }
              
          })
          .catch(error => {
              console.log(error);
          });

    },
   
    sendnegociation(){
        axios
        .post('http://localhost:5000/adrequest/'+this.jobid+'/negociation',{
              price: this.price,
          },{
              headers: { Authorization: this.auth }})
          .then(response => {
              if(response.status == 200){
                  alert('Negociation Sent');
                  this.price = '';
                  this.getad();
              }
              else{
                  alert('Negociation not sent Reason: '+ response.data.message);
              }
              
          })
          .catch(error => {
              console.log(error);
          });
    },
          approverequest(){
            axios
            .put('http://localhost:5000/influencer/adrequest/'+this.jobid+'/accept',{},
                 {headers: {Authorization: this.auth}})
            .then((response) => {
                console.log(response);
                alert('Ad Request Approved Successfully');
                this.$router.push('/InfluencerDash');
              })
            .catch((error) => {
                alert('Ad Request Approval Failed! Reason: ' + response.data.message +' Please try again');
                console.log(error);
            });
          },
          rejectrequest(){
            axios
            .put('http://localhost:5000/influencer/adrequest/'+this.jobid+'/reject',{},
                 {headers: {Authorization: this.auth}})
            .then((response) => {
                console.log(response);
                alert('Ad Request Rejected Successfully');
                this.$router.push('/InfluencerDash');
              })
            .catch((error) => {
                alert('Ad Request Rejected Failed! Reason: ' + response.data.message +' Please try again');
                console.log(error);
            });
          },

    checkname(name){
      if(name==this.username){
        return true;
      }
      else{
        return false;
      }
    },
    getad(){
      axios
          .get('http://localhost:5000/adrequest/'+this.jobid+'/ad',{
              headers: { Authorization: this.auth }})
          .then(response => {
              console.log(response.data);
              this.ad = response.data;
          })
          .catch(error => {
              console.log(error);
          });
    },
    refresh(){
      this.getmessages();
      this.getad();
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
    this.username = localStorage.getItem('username');
    this.userid = localStorage.getItem('userid');
    this.jobid = this.$route.params.request_id;
    if (!this.auth) {
      this.$router.push({ name: 'LoginPage' });
    }
    if(localStorage.getItem('userrole')!='Influencer'){
        alert('You are not authorized to view this page');
        this.$router.go(-1);
    }
    this.getmessages();
    this.getad();
  }
}
</script>

<style scoped>
.dash {
  display: flex;
  align-self: center;
  min-height: 100vh;
  background-color: #f3f4f6;
  border: 5px solid #080808;
  width:80%;
  margin:30px;
  flex-direction: row;
  flex-wrap: wrap;

}

.negociations {
  display: flex;
  flex-direction: column;
  width: 40%;
  height: 100%;
  background-color: #f3f4f6;
  padding: 10px;
  flex-wrap: wrap;

}

.negociationcont {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100vh;
  background-color: #f3f4f6;
  
  padding: 10px;
  flex-wrap: wrap;
  justify-content: center;
  gap: 10px;
}


.chats {
  display: flex;
  background-color: #f3f4f6;
  border-right: 4px dotted #080808;
  width:60%;
  padding: 10px;
  flex-direction: column;
  flex-wrap: wrap;

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
  gap: 20px;
  flex-wrap: wrap;
  justify-content: space-evenly;
  align-self: center;
}
table {
  width: 100%;
  table-layout: auto;
  max-height: 100vh;
}

table, th, td {
  border-collapse: collapse;
  text-align: left;
  padding: 1rem;
  min-width: 100px;
}
.form {
  display: flex;
  width: 100%;
  padding: 10px;
  background-color: #f3f4f6;
 
  align-items: bottom;

}

@media (max-width: 1300px) {
  table td{
    min-height: 80vh;
  }
  #actions{
    display: flex;
    flex-direction: row;
    justify-content: space-evenly;
    margin-right: 0px;
    gap: 25px;
    font-size: larger;
  }
  .dash{
    width: 90%;
    display: flex;
    flex-direction: column;
    padding: 0px;
    
  }
  .chats{
    width: 100%;
    display: flex;
    flex-direction: column;
    border-right: 0px;
    border-bottom: dotted 4px #080808;
    padding: 10px;
  }
  .negociations{
    width: 100%;
    display: flex;
    flex-direction: column;
    
  }
  .negociationcont{
    width: 100%;
    display: flex;
    flex-direction: column;
    
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

.chats .table__body {
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

.chats .inactivesponsor .table__body {
  display: flex;
  gap: 20px;
  border-radius: 30px;
  flex-wrap: wrap;
  overflow-x: auto;
  overflow-y: auto;
  width: 100%;
  margin: .8rem auto;
  border-radius: .6rem;
}

.chats .inactivesponsor{
  display: flex;
  flex-direction: column;
  
  width: 100%;
  
  min-height: 88vh;
  max-height: 85vh;
  

}

</style>