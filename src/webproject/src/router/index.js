import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import CityPopularity from "../components/CityPopularity";
import TravelPartner from "../components/TravelPartner";
import ScreenPage from "../views/ScreenPage";
import ScreenPage2 from "../views/ScreenPage2";
import Map from "../components/Map";
import Cloud from "../components/Cloud";
import testpage from "../views/testpage";
import ScreenPage3 from "../views/ScreenPage3";

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '*',
      redirect: '/screen'
    },
    {
      path :'/screen',
      component : ScreenPage
    },
    {
      path : '/screen2',
      component : ScreenPage2
    },
    {
      path : '/screen3',
      component : ScreenPage3
    },
    {
      path : '/test',
      component : CityPopularity
    }

  ]
})
