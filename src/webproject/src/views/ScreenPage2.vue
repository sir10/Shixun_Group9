<template>

  <div class="screen-container">
    <div class="topbnt_left fl">
      <ul><li><a href="http://localhost:8080/#/screen">页面1</a></li>
        <li><a href="http://localhost:8080/#/screen2">页面2</a></li>
        <li class="active"><a href="http://localhost:8080/#/screen3">页面3</a></li>
      </ul>
    </div>
    <header class="screen-header">
      <span class="title">旅游数据分析</span>
    </header>
    <div class="screen-body">
      <section class="screen-left">
        <div id="left-top">
            <div class="table" style="width: 97%; height: 100%;" >
              <div class="cname">{{$store.state.partoneData.cluster_name}}</div>
                <el-scrollbar style="height: 100%;" wrap-class="default-scrollbar__wrap">
                  <div class="fordiv" v-for="(item,index) in this.$store.state.partoneData.tourist_route" v-if="index%2==0">
                    <div class="content lefttop" >
                      <a class="a1" :href = $store.state.partoneData.tourist_route[index].url>{{$store.state.partoneData.tourist_route[index].route_name}}</a>
                    </div>

                    <div class="content ltbg" v-if="index < $store.state.partoneData.tourist_route.length - 1" >
                      <a class="a1" :href = $store.state.partoneData.tourist_route[index+1].url>{{$store.state.partoneData.tourist_route[index+1].route_name}}</a>
                    </div>
                  </div>
                </el-scrollbar>
              </div>
        </div>
        <div id="left-bottom">
          <div class="table" style="width: 97%; height: 100%;" >
            <div class="cname">{{$store.state.parttwoData.cluster_name}}</div>
            <el-scrollbar style="height: 100%;" wrap-class="default-scrollbar__wrap">
              <div class="fordiv" v-for="(item,index) in this.$store.state.parttwoData.tourist_route" v-if="index%2==0">
                <div class="content" >
                  <a class="a1" :href = $store.state.parttwoData.tourist_route[index].url>{{$store.state.parttwoData.tourist_route[index].route_name}}</a>
                </div>
                <div class="content bg" v-if="index < $store.state.parttwoData.tourist_route.length - 1" >

                  <a class="a1" :href = $store.state.parttwoData.tourist_route[index+1].url>{{$store.state.parttwoData.tourist_route[index+1].route_name}}</a>
                </div>
              </div>
            </el-scrollbar>
          </div>
        </div>
      </section>
      <section class="screen-middle">
        <div id="middle-top">
          <div class="table" style="width: 97%; height: 100%;" >
            <div class="cname">{{$store.state.partthreeData.cluster_name}}</div>
            <el-scrollbar style="height: 100%;" wrap-class="default-scrollbar__wrap">
              <div class="fordiv" v-for="(item,index) in this.$store.state.partthreeData.tourist_route" v-if="index%2==0">
                <div class="content middletop" >
                  <a class="a1" :href = $store.state.partthreeData.tourist_route[index].url>{{$store.state.partthreeData.tourist_route[index].route_name}}</a>
                </div>
                <div class="content mtbg " v-if="index < $store.state.partthreeData.tourist_route.length - 1" >
                  <a class="a1" :href = $store.state.partthreeData.tourist_route[index+1].url>{{$store.state.partthreeData.tourist_route[index+1].route_name}}</a>
                </div>
              </div>
            </el-scrollbar>
          </div>
        </div>


        <div class="search">
          <el-col :span="60">
            <input class="test" v-model="searchVal" style="border:1px solid #ffffff" >
            <button type="button" @click="search">Click Me!</button>
          </el-col>
        </div>


        <div id="middle-bottom">
          <div class="table" style="width: 97%; height: 100%;" >
            <div class="cname">{{$store.state.partfourData.cluster_name}}</div>
            <el-scrollbar style="height: 100%;" wrap-class="default-scrollbar__wrap">
              <div class="fordiv" v-for="(item,index) in this.$store.state.partfourData.tourist_route" v-if="index%2==0">
                <div class="content middlebottom" >
                  <a class="a1" :href = $store.state.partfourData.tourist_route[index].url>{{$store.state.partfourData.tourist_route[index].route_name}}</a>
                </div>
                <div class="content mbbg" v-if="index < $store.state.partfourData.tourist_route.length - 1" >

                  <a class="a1" :href = $store.state.partfourData.tourist_route[index+1].url>{{$store.state.partfourData.tourist_route[index+1].route_name}}</a>
                </div>
              </div>
            </el-scrollbar>
          </div>
        </div>
      </section>
      <section class="screen-right">
        <div id="right-top">
          <div class="table" style="width: 97%; height: 100%;" >
            <div class="cname">{{$store.state.partfiveData.cluster_name}}</div>
            <el-scrollbar style="height: 100%;" wrap-class="default-scrollbar__wrap">
              <div class="fordiv" v-for="(item,index) in this.$store.state.partfiveData.tourist_route" v-if="index%2==0">
                <div class="content" >
                  <a class="a1" :href = $store.state.partfiveData.tourist_route[index].url>{{$store.state.partfiveData.tourist_route[index].route_name}}</a>
                </div>
                <div class="content bg" v-if="index < $store.state.partfiveData.tourist_route.length - 1" >
                  <a class="a1" :href = $store.state.partfiveData.tourist_route[index+1].url>{{$store.state.partfiveData.tourist_route[index+1].route_name}}</a>
                </div>
              </div>
            </el-scrollbar>
          </div>

      </div>
        <div id="right-bottom">
          <div class="table" style="width: 97%; height: 100%;" >
            <div class="cname">{{$store.state.partsixData.cluster_name}}</div>
            <el-scrollbar style="height: 100%;" wrap-class="default-scrollbar__wrap">
              <div class="fordiv" v-for="(item,index) in this.$store.state.partsixData.tourist_route" v-if="index%2==0">
                <div class="content rightbottom" >
                  <a class="a1" :href = $store.state.partsixData.tourist_route[index].url>{{$store.state.partsixData.tourist_route[index].route_name}}</a>
                </div>
                <div class="content bg" v-if="index < $store.state.partsixData.tourist_route.length - 1" >
                  <a class="a1" :href = $store.state.partsixData.tourist_route[index+1].url>{{$store.state.partsixData.tourist_route[index+1].route_name}}</a>
                </div>
              </div>
            </el-scrollbar>
          </div>
          </div>
      </section>
    </div>
  </div>


</template>

<script>
    export default {
      name: "ScreenPage2",
      data() {
        return {
          allData: null,
          partData: null,
          searchVal: ''
        }
      },
      created(){

        // this.search().then(response=>{
        //   // console.log(response[1])
        //   this.$store.commit('GetPartOneData',response[0])
        //   this.$store.commit("GetPartTwoData",response[1])
        //   this.$store.commit("GetPartThreeData",response[2])
        //   this.$store.commit("GetPartFourData",response[3])
        //   this.$store.commit("GetPartFiveData",response[4])
        //   this.$store.commit("GetPartSixData",response[5])
        //
        // });
      },

      mounted() {
        // console.log(this.$store.state.partoneData)
        // console.log(this.searchVal)
      },
      methods:{
        async search() {
          console.log(this.searchVal)
          const {data: result} = await this.$http.get("cluster/" + this.searchVal)

          this.allData = result
          console.log(this.allData)
          this.$store.commit('GetPartOneData',this.allData[0])
          this.$store.commit("GetPartTwoData",this.allData[1])
          this.$store.commit("GetPartThreeData",this.allData[2])
          this.$store.commit("GetPartFourData",this.allData[3])
          this.$store.commit("GetPartFiveData",this.allData[4])
          this.$store.commit("GetPartSixData",this.allData[5])
          console.log(this.$store.state.partsixData)
        },





        }

    }

</script>

<style scoped>
  .screen-container {
    width: 100%;
    height: 100%;
    padding: 0 50px;
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
    width: 30%;
  }
  #left-top{
    height: 37%;
    position: relative;
    padding-bottom: 5px;
    margin-bottom: 5px;
    /*background: url(../assets/images/purightbott.png);*/
    background-repeat: no-repeat;
    background-size: 100% 100%;
    background-position:0 0;

  }
  #left-bottom{
    height: 37%;
    margin-top: 65px;
    position: relative;
    /*background: url(../assets/images/purightbott.png);*/
    background-repeat: no-repeat;
    background-size: 100% 100%;
    background-position:0 0;
  }
  .screen-middle{
    height: 100%;
    width: 30%;
    margin-left: 5%;
    margin-right: 5%;
  }
  #middle-top{
    width: 100%;
    height: 30%;
    position: relative;
    background-repeat: no-repeat;
    background-size: 100% 100%;
    background-position:0 0;
  }
  #middle-bottom{
    margin-top: 67px;
    width: 100%;
    height: 28%;
    position: relative;
    background-repeat: no-repeat;
    background-size: 100% 100%;
    background-position:0 0;
  }
  .screen-right{
    height: 100%;
    width: 30%;
  }
  #right-top{
    height: 37%;
    position: relative;
    padding-bottom: 5px;
    margin-bottom: 5px;
    /*background: url(../assets/images/purightbott.png);*/
    background-repeat: no-repeat;
    background-size: 100% 100%;
    background-position:0 0;
  }
  #right-bottom{
    height: 37%;
    margin-top: 65px;
    position: relative;
    /*background: url(../assets/images/purightbott.png);*/
    background-repeat: no-repeat;
    background-size: 100% 100%;
    background-position:0 0;
  }
  .screen-header {
    width: 100%;
    height: 64px;
    font-size: 20px;
    position: relative;
  }
  .table{
    padding-top: 13px;
    padding-left: 3%;
    /*overflow: ;*/

  }
  .fordiv{
    margin-top: 0.1rem;
    padding-left: 0.02rem;
    padding-right: 3.1rem;
    overflow: hidden;
  }
  .content {
    margin-top: 0.2rem;
    height: 2.4rem;
    width: 7rem;
    background: rgba(1, 202, 217, .2) url(../assets/images/icosjx.png) no-repeat top left;
    position: relative;
    overflow: hidden;
    padding: 2% 6%;
    padding-top: 0.4rem;
    color: rgba(255, 255, 255, 0.7);
    /*line-height: 20%;*/
    font-size: 2px;
    border-top-left-radius : 15px;
    border-top-right-radius : 15px;
    border-bottom-right-radius : 15px;
    border-bottom-left-radius : 15px;
    letter-spacing:10px;
    z-index: 0;
  }
  .bg{
  background: rgba(0,255,255,.4) url(../assets/images/icosjx.png) no-repeat  top left;
  }
  .cname{
    text-align: center;
  }
  .lefttop{
    background: rgba(101, 212, 255, 0.4) url(../assets/images/icosjx.png) no-repeat  top left;
  }
  .middletop{
    background: rgba(101, 212, 255, 0.4) url(../assets/images/icosjx.png) no-repeat  top left;
  }
  .mtbg{
    background: rgba(84, 237, 204, 0.4) url(../assets/images/icosjx.png) no-repeat  top left;
  }
  .middlebottom{
    background: rgba(94, 223, 237, 0.4) url(../assets/images/icosjx.png) no-repeat  top left;
  }
  .mbbg{
    background: rgba(101, 212, 255, 0.4) url(../assets/images/icosjx.png) no-repeat  top left;
  }
  .rightbottom{
    background: rgba(87, 255, 130, 0.3) url(../assets/images/icosjx.png) no-repeat  top left;
  }
  .a1{
    height: 10%;
    width: 0.2rem;
    color: rgba(255, 255, 255, 0.7);
    /*padding-left: 3rem;*/
    z-index: 999;
    text-decoration:none;
  }
  .search{
    width: 500px;
    height: 30px;
    padding-top: 70px;
  }
  .test{
    width: 300px;
    height: 30px;
    border: 3px solid #eeeeee;
    border-radius: 15px;
    background: transparent;
    padding-left: 30px;
    margin-left: 35px;
    /*background: rgba(64, 125, 255, 0.4) url(../assets/images/icosjx.png) no-repeat  top left;*/
  }
  button {
    background-color: #428bca;
    border-color: #357ebd;
    color: #fff;
    -moz-border-radius: 10px;
    -webkit-border-radius: 10px;
    border-radius: 10px; /* future proofing */
    text-align: center;
    vertical-align: middle;
    border: 1px solid transparent;
    font-weight: 900;
    font-size:100%
  }
  input{
    padding-left: 10px;
    color: white;
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
