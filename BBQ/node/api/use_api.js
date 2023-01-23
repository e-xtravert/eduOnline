const express = require('express')
const app = express()

const router = require('./apiRouter')



//这个/api是跟路径？
app.use('/api', router.router)

//启动web服务器
app.listen(80, () => {
  console.log('express server running at http://127.0.0.1')
})
