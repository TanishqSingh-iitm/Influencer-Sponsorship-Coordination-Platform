<script setup>
import Topbar from '../../components/Topbar.vue'

</script>

<template>
<div >
    <Topbar />
</div>
    <h1 class="display-1" style="margin-left: 100px;">
        Delete Sponsor Account
    </h1>
    <div class="container">
    <p class="f-3" style="font-size:23px;">Are you sure you want to delete your Sponsor Account with username <b>@ {{this.username}}</b>?</p>
    
    <form>
        <div class="form-group">
            <label for="pass" class="form-label" style="font-size: 25px;">Your Password:</label>
            <input type="text" name="pass" placeholder="Type your Password to Confirm this deletion!" id="pass" class="form-control" required style="border-radius:60px" v-model="this.password">
        </div><br>
        <button type="submit" class="btn btn-danger"  style="font-size:15px; border-radius:30px" @click.prevent="deleteaccount">
            <span class="mdi mdi-delete-forever"></span>
            Confirm Delete
        </button>
    </form>
    </div>
    <div style="background-color: #333; color: white; text-align: center; position: relative; bottom: 0; left: 0; width: 100%; font-family: 'Doto', sans-serif; font-optical-sizing: auto; font-weight: 1000; font-style: normal; font-variation-settings: 'ROND' 100; font-size: 1.1rem; height: 50px;">
  <p align="center" style="margin: 0; line-height: 50px;">© 2024 | © 21F3001516 | Influencer Engagement Sponsor Coordination Platform | © CreativeMerge</p>
</div>
    </template>
    
    <script>
    import axios from 'axios';
    
    export default {
        data(){
            return{
                user_id: null,
                username: null,
                role: null,
                token: null,
                password: '',
            }
        },
        created(){
            this.user_id = localStorage.getItem('userid');
            this.token = localStorage.getItem('AuthToken');
            this.username = localStorage.getItem('username');
            if (!this.token) {
                this.$router.push('/login');
            }
        },
        methods: {
            deleteaccount(){
                axios
                .post(
                        `http://localhost:5000/sponsorprofile/deleteaccount/${this.user_id}`,
                            { pass: this.password },
                        {
                             headers: {
                                Authorization: this.token,
                            },
                            }         
                        )
                    .then(response => {
                    if(response.status==200){
                        localStorage.removeItem('AuthToken');
                        localStorage.removeItem('username');
                        localStorage.removeItem('userrole');
                        localStorage.removeItem('profilepic');
                        localStorage.removeItem('userid');
                        alert("Account Deleted Successfully");
                        this.$router.push('/login');
                    }
                    else{
                        alert(response.data.message);
                    }
                }).catch(error => {
                    console.log(error);
                });
            }
        }
    };
    </script>
    
    <style>
    .container {
        justify-content: start;
        justify-items: start;
        width: 100%;
        max-width: 1000px;
        margin-top: 20px;
        padding: 60px;
        border-style: solid;
        border-radius: 30px;
        background-color: #f0f0f0;
        margin-bottom: 100px;
    }
    </style>