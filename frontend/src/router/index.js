import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/Logins',
      name: 'home',
      component: () => import('../views/logins/Login.vue')
    },
    {
      path: '/',
      name: 'Landing',
      component: () => import('../views/logins/Login.vue')
    },
    {
      path: '/Login',
      name: 'LoginPage',
      component: () => import('../views/logins/Login.vue')
    },
    {
      path: '/Register',
      name: 'RegisterPage',
      component: () => import('../views/logins/Registerchoice.vue')
    },
    {
      path: '/RegisterSponsor',
      name: 'RegisterSponsorPage',
      component: () => import('../views/logins/Registersponsor.vue')
    },
    {
      path: '/RegisterInfluencer',
      name: 'RegisterInfluencerPage',
      component: () => import('../views/logins/Registerinfluencer.vue')
    },
    {
      path: '/Influencer_Terms',
      name: 'InfluencerTermsPage',
      component: () => import('../views/logins/termsinflu.vue')
    },
    {
      path: '/Sponsor_Terms',
      name: 'SponsorTermPage',
      component: () => import('../views/logins/termspon.vue')
    },
    {
      path: '/influencerhome',
      name: 'InfluencerHomePage',
      component: () => import('../views/influencer/influencerhome.vue')
    },
    {
      path: '/sponsorhome',
      name: 'SponsorHomePage',
      component: () => import('../views/sponsor/sponsorhome.vue')
    },
    {
      path: '/AdminProfile',
      name: 'AdminProfilePage',
      component: () => import('../views/admin/adminprofile.vue')
    },
    {
      path: '/AdminProfileEdit',
      name: 'AdminProfileEditPage',
      component: () => import('../views/admin/adminprofileedit.vue')
    },
    {
      path: '/InfluencerProfile',
      name: 'InfluencerProfilePage',
      component: () => import('../views/profiles/influencerprofileprivate.vue')
    },
    {
      path: '/SponsorProfile',
      name: 'SponsorProfilePage',
      component: () => import('../views/profiles/sponsorprofile.vue')
    },
    {
      path: '/EditSponsorProfile',
      name: 'SponsorProfileEditPage',
      component: () => import('../views/profiles/editprofilesponsor.vue')
    },
    {
      path: '/DeleteSponsorProfile',
      name: 'SponsorProfileDeletePage',
      component: () => import('../views/profiles/deletesponsorprofile.vue')
    },
    {
      path: '/SponsorProfilePublic/:users_id',
      name: 'SponsorProfilePublicPage',
      component: () => import('../views/profiles/sponsorprofilepublic.vue')
    },
    {
      path: '/InfluencerProfilePublic/:users_id',
      name: 'InfluencerProfilePublicPage',
      component: () => import('../views/profiles/influencerprofilepublic.vue')
    },
    {
      path: '/EditInfluencerProfile',
      name: 'InfluencerProfileEditPage',
      component: () => import('../views/profiles/editinfluencerprofile.vue')
    },
    {
      path: '/DeleteInfluencerProfile',
      name: 'InfluencerProfileDeletePage',
      component: () => import('../views/profiles/deleteinfluencerprofile.vue')
    },
    {
      path: '/AdminSponsorDash',
      name: 'AdminSponsorDashboardPage',
      component: () => import('../views/admin/adminsponsor.vue')
    },
    {
      path: '/AdminInfluencerDash',
      name: 'AdminInfluencerDashboardPage',
      component: () => import('../views/admin/admininfluencer.vue')
    },
    {
      path: '/AdminCampaignDash',
      name: 'AdminCampaignDashboardPage',
      component: () => import('../views/admin/admincampaign.vue')
    },
    {
      path: '/AdminReports/:users_id',
      name: 'AdminReportsPage',
      component: () => import('../views/admin/adminreports.vue')
    },
    {
      path: '/AdminReportsCampaign/:campaign_id',
      name: 'AdminReportsCampaignPage',
      component: () => import('../views/admin/adminreportcampaign.vue')
    },
    {
      path: '/AdminStats',
      name: 'AdminStatisticsPage',
      component: () => import('../views/admin/adminstats.vue')
    },
    {
      path: '/SponsorStats',
      name: 'SponsorStatisticsPage',
      component: () => import('../views/sponsor/sponsorstats.vue')
    },
    {
      path: '/InfluencerStats',
      name: 'InfluencerStatisticsPage',
      component: () => import('../views/influencer/influencerstats.vue')
    },
    {
      path: '/SponsorDashboard',
      name: 'SponsorDashboardPage',
      component: () => import('../views/sponsor/sponsordash.vue')
    },
    {
      path: '/CreateCampaign',
      name: 'CreateCampaignPage',
      component: () => import('../views/campaign/campaignadd.vue')
    },
    {
      path: '/EditCampaign/:campaign_id',
      name: 'EditCampaignPage',
      component: () => import('../views/campaign/campaignedit.vue')
    },
    {
      path: '/DeleteCampaign/:campaign_id',
      name: 'DeleteCampaignPage',
      component: () => import('../views/campaign/campaigndelete.vue')
    },
    {
      path: '/AddMoney/:campaign_id/PaymentPage',
      name: 'PaymentPage',
      component: () => import('../views/campaign/payments.vue')
    },
    {
      path: '/Wallet',
      name: 'UserWalletPage',
      component: () => import('../views/profiles/wallet.vue')
    },
    {
      path: '/ViewCampaign/:campaign_id',
      name: 'ViewCampaignPage',
      component: () => import('../views/campaign/campaign.vue')
    },
    {
      path: '/ViewCampaignPublic/:campaign_id',
      name: 'ViewCampaignPublicPage',
      component: () => import('../views/campaign/campaignpublic.vue')
    },
    {
      path: '/ViewCampaign/:campaign_id/CreateAd',
      name: 'CreateAdPage',
      component: () => import('../views/ad/Adadd.vue')
    },
    {
      path: '/EditAd/:Ad_id',
      name: 'EditAdPage',
      component: () => import('../views/ad/editad.vue')
    },
    {
      path: '/ViewCampaign/:campaign_id/Ad/:Ad_id/HireInfluencer',
      name: 'HireInfluencerPage',
      component: () => import('../views/sponsor/hireinfluencer.vue')
    },
    {
      path: '/RequestJob/:request_id/Negociation',
      name: 'NegociationPage',
      component: () => import('../views/sponsor/negociationsponsor.vue')
    },
    {
      path: '/Adrequestdash',
      name: 'AdRequestDashPage',
      component: () => import('../views/sponsor/adrequestdash.vue')
    },
    {
      path: '/InfluencerDash',
      name: 'InfluencerDashboardPage',
      component: () => import('../views/influencer/influencerdash.vue')
    },
    {
      path: '/AdminUserReviews/:users_id',
      name: 'AdminUserReviewsPage',
      component: () => import('../views/admin/adminuserreview.vue')
    },
    {
      path: '/InfluencerReviews',
      name: 'InfluencerReviewsPage',
      component: () => import('../views/influencer/influencerreview.vue')
    },
    {
      path: '/InfluencerNegociation&Messages/:request_id',
      name: 'InfluencerNegociationMessagePage',
      component: () => import('../views/influencer/negociationinfluencer.vue')
    },
    {
      path: '/SponsorNegociation&Messages/:request_id',
      name: 'SponsorNegociationMessagePage',
      component: () => import('../views/sponsor/negociationsponsor.vue')
    },

  ]
})

router.beforeEach((to, from, next) => { 
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth); 
  const isAuthenticated = localStorage.getItem('AuthToken'); if (requiresAuth && !isAuthenticated) { 
    alert('You need to be logged in to access this page'); 
    next('/login'); 
  } 
  else { 
    next(); 
  } 
});

export default router
