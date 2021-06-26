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
    <div id="alert" ref="alert">
      <div class="alert_content">
        <el-scrollbar style="height: 100%;" wrap-class="default-scrollbar__wrap">
        <div class="alert_title" style="color:#000; font-size: 25px;">
          景点名称：{{name}}
        </div>
        <div class="alert_body" style="color: black; font-size: 15px">
          景点简介: {{introduction}}
          <br/><br/>
          景点地址: {{address}}
          <br/><br/>
          推荐交通路线: {{traffic}}
          <br/><br/>
          评分: {{score}}
          <br/><br/>
          等级: {{rank}}
          <br/><br/>
          景点图片: <img :src= this.picurl style="width: 300px;height: 300px;display: block;">
          <br/><br/>
          开放时间: {{time}}
          <br/><br/>
          关键词: {{keyword}}
          <br/><br/>
          景点评价:
          <br/><br/>
          {{usercomments1}}
          <br/><br/>
          {{usercomments2}}
        </div>
        </el-scrollbar>
        <div class="alert_btn">
          <button @click="closeScenic">X</button>
        </div>
      </div>
    </div>
    <div class="screen-body">
      <section class="screen-left">
        <div id="left-top">
          <el-col :span="60">
            <input class="test" v-model="searchVal" style="border:1px solid #ffffff" >
            <button type="button" @click="search">Click Me!</button>
          </el-col>
        </div>
        <div class="left-middle">
          <span style="color: #fff; font-weight: bold; font-size: 25px; text-align: center; display: block; padding-top: 5px">旅游路线推荐</span>
          <div id="left-middle-top" class="table" style="font-size: 20px">
              <span style="color: #ffffff; font-size: 20px; padding-bottom: 10px">推荐旅游路线</span>
              {{this.recommendinfo}}
          </div>
          <div id="left-middle-bottom">
            <div class="table_name" style="font-size: 20px">
              <span style="color: #ffffff; font-size: 20px">实际旅游路线</span>
            </div>
            <el-scrollbar style="height: 50%;" wrap-class="default-scrollbar__wrap">
            <div class="table_content2" v-for="item in real_route" v-bind:key="item">
<!--              {{this.routeinfo}}-->
              <a :href = item.url style="color: white; font-size: 20px; text-decoration: none">{{item.name}}</a >
            </div>
            </el-scrollbar>
          </div>
        </div>
        <div id="left-bottom">
          <span style="color: #fff; font-weight: bold; font-size: 25px; text-align: center; display: block; padding-top: 5px">景点推荐</span>
          <el-scrollbar style="height: 80%;" wrap-class="default-scrollbar__wrap">
            <div class="leftbottom" style="font-size: 20px" @click="showScenic(item.introduction, item.name, item.address, item.traffic, item.score, item.rank, item.picurl, item.comments, item.time, item.keyword)" v-for="item in scenicData" v-bind:key="item">
              {{item.name}}
            </div>
          </el-scrollbar>
        </div>
      </section>
      <section class="screen-right">
        <div id="right-top">
          <span style="color: #fff; font-weight: bold; font-size: 25px; text-align: center; display: block">游记展示</span>
          <el-scrollbar style="height: 100%;" wrap-class="default-scrollbar__wrap">
          <div class="righttop" v-for="item in noteData" v-bind:key="item">
            <div class="notetitle">
<!--              <span style="color: #fff; font-size: 20px; text-align: center; display: block">标题:</span>-->
              <a :href = item.url style="color: #fff; font-size: 20px; text-align: center; display: block; text-decoration: none" >{{item.title}}</a>
<!--              {{item.title}}-->
            </div>
            <div class="notecontent" style="font-size: 15px; color: white">
              <span style="color: #ffffff; font-size: 20px">游记内容:</span>
              {{item.content}}
            </div>
          </div>
          </el-scrollbar>
        </div>
        <div id="right-middle">
          <el-col :span="60">
            <input class="test" v-model="searchkey" style="border:1px solid #ffffff" >
            <button type="button" @click="secrchpoem">Click Me!</button>
          </el-col>
        </div>
        <div id="right-bottom">
          <el-scrollbar style="height: 100%;" wrap-class="default-scrollbar__wrap">
          <div class="poemtitle" style="font-size: 25px; text-align: center; display: block">{{poemkeyword}}</div>
          <div class="poemcontent">
            <div class="eachrow" style="font-size: 25px; text-align: center; display: block" v-for="item in poemcontent" v-bind:key="item">
              {{item}}
            </div>
          </div>
          </el-scrollbar>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ScreenPage3',
  data () {
    return {
      searchVal: '',
      searchkey: '',
      popup: 0,

      routeData: null,
      recommendinfo: null,
      routeinfo: null,
      linkinfo: null,
      real_route: null,

      noteData: null,
      title: null,
      content: null,
      like: null,
      comments: null,

      scenicData: null,
      scenicname: null,
      address: null,
      picurl: null,
      introduction: null,
      time: null,
      traffic: null,
      keyword: null,
      rank: null,
      score: null,
      usercomments1: null,
      usercomments2: null,

      poemData: null,
      poemkeyword: null,
      poemcontent: null
    }
  },
  methods: {
    async search () {
      // console.log(this.searchVal)
      // 旅游路线数据


      // clearTimeout(this.timer);  //清除延迟执行

      const { data: route } = await this.$http.get('route/' + this.searchVal)


      this.routeData = route
      this.recommendinfo = this.routeData[0].recommend_route
      this.real_route = this.routeData[0].real_route
      this.routeinfo = this.real_route[0].name
      this.linkinfo = this.real_route[0].url
      // console.log(this.routeData[0].real_route[0].name)

      // 旅游文案数据
      const { data: note } = await this.$http.get('note/' + this.searchVal)
      this.noteData = note
      this.title = this.noteData[0].title
      this.content = this.noteData[0].content
      this.like = this.noteData[0].like
      this.comments = this.noteData[0].comments
      // console.log(this.comments)

      // 旅游景点数据
      const { data: scenic } = await this.$http.get('scenic/' + this.searchVal)
      this.scenicData = scenic
      // this.scenicname = this.scenicData[0].name
      // this.address = this.scenicData[0].address
      // this.picurl = this.scenicData.pic_url[0]
      // this.keyword = this.scenicData[0].key_word
      // this.rank = this.scenicData[0].rank
      // this.score = this.scenicData[0].score
      // console.log(this.address)
      // console.log(this.picurl)
    },
    async secrchpoem () {
      // 旅游文案数据

      const { data: poem } = await this.$http.get('poem/' + this.searchkey)

      this.poemcontent = ['正在生成中，请稍候...']
      // clearTimeout(this.timer);  //清除延迟执行
      this.timer = setTimeout(()=>{   //设置延迟执行

        this.poemData = poem
        this.poemkeyword = this.poemData[0].keyword
        this.poemcontent = this.poemData[0].content
      },9000);

      // this.poemData = poem
      // this.poemkeyword = this.poemData[0].keyword
      // this.poemcontent = this.poemData[0].content
      // console.log(this.poemData)
      // console.log(this.poemkeyword)
      // console.log(this.poemcontent)
    },
    showScenic (introduction, name, address, traffic, score, rank, picurl, comments, time, keyword) {
      // console.log(address)
      this.introduction = introduction
      this.name = name
      this.address = address
      this.traffic = traffic
      this.score = score
      this.rank = rank
      this.picurl = picurl[0]
      // this.key_word = key_word[0]
      this.usercomments1 = comments[0].user_comment
      this.usercomments2 = comments[1].user_comment
      this.time = time
      this.keyword = keyword[0]
      console.log(this.usercomments)
      this.$refs.alert.style.display = 'flex'
    },
    closeScenic () {
      // console.log(this)
      this.$refs.alert.style.display = 'none'
    }
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
}
#alert{
  width: 100%;
  height: 100%;
  background: transparent;
  position: fixed;
  left: 0;
  top: 0;
  z-index: 20;
  display: none;
}
.alert_content{
  width: 600px;
  height: 700px;
  background-color: #fff;
  border-radius: 5px;
  margin: auto;
  position: relative;
}
.alert_title{
  padding: 10px;
  border-bottom: 1px;
  width: 100%;
}
.alert_body{
  padding-left: 10px;
  padding-right: 20px;
  padding-bottom: 10px;
  width: 100%;
  height: 70%;
}
.alert_btn{
  position: absolute;
  right: 0;
  top: 0;
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
  width: 50%;
}
#left-top{
  width: 500px;
  height: 15px;
  padding-top: 40px;
  padding-bottom: 15px;
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
.left-middle{
  height: 40%;
  margin-top: 25px;
  margin-left: 25px;
  margin-right: 25px;
  position: relative;
  background: url("../assets/images/line(1).png") rgba(255, 255, 255, 0.1);
  line-height: 28px;
}

#left-middle-top{
  margin-top: 25px;
  margin-left: 25px;
  margin-right: 25px;
  position: relative;
  background: rgba(1, 202, 217, .2) url(../assets/images/div3.png) no-repeat top left;
  -moz-border-radius: 60px;
  -webkit-border-radius: 60px;
  border-radius: 60px;
  margin-top: 20px;
}
.table_name{
  width: 30%;
}
#left-middle-bottom{
  height: 100%;
  margin-top: 25px;
  margin-left: 25px;
  margin-right: 25px;
  position: relative;
}
.table_content2{
  height: 100%;
  background: rgba(1, 202, 217, .2) url(../assets/images/div3.png) no-repeat top left;
}
.bigleftbottom{
  height: 300px;
}
#left-bottom{
  margin-top: 20px;
  margin-left: 25px;
  margin-right: 25px;
  width: 95%;
  height: 35%;
  position: relative;
  background: url("../assets/images/line(1).png") rgba(255, 255, 255, 0.1);
  line-height: 15px;
}
.leftbottom{
  padding-left: 40px;
  padding-bottom: 10px;
  margin-bottom: 20px;
  height: 2%;
}
.screen-right{
  height: 100%;
  width: 50%;
}
#right-top{
  height: 40%;
  margin-top: 45px;
  margin-left: 25px;
  margin-right: 25px;
  position: relative;
  background: url("../assets/images/line(1).png") rgba(255, 255, 255, 0.1);
}
.notetitle{
  height: 0%;
  left: 10%;
  background: rgba(1, 202, 217, .2) url(../assets/images/div3.png) no-repeat top left;
  /*border: 10px solid hsla(0,0%,100%,.2);*/
  -moz-border-radius: 60px;
  -webkit-border-radius: 60px;
  border-radius: 60px;
  margin-top: 20px;
}
.notecontent{
  right: 10%;
  /*background: url("../assets/images/line(1).png") rgba(255, 255, 255, 0.2);*/
  /*mso-line-height-alt: 100px;*/
  line-height: 30px;
  margin-top: 20px;
}
#right-middle{
  width: 500px;
  height: 15px;
  padding-top: 45px;
  padding-bottom: 15px;
}
#right-bottom{
  height: 32%;
  margin-top: 25px;
  margin-left: 25px;
  margin-right: 25px;
  position: relative;
  background: url("../assets/images/line(1).png") rgba(255, 255, 255, 0.1);
}
.poemtitle{
  left: 10%;
  height: 50px;
  width: 100%;
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

.screen-header {
  width: 100%;
  height: 64px;
  font-size: 20px;
  position: relative;
  z-index: 0;
}
</style>
