

const express = require('express')

const app = express()

//注意一个"./"表示出了当前文件，两个点才是出了当前文件，再出当前文件所在的文件
app.use(express.static('../dateFormat'))
//如果要托管多个静态资源目录，要多次调用express.static()函数
app.use(express.static('../express'))

//如果想要加上前缀，就在第一个参数写上要加的路径
app.use('/extrovert-tools', express.static('../extrovert-tools'))


app.listen(80, () => {
  console.log('express server running at http://127.0.0.1')
})
