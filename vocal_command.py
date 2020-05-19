import speech_recognition as sr
import difflib
import os
from gtts import gTTS
from playsound import playsound
from io import BytesIO

def assistant_speak(text, lang):
    tts = gTTS(text, lang=lang)
    mp3_fp = BytesIO()
    filename = "/tmp/.output.mp3"
    tts.save(filename)
    playsound(filename)
    os.remove(filename)

def get_config(config_file):
    config = {}
    with open(config_file) as f:
        line = f.readline()
        lang = line.split("=")
        if (len(lang) != 2 or lang[0] != "lang"):
            print("error: the first line of the config file should specify a lang")
            return -1
        else:
            lang = "".join(lang[1].split()).replace("\"", "")
            config["lang"] = lang
            for line in f:
                splitted_line = line.split(":")
                if (len(splitted_line) == 2):
                    config[splitted_line[0].replace('"', "").strip()] = [splitted_line[1].replace('"', "").strip()]
                elif (len(splitted_line) == 3):
                    config[splitted_line[0].replace('"', "").strip()] = [splitted_line[i].replace('"', "").strip() for i in range(1, 3)]
            return config

def getaudio(lang):
    r  = sr.Recognizer()
    with sr.Microphone() as source: 
        audio = r.listen(source, phrase_time_limit = 2)  
    try:
        text = r.recognize_google(audio, language="Fr-fr")
        return text
    except:
        print("Error")

def execute_command(text, config):
    for key in config:
        if (key == "lang"):
            continue
        ratio = difflib.SequenceMatcher(None, key, text).ratio()
        if (ratio > 0.85):
            if (len(config[key]) == 2):
                assistant_speak(config[key][1], config["lang"])
            os.system(config[key][0])
            return

def main():
    config = get_config(os.environ["VOCAL_COMMAND_CONFIG"])
    if (config == -1):
        return
    text = getaudio(config["lang"])
    execute_command(text, config)
    
if __name__ == "__main__":
    main()
