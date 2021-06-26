<!--<template>-->
<!--  <ul>{{bookname}}</ul>-->
<!--  <div>-->
<!--    <el-col :span="12">-->
<!--      <el-input placeholder="请输入内容" v-model="searchVal" class="input-with-select" style="width: 100%">-->
  <!--        <el-button type="primary" slot="append" icon="el-icon-search" @click="search">搜索</el-button>-->
  <!--      </el-input>-->
  <!--    </el-col>-->
  <!--    <br/>-->
<!--    <br/>-->
<!--    <a v-for="item in allData">-->
<!--      评论人: {{item.people}}-->
<!--      <br/>-->
<!--      书名：{{item.book_name}}-->
<!--      <br/>-->
<!--      评论 ：{{item.review}}</a>-->
<!--    <br/>-->

<!--    <p></p>-->
<!--    <div class="comment-table">-->
<!--      <el-table-->
<!--        style="width: 100%"-->
<!--        border-->
<!--        height="500"-->
<!--        :data='this.tableData'>-->
<!--        <el-table-column-->
<!--          label="id"-->
<!--          align="center"-->
<!--          width="100"-->
<!--          type="index"-->
<!--          :index='indexMethod'>-->
<!--        </el-table-column>-->
<!--        <el-table-column-->
<!--          label="书名"-->
<!--          show-overflow-tooltip-->
<!--          prop="book_name">-->
<!--        </el-table-column>-->
<!--        <el-table-column-->
<!--          label="评论人"-->
<!--          show-overflow-tooltip-->
<!--          prop="people">-->
<!--        </el-table-column>-->
<!--        <el-table-column-->
<!--          label="评论"-->
<!--          align="center"-->
<!--          show-overflow-tooltip-->
<!--          prop="review">-->
<!--        </el-table-column>-->
<!--        <el-table-column-->
<!--          width="200"-->
<!--          align="center"-->
<!--          label="操作">-->
<!--          <template slot-scope="{ row }">-->
<!--            <el-button size="mini">查看</el-button>-->
<!--          </template>-->
<!--        </el-table-column>-->
<!--      </el-table>-->
<!--      <el-pagination-->
<!--        @size-change="handleSizeChange"-->
<!--        @current-change="handleCurrentChange"-->
<!--        :current-page="currentPage"-->
<!--        :page-sizes="[5, 10, 20, 40]"-->
<!--        :page-size="pagesize"-->
<!--        layout="total, sizes, prev, pager, next, jumper"-->
<!--        :total="allData.length">-->
<!--      </el-pagination>-->
<!--    </div>-->


<!--  </div>-->


<!--</template>-->

<!--<script>-->
<!--import App from "../App";-->
<!--export default {-->
<!--  name: 'HelloWorld',-->
<!--  components: {App},-->
<!--  props : ['bookname'],-->
<!--  data () {-->
<!--    return {-->
<!--      allData : null,-->
<!--      tableData : null,-->
<!--      searchVal: '',-->
<!--      currentPage:1, //初始页-->
<!--      pagesize:10,    //    每页的数据-->
<!--      totalLength:0,-->
<!--    }-->
<!--  },-->
<!--  async mounted() {-->



<!--  },-->
<!--  methods:{-->
<!--    async search() {-->
<!--      console.log(this.searchVal)-->
<!--      const {data: result} = await this.$http.get("test/" + this.searchVal)-->
<!--      this.allData = result-->
<!--      this.tableData = result-->
<!--      console.log(this.allData)-->
<!--    },-->
<!--    indexMethod(index) {-->
<!--      // console.log(index)-->
<!--      return index;-->

<!--    },-->
<!--    getTabelData(){-->
<!--      this.tableData = this.allData.slice(-->
<!--        (this.currentPage -1) * this.pagesize,-->
<!--        this.currentPage * this.pagesize-->
<!--      );-->

<!--    },-->
<!--    handleSizeChange: function (size) {-->
<!--      this.pagesize = size;-->
<!--      console.log(size)-->
<!--      // this.handleUserList();-->
<!--      console.log(this.pagesize)  //每页下拉显示数据-->
<!--      this.getTabelData()-->
<!--    },-->
<!--    handleCurrentChange: function(currentPage){-->
<!--      this.currentPage = currentPage;-->
<!--      // this.handleUserList();-->
<!--      console.log(this.currentPage)  //点击第几页-->
<!--      this.getTabelData()-->
<!--    },-->
<!--  }-->
<!--}-->
<!--</script>-->

<!--&lt;!&ndash; Add "scoped" attribute to limit CSS to this component only &ndash;&gt;-->
<!--<style scoped>-->


<!--</style>-->
