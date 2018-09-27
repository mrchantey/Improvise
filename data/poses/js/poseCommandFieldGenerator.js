
const SaveJson = require('./utility').SaveJson

const poseCommandFieldDir = "poseCommandFields.json"

module.exports = {
  GeneratePoseCommandFields
}

function GeneratePoseCommandFields(poses) {
  const commandFields = [
    {
      name: "fullName",
      value: "body_none_standOrigin",
      predicates: [
        {
          name: "commandName",
          value: "pose"
        }
      ],
      options: poses.sort(compare).map(p => p.fullName)
    }
  ]
  SaveJson(commandFields, poseCommandFieldDir)
}

function compare(a, b) {
  if (a.fullName < b.fullName)
    return -1
  if (a.fullName > b.fullName)
    return 1
  return 0
}