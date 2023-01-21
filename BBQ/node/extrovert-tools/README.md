## 安装
```angular2html
npm install extrovert-tools
```

## 导入
```js
const extrovert = require("extrovert-tools")
```

## 格式化时间
```js
const dtnew = htmlEscape.dateFormat(new Date())
// 2023-001-21 23:28:52
console.log(dtnew)
```

## 转义HTML中的特殊字符
```js
// 要转义的HTML字符串
const htmlStr = '<h1 title="abc">这是h1标签<span>123&nbsp;</aspan></hh1>'
//调用方法进行转义
const str = htmlEscape.htmlEscape(htmlStr)
//查看转换的结果
console.log(str)
```

## 还原HTML中的特殊字符
```js
//待还原的HTML字符
const str1 = htmlEscape.htmlUnEscape(str)
//输出的结果 <h1 title="abc">这是h1标签<span>123&nbsp;</aspan></hh1>
console.log(str1)
```

## 开源协议
ISC
