
const express = require('express')

const app = express()

//定义在路由函数之前
app.use(express.json())
//获取body的json格式数据和URL-encoded，在发送请求的body里面有对应的类型
app.use(express.urlencoded({extended: false}))

app.post('/user', (req, res) => {
  //可以用req.body去接收客户端发送来的数据，但是这样默认显示的是undefined，需要使用express.jaon内置中间件
  console.log(req.body)
  res.send('ok')
})
app.post('/book', (req, res) => {
  console.log(req.body) // 默认是空对象
  res.send('okkk')
})

//放在后面还没用，要定义在前面
// app.use(express.json())



app.listen(80, () => {
  console.log('express server running at http://127.0.0.1')
})
