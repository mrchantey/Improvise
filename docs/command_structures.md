
# Command Structures

## all

```json
{
    "commandName":"naoqi",
    "async":false
    "respond":"true"
}
```

## naoqi
```json
{
    "commandName":"naoqi",
    "async":false
    "service":"ALTextToSpeech",
    "method":"say",
    "param1:"hello"
}
```

## say

```json
{
    "commandName":"say"
    "async":false
    "phrase":"hi there"
    "animated":false
}
```

## run behavior

```json
{
    "commandName":"runbehavior",
    "async":false,
    "path":"/animations/emotions/happy"
}
```

## action

```json
{
    "commandName":"physiobehavior",
    "async":false,
    "actionname":"physio/forearmpronation",
}
```
## physio action

```json
{
    "commandName":"physiobehavior",
    "async":false,
    "actionname":"physio/forearmpronation",
    "repetitions":5,
    "speed":1
}
```