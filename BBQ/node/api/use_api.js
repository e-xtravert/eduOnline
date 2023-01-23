const express = require('express')
const cors = require('cors')
const app = express()


//这个中间件要写在上面，不然输出undefined
app.use(express.json())
// app.use(express.urlencoded({extended: false}))

app.use(cors())
const router = require('./apiRouter')
//这个/api是跟路径？
app.use('/api', router.router)

//启动web服务器
app.listen(80, () => {
  console.log('express server running at http://127.0.0.1')
})
