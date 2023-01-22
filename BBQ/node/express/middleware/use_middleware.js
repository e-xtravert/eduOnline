const express = require('express')

const app = express()

//定义一个最简单的中间件函数
const mw = function (req, res, next) {
  console.log('这是最简单的中间件函数，局部中间件')
  //把流转关系，转交给下一个中间件或路由
  next()
}

const mw1 = function (req, res, next) {
  console.log('this is second part middleware')
  next()
}
//挂载到app.use上就是全局中间件，放到路由里面当形参就是局部中间件
app.use(function (req, res, next) {
  console.log('这是最简单的中间件函数')
  //把流转关系，转交给下一个中间件或路由
  // 可以把下面
  const time = Date.now()
  req.startTime = time
  next()
})
app.use(function (req, res, next) {
  console.log('this is the second middleware')
  next()
})
//定义多个part 有效中间件,中括号可加可不加
app.get('/zjb', [mw, mw1], (req, res) => {
  console.log('1323')
  res.send("hello express" + req.startTime)
})
app.post('/',(req ,res) => {
  console.log('456')
  res.send("post successful" + req.startTime)
})


//启动web服务器
app.listen(80, () => {
  console.log('express server running at http://127.0.0.1')
})
