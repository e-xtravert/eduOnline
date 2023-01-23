const express = require('express')

const router = express.Router()

//get接口函数
router.get('/get', (req, res) => {
  //获取客户端通过查询字符串，发送到服务器的数据，这个query是得到params面板里面的参数,就是拼接在url后面的
  const query = req.query
  // response result to client use res.send()
  res.send({
    status: 0,
    msg: 'get request successful!',
    data: query
  })
})

router.post('/post', (req, res) => {
  //post那这里就是body面板里面的json那些东西
  const body = req.body
  console.log(body)
  res.send({
    status: 0,
    msg: 'post request successful！',
    data: body
  })
})


module.exports = {
  router
}
