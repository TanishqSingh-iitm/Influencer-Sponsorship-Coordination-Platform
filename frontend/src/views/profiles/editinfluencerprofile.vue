<script setup>
import Topbar from '../../components/Topbar.vue'
</script>

<template>
  <div>
    <Topbar />    
  </div>
  <div style="margin-top:20px">
    <h2 class="display-4 " align="center">Influencer Profile Edit Portal</h2>
  </div>
  <div class="registerform">
    <div class="logoavatar">
    <img src="../../assets/logo.png" alt="logo" class="avatar">
    </div>
    <form class="regis">
    <div class="form-group">
        <label for="username" class="form-label" style="font-size: 20px;">
            <span class="mdi mdi-account"></span> Username</label>
        <input type="text" name="username" placeholder="Type your Username" required class="form-control" style="border-radius: 60px; font-size: 15px;" v-model="username">
    </div><br>
    <div class="form-group">
        <label for="password" class="form-label" style="font-size: 20px;"><span class="mdi mdi-form-textbox-password"></span> Password</label>
        <input type="password" name="password" placeholder="Type your password" required class="form-control" style="border-radius: 60px; font-size: 15px;" v-model="password">
    </div><br>
    <div class="form-group">
        <label for="confirm_password" class="form-label" style="font-size: 20px;"><span class="mdi mdi-form-textbox-password"></span> Confirm Password</label>
        <input type="password" name="confirm_password" placeholder="Retype your password" required class="form-control" style="border-radius: 60px; font-size: 15px;" v-model="confirm_password">
    </div><br>
    <div class="form-group">
        <label for="name" class="form-label" style="font-size: 20px;"><span class="mdi mdi-card-text"></span> Influencer Name</label>
        <input type="text" name="name" placeholder="Type your Influencer Name" required class="form-control" style="border-radius: 60px; font-size: 15px;" v-model="name">
    </div><br>
    <div class="form-group">
        <label for="email" class="form-label" style="font-size: 20px;"><span class="mdi mdi-email"></span> Influencer E-mail</label>
        <input type="text" name="email" placeholder="Type your Email address (OPTIONAL)" class="form-control" style="border-radius: 60px; font-size: 15px;" v-model="email">
    </div><br>
    <div class="form-group">
        <label for="industry" class="form-label" style="font-size: 20px;"><span class="mdi mdi-domain"></span> Influencer Industry</label>
        <input type="text" name="industry" placeholder="Type your Working Industry" class="form-control" style="border-radius: 60px; font-size: 15px;" v-model="industry">
    </div><br>
    <div class="form-group">
        <label for="website" class="form-label" style="font-size: 20px;"><span class="mdi mdi-television-play"></span> Niche</label>
        <input type="text" name="website" placeholder="Type your Niche" class="form-control" style="border-radius: 60px; font-size: 15px;" v-model="niche">
    </div><br>
    <div class="form-group">
        <label for="Info" class="form-label" style="font-size: 20px;"><span class="mdi mdi-information-variant-circle"></span> Additonal Info or Bio</label>
        <input type="text" name="Info" placeholder="Type your Additional Information (OPTIONAL)" class="form-control" style="border-radius: 60px; font-size: 15px;" v-model="infor">
    </div><br>

    <label for="Info" class="form-label" style="font-size: 20px;">
        <span class="mdi mdi-monitor-cellphone-star"></span> Your Influence Presence</label>
    <div class="platforms">
        
        <div class="yt">
            <div class="input-group mb-3">
                <div class="input-group-text">
                    <input id="checking" class="form-check-input mt-0" type="checkbox" value="" aria-label="Checkbox for following text input" v-model="isyt">
                   
                </div>
                <span class="input-group-text" id="basic-addon2"><span class="mdi mdi-youtube"></span>Youtube</span>
                <input id="platin" type="text" placeholder="Followers No" class="form-control" aria-label="Text input with checkbox" v-model="ytfollowers" :disabled="!isyt">
                <input id="platin" type="text" placeholder="Link" class="form-control" aria-label="Text input with checkbox" v-model="ytlink" :disabled="!isyt">
            </div>
        </div>
        <div class="insta">
            <div class="input-group mb-3">
                <div class="input-group-text">
                    <input id="checking" class="form-check-input mt-0" type="checkbox" value="" aria-label="Checkbox for following text input" v-model="isinsta">
                   
                </div>
                <span class="input-group-text" id="basic-addon2"><span class="mdi mdi-instagram"></span>Instagram</span>
                <input id="platin" type="text" placeholder="Followers No" class="form-control" aria-label="Text input with checkbox" v-model="instafollowers" :disabled="!isinsta">
                <input id="platin" type="text" placeholder="Link" class="form-control" aria-label="Text input with checkbox" v-model="instalink" :disabled="!isinsta">
            </div>
        </div>
        <div class="x">
            <div class="input-group mb-3">
                <div class="input-group-text">
                    <input id="checking" class="form-check-input mt-0" type="checkbox" value="" aria-label="Checkbox for following text input" v-model="isx">
                   
                </div>
                <span class="input-group-text" id="basic-addon2"><span class="mdi mdi-twitter"></span>Twitter/X</span>
                <input id="platin" type="text" placeholder="Followers No" class="form-control" aria-label="Text input with checkbox" v-model="xfollowers" :disabled="!isx">
                <input id="platin" type="text" placeholder="Link" class="form-control" aria-label="Text input with checkbox" v-model="xlink" :disabled="!isx">
            </div>
        </div>
        <div class="thread">
            <div class="input-group mb-3">
                <div class="input-group-text">
                    <input id="checking" class="form-check-input mt-0" type="checkbox" value="" aria-label="Checkbox for following text input" v-model="isthread">
                   
                </div>
                <span class="input-group-text" id="basic-addon2"><span class="mdi mdi-at"></span>Threads</span>
                <input id="platin" type="text" placeholder="Followers No" class="form-control" aria-label="Text input with checkbox" v-model="threadfollowers" :disabled="!isthread">
                <input id="platin" type="text" placeholder="Link" class="form-control" aria-label="Text input with checkbox" v-model="threadlink" :disabled="!isthread">
            </div>
        </div>
        <div class="fb">
            <div class="input-group mb-3">
                <div class="input-group-text">
                    <input id="checking" class="form-check-input mt-0" type="checkbox" value="" aria-label="Checkbox for following text input" v-model="isfb">
                   
                </div>
                <span class="input-group-text" id="basic-addon2"><span class="mdi mdi-facebook"></span>Facebook</span>
                <input id="platin" type="text" placeholder="Followers No" class="form-control" aria-label="Text input with checkbox" v-model="fbfollowers" :disabled="!isfb">
                <input id="platin" type="text" placeholder="Link" class="form-control" aria-label="Text input with checkbox" v-model="fblink" :disabled="!isfb">
            </div>
        </div>
        <div class="tick">
            <div class="input-group mb-3">
                <div class="input-group-text">
                    <input id="checking" class="form-check-input mt-0" type="checkbox" value="" aria-label="Checkbox for following text input" v-model="istik">
                   
                </div>
                <span class="input-group-text" id="basic-addon2"><span class="mdi mdi-music-note-outline"></span>TikTok</span>
                <input id="platin" type="text" placeholder="Followers No" class="form-control" aria-label="Text input with checkbox" v-model="tikfollowers" :disabled="!istik">
                <input id="platin" type="text" placeholder="Link" class="form-control" aria-label="Text input with checkbox" v-model="tiklink" :disabled="!istik">
            </div>
        </div>
        <div class="kick">
            <div class="input-group mb-3">
                <div class="input-group-text">
                    <input id="checking" class="form-check-input mt-0" type="checkbox" value="" aria-label="Checkbox for following text input" v-model="iskick">
                   
                </div>
                <span class="input-group-text" id="basic-addon2"><span class="mdi mdi-kickstarter"></span>Kick</span>
                <input id="platin" type="text" placeholder="Followers No" class="form-control" aria-label="Text input with checkbox" v-model="kickfollowers" :disabled="!iskick">
                <input id="platin" type="text" placeholder="Link" class="form-control" aria-label="Text input with checkbox" v-model="kicklink" :disabled="!iskick">
            </div>
        </div>
        <div class="twitch">
            <div class="input-group mb-3">
                <div class="input-group-text">
                    <input id="checking" class="form-check-input mt-0" type="checkbox" value="" aria-label="Checkbox for following text input" v-model="istwitch">
                   
                </div>
                <span class="input-group-text" id="basic-addon2"><span class="mdi mdi-twitch"></span>Twitch</span>
                <input id="platin" type="text" placeholder="Followers No" class="form-control" aria-label="Text input with checkbox" v-model="twitchfollowers" :disabled="!istwitch">
                <input id="platin" type="text" placeholder="Link" class="form-control" aria-label="Text input with checkbox" v-model="twitchlink" :disabled="!istwitch">
            </div>
        </div>
        <div class="snap">
            <div class="input-group mb-3">
                <div class="input-group-text">
                    <input id="checking" class="form-check-input mt-0" type="checkbox" value="" aria-label="Checkbox for following text input" v-model="issnap">
                   
                </div>
                <span class="input-group-text" id="basic-addon2"><span class="mdi mdi-snapchat"></span>SnapChat</span>
                <input id="platin" type="text" placeholder="Followers No" class="form-control" aria-label="Text input with checkbox" v-model="snapfollowers" :disabled="!issnap">
                <input id="platin" type="text" placeholder="Link" class="form-control" aria-label="Text input with checkbox" v-model="snaplink" :disabled="!issnap">
            </div>
        </div>
        <div class="linkedin">
            <div class="input-group mb-3">
                <div class="input-group-text">
                    <input id="checking" class="form-check-input mt-0" type="checkbox" value="" aria-label="Checkbox for following text input" v-model="islinked">
                   
                </div>
                <span class="input-group-text" id="basic-addon2"><span class="mdi mdi-linkedin"></span>LinkedIn</span>
                <input id="platin" type="text" placeholder="Followers No" class="form-control" aria-label="Text input with checkbox" v-model="linkedfollowers" :disabled="!islinked">
                <input id="platin" type="text" placeholder="Link" class="form-control" aria-label="Text input with checkbox" v-model="linkedlink" :disabled="!islinked">
            </div>
        </div>
    </div><br>

    <div class="profile">
        <div class="form-group" id="haveprofile"><br>
            <input type="checkbox" class="form-check-input" name="profpic" id="prof" style="margin-top:5px; margin-right: 10px;" v-model="haveprofile">
            <label class="form-check-label" for="profpic" style="font-size: 15px; margin-bottom:5px">Have Profile Pic</label>
        </div><br>
        <label for="Info" id="uploadtext" class="form-label" style="font-size: 20px;"><span class="mdi mdi-cloud-upload"></span> Upload Profile Pic</label>
        
    <div class="input-group mb-3" id="profpic">
            <input type="file" class="form-control" id="inputGroupFile02" style="border-top-left-radius: 60px; border-bottom-left-radius: 60px;" :disabled="!haveprofile" @change="addImage">
            <label class="input-group-text" for="inputGroupFile02" style="border-top-right-radius: 60px; border-bottom-right-radius: 60px;" ><span class="mdi mdi-upload"></span> Upload</label>
            
    </div>
    
    </div>

    
    <div class="form-group" id="checkingterm"><br>
        <input type="checkbox" class="form-check-input" name="isterms" id="isterms" style="margin-top:5px; margin-right: 10px;" v-model="isterms">
        <label class="form-check-label" for="isterms" style="font-size: 15px; margin-bottom:5px"> I accept <router-link to="/Influencer_Terms" style="margin-right: 20px;"> Terms & Conditions and Privacy Policy.</router-link></label>
    </div><br>
    
    <div class="form-group"  id="submitting">
        <button type="submit" id="submission" class="btn"   @click.prevent="submitForm"><span class="mdi mdi-account-edit"></span> Edit Profile
            </button>
    </div>
</form>
</div>
<div style="background-color: #333; color: white; text-align: center; position: relative; bottom: 0; left: 0; width: 100%; font-family: 'Doto', sans-serif; font-optical-sizing: auto; font-weight: 1000; font-style: normal; font-variation-settings: 'ROND' 100; font-size: 1.1rem; height: 50px;">
  <p align="center" style="margin: 0; line-height: 50px;">© 2024 | © 21F3001516 | Influencer Engagement Sponsor Coordination Platform | © CreativeMerge</p>
</div>
</template>

<script>
import axios from 'axios';
export default {
  name: '',
  data() {
    return { 
        Image: null,
        username: '',
        password: '',
        confirm_password: '',
        name: '',
        email: '',
        industry: '',
        niche: '',
        infor: '',
        isterms: false,
        role: 'Influencer',
        haveprofile: false,
        isyt: false,
        isinsta: false,
        isx: false,
        isthread: false,
        isfb: false,
        istik: false,
        iskick: false,
        istwitch: false,
        issnap: false,
        islinked: false,
        ytfollowers: '',
        ytlink: '',
        instafollowers: '',
        instalink: '',
        xfollowers: '',
        xlink: '',
        threadfollowers: '',
        threadlink: '',
        fbfollowers: '',
        tikfollowers: '',
        kickfollowers: '',
        twitchfollowers: '',
        snapfollowers: '',
        linkedfollowers: '',
        ytlink: '',
        instalink: '',
        xlink: '',
        threadlink: '',
        fblink: '',
        tiklink: '',
        kicklink: '',
        twitchlink: '',
        snaplink: '',
        linkedlink: '',
        user_id: ''
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
    validateform(){
        // Initial validation checks 
        if (this.username === '' || this.password === '' || this.confirm_password === '' || this.name === '' || this.isterms === false || this.industry === '') { 
            alert("Please fill all the fields and accept the terms and conditions"); 
            return false; 
        } 
        if (this.password !== this.confirm_password) { 
            alert("Password and Confirm Password do not match"); 
            return false; 
        } 
        if (this.isyt === false && this.isinsta === false && this.isx === false && this.isthread === false && this.isfb === false && this.istik === false && this.iskick === false && this.istwitch === false && this.issnap === false && this.islinked === false) { 
            alert("Please select at least one platform"); return false; 
        } 
        // Platform-specific validation checks 
        if (this.isyt === true && (this.ytfollowers === '' || this.ytlink === '')) { 
            alert("Please fill all the fields for YouTube"); 
            return false; 
        } 
        if (this.isinsta === true && (this.instafollowers === '' || this.instalink === '')) { 
            alert("Please fill all the fields for Instagram"); 
            return false; 
        } 
        if (this.isx === true && (this.xfollowers === '' || this.xlink === '')) { 
            alert("Please fill all the fields for Twitter/X"); 
            return false; 
        } 
        if (this.isthread === true && (this.threadfollowers === '' || this.threadlink === '')) { 
            alert("Please fill all the fields for Threads"); 
            return false; 
        } 
        if (this.isfb === true && (this.fbfollowers === '' || this.fblink === '')) { 
            alert("Please fill all the fields for Facebook"); 
            return false; 
        } 
        if (this.istik === true && (this.tikfollowers === '' || this.tiklink === '')) { 
            alert("Please fill all the fields for TikTok"); 
            return false; 
        } 
        if (this.iskick === true && (this.kickfollowers === '' || this.kicklink === '')) { 
            alert("Please fill all the fields for Kick"); 
            return false; 
        } 
        if (this.istwitch === true && (this.twitchfollowers === '' || this.twitchlink === '')) { 
            alert("Please fill all the fields for Twitch"); 
            return false; 
        } 
        if (this.issnap === true && (this.snapfollowers === '' || this.snaplink === '')) { 
            alert("Please fill all the fields for Snapchat"); 
            return false; 
        } 
        if (this.islinked === true && (this.linkedfollowers === '' || this.linkedlink === '')) { 
            alert("Please fill all the fields for LinkedIn"); 
            return false; 
        } 
        // If all validations pass 
        return true;
      },
    submitForm() { 
        if (this.validateform()) { 
            this.signup();
            this.uploadimg(); 
        }
    },
    signup(){
        axios
                .post('http://localhost:5000/editinfluencerprofile/' + this.user_id,{
                    username: this.username,
                    password: this.password,
                    confirm_password: this.confirm_password,
                    name: this.name,
                    email: this.email,
                    isterms: this.isterms,
                    role: "Influencer",
                    industry: this.industry,
                    niche: this.niche,
                    addinfo: this.infor,
                    haveprofile: this.haveprofile,
                    isyt: this.isyt,
                    isinsta: this.isinsta,
                    isx: this.isx,
                    isthread: this.isthread,
                    isfb: this.isfb,
                    istik: this.istik,
                    iskick: this.iskick,
                    istwitch: this.istwitch,
                    issnap: this.issnap,
                    islinked: this.islinked,
                    ytfollowers: this.ytfollowers,
                    ytlink: this.ytlink,
                    instafollowers: this.instafollowers,
                    instalink: this.instalink,
                    xfollowers: this.xfollowers,
                    xlink: this.xlink,
                    threadfollowers: this.threadfollowers,
                    threadlink: this.threadlink,
                    fbfollowers: this.fbfollowers,
                    fblink: this.fblink,
                    tikfollowers: this.tikfollowers,
                    tiklink: this.tiklink,
                    kickfollowers: this.kickfollowers,
                    kicklink: this.kicklink,
                    twitchfollowers: this.twitchfollowers,
                    twitchlink: this.twitchlink,
                    snapfollowers: this.snapfollowers,
                    snaplink: this.snaplink,
                    linkedfollowers: this.linkedfollowers,
                    linkedlink: this.linkedlink,

                },
                {
                    headers: {
                        Authorization: this.token,
                    },
                })
                .then((response) => {
                    console.log("Response Block", response);
                    if(response.status == 200){
                        console.log("Profile Edit Successfull");
                        this.username = null,
                        this.password = null,
                        this.confirm_password = null,
                        this.name = null,
                        this.email = null,
                        this.isterms = false,
                        this.industry = null,
                        this.niche = null,
                        this.infor = null,
                        this.haveprofile = false,
                        this.isyt = false,
                        this.isinsta = false,
                        this.isx = false,
                        this.isthread = false,
                        this.isfb = false,
                        this.istik = false,
                        this.iskick = false,
                        this.istwitch = false,
                        this.issnap = false,
                        this.islinked = false,
                        this.ytfollowers = '',
                        this.instafollowers = '',
                        this.xfollowers = '',
                        this.threadfollowers = '',
                        this.fbfollowers = '',
                        this.tikfollowers = '',
                        this.kickfollowers = '',
                        this.twitchfollowers = '',
                        this.snapfollowers = '',
                        this.linkedfollowers = '',
                        this.ytlink = '',
                        this.instalink = '',
                        this.xlink = '',
                        this.threadlink = '',
                        this.fblink = '',
                        this.tiklink = '',
                        this.kicklink = '',
                        this.twitchlink = '',
                        this.snaplink = '',
                        this.linkedlink = '';

                        alert('Profile Edited Successfully!');
                        this.$router.push('/InfluencerProfile');
                    }
                    else{
                        console.log("Profile Edit Failed");
                        alert('Profile Edit Failed! Reason: ' + response.data.message +' Please try again');
                    }
                })
                .catch((error) => {
                    console.log(error);
                });
      },
      addImage(event){
        this.Image = event.target.files[0];
      },
      uploadimg(){
        let formData = new FormData();
        formData.append('file', this.Image);
        formData.append('username', this.username);
        formData.append('role', this.role);
        formData.append('profpic', this.haveprofile);
        axios.post('http://localhost:5000/uploadprofpic', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        });
      }
  },
  computed: {
    
  },
  watch: {
     isyt(newVal) { 
        if (!newVal) { 
            this.ytfollowers = ''; 
            this.ytlink = ''; 
        } 
    }, 
    isinsta(newVal) { 
        if (!newVal) { 
            this.instafollowers = ''; 
            this.instalink = ''; 
        } 
    }, 
    isx(newVal) { 
        if (!newVal) { 
            this.xfollowers = ''; 
            this.xlink = ''; 
        } 
    }, 
    isthread(newVal) { 
        if (!newVal) { 
            this.threadfollowers = ''; 
            this.threadlink = ''; 
        } 
    }, 
    isfb(newVal) { 
        if (!newVal) { 
            this.fbfollowers = ''; 
            this.fblink = ''; 
        } 
    }, 
    istik(newVal) { 
        if (!newVal) { 
            this.tikfollowers = ''; 
            this.tiklink = ''; 
        } 
    }, 
    iskick(newVal) { 
        if (!newVal) { 
            this.kickfollowers = ''; 
            this.kicklink = ''; 
        } 
    }, 
    istwitch(newVal) { 
        if (!newVal) { 
            this.twitchfollowers = ''; 
            this.twitchlink = ''; 
        } 
    }, 
    issnap(newVal) { 
        if (!newVal) { 
            this.snapfollowers = ''; 
            this.snaplink = ''; 
        } 
    }, 
    islinked(newVal) { 
        if (!newVal) { 
            this.linkedfollowers = ''; 
            this.linkedlink = ''; 
        } 
    },
    
  },
  mounted() {
    
  }
}
</script>

<style scoped>
.footer {
        background-color: #333;
        color: #fff;
        text-align: center;
        padding: 10px 0;
        bottom: 0;
        width: 100%;
    }
.registerform {
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
  flex-wrap: wrap;
  align-content: center;
  align-self: center;
  margin-top: 50px;
  justify-content: space-evenly;
  min-width: 360px;
  margin-bottom: 20px;
  border-color: rgb(27, 28, 28);
  border-style: solid;
  border-radius: 30px;
  background-color: #e8e8e8;
 
}
@media (max-width: 768px) { 
    .registerform { 
        padding: 5px; /* Increased padding for smaller screens */ 
        margin: 20px; /* Adding margin around the form */ 
    } 
}

.regis #checkingterm{
    margin-left: 5%;
}

.regis #submitting{
    flex-direction: column;
    align-items: center;
    justify-content: center;
    align-content: center;
    justify-items: center;
    align-self: center;

}

.regis{
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    margin-top: 10px;
    justify-content: center;
    align-items: center;
    align-content: center;
    justify-items: center;
    align-self: center;
    gap:15px;
    max-width: 1000px;
    padding-bottom: 20px;
    
}

.platforms{
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    margin-top: 10px;
    justify-content: space-evenly;
    align-items: center;
    align-content: center;
    justify-items: center;
    align-self: center;
    max-width: 1000px;
    gap:5px;
    
}
.platforms .input-group { 
    margin-bottom: 10px; 
    width: 100%; 
    max-width: 400px; 
     

} 

.platforms .input-group-text { 
    text-align: center; 
    display: flex; 
    justify-content: center; 
    align-items: center; 
}

.platforms .input-group-text span { 
    justify-content: space-evenly;
    align-items: center;
    max-width: 100px;
    margin-right: 2px; /* Spacing between icon and text */ 
}



.platforms .form-control { 
    border-radius: 60px; 
    font-size: 15px; 
    padding-left: 10px; 
    padding-right: 10px; 
    height: 40px; 
    width: 10%; 
}

.profile{
    display: flex;
    flex-direction: column;
    flex-wrap: wrap;
    max-width: 100%;
    align-content: flex-start;
    justify-content: flex-start;
    align-items: flex-start;
    justify-items: flex-start;
    align-self: flex-start;
    margin-left: 10px;
    
    
}

.profile #haveprofile{
    align-items: flex-start;
    justify-content: flex-start;
    align-content: flex-start;
    justify-items: flex-start;
    align-self: flex-start;

}

#submission {
  background-color: blueviolet;
  color:aliceblue; 
  border-radius: 30px; 
  align-content: center;
  align-items: center;
  font-size: 20px;
  color: #fff;
  outline: none;
  align-self: center;
  border: none;
  width: 100%;
  cursor: pointer;
}
#submission:hover {
    background-color: #4CAF50;
}
</style>