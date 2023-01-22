//express建议我们这么做，将路由作为单独的模块
const express = require("express")
const router = express.Router()


router.get('/', (req, res) => {
  res.send("get successful")
})

router.post("/", (req, res) => {
  res.send("post successful")
})

//注意这里的导出问题，如果导出一个对象在使用的时候别忘了router.router
module.exports = {
  router
}

