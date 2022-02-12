import pyttsx3

x = True

text = pyttsx3.init()

text.say("what do you want me to say?")
text.runAndWait()
ans = input("enter:")

while x==True:
    if(ans!="nothing"):
        text.say(ans)
        text.runAndWait()
        text.say("anything else?")
        text.runAndWait()
        ans = input("enter:")

    else:

        text.say("alright, catch ya later")
        text.runAndWait()
        x = False
