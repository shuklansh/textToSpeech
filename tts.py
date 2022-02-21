import pyttsx3

x = True
text = pyttsx3.init()
text = pyttsx3.init()
voices = text.getProperty('voices')
text.setProperty('voice', voices[1].id) #1 for female voice, 0 for male voice


def speak(s):
    text.say(s)
    text.runAndWait()


speak("what do you want me to say")

ans = input("enter:")

while x:
    if ans != "nothing":
        speak(ans)
        speak("anything else?")
        ans = input("enter:")

    else:

        speak("alright, catch ya later")
        x = False
