// 包的入口文件
// 一般index里面什么内容都没有，只挂载方法函数
// function dateFormat(dateStr) {
//   const dt = new Date(dateStr)
//
//   const y = dt.getFullYear()
//   const m = padZero(dt.getMonth()) + 1
//   const d = padZero(dt.getDate())
//
//   const hh = padZero(dt.getHours())
//   const mm = padZero(dt.getMinutes())
//   const ss = padZero(dt.getSeconds())
//
//   return `${y}-${m}-${d} ${hh}:${mm}:${ss}`
// }
//
// function padZero(n) {
//   return n > 9 ? n: '0' + n
// }
//
// // 定义转义HTML字符的函数
// function htmlEscape(htmlstr) {
//   return htmlstr.replace(/<|>|"|&/g, (match) => {
//     switch (match) {
//       case "<":
//         return '&lt;'
//       case '>':
//         return '&gt;'
//       case '"':
//         return '&quot;'
//       case '&':
//         return '&amp;'
//     }
//   })
// }
//
// //定义还原HTML的方法
// function htmlUnEscape(str) {
//   return str.replace(/&lt;|&gt;|&quot;|&amp;/g, (match) => {
//     switch (match) {
//       case '&lt;':
//         return '<'
//       case '&gt;':
//         return '>'
//       case '&quot;':
//         return '"'
//       case '&amp;':
//         return '&'
//     }
//   })
// }

//require的文件没有导出会显示绿色，成功导出导入则显示紫色
const date = require('./src/dateFormat')
const escape = require('./src/htmlEscape')

module.exports = {
  //三个点表示展开
  ...date,
  ...escape
}
