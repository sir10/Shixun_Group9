<template>
  <div class="com-container">
    <div class="com-chart" ref="average_ref"></div>
    <span class="iconfont arr-left"  @click="toLeft" :style="comStyle">&#xe6ef;</span>
    <span class="iconfont arr-right" @click="toRight" :style="comStyle">&#xe6ed;</span>
  </div>
</template>

<script>
  import { getChineseName } from '../utils/map_utils.js'
  export default {
    name: 'BarV',
    data () {
      return {
        chartInstance: null,
        allData: null,
        titleFontSize: null,
        totalPage: 0,
        currentPage: 1
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
    },
    methods: {
      initChart () {
        this.chartInstance = this.$echarts.init(this.$refs.average_ref, 'dark')
        const initOption = {
          title: {
            text: '不同城市的行程安排，导游服务，酒店体验评分分析',
            left: 150,
            top: 3.5,
            textStyle: {
              color: 'white',
              fontSize: '30px',
            },
            // textStyle: {
            //   fontSize: '30px',
            // }
          },
          backgroundColor: 'transparent',
          tooltip: {
            trigger: 'axis',
            axisPointer: {
              type: 'shadow'
            }
          },
          legend: {
            data: ['行程安排', '导游服务', '酒店体验'],
            align: 'left',
            right: 60,
            top: 45,
            textStyle: {
              color: '#fff'
            },
            itemWidth: 15,
            itemHeight: 11,
            itemGap: 10
          },
          grid: {
            left: '60',
            right: '40',
            bottom: '30',
            top: '70'
          },
          xAxis: [
            {
              type: 'category',
              axisLine: {
                lineStyle: {
                  color: '#355b68'
                }
              },
              axisLabel: {
                color: '#fff',
                fontSize: 14,
                interval: 0
              },
              splitLine: {
                lineStyle: {
                  color: '#00314a'
                }
              },
              axisTick: {
                show: false
              }
            }
          ],
          yAxis: [
            {
              type: 'value',
              nameTextStyle: {
                color: '#fff',
                fontSize: 13
              },
              axisLine: {
                lineStyle: {
                  color: '#355b68'
                }
              },
              axisTick: {
                show: false
              },
              splitLine: {
                lineStyle: {
                  color: '#355b68'
                }
              },
              axisLabel: {
                color: '#fff',
                fontSize: 14,
                formatter: '{value}'
              }
            }
          ],
          series: [
            {
              name: '行程安排',
              type: 'bar',
              barWidth: 10,
              barGap: '100%', // 柱图间距
              itemStyle: {
                barBorderRadius: [20, 20, 0, 0],
                color: new this.$echarts.graphic.LinearGradient(0, 0, 0, 1, [
                  { offset: 0, color: '#f4e106' },
                  { offset: 0.5, color: '#f9bd14' },
                  { offset: 1, color: '#ff9f2e' }
                ])
              }
            },
            {
              name: '导游服务',
              type: 'bar',
              // data: _self.HighFreWeekly.listZ,
              barWidth: 10,
              barGap: '100%',
              itemStyle: {
                barBorderRadius: [20, 20, 0, 0],
                color: new this.$echarts.graphic.LinearGradient(0, 0, 0, 1, [
                  { offset: 0, color: '#00fef6' },
                  { offset: 0.5, color: '#00c5f9' },
                  { offset: 1, color: '#188df0' }
                ])
              }
            },
            {
              name: '酒店体验',
              type: 'bar',
              // data: _self.HighFreWeekly.listZ,
              barWidth: 10,
              barGap: '100%',
              itemStyle: {
                barBorderRadius: [20, 20, 0, 0],
                color: new this.$echarts.graphic.LinearGradient(0, 0, 0, 1, [
                  { offset: 0, color: '#00ff5b' },
                  { offset: 0.5, color: '#52c234' },
                  { offset: 1, color: '#3CA55C' }
                ])
              }
            }
          ]
        }

        this.chartInstance.setOption(initOption)
      },
      async getData () {
        // 这里没有传过来数据
        const { data: result } = await this.$http.get('everyscore')
        this.allData = result
        // console.log(this.allData)
        var count = parseInt(this.allData.length / 4)
        this.totalPage = this.allData.length % 4 === 0 ? count : count + 1
        this.updateChart()
      },
      updateChart () {
        const start = (this.currentPage - 1) * 4 // 0
        const end = this.currentPage * 4 // 4
        const showdata = this.allData.slice(start, end)
        const cityArr = showdata.map(item => {
          const provinceInfo = getChineseName(item.cityname)
          console.log(provinceInfo)
          return provinceInfo.key
        })
        console.log(cityArr)

        const journeyArr = showdata.map(item => {
          return item.scheduling
        })
        console.log(journeyArr)
        const guideArr = showdata.map(item => {
          return item.hotelexperience
        })
        // console.log(guideArr)
        const hotelArr = showdata.map(item => {
          return item.tourguide
        })
        // console.log(hotelArr)
        const dataOption = {
          xAxis: [
            {
              data: cityArr
            }
          ],
          series: [
            {
              data: journeyArr
            },
            {
              data: guideArr
            },
            {
              data: hotelArr
            }
          ]

        }

        this.chartInstance.setOption(dataOption)
      },

      screenAdapter () {
        const adapterOption = {}
        this.chartInstance.setOption(adapterOption)
        this.chartInstance.resize()
      },
      toLeft () {
        this.currentPage--
        if (this.currentPage < 1) {
          this.currentPage = this.totalPage
        }
        this.updateChart()
      },
      toRight () {
        this.currentPage++
        if (this.currentPage > this.totalPage) {
          this.currentPage = 1
        }
        this.updateChart()
      }
    }
  }
</script>

<style scoped>
  .arr-left{
    position: absolute;
    left: 4%;
    top: 50%;
    transform: translateY(-50%);
    cursor: pointer;
    color: #ffffff;
  }
  .arr-right{
    position: absolute;
    right: 4%;
    top: 50%;
    transform: translateY(-50%);
    cursor: pointer;
    color : white;

  }
</style>
