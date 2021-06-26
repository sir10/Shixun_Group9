<template>
  <div class="com-container">
    <div class="com-chart" ref="citypopularity_ref"></div>
  </div>
</template>

<script>
  import { getChineseName } from '../utils/map_utils.js'
  export default {
    data () {
      return {
        chartInstance: null,
        allData: null,
        currentPage: 1, // 当前显示的页数
        totalPage: 0, // 一共多少页
        timeId: null // 定时器
      }
    },
    mounted () {
      this.initChart()
      this.getData()
      window.addEventListener('resize', this.screenAdapter)
      // 在页面加载完成时，主动进行屏幕适配
      this.screenAdapter()
    },
    destroyed () {
      clearInterval(this.timeId)
      // 在组件销毁的时候，需要将监听器取消
      window.removeEventListener('resize', this.screenAdapter)
    },
    methods: {
      initChart () {
        this.chartInstance = this.$echarts.init(this.$refs.citypopularity_ref, 'chalk')
        // 对图片初始化配置
        const initOption = {
          title: {
            text: '不同城市的平均评分',
            textStyle: {
              fontSize: 15
            },
            left: 135,
            top: 7
          },
          backgroundColor: 'transparent',
          grid: {
            top: '20%',
            left: '3%',
            right: '6%',
            bottom: '3%',
            containLabel: true // 距离是包含坐标轴文字
          },
          xAxis: {
            type: 'value'
          },
          yAxis: {
            type: 'category'
          },
          tooltip: {
            trigger: 'axis',
            axisPointer: {
              type: 'line',
              z: 0,
              lineStyle: {
                width: 66,
                color: '#2D3443'
              }
            }
          },
          series: [
            {
              type: 'bar',
              barWidth: 30,
              label: {
                show: true,
                position: 'right',
                textStyle: {
                  color: 'white'
                }
              }
              // itemStyle: {
              // 指明颜色渐变的方向
              // 指明不同百分比之下颜色的值
              // color: new this.$echarts.graphic.LinearGradient(0, 0, 1, 0, [
              //   {
              //     offset: 0,
              //     color: '#95ace0'
              //   },
              //   {
              //     offset: 1,
              //     color: '#1ee2be'
              //   }
              // ])
              // }
              // }
            }
          ]
        }
        this.chartInstance.setOption(initOption)
        // 对图表对象进行鼠标事件的监听
        this.chartInstance.on('mouseover', () => {
          clearInterval(this.timeId)
        })
        this.chartInstance.on('mouseout', () => {
          this.startInterval()
        })
      },
      async getData () {
        const { data: ret } = await this.$http.get('citypopularity')
        // console.log(ret)
        this.allData = ret
        // 对数组进行排序
        this.allData.sort((a, b) => {
          return a.score - b.score // 从小到大
        })
        // 每5个元素显示一页
        this.totalPage = this.allData.length % 5 === 0 ? this.allData.length / 5 : this.allData.length / 5 + 1
        this.updateChart()
        // 启动定时器
        this.startInterval()
      },
      updateChart () {
        const colorArr = [
          ['#faaca8', '#ddd6f3', '#eecda3'],
          ['#fbc7d4', '#DBD4B4', '#6dd5ed'],
          ['#2BC0E4', '#EAECC6', '#93F9B9']
        ]
        const start = (this.currentPage - 1) * 5
        const end = this.currentPage * 5
        const showData = this.allData.slice(start, end)
        const cityNames = showData.map((item) => {
          const provinceInfo = getChineseName(item.cityName)
          console.log(provinceInfo)
          return provinceInfo.key
        })
        const cityValues = showData.map((item) => {
          return item.score
        })
        const dataOption = {
          yAxis: {
            data: cityNames
          },
          series: [
            {
              data: cityValues,
              itemStyle: {
                color: arg => {
                  let targetColorArr = null
                  if (arg.value > 4.65) {
                    targetColorArr = colorArr[0]
                  } else if (arg.value > 4.55) {
                    targetColorArr = colorArr[1]
                  } else {
                    targetColorArr = colorArr[2]
                  }
                  return new this.$echarts.graphic.LinearGradient(0, 0, 1, 0, [
                    {
                      offset: 0,
                      color: targetColorArr[0]
                    },
                    {
                      offset: 0.5,
                      color: targetColorArr[1]
                    },
                    {
                      offset: 1,
                      color: targetColorArr[2]
                    }
                  ])
                }
              }
            }]
        }
        this.chartInstance.setOption(dataOption)
      },
      startInterval () {
        if (this.timeId) {
          clearInterval(this.timeId)
        }
        this.timeId = setInterval(() => {
          this.currentPage++
          if (this.currentPage > this.totalPage) {
            this.currentPage = 1
          }
          this.updateChart()
        }, 3000)
      },
      // 当浏览器当大小发生变化的时候，会调用的方法，来完成屏幕的适配
      screenAdapter () {
        const titleFontSize = this.$refs.citypopularity_ref.offsetWidth / 100 * 3.6
        // console.log(titleFontSize)
        // 和分辨率大小相关的配置项
        const adapterOption = {
          title: {
            textStyle: {
              fontSize: titleFontSize
            }
          },
          tooltip: {
            lineStyle: {
              width: titleFontSize
            }
          },
          series: [
            {
              barWidth: titleFontSize,
              itemStyle: {
                barBorderRadius: [0, titleFontSize / 2, titleFontSize / 2, 0]
              }
            }
          ]
        }
        this.chartInstance.setOption(adapterOption)
        // 手动调用图表对象的resize才能产生效果
        this.chartInstance.resize()
      }
    }
  }
</script>

<style scoped>

</style>
