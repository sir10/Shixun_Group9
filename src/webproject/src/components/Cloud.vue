<template>
  <div class="com-container">
    <div class="com-chart" ref="cloud_ref">


    </div>
  </div>
</template>

<script>
  export default {
    name: "Cloud",
    data(){
      return{
        chartInstance : null,
        allData : null
      }
    },
    mounted() {
      this.initChart()
      this.getData()
      window.addEventListener('resize',this.screenAdapter)
      this.screenAdapter()
    },
    destroyed() {
      window.removeEventListener('resize',this.screenAdapter)
    },
    methods : {
      initChart(){
        this.chartInstance = this.$echarts.init(this.$refs.cloud_ref,'dark')

      },
      async getData() {
        // const {data: result} = await this.$http.get('cloud')
        // this.allData = result
        // console.log(this.allData)
        this.updateChart()
      },
      updateChart(){
        // const dataArr = this.allData.map(item =>{
        //   return{
        //     'name' : item.name,
        //     'value' : item.value
        //   }
        // })
        // var list = []
        // list.push(dataArr)
        // console.log(list)
        const initOption = {

          title: {
            text: '词云',
            x: 'center',
            top : 5,
            textStyle: {
              fontSize: 15
            }

          },
          backgroundColor: 'transparent',
          legend :{
            top : '15%',
            icon : 'circle',

          },
          tooltip: {
            show: true
          },
          series: [{
            name: '热点分析',//数据提示窗标题
            type: 'wordCloud',
            sizeRange: [6, 40],//画布范围，如果设置太大会出现少词（溢出屏幕）
            rotationRange: [-90, 90],//数据翻转范围
            // shape: 'circle',
            textPadding: 0,
            autoSize: {
              enable: true,
              minSize: 6
            },
            drawOutOfBound: false,//词云显示完整，超出画布的也显示
            textStyle: {
              normal: {
                color: function () {
                  return 'rgb(' + [
                    // Math.round(Math.random() * 160),
                    // Math.round(Math.random() * 160),
                    // Math.round(Math.random() * 160)
                    Math.round(Math.random() * 300),
                    Math.round(Math.random() * 255),
                    Math.round(Math.random() * 255)
                  ].join(',') + ')';
                }
              },
              emphasis: {
                shadowBlur: 10,
                shadowColor: '#333'
              },
            },
            data: [
              {
                name: '导游讲解详细',
                value: 2394
              },
              {
                name: '风景美',
                value: 2633
              },
              {
                name: '航班不错',
                value: 110
              },
              {
                name: '旅游地值得',
                value: 2133
              },
              {
                name: '酒店赞',
                value: 2903
              },
              {
                name: '酒店设施好',
                value: 376
              },
              {
                name: '客服很好',
                value: 1000
              },
              {
                name: '领队不错',
                value: 102
              },
              {
                name: '酒店服务热情',
                value: 593
              },
              {
                name: '性价比高',
                value: 1475
              },
              {
                name: '酒店位置佳',
                value: 526
              },
              {
                name: '交通便利',
                value: 525
              },
              {
                name: '团餐赞',
                value: 968
              },
              {
                name: '无强制消费',
                value: 2021
              },
              {
                name: '导游服务好',
                value: 2901
              },
              {
                name: '自由活动充足',
                value: 113
              },
              {
                name: '酒店餐食赞',
                value: 591
              },
              {
                name: '旅游地美食多',
                value: 120
              },
              {
                name: '产品描述相符',
                value: 872
              },
              {
                name: '包车赞',
                value: 2058
              },
              {
                name: '酒店房间好',
                value: 624
              },
              {
                name: '接送机服务赞',
                value: 1145
              },
              {
                name: '行程棒',
                value: 3380
              }
            ]
            // data : list
          }]
        }
        this.chartInstance.setOption(initOption)
        // this.chartInstance.setOption(dataOption)
      },
      screenAdapter(){
        const adapterOption = {}
        this.chartInstance.setOption(adapterOption)
        this.chartInstance.resize()
      }

    }
  }
</script>

<style scoped>

</style>
