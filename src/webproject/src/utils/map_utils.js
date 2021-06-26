const name1pinyin = {
  changsha: '长沙',
  chengdu: '成都',
  chongqing: '重庆',
  dali: '大连',
  guangzhou: '广州',
  guiling: '桂林',
  hangzhou: '杭州',
  huangshan: '黄山',
  hulunbeier: '呼伦贝尔',
  jiuzhaigou: '九寨沟',
  kunming: '昆明',
  lasa: '拉萨',
  lijiang: '丽江',
  nanjing: '南京',
  qingdao: '青岛',
  sanya: '三亚',
  shanghai: '上海',
  suzhou: '苏州',
  xiameng: '厦门',
  xian: '西安',
  zhangjiajie: '张家界'
}
const name2pinyin = {
  安徽: 'anhui',
  陕西: 'shanxi1',
  澳门: 'aomen',
  北京: 'beijing',
  重庆: 'chongqing',
  福建: 'fujian',
  甘肃: 'gansu',
  广东: 'guangdong',
  广西: 'guangxi',
  贵州: 'guizhou',
  海南: 'hainan',
  河北: 'hebei',
  黑龙江: 'heilongjiang',
  河南: 'henan',
  湖北: 'hubei',
  湖南: 'hunan',
  江苏: 'jiangsu',
  江西: 'jiangxi',
  吉林: 'jilin',
  辽宁: 'liaoning',
  内蒙古: 'neimenggu',
  宁夏: 'ningxia',
  青海: 'qinghai',
  山东: 'shandong',
  上海: 'shanghai',
  山西: 'shanxi',
  四川: 'sichuan',
  台湾: 'taiwan',
  天津: 'tianjin',
  香港: 'xianggang',
  新疆: 'xinjiang',
  西藏: 'xizang',
  云南: 'yunnan',
  浙江: 'zhejiang'
}

export function getProvinceMapInfo (arg) {
  const path = `/static/map/province/${name2pinyin[arg]}.json`
  return {
    key: name2pinyin[arg],
    path: path
  }
}

export function getChineseName (arg) {
  return {
    key: name1pinyin[arg]
  }
}
