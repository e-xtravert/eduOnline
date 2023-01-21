// 格式化时间传统方法
function dateFormat(dtStr) {
  const dt = new Date(dtStr)

  const y = dt.getFullYear()
  const m = padZero(dt.getMonth() + 1) //month获取的是0-11
  const d = padZero(dt.getDay())


  const hh = padZero(dt.getHours())
  const mm = padZero(dt.getMinutes())
  const ss = padZero(dt.getSeconds())

  return `${y} - ${m} - ${d} - ${hh} - ${mm} - ${ss}`

}
function padZero(n) {
  return n > 9? n : '0' + n
}


module.exports = {
  dateFormat
}
