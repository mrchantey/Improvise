const OpenJson = require('./utility').OpenJson

const motorFiltersDir = "motorFilters.json"

module.exports = {
  FilterMotors
}


function FilterMotors(unfilteredPoses) {
  const motorFilters = OpenJson(motorFiltersDir)
  unfilteredPoses.forEach(p => {
    const motorNames = GetPoseMotorNames(motorFilters, p)
    p.motors = p.motors.filter(m => motorNames.includes(m.name))
  })
  return unfilteredPoses
}

function GetPoseMotorNames(motorFilters, pose) {
  const filter = motorFilters.find(f =>
    f.bodyPart === pose.bodyPart
    && f.bodyPoses.includes(pose.bodyPose))
  if (pose.bodySide === "none")
    return filter.motorNames
  else if (pose.bodySide === "left")
    return filter.motorNames.map(n => "L" + n)
  else if (pose.bodySide === "right")
    return filter.motorNames.map(n => "R" + n)
  else if (pose.bodySide === "both")
    return filter.motorNames.map(n => "L" + n)
      .concat(filter.motorNames.map(n => "R" + n))
}
