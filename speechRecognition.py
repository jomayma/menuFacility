import speech_recognition as sr

def reconocer_voz():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Di algo:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5)

    try:
        print("Transcripción: " + recognizer.recognize_google(audio, language="es-ES"))
    except sr.UnknownValueError:
        print("No se pudo entender la voz")
    except sr.RequestError as e:
        print("Error en la solicitud a la API de Google: {0}".format(e))

if __name__ == "__main__":
    reconocer_voz()