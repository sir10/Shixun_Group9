// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from "axios";
import store from './store'
import Element from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css';
import './assets/css/global.less'
import 'lib-flexible/flexible.js'
import { HappyScroll } from 'vue-happy-scroll'
import 'vue-happy-scroll/docs/happy-scroll.css'

// const cors = require('koa2-cors');
// Vue.use(cors());

Vue.prototype.$echarts = window.echarts
axios.defaults.baseURL = 'http://localhost:8888/'
//将axios挂载到vue的原型对象上

Vue.prototype.$http = axios

Vue.use(Element)

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
