const parseXmlString = require('xml2js').parseString
const fs = require('fs')

const rawPoseDir = '../../choregraphe/physio_pose_library_2.xap'

module.exports = {
  OpenRawPoseLibrary
}

function OpenRawPoseLibrary() {
  return new Promise((resolve, reject) => {
    const fileStr = fs.readFileSync(rawPoseDir, 'utf-8')
    parseXmlString(fileStr,
      (err, result) => {
        const poses = ParseRawPoseLibary(result)
        resolve(poses)
      })
  });
}

function ParseRawPoseLibary(result) {
  const rawPoses = result.ChoregraphePositionLibrary.position;
  const poses = rawPoses.map(p => {
    const splitName = p.name[0].split('_')
    return {
      fullName: p.name[0],
      bodyPart: splitName[0],
      bodySide: splitName[1],
      bodyPose: splitName[2],
      motors: p.Motors[0].Motor
        .map(m => {
          return {
            name: m.name[0],
            value: m.value[0]
          }
        })
    }
  })
  return poses
}

