
// 定义转义HTML字符的函数
function htmlEscape(htmlstr) {
  return htmlstr.replace(/<|>|"|&/g, (match) => {
    switch (match) {
      case "<":
        return '&lt;'
      case '>':
        return '&gt;'
      case '"':
        return '&quot;'
      case '&':
        return '&amp;'
    }
  })
}

//定义还原HTML的方法
function htmlUnEscape(str) {
  return str.replace(/&lt;|&gt;|&quot;|&amp;/g, (match) => {
    switch (match) {
      case '&lt;':
        return '<'
      case '&gt;':
        return '>'
      case '&quot;':
        return '"'
      case '&amp;':
        return '&'
    }
  })
}

module.exports = {
  //导出要全，不然后面test找不到函数
  htmlEscape,
  htmlUnEscape
}
