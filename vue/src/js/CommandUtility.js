import ORIGINAL_AvailableCommandFields from "../../../pkg/data/commandFields.json"
import ORIGINAL_CommandPresets from "../../../pkg/data/presets.json"

export default {
    GetDefaultCommand,
    GetCommandPresets,
    FilterCommand,
    DownloadCommandBody,
    UploadCommandBodyAsync,
    CommandFieldsToCommandBody,
    CommandBodyToCommandFields
}

// TODO: Presets live on firebase
function GetCommandPresets() {
    const presetBodies = RecursiveCopy(ORIGINAL_CommandPresets)
    // const presetFields = presetBodies.map(b => CommandBodyToCommandFields(b))
    return presetBodies
}

function GetAvailableCommandFields() {
    return RecursiveCopy(ORIGINAL_AvailableCommandFields)
}

function GetDefaultCommand() {
    const command = {
        fields: GetAvailableCommandFields()
    }
    FilterCommand(command)
    return command
}

function GetPresets() {

}

function CommandFieldsToCommandBody(command) {
    const commandBody = {};
    command.fields.forEach(f => (commandBody[f.name] = f.value));
    if (commandBody['commands'] !== undefined)
        commandBody['commands'] = commandBody['commands'].map(c => CommandFieldsToCommandBody(c))
    return commandBody
}

function CommandBodyToCommandFields(command) {
    const commandFields = {
        "fields": Object.keys(command).map(k => {
            const field = { name: k }
            if (Array.isArray(command[k]))
                field.value = command[k].map(el => CommandBodyToCommandFields(el))
            else if (typeof (command[k]) === "object")
                field.value = CommandBodyToCommandFields(command[k])
            else
                field.value = command[k]
            return field
        })
    }
    // FilterCommand(commandFields)
    return commandFields
}

function FilterCommand(command) {
    const matchingFields = GetAvailableCommandFields()
        .filter(f => CheckFieldPredicate(f.predicates, command.fields))
    matchingFields.forEach(mf => {
        const existingField = command.fields.find(f => f.name === mf.name);
        if (existingField !== undefined)
            Object.assign(mf, existingField)
    })
    command.fields = matchingFields
}

function CheckFieldPredicate(predicates, commandFields) {
    if (predicates === undefined)
        return true
    return predicates
        .every(p => {
            const field = commandFields.find(f => f.name === p.name)
            return field === undefined ? false : (p.value === field.value)
        })
}


function RecursiveCopy(obj) {
    if (Array.isArray(obj))
        return obj.map(el => RecursiveCopy(el))
    else if (typeof (obj) === 'object') {
        const newObj = {};
        Object.keys(obj).forEach(k => newObj[k] = RecursiveCopy(obj[k]))
        return newObj
    }
    else
        return obj
}

function DownloadCommandBody(command) {
    const name = command.name === undefined ? "command" : command.name
    const cmdString = JSON.stringify(command)
    const elt = document.createElement('a')
    elt.setAttribute('href', 'data:application/json;charset=utf-8,' + encodeURIComponent(cmdString))
    elt.setAttribute('download', name + '.json')
    elt.style.display = 'none'
    document.body.appendChild(elt)
    elt.click()
    document.body.removeChild(elt)
}

function UploadCommandBodyAsync() {
    return new Promise((resolve, reject) => {
        const elt = document.createElement('input')
        elt.setAttribute('type', 'file')
        elt.setAttribute('accept', 'application/json')
        elt.addEventListener('change', OpenFile)
        function OpenFile(event) {
            console.log('file upload');
            const input = event.target
            const reader = new FileReader()
            reader.onload = function () {
                const text = reader.result
                const obj = JSON.parse(text)
                console.log(obj);
                resolve(obj)
            }
            reader.readAsText(input.files[0])
        }
        document.body.appendChild(elt)
        elt.click()
        document.body.removeChild(elt)
    })
}

// function CheckExistingField(fields, subFields) {
//     return fields
//         .map(f => f.name)
//         .some(n => subFields
//             .map(sf => sf.name)
//             .includes(n))
// }