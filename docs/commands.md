


# Commands:


###Rational

At the moment input is sent to the robot in may different forms from the web browser, firebase and internally

These need to be made uniform to create a more stabledesign


## Command sources:
* Internal
    * Speech Recognition
    * Visual
    * Tactile
* Firebase Polls
    * Custom
    * DialogFlow
    * Google Assistant
* Local Server
    * Web Browser
        * Buttons
        * Speech Recognition
    * Postman


## Sequence of execution:
### Commands Class: OnCommand
    1. Channel to NAO Module
    2. Get Response
    3. Check command response instructions
    4. Channel response instructions accordingly


# Command Structures

The Structures themselves live in firebase, to be downloaded by different sources.

For instance, the browser may display the command choices on a web page.

A dialogflow agent creator may be able to read the commands as well as available behaviors in the physio app, for example


json layout:{
    sender:{
        timestamp:"1994-11-05T08:15:30-05:00",
        sourceType: "local browser","dialogflow","internal speech"
    },
    commandTitle""
    directive:"runBehavior","say","setMemory"
    parameters:{
        "value":"",
        "phrase":"",
        "async":false
    }


}



# Firebase Structure


{
    "Commands":[
        {
            "name":"Run Physio Behavior"
        },
        {
            "name":"say"
        }
    ],
    "Physio Behaviors":[
        "HeadLeftRight",
        "LeftForearmPronationSupination"
    ],
    "Monologue Behaviors":[
        "Man from Snowy River"
    ]




}


next steps:
start with internal, then local, then polling