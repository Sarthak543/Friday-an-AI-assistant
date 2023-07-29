import os.path
import speech_recognition as sr
import pyttsx3
import webbrowser
import openai
import datetime
import pywhatkit
from config import apiKey

FileNumber = 0  # this file number is used to name the file which is created by Friday
openai.api_key = apiKey
speaker = pyttsx3.init()
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)


# METHODS OF FRIDAY
# todo: say is a function used to convert text into speech
def say(message):
    speaker.say(message)
    speaker.runAndWait()


# todo:take_command is a function used to convert speech into text
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.energy_threshold = 100
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            return query
        except Exception as e:
            return say("Sorry I don't Understand")


# todo: function to write response into a file
def write_into_file(data, FileNumber=None):
    # code to create a folder named OpenAI for the document we want friday to save in the file
    if not os.path.exists("Responses"):
        os.mkdir("Responses")
    FileNumber += 1
    file_path = f"prompt-{FileNumber}.txt"
    with open(f"Responses/prompt-{FileNumber}.txt", "w") as f:
        f.write(data)
    return file_path


def open_ai(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response["choices"][0]["text"]


# FRIDAY PROGRAMING

if __name__ == '__main__':
    flag = True
    while flag:
        print("Listening...")
        text = take_command()
        print('Recognizing')
        sites = [["google", "https://www.google.com/"], ["wikipedia", "https://www.wikipedia.org/"],
                 ["youtube", "https://www.youtube.com"], ["Graphic Era Website", "https://geu.ac.in/"],
                 ["Instagram", "https://www.instagram.com/"]]
        musics = [["who is she", "C:/Users/LENOVO/Downloads/Who is she？.mp3"],
                  ["Gangsta paradise", "C:/Users/LENOVO/Downloads/Gp.mp3"],
                  ["rao sahab", "C:/Users/LENOVO/Downloads/rao sahab.mp3"],
                  ["rap god", "C:/Users/LENOVO/Downloads/Eminem - Rap God (Explicit).mp3"]]
        # todo: checking type of command
        command = text.split()[0]

        # todo: exit
        if text.lower() == 'exit':
            flag = False
        # todo: questions about Friday
        elif "what is your name" == text.lower():
            say("I'm Friday. Nice to meet you")
        elif "who are you" == text.lower():
            say("I'm Friday an AI assistant created by Sarthak. You can ask me any question if i know i will "
                "answer them. Now do you want to know something")

        # todo: will search the content in browser
        elif command.lower() == "search":
            search_text = text.split()[1:]
            pywhatkit.search(search_text)

            # todo: opening things
        elif command.lower() == "open":
            for site in sites:
                if f"open {site[0]}".lower() in text.lower():
                    webbrowser.open(site[1])
                    say(f"Opening {site[0]}")

        # todo: playing musing
        elif command.lower() == "play":
            pywhatkit.playonyt(text)

        # todo: solving question using openAI power
        elif command.lower() == "what's" or command.lower() == "what" or command.lower() == "can" or command.lower() == "do" or command.lower() == "how" or command.lower() == "is" or command.lower() == "who" or command.lower() == "when" or command.lower() == "write":
            if "time" in text:
                strftime = datetime.datetime.now().strftime("%H:%M:%S")
                say(f"sir the time is {strftime}")
            elif "write" == command:
                answer = open_ai(prompt=text)
                # writing the response into a file
                file_path = write_into_file(data=answer, FileNumber=FileNumber)
                say(f"I have written your content in {file_path} which is in the responses directory")
                say("Should I read it or not?")
                print("Listening")
                temp = take_command()
                print("Recognizing")
                temp = temp.split()[0]
                if temp.lower() == "yes":
                    say(answer)
                else:
                    say("ok no problem")
            else:
                answer = open_ai(prompt=text)
                say(answer)

        # todo: any other question
        else:
            answer = open_ai(prompt=text)
            say(answer)
