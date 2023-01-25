const express = require('express')

const app = express()

//配置跨越
const cors = require('cors')
app.use(cors())

//配置解析表单中间件
app.use(express.urlencoded({extended: false}))

//在路由之前封装res.cc函数，简化请求响应函数,类似于之前的项目里面的R工具类
app.use((req, res, next) => {
  res.cc = function (err, status = 1) {
    res.send({
      status,
      message: err instanceof Error? err.message : err,
    })
  }
  next()
})

const router = require('./router/user')
app.use('/api', router)

app.listen(3007, () => {
  console.log('api server running at http://127.0.0.1:3007')
})
