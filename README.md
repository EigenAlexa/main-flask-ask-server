This is an Alexa Skills Kit Flask server which takes requests from alexa and reroutes them to a discriminator.
run ``zappa deploy production`` to deploy to lamda function

To change the discriminator backend run change the value of DISCIMINATOR\_URI in update.json and then run `` aws lambda update-function-configuration --cli-input-json file://update.json``
