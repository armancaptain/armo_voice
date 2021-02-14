import pyttsx3 as p3

engine=p3.init
engine.say('hello')
engine.runAndWait()
engine.save_to_file("hello",r"C:\Users\arman\Desktop\ \armo_program\1.mp3")
engine.runAndWait()
