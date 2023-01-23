
const express = require('express')

const app = express()


app.get('/', (req, res) => {
  // 人为定义的错误
  throw new Error('sever inside occurs error')
  res.send('home page')
})

//(视频讲的这种用法好像不行了)定义错误级别的中间件，他这里是说捕获整个项目的异常错误，所以上面要有错误发生才行
app.use((err, req, res, next) => {
  console.log('occur error!' + err.message)  //这个message就是捕获的错误的信息，在这里就是输出上面抛出的异常里面的内容
  res.send('error' + err.message)
})

app.listen(80, () => {
  console.log('express server running at http://127.0.0.1')
})
