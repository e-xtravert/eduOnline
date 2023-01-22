//这里写一点点东西，主要是作为入口，不写太多内容显得冗余
const express = require('express')
const app = express()

//导入路由模块
const router = require('./router')
//注册路由模块
// app.use(router.router)

//为路由添加访问前缀
app.use('/zjb', router.router)
app.listen(80, () => {
  console.log('http://127.0.0.1')
})
