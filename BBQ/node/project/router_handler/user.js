//直接导出函数内容，然后在需要的文件导入函数
exports.regUser = (req, res) => {
  res.cc('reguser success!', 0)
}

exports.login = (req, res) => {
  res.send('login success!')
}
