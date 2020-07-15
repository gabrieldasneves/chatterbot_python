import speech_recognition as sr

def listen_micro():
    micro = sr.Recognizer()
    with sr.Microphone() as source:
        micro.adjust_for_ambient_noise(source)
        print("Diga alguma coisa: ")
        audio  = micro.listen(source)

    try:
    
        frase = micro.recognize_google(audio,language='pt-BR')
    
        print("Você disse: " + frase)
    except sr.UnkownValueError:
        print("Não entendi")
        
    

    return frase

listen_micro()