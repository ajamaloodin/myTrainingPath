import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

# escuchar nuestro microfono y devolve el audio como texto

def transformar_audio_en_texto():

    # almacenar el reconocedor en un variable
    r = sr.Recognizer()

    # Configurar el microfono
    with sr.Microphone() as origen:

        # tiempo de espera
        r.pause_threshold = 0.8

        # informar que comenzó la grabación
        print("Ya puedes hablar")

        # Guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            # Buscar en Google
            pedido = r.recognize_google(audio, language='es-ve')

            # prueba de lo que grabo
            print("dijiste: " + pedido)

            # devolver pedido si todo ok
            return pedido

        # EN caso de que no comprenda el audio
        except sr.UnknownValueError:

            # caso de que no entendio el audio
            print("ups! no entendi Joer")

            # devolver error
            return "sigo esperando"

        # En caso de no poder resolver el pedido
        except sr.RequestError:

            # caso de que no entendio el audio
            print("ups! no hay servicio")

            # devolver error
            return "sigo esperando"

        except:

            # caso de que no entendio el audio
            print("ups! algo salio mal")

            # devolver error
            return "sigo esperando"

# Funcion para que el asistente pueda ser escuchado
def hablar(mensaje):

    # Encender el engine de pyttsx3
    engine = pyttsx3.init('dummy')
    engine.setProperty('voice', id2)

    # Diga el mensaje
    engine.say(mensaje)
    engine.runAndWait()


id1 = 'dummy.voice1'
id2 = 'dummy.voice2'
id3 = 'dummy.voice3'

hablar("Hello")