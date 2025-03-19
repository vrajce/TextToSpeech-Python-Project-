import pyttsx3

engine = pyttsx3.init()

while (True):

    command = input("Enter What you Want me to say : ")
    if(command.lower() == "quit"):
        engine.say("bye byee ")
        engine.runAndWait()
        break
    engine.say(command)
    engine.runAndWait()
