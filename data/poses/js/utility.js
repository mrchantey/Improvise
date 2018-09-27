const fs = require('fs')

module.exports = {
  OpenJson,
  SaveJson
}


function OpenJson(path) {
  const objStr = fs.readFileSync(path, 'utf-8')
  return JSON.parse(objStr)
}

function SaveJson(obj, path) {
  const objStr = JSON.stringify(obj)
  fs.writeFileSync(path, objStr, 'utf-8')
}