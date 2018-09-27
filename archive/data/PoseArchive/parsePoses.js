const fs = require('fs')
const parseXmlString = require('xml2js').parseString

const sourceDir = '../../choregraphe/physio_pose_library.xap';
const destPoseDir = 'poses.json'
const destPoseNameDir = 'poseNames.json'


const fileStr = fs.readFileSync(sourceDir, 'utf-8')
const poseFiltersStr = fs.readFileSync('./poseFilters.json')
const poseFilters = JSON.parse(poseFiltersStr)
// console.dir(poseFilters);

parseXmlString(fileStr, (err, result) => ParsePoseLibrary(result.ChoregraphePositionLibrary.folder))

function ParsePoseLibrary(folders) {
  const poseFolders = folders.map(f => {
    const folderName = f.title[0]
    const poseFilter = poseFilters[folderName]
    const rawPoses = Array.isArray(f.position) ? f.position : [f.position]
    return rawPoses.map(p => ParsePose(p, folderName, poseFilter))
  })
  const poses = poseFolders.reduce((acc, val) => acc.concat(val), [])
  const posesStr = JSON.stringify(poses)
  fs.writeFileSync(destPoseDir, posesStr, 'utf-8')
  const poseNames = poses.map(p => p.name)
  const poseNamesStr = JSON.stringify(poseNames)
  fs.writeFileSync(destPoseNameDir, poseNamesStr, 'utf-8')


}




function ParsePose(rawPose, folderName, poseFilter) {
  return {
    name: folderName + '/' + rawPose.name[0],
    motors: rawPose.Motors[0].Motor
      .filter(m => poseFilter.motors.includes(m.name[0]))
      .map(m => {
        return {
          name: m.name[0],
          value: m.value[0]
        }
      })
  }
}
