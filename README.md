# vocal_command
Configurable vocal command program using google speech.

## config
The commands and language are defined in a config file that need to be set in the`VOCAL_COMMAND_CONFIG` environment variable
`export VOCAL_COMMAND_CONFIG=[PATH_TO_CONFIG_FILE]`

The format of the config file must be:
`lang=[LANG]`

`"[COMMAND TO CALL]" : "[SHELL COMMAND TO EXECUTE]" : "[RESPONSE FROM THE ASSISTANT !OPTIONAL]"`

exemple:

`lang="en-US`

`"open youtube" : "google-chrome www.youtube.com" : "YES SIR !"`
`"open facebook" : "google-chrome www.facebook.com" : "openning facebook right now"`
`"open desktop" : "xdg-open Desktop"`

Here is the list of the accepted languages: https://cloud.google.com/speech-to-text/docs/languages?hl=fr

## usage
`python3 vocal_command.py`
