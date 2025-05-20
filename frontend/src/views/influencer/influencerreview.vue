<script setup>
import Topbar from '../../components/Topbar.vue'

</script>

<template>
  <div>
    <Topbar />
  </div>
  <div class="reportheader">
                    <h1>@ {{ username }} Reviews's</h1>
                </div>
  <div class="reportbody">
        <div class="reports" v-for="(Data, index) in data" :key="data.id">
            <div class="report">
                <div class="reportcontentheader">
                        <h4>Review No {{ index + 1}}</h4>
                </div>
                <div class="reportcontent">
                    <div class="reportcontentheader">
                        <h4>Reviewed on:</h4>
                        <h5>{{Data.date_created}}</h5>
                    </div>
                </div>
                <div class="reportcontent">
                    <div class="reportcontentheader">
                        <h4>Review Ratings:</h4>
                        <h5>{{Data.rating}}</h5>
                    </div>
                </div>
                <div class="reportcontent">
                    <div class="reportcontentheader">
                        <h4>Submitted by:</h4>
                        <h5>{{Data.submitted_by}}</h5>
                    </div>
                </div>
                <div class="reportcontent">
                    <div class="reportcontentheader">
                        <h4>Review:</h4>
                        <h5 style="text-align: justify;">{{Data.review}}</h5>
                    </div>
                </div>
                
            </div>
        </div>
  </div>
  <div class="reports" v-if="data.length==0">
            <div class="report">
                <div class="reportcontentheader" style="align-items: center; justify-content: center; align-self: center;">
                        <h4> No Reviews yet!</h4>
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
  name: 'AdminReports',
  data() {
    return {
            auth:'',
            users_id:'',
            data:[],
            username:'',
    }
  },
  methods: {
    getdata() {
      axios.get('http://localhost:5000/influencer/reviews', {
        headers: {
          'Authorization':  this.auth
        }
      })
      .then(response => {
        console.log(response);
        this.data = response.data.data;
        this.username = response.data.username;
      })
      .catch(error => {
        console.log(error);
      })
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
            this.users_id = this.$route.params.users_id;
            this.getdata();
  }
}
</script>

<style scoped>

.reportheader {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 20px;
}

.reportbody {
    display: flex;
    width: 60%;
    margin-top: 20px;
    align-self: center;
    padding: 10px;
    flex-direction: column;
    flex-wrap: wrap;
    gap: 10px;
    overflow-y:    auto; /* Enable vertical scrolling */
}

@media screen and (max-width: 1000px) {
    .reportbody {
        width: 100%;
    }
}

.reports {
    display: flex;
    flex-direction: column;
    flex-wrap: wrap;
    padding: 10px;
    gap: 10px;
}

.report {
    display: flex;
    flex-direction: column;
    flex-wrap: wrap;
    border: 4px solid #0b0a0a;
    padding: 10px;
    margin: 10px;
    border-radius: 20px;
    background-color: aliceblue;
    gap: 10px;
}

.reportcontentheader {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    gap:20px
}

h4 {
    font-size: 20px;
    font-weight: bold;
    color: #000;
}
</style>