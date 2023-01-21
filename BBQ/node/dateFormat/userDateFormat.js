// 导入模块
const time0 = require('./dateFormat')

// 使用Date函数
const dt = new Date()

// 调用方法，使用自定义格式化时间格式
const dt1 = time0.dateFormat(dt)
console.log(dt1)
