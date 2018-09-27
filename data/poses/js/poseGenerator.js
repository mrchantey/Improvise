
const OpenRawPoseLibrary = require('./importRawPoses').OpenRawPoseLibrary
const FilterMotors = require('./filterMotors').FilterMotors
const GeneratePoseCommandFields = require('./poseCommandFieldGenerator').GeneratePoseCommandFields
const utility = require('./utility')


const poseTemplatesDir = "poseTemplates.json"
const destPoseDir = "generatedPoses.json"
const destPoseCommandFieldDir = "poseCommandFields.json"


OpenRawPoseLibrary()
  .then(rawPoses => {
    const unfilteredPoses = GeneratePoses(rawPoses)
    const poses = FilterMotors(unfilteredPoses)
    GeneratePoseCommandFields(poses)
    utility.SaveJson(poses, destPoseDir)
  })


function GeneratePoses(rawPoses) {
  const poseTemplates = utility.OpenJson(poseTemplatesDir)
  const arr = []
  poseTemplates.forEach(t => {
    t.rawPoses.forEach(rpName => {
      const rawPose = rawPoses.find(p => p.fullName === rpName)
      t.rawBodyParts.forEach(bodyPart => {
        t.rawBodySides.forEach(bodySide => {
          const newPose = {
            fullName: bodyPart + "_" + bodySide + "_" + rawPose.bodyPose,
            bodyPart: bodyPart,
            bodySide: bodySide,
            bodyPose: rawPose.bodyPose,
            motors: rawPose.motors
          }
          arr.push(newPose)
        })
      })
    })
    // return arr
  })
  // arr.Append(rawPoses)
  return rawPoses.concat(arr)
}

