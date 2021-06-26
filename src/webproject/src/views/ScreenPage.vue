<template>
  <div class="screen-container">
    <div class="topbnt_left fl">
      <ul><li><a href="http://localhost:8080/#/screen">页面1</a></li>
        <li><a href="http://localhost:8080/#/screen2">页面2</a></li>
        <li class="active"><a href="http://localhost:8080/#/screen3">页面3</a></li>
      </ul>
    </div>
    <div class="screen-header">
      <span class="title">旅游数据分析</span>
    </div>
    <div class="screen-body">
      <section class="screen-left">
        <div id="left-top">
          <citypopularity></citypopularity>
        </div>
        <div id="left-bottom">
          <travelpartner></travelpartner>
        </div>
      </section>
      <section class="screen-middle">
        <div id="middle-top">
          <map1></map1>
        </div>
        <div id="middle-bottom">
          <every></every>
        </div>
      </section>
      <section class="screen-right">
        <div id="right-top">
          <cityprice></cityprice>
        </div>
        <div id="right-bottom">
          <cloud></cloud>
        </div>
      </section>
    </div>
  </div>
</template>

<script>

  import CityPopularity from "../components/CityPopularity";
  import TravelPartner from "../components/TravelPartner";
  import CityPrice from "../components/CityPrice";
  import Cloud from "../components/Cloud";
  import Map from "../components/Map";
  import EveryScore from "../components/EveryScore";

  export default {
    name: 'ScreenPage',
    components:{
      citypopularity: CityPopularity,
      travelpartner: TravelPartner,
      cityprice :  CityPrice,
      cloud : Cloud,
      map1 : Map,
      every : EveryScore
    }
  }
</script>

<style scoped>
  .screen-container {
    width: 100%;
    height: 100%;
    padding: 0 50px;
    /*background-color: #161522;*/
    color: #fff;
    box-sizing: border-box;
  }
  .screen-header {
    width: 100%;
    height: 64px;
    font-size: 20px;
    position: relative;
    z-index: 0;
  }
  span{
    padding-top: 1px;
  }
  .title{
    position: absolute;
    left: 50%;
    top: 50%;
    font-size: 20px;
    transform: translate(-50%, -50%);
  }
  .screen-body{
    width: 100%;
    height: 100%;
    display: flex;
    margin-top: 10px;
  }
  .screen-left{
    height: 100%;
    width: 27.6%;
  }
  #left-top{
    height: 46%;
    position: relative;
    background: url(../assets/images/purightbott.png);
    background-repeat: no-repeat;
    background-size: 100% 100%;
    background-position:0 0;
  }
  #left-bottom{
    height: 38%;
    margin-top: 25px;
    position: relative;
    background:url(../assets/images/purightbott.png);
    background-repeat: no-repeat;
    background-size: 100% 100%;
    background-position:0 0;
  }
  .screen-middle{
    height: 100%;
    width: 41.5%;
    margin-left: 1.6%;
    margin-right: 1.6%;
  }
  #middle-top{
    width: 100%;
    height: 56%;
    position: relative;
    background: url(../assets/images/purightbott.png);
    background-repeat: no-repeat;
    background-size: 100% 100%;
    background-position:0 0;
  }
  #middle-bottom{
    margin-top: 25px;
    width: 100%;
    height: 28%;
    position: relative;
    background: url(../assets/images/purightbott.png);
    background-repeat: no-repeat;
    background-size: 100% 100%;
    background-position:0 0;
  }
  .screen-right{
    height: 100%;
    width: 27.6%;
  }
  #right-top{
    height: 46%;
    position: relative;
    background: url(../assets/images/purightbott.png);
    background-repeat: no-repeat;
    background-size: 100% 100%;
    background-position:0 0;
  }
  #right-bottom{
    height: 38%;
    margin-top: 25px;
    position: relative;
    background: url(../assets/images/purightbott.png);
    background-repeat: no-repeat;
    background-size: 100% 100%;
    background-position:0 0;
  }


  .topbnt_left li a {
    text-decoration: none;
    color: #fff;
  }

  .topbnt_left li.active, .topbnt_right li.active {
    background: url(../assets/images/bntactive.png) no-repeat center;
  }


  .topbnt_left {
    width: 33%;
  }

  .fl {
    float: left;
  }

  div {
    display: block;
  }

  .topbnt_left ul {
    padding-top: 10px;
    padding-left: 1%;
    width: 100%;
  }

  .topbnt_left li.active, .topbnt_right li.active {
    background: url(../assets/images/bntactive.png) no-repeat center;
  }

  .topbnt_left li {
    background: url(../assets/images/bnt.png) center;
    font-size: 14px;
    line-height: 33px;
    background-repeat: no-repeat;
    width: 18%;
    height: 35px;
    float: left;
    text-align: center;
    margin-left: 1%;
  }

  li {
    display: list-item;
    text-align: -webkit-match-parent;
    list-style: none;
  }
  .topbnt_left{
    position: relative;
    z-index: 9999;
  }




</style>
