
<template>
<div class="navig">
<LandingTopbar />
</div>

<div class="container">
	<div class="screen">
		<div class="screen__content">
			<form class="login">
				<div class="login__field">
					<i class="login__icon fas fa-user"></i>
					<input type="text" class="login__input" placeholder="User name / Email">
				</div>
				<div class="login__field">
					<i class="login__icon fas fa-lock"></i>
					<input type="password" class="login__input" placeholder="Password">
				</div>
				<button class="button login__submit">
					<span class="button__text">Log In Now</span>
					<i class="button__icon fas fa-chevron-right"></i>
				</button>				
			</form>
			<div class="social-login">
				<h3>log in via</h3>
				<div class="social-icons">
					<a href="#" class="social-login__icon fab fa-instagram"></a>
					<a href="#" class="social-login__icon fab fa-facebook"></a>
					<a href="#" class="social-login__icon fab fa-twitter"></a>
				</div>
			</div>
		</div>
		<div class="screen__background">
			<span class="screen__background__shape screen__background__shape4"></span>
			<span class="screen__background__shape screen__background__shape3"></span>		
			<span class="screen__background__shape screen__background__shape2"></span>
			<span class="screen__background__shape screen__background__shape1"></span>
		</div>		
	</div>
</div>
</template>
<script setup>
import Button from 'primevue/button';
import Checkbox from 'primevue/checkbox';
import InputText from 'primevue/inputtext';
import LandingTopbar from '../components/LandingTopbar.vue'
import { ref } from 'vue';

const checked1 = ref(true);
</script>
<style>
* {
	box-sizing: border-box;
	margin: 0;
	padding: 0;	
	font-family: Raleway, sans-serif;
}

body {
	background: linear-gradient(90deg, #C7C5F4, #776BCC);		
}

.container {
	display: flex;
	align-items: center;
	justify-content: center;
	min-height: 100vh;
}

.screen {		
	background: linear-gradient(90deg, #5D54A4, #7C78B8);		
	position: relative;	
	height: 600px;
	width: 360px;	
	box-shadow: 0px 0px 24px #5C5696;
}

.screen__content {
	z-index: 1;
	position: relative;	
	height: 100%;
}

.screen__background {		
	position: absolute;
	top: 0;
	left: 0;
	right: 0;
	bottom: 0;
	z-index: 0;
	-webkit-clip-path: inset(0 0 0 0);
	clip-path: inset(0 0 0 0);	
}

.screen__background__shape {
	transform: rotate(45deg);
	position: absolute;
}

.screen__background__shape1 {
	height: 520px;
	width: 520px;
	background: #FFF;	
	top: -50px;
	right: 120px;	
	border-radius: 0 72px 0 0;
}

.screen__background__shape2 {
	height: 220px;
	width: 220px;
	background: #6C63AC;	
	top: -172px;
	right: 0;	
	border-radius: 32px;
}

.screen__background__shape3 {
	height: 540px;
	width: 190px;
	background: linear-gradient(270deg, #5D54A4, #6A679E);
	top: -24px;
	right: 0;	
	border-radius: 32px;
}

.screen__background__shape4 {
	height: 400px;
	width: 200px;
	background: #7E7BB9;	
	top: 420px;
	right: 50px;	
	border-radius: 60px;
}

.login {
	width: 320px;
	padding: 30px;
	padding-top: 156px;
}

.login__field {
	padding: 20px 0px;	
	position: relative;	
}

.login__icon {
	position: absolute;
	top: 30px;
	color: #7875B5;
}

.login__input {
	border: none;
	border-bottom: 2px solid #D1D1D4;
	background: none;
	padding: 10px;
	padding-left: 24px;
	font-weight: 700;
	width: 75%;
	transition: .2s;
}

.login__input:active,
.login__input:focus,
.login__input:hover {
	outline: none;
	border-bottom-color: #6A679E;
}

.login__submit {
	background: #fff;
	font-size: 14px;
	margin-top: 30px;
	padding: 16px 20px;
	border-radius: 26px;
	border: 1px solid #D4D3E8;
	text-transform: uppercase;
	font-weight: 700;
	display: flex;
	align-items: center;
	width: 100%;
	color: #4C489D;
	box-shadow: 0px 2px 2px #5C5696;
	cursor: pointer;
	transition: .2s;
}

.login__submit:active,
.login__submit:focus,
.login__submit:hover {
	border-color: #6A679E;
	outline: none;
}

.button__icon {
	font-size: 24px;
	margin-left: auto;
	color: #7875B5;
}

.social-login {	
	position: absolute;
	height: 140px;
	width: 160px;
	text-align: center;
	bottom: 0px;
	right: 0px;
	color: #fff;
}

.social-icons {
	display: flex;
	align-items: center;
	justify-content: center;
}

.social-login__icon {
	padding: 20px 10px;
	color: #fff;
	text-decoration: none;	
	text-shadow: 0px 0px 8px #7875B5;
}

.social-login__icon:hover {
	transform: scale(1.5);	

}
</style>



<div class="adsbody">
	<div class="card text-bg-light mb-3" style="max-width: 20rem;" v-for="(ad, index) in ads" :key="ad.id">
		<div class="card-header" align="center">Ad Request</div>
		<div class="card-body">
		  <h5 class="card-title">{{ad.title}}</h5>
		  <h6>Base Price: &#8377 {{ ad.baseprice }}</h6>
		  <h6>Date Created: {{ ad.date_created }}</h6>
		  <h6>Preferred Platforms:</h6>
		  <h6><span class="mdi mdi-youtube" v-if="ad.preferedplatforms.youtube" ></span><span class="mdi mdi-instagram"  v-if="ad.preferedplatforms.instagram" ></span>
					<span class="mdi mdi-facebook" v-if="ad.preferedplatforms.facebook" ></span><span class="mdi mdi-twitter"  v-if="ad.preferedplatforms.twitter" ></span>
					<span class="mdi mdi-at"  v-if="ad.preferedplatforms.thread"  ></span><span class="mdi mdi-music-note-outline"  v-if="ad.preferedplatforms.tiktok" ></span>
					<span class="mdi mdi-twitch"  v-if="ad.preferedplatforms.twitch" ></span><span class="mdi mdi-kickstarter"  v-if="ad.preferedplatforms.kick" ></span>
					<span class="mdi mdi-snapchat"  v-if="ad.preferedplatforms.snapchat"  ></span><span class="mdi mdi-linkedin"  v-if="ad.preferedplatforms.linkedin" ></span></h6>
		  <h6>Description / Requirements</h6>
		  <p class="card-text" style="text-align: justify;">{{ad.description}}</p>
		  <label for="badge"> Ad Status:</label>
		  <span class="badge badge-pill" style="border-radius:30px;background:rgb(0, 88, 150); margin-left: 10px;" v-if="ad.status=='Open'">{{ ad.status }}</span>
		  <span class="badge badge-pill" style="border-radius:30px;background:rgb(76, 175, 80);  margin-left: 10px;" v-if="ad.status=='Approved'">  {{ ad.status }}</span>
		  <span class="badge badge-pill" style="border-radius:30px;background:rgb(244, 67, 54);  margin-left: 10px;" v-if="ad.status=='Rejected'"> {{ ad.status }}</span>
		  <span class="badge badge-pill" style="border-radius:30px;background:rgb(255, 152, 0);  margin-left: 10px;" v-if="ad.status=='Requested'"> {{ ad.status }}</span>
		  <span class="badge badge-pill" style="border-radius:30px;background:rgb(33, 150, 243);  margin-left: 10px;" v-if="ad.status=='In Progress'"> {{ ad.status }}</span>
		  <span class="badge badge-pill" style="border-radius:30px;background:rgb(0, 128, 128); margin-left: 10px;" v-if="ad.status=='Completed'"> {{ ad.status }}</span>
		  <span class="badge badge-pill" style="border-radius:30px;background:rgb(128, 0, 128);  margin-left: 10px;" v-if="ad.status=='Pending'">{{ ad.status }}</span>
		  <span class="badge badge-pill" style="border-radius:30px;background:rgb(184, 134, 11);  margin-left: 10px;" v-if="ad.status=='Negotiated'"> {{ ad.status }}</span>
		</div>
		<div class="card-footer" style="display: flex; gap: 5px;">
		  <button type="button" class="btn btn-primary" style="border-radius: 10px;font-size:15px;"v-tooltip.bottom="'View Ad'"><span class="mdi mdi-advertisements"></span></button>
		  <button type="button" class="btn btn-warning" style="border-radius: 10px;font-size:15px;"v-tooltip.bottom="'Edit Ad'"><span class="mdi mdi-comment-edit"></span></button>
		  <button type="button" class="btn btn-danger" style="border-radius: 10px;font-size:15px;"v-tooltip.bottom="'Delete Ad'"><span class="mdi mdi-delete-forever"></span></button>
		  <button type="button" class="btn btn-success" style="border-radius: 10px;font-size:15px;"v-tooltip.bottom="'Hire Influencer'"><span class="mdi mdi-account-supervisor"></span></button>
		  <button type="button" class="btn btn-primary" style="border-radius: 10px;font-size:15px;"><span class="mdi mdi-comment-text-multiple"></span></button>
		</div>
	  </div>
   </div>