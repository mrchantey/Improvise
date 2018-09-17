import CommandOptions from "../../../pkg/data/commandOptions.json"


export default {
    GetCommandOptions,
    GetDefaultCommand
}

function GetDefaultCommand() {
    const options = Object.assign({}, CommandOptions);
    return GetCommandOptions(options)
}


function GetCommandOptions(commandOption) {
    if (commandOption.subOptions != null) {
        ApplySubOptionFields(commandOption)
        commandOption.subOptions.forEach(o => GetCommandOptions(o))
    }
    return commandOption
}

function ApplySubOptionFields(commandOption) {
    commandOption.fields = commandOption.subOptions
        .filter(o => CheckCommandOptionPredicate(o.predicates, commandOption.fields))
        .map(o => o.fields)
        .reduce((acc, val) => acc.concat(val), commandOption.fields)

}


function CheckCommandOptionPredicate(predicates, commandFields) {
    return predicates
        .some(p =>
            (p.value === commandFields
                .find(f => f.name === p.name)
                .value))
}
