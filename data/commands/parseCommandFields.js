const fs = require('fs')


const fields = OpenJson('commandFields_template.json')
// const poseNames = OpenJson('../poses/poseNames.json')
const installedBehaviors = OpenJson('../behaviors/behaviors.json')
const poseCommandFields = OpenJson('../poses/poseCommandFields.json')
// fields.find(f => f.name === 'poseName').options = poseNames
fields.find(f => f.name === 'path').options = installedBehaviors
const combinedFields = fields.concat(poseCommandFields)

SaveJson('commandFields.json', combinedFields)





function OpenJson(path) {
  const str = fs.readFileSync(path, 'utf-8')
  return JSON.parse(str)
}

function SaveJson(path, data) {
  const str = JSON.stringify(data)
  fs.writeFileSync(path, str, 'utf-8')
}

