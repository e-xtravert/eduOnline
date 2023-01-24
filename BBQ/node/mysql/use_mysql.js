//导入mysql
const mysql = require('mysql')
//数据库配置
const db = mysql.createPool({
  host: '127.0.0.1',
  user: 'root',
  password: '123456',
  database: 'crud'
})
//测试mysql连接是否正常工作
db.query(`select 1`, (err, results) => {
  if (err) return console.log(err.message)
  console.log(results) //打印结果[ RowDataPacket { '1': 1 } ]什么含义也不表示单纯就是测试连接

})
