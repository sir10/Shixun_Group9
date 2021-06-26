<template>
  <div class="com-container">
    <div class="com-chart" ref="rank_ref"></div>
  </div>
</template>

<script>
  import { getChineseName } from '../utils/map_utils.js'
  export default {
    data () {
      return {
        chartInstance: null,
        allData: null,
        startValue: 0, // 区域缩放的起点值
        endValue: 3, // 区域缩放的终点值
        timeId: null // 定时器的标示
      }
    },
    mounted () {
      this.initChart()
      this.getData()
      window.addEventListener('resize', this.screenAdapter)
      this.screenAdapter()
    },
    destroyed () {
      window.removeEventListener('resize', this.screenAdapter)
      clearInterval(this.timeId)
    },
    methods: {
      initChart () {
        this.chartInstance = this.$echarts.init(this.$refs.rank_ref, 'chalk')
        const initOption = {
          title: {
            text: '不同城市旅游价位分析',
            textStyle: {
              fontSize: 30
            },
            left: 125,
            top: 8
          },
          backgroundColor: 'transparent',
          grid: {
            top: '40%',
            left: '5%',
            right: '5%',
            bottom: '5%',
            containLabel: true
          },
          tooltip: {
            show: true
          },
          xAxis: {
            type: 'category'
          },
          yAxis: {
            type: 'value'
          },
          series: [
            {
              type: 'bar'
            }
          ]
        }
        this.chartInstance.setOption(initOption)
        this.chartInstance.on('mouseover', () => {
          clearInterval(this.timeId)
        })
        this.chartInstance.on('mouseout', () => {
          this.startInterval()
        })
      },
      async getData () {
        const { data: ret } = await this.$http.get('cityprice')
        this.allData = ret
        // 对alldata里对每一个元素，进行排序，从大到小
        this.allData.sort((a, b) => {
          return b.value - a.value
        })
        // console.log(this.allData)
        this.updateChart()
        this.startInterval()
      },
      updateChart () {
        // 所有省份所形成的数组
        const movieArr = this.allData.map(item => {
          // console.log(item)
          const provinceInfo = getChineseName(item.cityname)
          console.log(provinceInfo)
          return provinceInfo.key
        })
        // 所有省份对应的销售金额
        const valueArr = this.allData.map(item => {
          return item.averageprice
        })
        const dataOption = {
          xAxis: {
            data: movieArr
          },
          dataZoom: {
            show: false,
            startValue: this.startValue,
            endValue: this.endValue
          },
          series: [
            {
              data: valueArr,
              itemStyle: {
                color: arg => {
                  return new this.$echarts.graphic.LinearGradient(0, 0, 0, 1, [
                    {
                      offset: 0,
                      color: '#5052EE'
                    },
                    {
                      offset: 1,
                      color: '#AB6EE5'
                    }
                  ])
                }
              }
            }
          ]
        }
        this.chartInstance.setOption(dataOption)
      },
      screenAdapter () {
        const titleFontSize = this.$refs.rank_ref.offsetWidth / 100 * 3.6
        const adapterOption = {
          title: {
            textStyle: {
              fontSize: titleFontSize
            }
          },
          xAxis: {
            axisLabel: {
              textStyle: {
                fontSize: '8.5'
              }
            }
          },
          series: [
            {
              barWidth: titleFontSize,
              itemStyle: {
                barBorderRadius: [titleFontSize / 2, titleFontSize / 2, 0, 0]
              }
            }
          ]
        }
        this.chartInstance.setOption(adapterOption)
        this.chartInstance.resize()
      },
      startInterval () {
        if (this.timeId) {
          clearInterval(this.timeId)
        }
        this.timeId = setInterval(() => {
          this.startValue++
          this.endValue++
          if (this.endValue > this.allData.length - 1) {
            this.startValue = 0
            this.endValue = 4
          }
          this.updateChart()
        }, 2000)
      }
    }
  }
</script>

<style scoped>

</style>
