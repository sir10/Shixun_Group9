<template>
  <div class="com-container" @dblclick="revertMap">
    <div class="com-chart" ref="map_ref"></div>
  </div>
</template>

<script>
  import axios from 'axios'
  import { getChineseName } from '@/utils/map_utils'
  // import { getProvinceMapInfo } from '../utils/map_utils.js'
  export default {
    name: 'Map',
    data () {
      return {
        chartInstance: null,
        allData: null,
        titleFontSize: null,
        mapData: {} // 所获取的省份的地图矢量数据
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
      async initChart () {
        // var colors = ['#1DE9B6', '#EEDD78', '#32c5e9', '#FFDB5C', '#37A2DA', '#04B9FF']
        this.chartInstance = this.$echarts.init(this.$refs.map_ref, 'chalk')
        // 获取中国地图矢量数据
        // 由于我们现在获取的地图矢量数据不是位于后端，不能使用$http
        const ret = await axios.get('http://localhost:8080/static/map/china.json')
        console.log(ret)
        this.$echarts.registerMap('china', ret.data)
        const initOption = {
          title: {
            text: '旅行线路统计分析',
            textStyle: {
              fontSize: 20
            },
            left: 200,
            top: 10
          },
          backgroundColor: 'transparent',
          animation: true,
          animationDuration: 1000,
          animationEasing: 'cubicInOut',
          animationDurationUpdate: 1000,
          animationEasingUpdate: 'cubicInOut',
          grid: {
            right: '2%',
            top: '10%',
            bottom: '10%',
            width: '18%'
          },
          roam: true,
          tooltip: {
            trigger: 'axis', // hover触发器
            axisPointer: { // 坐标轴指示器，坐标轴触发有效
              type: 'shadow', // 默认为直线，可选为：'line' | 'shadow'
              shadowStyle: {
                color: 'rgba(150,150,150,0.1)' // hover颜色
              }
            }
          },
          visualMap: {
            min: 2500,
            max: 4000,
            left: 'left',
            top: 'bottom',
            text: ['高', '低'],
            textStyle: {
              color: 'white'
            },
            calculable: true,
            colorLightness: [0.8, 100],
            color: ['#c05050', '#e5cf0d', '#5ab1ef'],
            dimension: 0

          },
          geo: {
            show: true,
            map: 'china',
            roam: true,
            zoom: 1,
            center: [113.83531246, 34.0267395887],
            label: {
              emphasis: {
                show: true
              }
            },
            itemStyle: {
              normal: {
                borderColor: 'rgba(147, 235, 248, 1)',
                borderWidth: 1,
                areaColor: {
                  type: 'radial',
                  x: 0.5,
                  y: 0.5,
                  r: 0.8,
                  colorStops: [{
                    offset: 0,
                    color: 'rgba(147, 235, 248, 0)' // 0% 处的颜色
                  }, {
                    offset: 1,
                    color: 'rgba(147, 235, 248, .2)' // 100% 处的颜色
                  }],
                  globalCoord: false // 缺省为 false
                },
                shadowColor: 'rgba(128, 217, 248, 1)',
                // shadowColor: 'rgba(255, 255, 255, 1)',
                shadowOffsetX: -2,
                shadowOffsetY: 2,
                shadowBlur: 10
              },
              emphasis: {
                areaColor: '#389BB7',
                borderWidth: 0
              }
            }
          }
        }
        this.chartInstance.setOption(initOption)
        // 点击某个省份，打开这个省份 arg.name 得到所点击的省份，这个省份是中文
        // this.chartInstance.on('click', async (arg) => {
        //   // console.log(arg)
        //   const provinceInfo = getProvinceMapInfo(arg.name)
        //   // console.log(provinceInfo)
        //   // 需要获取这个省份的地图矢量数据
        //   // 判断当前所点击的省份地图矢量数据在mapdata中是否存在
        //   if (!this.mapData[provinceInfo.key]) {
        //     const ret = await axios.get('http://localhost:8999' + provinceInfo.path)
        //     this.mapData[provinceInfo.key] = ret.data
        //     // console.log(ret)
        //     this.$echarts.registerMap(provinceInfo.key, ret.data)
        //   }
        //   const changeOption = {
        //     geo: {
        //       map: provinceInfo.key
        //     }
        //   }
        //   this.chartInstance.setOption(changeOption)
        // })
      },
      async getData () {
        const { data: result } = await this.$http.get('map')
        this.allData = result
        this.allData.sort((a, b) => {
          return a.value - b.value // 从小到大
        })
        // console.log(result)
        this.updateChart()
      },
      updateChart () {
        const path = [{
          fromName: '北京',
          toName: '长沙',
          coords: [
            [116.4551, 40.2539],
            [112.95, 28.23]
          ]
        }, {
          fromName: '北京',
          toName: '成都',
          coords: [
            [116.4551, 40.2539],
            [116.42, 39.86]
          ]
        }, {
          fromName: '北京',
          toName: '重庆',
          coords: [
            [116.4551, 40.2539],
            [116.41, 39.91]
          ]
        }, {
          fromName: '北京',
          toName: '大连',
          coords: [
            [116.4551, 40.2539],
            [121.63, 38.92]
          ]
        }, {
          fromName: '北京',
          toName: '广州',
          coords: [
            [116.4551, 40.2539],
            [113.27, 23.13]
          ]
        }, {
          fromName: '北京',
          toName: '桂林',
          coords: [
            [116.4551, 40.2539],
            [110.19, 25.24]
          ]
        }, {
          fromName: '北京',
          toName: '杭州',
          coords: [
            [116.4551, 40.2539],
            [120.21, 30.25]
          ]
        }, {
          fromName: '北京',
          toName: '黄山',
          coords: [
            [116.4551, 40.2539],
            [118.31, 29.71]
          ]
        }, {
          fromName: '北京',
          toName: '呼伦贝尔',
          coords: [
            [116.4551, 40.2539],
            [119.77, 49.17]
          ]
        }, {
          fromName: '北京',
          toName: '九寨沟',
          coords: [
            [116.4551, 40.2539],
            [121.4648, 31.2891]
          ]
        }, {
          fromName: '北京',
          toName: '昆明',
          coords: [
            [116.4551, 40.2539],
            [102.83, 24.88]
          ]
        }, {
          fromName: '北京',
          toName: '拉萨',
          coords: [
            [116.4551, 40.2539],
            [91.17, 29.66]
          ]
        }, {
          fromName: '北京',
          toName: '丽江',
          coords: [
            [116.4551, 40.2539],
            [100.23, 26.86]
          ]
        }, {
          fromName: '北京',
          toName: '南京',
          coords: [
            [116.4551, 40.2539],
            [118.80, 32.06]
          ]
        }, {
          fromName: '北京',
          toName: '青岛',
          coords: [
            [116.4551, 40.2539],
            [120.38, 36.07]
          ]
        }, {
          fromName: '北京',
          toName: '三亚',
          coords: [
            [116.4551, 40.2539],
            [109.52, 18.23]
          ]
        }, {
          fromName: '北京',
          toName: '上海',
          coords: [
            [116.4551, 40.2539],
            [121.46, 31.23]
          ]
        }, {
          fromName: '北京',
          toName: '苏州',
          coords: [
            [116.4551, 40.2539],
            [120.59, 31.31]
          ]
        }, {
          fromName: '北京',
          toName: '厦门',
          coords: [
            [116.4551, 40.2539],
            [118.10, 24.49]
          ]
        }, {
          fromName: '北京',
          toName: '张家界',
          coords: [
            [116.4551, 40.2539],
            [110.48, 29.13]
          ]
        }, {
          fromName: '北京',
          toName: '西安',
          coords: [
            [116.4551, 40.2539],
            [118.94, 34.35]
          ]
        }]
        const city = [
          {
            name: '北京',
            value: [116.4551, 40.2539]
          }, {
            name: '长沙',
            value: [112.95, 28.23]
          }, {
            name: '成都',
            value: [104.07, 30.58]
          }, {
            name: '重庆',
            value: [106.55, 29.56]
          }, {
            name: '大连',
            value: [121.63, 38.92]
          }, {
            name: '广州',
            value: [113.27, 23.13]
          }, {
            name: '桂林',
            value: [110.19, 25.24]
          }, {
            name: '杭州',
            value: [120.21, 30.25]
          }, {
            name: '黄山',
            value: [118.31, 29.71]
          }, {
            name: '呼伦贝尔',
            value: [119.77, 49.17]
          }, {
            name: '九寨沟',
            value: [104.14, 33.16]
          }, {
            name: '昆明',
            value: [102.83, 24.88]
          }, {
            name: '拉萨',
            value: [91.17, 29.66]
          }, {
            name: '丽江',
            value: [100.23, 26.86]
          }, {
            name: '南京',
            value: [118.80, 32.06]
          }, {
            name: '青岛',
            value: [120.38, 36.07]
          }, {
            name: '三亚',
            value: [109.52, 18.23]
          }, {
            name: '上海',
            value: [121.46, 31.23]
          }, {
            name: '苏州',
            value: [120.59, 31.31]
          }, {
            name: '厦门',
            value: [118.10, 24.49]
          }, {
            name: '西安',
            value: [118.94, 34.35]
          }, {
            name: '张家界',
            value: [110.48, 29.13]
          }
        ]
        const ValueArr = this.allData.map(item => {
          // console.log(item)
          return item.number
        })
        const NameArr = this.allData.map(item => {
          // console.log(item.name)
          const provinceInfo = getChineseName(item.cityname)
          console.log(provinceInfo)
          return provinceInfo.key
        })
        const dataOption = {
          xAxis: {
            type: 'value',
            scale: true,
            position: 'top',
            min: 0,
            boundaryGap: false,
            splitLine: {
              show: false
            },
            axisLine: {
              show: false
            },
            axisTick: {
              show: false
            },
            axisLabel: {
              margin: 1,
              textStyle: {
                color: '#aaa'
              }
            }
          },
          yAxis: {
            type: 'category',
            nameGap: 16,
            axisLine: {
              show: true,
              lineStyle: {
                color: '#ddd'
              }
            },
            axisTick: {
              show: false,
              lineStyle: {
                color: '#ddd'
              }
            },
            axisLabel: {
              interval: 0,
              textStyle: {
                color: '#ddd'
              }
            },
            data: NameArr
          },
          series: [
            {
              type: 'effectScatter',
              coordinateSystem: 'geo',
              zlevel: 1,
              showEffectOn: 'render',
              rippleEffect: {
                brushType: 'stroke'
              },
              symbolSize: function (val) {
                return 5
              },
              label: {
                normal: {
                  show: true,
                  position: 'right',
                  formatter: '{b}'
                }
              },
              itemStyle: {
                normal: {
                  color: '#1DE9B6',
                  shadowBlur: 10,
                  shadowColor: '#1DE9B6'
                }
              },
              data: city
            },
            {
              type: 'lines',
              zlevel: 2,
              effect: {
                show: true,
                period: 5,
                trailLength: 0.2,
                color: '#EEDD78',
                symbol: 'arrow',
                symbolSize: 6
              },
              lineStyle: {
                normal: {
                  color: '#1DE9B6',
                  opacity: 0.2,
                  width: 1,
                  curveness: 0.3
                }
              },
              data: path
            },
            {
              type: 'bar',
              zlevel: 1.5,
              barMaxWidth: 8,
              position: 'right',
              right: '20%',
              symbol: 'none',
              itemStyle: {
                normal: {
                  color: '#1DE9B6',
                  barBorderRadius: [0, 30, 30, 0]
                }
              },
              data: ValueArr
            }
          ]
        }
        this.chartInstance.setOption(dataOption)
      },
      screenAdapter () {
        const titleFontSize = this.$refs.map_ref.offsetWidth / 100 * 3.6
        const adapterOption = {
          title: {
            textStyle: {
              fontSize: titleFontSize
            }
          },
          legend: {
            itemHeight: titleFontSize / 2,
            itemWidth: titleFontSize / 2,
            itemGap: titleFontSize / 2,
            textStyle: {
              fontSize: titleFontSize / 2
            }
          }
        }
        this.chartInstance.setOption(adapterOption)
        this.chartInstance.resize()
      }
      // 回到中国地图
      // revertMap () {
      //   const reverOption = {
      //     geo: {
      //       map: 'china'
      //     }
      //   }
      //   this.chartInstance.setOption(reverOption)
      // }
    }
  }
</script>

<style scoped>

</style>
