<script setup>
import Topbar from '../../components/Topbar.vue'
</script>

<template>
  <div>
    <Topbar />
  </div>
  <div style="margin-top: 30px;margin-bottom: 20px; align-self: center;" >
              <h1><span class="mdi mdi-wallet-bifold"></span> {{ username }}'s Wallet</h1>
    </div>
    <div class="dashboard">
      <div class="sponsornav">
        <div class="square sunset-gradient"> 
                <h5><span class="mdi mdi-wallet"></span></h5>
                <h5>Wallet Amount</h5> 
                <h5 v-if="userrole!='Sponsor'" >&#8377 {{wallet}}</h5> 
        </div> 
        <div style="display: flex; flex-wrap: wrap; flex-direction: column; gap: 20px; padding: 5px;">
            <button type="submit" class="btn btn-success" style="font-size:20px; border-radius:20px;"  @click="createcampaign">
                <span class="mdi mdi-account-cash"></span>
                                  Withdraw Money
        </button>
        <button type="submit" class="btn btn-success" style="font-size:20px; border-radius:20px; " @click="create_csv">
        <span class="mdi mdi-table-arrow-right"></span>
                                  Export Transactions
        </button>
        </div>
      </div>
      
      <div class="activesponsor"  >
        <div class="heading">
              <h2>Transactions:</h2>
        </div>
        <section class="table__body" v-if=" transactions.length>0 " >
            <table>
                <thead>
                    <tr>
                        <th> S.No <span class="mdi mdi-arrow-down"></span></th>
                        <th> Transaction Type <span class="mdi mdi-cash-register"></span></th>
                        <th> Date Created <span class="mdi mdi-calendar-range"></span></th>
                        <th> Amount &#8377 </th>
                        <th> Description <span class="mdi mdi-text-box"></span></th>
                    </tr>
                </thead>
                <tbody>
                  <tr v-for="(Transaction, index) in transactions" :key="transactions.id">
                      <td>{{ index + 1}}</td>
                      <td>{{ Transaction.transaction_type }}</td>
                      <td>{{ Transaction.date_created }}</td>
                      <td>&#8377 {{ Transaction.amount }}</td>
                      <td>{{ Transaction.description }}</td>
                  </tr>
                </tbody>
            </table>
        </section>
        <div class="totals" align="right" v-if=" transactions.length>0 " >
          <span class="badge badge-pill" style="border-radius:30px;background:rgb(0, 88, 150)"> Total Transactions: {{ transactions.length }} </span>
        </div>
        <div class="notrans" style="justify-content: center; align-self: center;">
          <h3 v-if=" transactions.length==0 " >No Transactions Yet!</h3>
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
  name: 'Wallet',
  data() {
    return {
            transactions: [],
            auth: '',
            username: '',
            wallet: '',
            userrole: '',
    }
  },
  methods: {
            getdatasponsor(){
                axios
                    .get('http://localhost:5000/sponsor/wallet', {
                        headers: {
                            'Authorization': this.auth}})
                    .then(response => {
                        this.transactions = response.data;
                       
                    })
                    .catch(error => {
                        console.log(error);
                    });
            },
            getdataadmin(){
                axios
                    .get('http://localhost:5000/admin/wallet', {
                        headers: {
                            'Authorization': this.auth}})
                    .then(response => {
                        this.transactions = response.data.transactions;
                        this.wallet = response.data.balance;
                    })
                    .catch(error => {
                        console.log(error);
                    });
                },
            getdatainfluencer(){
                axios
                    .get('http://localhost:5000/influencer/wallet', {
                        headers: {
                            'Authorization': this.auth}})
                    .then(response => {
                        this.transactions = response.data.transactions;
                        this.wallet = response.data.balance;
                    })
                    .catch(error => {
                        console.log(error);
                    });
                },
          async create_csv(){
              const res = await fetch('http://localhost:5000/createcsvtransaction',
                 {headers: {Authorization: this.auth}});
              const task_id = (await res.json()).task_id;

              const interval = setInterval(async () => {
                  const res = await fetch(`http://localhost:5000/getcsvtransaction/${task_id}`,
                      {headers: {Authorization: this.auth}}
                  )
                  if (res.ok){
                    console.log('Data is Ready for Download')
                    window.open(`http://localhost:5000/getcsvtransaction/${task_id}`)
                    alert('Transactions Data is Ready for Download')
                    clearInterval(interval)
                  }
              }, 100);
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
    this.userrole = localStorage.getItem('userrole');
    if(this.auth == null){
      this.$router.push({ name: 'Login' });
    }
    if(localStorage.getItem('userrole') == 'Sponsor'){
        this.getdatasponsor();
    }
    if(localStorage.getItem('userrole') == 'Influencer'){
        this.getdatainfluencer();
    }
    if(localStorage.getItem('userrole') == 'Admin'){
        this.getdataadmin();
    }
  }
}
</script>

<style scoped>
.dashboard {
  display: flex;
  flex-wrap: wrap;
  flex-direction: column;
  gap: 5px;
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
  justify-content: space-between;
}

.dashboard .sponsornav h5 {
  display: flex;
  flex-direction: row;
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

.square { 
    width: 120px; 
    height: 120px; 
    display: flex; 
    flex-direction: column; 
    justify-content: center; 
    align-items: center; 
    width: 20%;
    color: rgb(15, 15, 15); 
    border-radius: 10px; 
    padding: 50px; 
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); 
    text-align: center; 
}

.sunset-gradient { background: linear-gradient(45deg, #FF7E5F, #FEB47B); /* Sunset orange and light pink */ color: white; }


</style>