import speech_recognition as sr


# class FileAudio:
#     def  __init__(self, file_url):
#         self.text=""
#         self.file_url = file_url
#         print(file_url)

def file_audio_recognise(file_url):
    recognizer = sr.Recognizer()

    text=""
    # ''' recording the sound '''
    
    with sr.AudioFile(file_url) as source:
        recorded_audio = recognizer.listen(source)
        print("Done recording")

    # ''' Recorgnizing the Audio '''
    try:
        print("Recognizing the text")
        text = recognizer.recognize_google(
                recorded_audio, 
                language="en-US"
            )
        print("Decoded Text : {}".format(text))

    except Exception as ex:
        print(ex)

    return text

# file = FileAudio()
# file.file_audio_recognise("test1.wav")