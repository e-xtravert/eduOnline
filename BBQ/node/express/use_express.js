//导入express
const express = require('express')
//创建web服务器
const app = express()

//注意箭头函数前面那个参数是request，后面表示response
app.get('/user', (req, res) => {
  res.send({ name:'zjb', age:23, gender:'男'})
})
app.post('/user', (req, res) => {
  res.send("请求成功")
})
//可以获取查询参数
app.get('/', (req, res) => {
  res.send(req.query)
  console.log(req.query)
})
//获取动态查询参数
app.get('/user/:id/:name', (req, res) => {
  res.send(req.params)
  console.log(req.params)
})
//启动web服务器
app.listen(80, () => {
  console.log('express server running at http://127.0.0.1')
})
