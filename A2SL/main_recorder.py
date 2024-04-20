import speech_recognition as sr


def recognizer_speech(statement_label):
    recognizer = sr.Recognizer()
    
    statement_label.configure(text="Adjusting noise")
    statement_label.update()
    with sr.Microphone() as source:
        print("Adjusting noise")
        recognizer.adjust_for_ambient_noise(source, duration=1)
    
    statement_label.configure(text="Speak - Recording for 4 seconds")
    statement_label.update()
    with sr.Microphone() as source:
        print("Recording for 4 seconds")
        recorded_audio = recognizer.listen(source, timeout=4)
        print("Done recording")

    statement_label.configure(text="Done Recording")
    statement_label.update()

    text=""

    try:
        print("Recognizing the text")
        statement_label.configure(text="Recognizing Text")
        statement_label.update()
        # Use the recognized audio to get string output
        text = recognizer.recognize_google(
                recorded_audio, 
                language="en-US"
            )
        
        print("Decoded Text : {}".format(text))
        statement_label.configure(text="All Done")
        statement_label.update()

    except Exception as ex:
        print(ex)
        statement_label.configure(text=ex)
        statement_label.update()

    sr.Microphone.list_microphone_names()
    return text

# def text_final(label):
#     label.configure(text="a")
#     label.update()
