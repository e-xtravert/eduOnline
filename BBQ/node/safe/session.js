const express = require('express')

const app = express()


app.use(express.json())
app.use(express.urlencoded({extended: false}))
//session中间件配置
const session = require('express-session')
app.use(
    session({
      secret: 'extrovert',
      resave: false,
      saveUninitialized: true
    })
)
//登录的api接口
app.post('/api/login',(req, res) => {
  if(req.body.username != 'admin' || req.body.password != '123456') {
    // console.log(req.body)
    return res.send({status: 1, msg: 'login fail!'})
  }

  //将获取到的用户信息保存到session中
  req.session.user = req.body
  req.session.islogin = true //记录一个登录状态


  res.send({status: 0, msg: 'login success!'})
})

//获取用户姓名的接口
app.get('/api/username', (req, res) => {
  if(!req.session.islogin) {
    return res.send({status: 1, msg: 'fail'})
  }
  res.send({
    status: 0,
    msg: 'success',
    username: req.session.user.username
  })
})

//退出登录的接口
app.post('/api/logout', (req, res) => {
  // clear session info
  req.session.destroy()
  res.send({
    status: 0,
    msg: 'logout success!'
  })
})



app.use(express.urlencoded({extended: false}))

app.listen(80, () => {
  console.log('express server run in http://127.0.0.1')
})
