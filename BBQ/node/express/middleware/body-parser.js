const express = require('express')

const app = express()


const parser = require('body-parser')

app.listen(80, () => {
  console.log('express server running at http://127.0.0.1')
})
