<script setup>
import axios from 'axios';
import Topbar from '../../components/Topbar.vue'
</script>


<template>
  <div>
    <Topbar />
  </div>

<div class="paymentpage">

  <div class="container1">
  <div class="card cart">
    <label class="title">CHECKOUT</label>
    <div class="steps">
      <div class="step">
        <div class="promo">
          <span>Add Money</span>
          <form class="form">
            <input class="input_field" placeholder="Enter a Amount of Money" type="text" v-model="money"/>
          </form>
        </div><hr>
        <div>
          <span>PAYMENT METHOD</span>
          <div>
            <p>Visa</p>
            <p>**** **** **** 4243</p>
          </div>
          <div style="display: flex; gap: 20px;">
            <p>Or</p>
            <p style="display: flex;"><span class="mdi mdi-pandora"></span>Paypal</p>
            <p style="display: flex;"><span class="mdi mdi-google"></span>Pay</p>
            <p style="display: flex;"><span class="mdi mdi-apple"></span>Pay</p>
          </div>
        </div>
        <div class="payments">
          <span>PAYMENT</span>
          <div class="details">
            <div style="display: flex; justify-content: space-between;">
              <span>Subtotal:</span>
              <span class="value">&#8377; {{ money }}</span>
            </div>
            <div style="display: flex; justify-content: space-between;">
              <span>Platform Charge:</span>
              <span class="value">&#8377; {{ charge }}</span>
            </div>   
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="card checkout">
    <div class="footer">
      <label class="price">&#8377; {{ finalmoney }} </label>
      <button @click="validate" class="checkout-btn">Checkout</button>
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
  name: 'PaymentPage',
  data() {
    return {
      money: 0,
      auth:'',
      campaign_id: '',
      userrole: '',
      finalmoney: 0,
      charge: 0

    }
  },
  methods: {
    validate(){
      if(this.money <= 0){
        alert("Please Enter a Amount of Money");
      }
      else{
        this.processpayment();
      }
    },
    calculateValues(value) { 
      this.charge = value * 0.05; 
      this.finalmoney = parseFloat(value) + this.charge; },
    processpayment(){
      axios 
            .put('http://localhost:5000/sponsor/campaign/'+this.campaign_id+'/addbudget', {
              budget: this.money,
              charge: this.charge,
            }, {
              headers: {
                'Authorization': this.auth
              }
            })
            .then((response) => {
              console.log("Response Block", response);
              alert("Payment Successful");
              this.$router.go(-1);
            })
            .catch((error) => {
              console.log("Error Block", error);
              alert("Payment Failed");
              this.$router.go(-1);
            });
    }
    
  },
  computed: {
    
  },
  watch: {
    money(newValue) { this.calculateValues(newValue); }
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
  }
}
</script>

<style scoped>

.paymentpage {
  align-self: center;
  margin-top: 40px;
  margin-bottom: 40px;
  justify-content: center;
  align-items: center;
  border-radius: 10px;
  border-top-left-radius: 22px;
  border-top-right-radius: 22px;
  min-height: 71vh;
}


.container1 {
  display: grid;
  grid-template-columns: auto;
  gap: 0px;

}

hr {
  height: 1px;
  background-color: #2e2e2e; /* Dark gray line */
  border: none;
}

.card {
  width: 400px;
  background: #1c1c1c; /* Dark background for a professional look */
  box-shadow:
    0px 187px 75px rgba(0, 0, 0, 0.01),
    0px 105px 63px rgba(0, 0, 0, 0.05),
    0px 47px 47px rgba(0, 0, 0, 0.09),
    0px 12px 26px rgba(0, 0, 0, 0.1),
    0px 0px 0px rgba(0, 0, 0, 0.1);
}

.title {
  width: 100%;
  height: 40px;
  position: relative;
  display: flex;
  align-items: center;
  padding-left: 20px;
  border-bottom: 1px solid #2e2e2e; /* Dark gray */
  font-weight: 700;
  font-size: 11px;
  color: #ffffff; /* White text */
}

/* Cart */
.cart {
  border-radius: 19px 19px 0px 0px;
}

.cart .steps {
  display: flex;
  flex-direction: column;
  padding: 20px;
}

.cart .steps .step {
  display: grid;
  gap: 10px;
}

.cart .steps .step span {
  font-size: 13px;
  font-weight: 600;
  color: #ffffff; /* White text */
  margin-bottom: 8px;
  display: block;
}

.cart .steps .step p {
  font-size: 11px;
  font-weight: 600;
  color: #bbbbbb; /* Light gray text */
}

/* Promo */
.promo form {
  display: grid;
  grid-template-columns: 1fr 80px;
  gap: 10px;
  padding: 0px;
}

.input_field {
  width: auto;
  height: 36px;
  padding: 0 0 0 12px;
  border-radius: 5px;
  outline: none;
  border: 1px solid #2e2e2e; /* Dark gray */
  background-color: #333333; /* Dark input background */
  color: #ffffff; /* White text */
  transition: all 0.3s cubic-bezier(0.15, 0.83, 0.66, 1);
}

.input_field:focus {
  border: 1px solid transparent;
  box-shadow: 0px 0px 0px 2px #555555; /* Light gray focus */
  background-color: #333333;
}

.promo form button {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  padding: 10px 18px;
  gap: 10px;
  width: 100%;
  height: 36px;
  background: #555555; /* Medium gray button */
  box-shadow:
    0px 0.5px 0.5px #555555,
    0px 1px 0.5px rgba(239, 239, 239, 0.5);
  border-radius: 5px;
  border: 0;
  font-weight: 600;
  font-size: 12px;
  line-height: 15px;
  color: #ffffff; /* White text */
  transition: all 0.3s cubic-bezier(0.15, 0.83, 0.66, 1);
}

/* Checkout */
.payments .details {
  display: flex;
  flex-direction: column;
  padding: 0px;
  gap: 5px;
  justify-content: space-between;
}

.payments .details span:nth-child(odd) {
  font-size: 12px;
  font-weight: 600;
  color: #ffffff; /* White text */
}

.payments .details span:nth-child(even) {
  font-size: 13px;
  font-weight: 600;
  color: #bbbbbb; /* Light gray text */
}

.checkout .footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px 10px 10px 20px;
  border-radius: 0px 0px 19px 19px;
  background-color: #2e2e2e; /* Dark gray background */
  border: 3px solid #1c1c1c;
}

.price {
  font-size: 22px;
  color: #ffffff; /* White text */
  font-weight: 900;
}

.checkout .checkout-btn {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  width: 150px;
  height: 36px;
  background: #555555; /* Medium gray button */
  border-radius: 7px;
  border: 1px solid #2e2e2e; /* Dark gray border */
  color: #ffffff; /* White text */
  font-size: 13px;
  font-weight: 600;
  transition: all 0.3s cubic-bezier(0.15, 0.83, 0.66, 1);
}

.checkout .checkout-btn:hover {
  background-color: #777777; /* Slightly lighter gray on hover */
}

</style>