import './assets/main.css'
import Aura from '@primevue/themes/aura';
import { createApp} from 'vue'
import App from './App.vue'
import router from './router'
import PrimeVue from 'primevue/config';
import Button from 'primevue/button';
import Checkbox from 'primevue/checkbox';
import InputText from 'primevue/inputtext';
import Rating from 'primevue/rating';
import Tooltip from 'primevue/tooltip';
import Knob from 'primevue/knob';

const app = createApp(App)

app.use(router)
app.use(PrimeVue,{
    theme: {
        preset: Aura,
        options: {
            prefix: 'p',
            darkModeSelector: 'system',
            cssLayer: false
        }
    }
 })

app.component('Button', Button)
app.component('Checkbox', Checkbox)
app.component('InputText', InputText)
app.component('Rating', Rating)
app.directive('tooltip', Tooltip);
app.component('Knob', Knob)
app.mount('#app')
