from flask import Flask, render_template, request
import spacy
import random
import time
from spacy.matcher import PhraseMatcher
import speech_recognition as sr

app = Flask(__name__)

# Define your menu dataset
menu = {
    "Entrantes": ["Tostada con tomate y jamon", "Setas estofadas", "Guisantes con jamon"],
    "main_courses": ["Pollo asado", "Salmon a la plancha", "Pasta Vegetariana"],
    "desserts": ["Pastel de chocolate", "Tarta de queso", "Flan", "Pastel de manzana"]
}
speech_recognized = "init"

# Load spaCy model
nlp = spacy.load("es_core_news_sm")

# Create a PhraseMatcher with menu items
matcher = PhraseMatcher(nlp.vocab, attr='LOWER')
for category, items in menu.items():
    patterns = [nlp.make_doc(item.lower()) for item in items]
    matcher.add(category, None, *patterns)

def transcribe_voice_to_text():
    recognizer = sr.Recognizer()
    audio = recognizer.get_audio_input()
    text = recognizer.recognize_google(audio)
    print(text)

def reconocer_voz():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Di algo:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5)

    try:
        speech_recognized = recognizer.recognize_google(audio, language="es-ES")
        print("Transcripción: " + speech_recognized)
        return speech_recognized
    except sr.UnknownValueError:
        print("No se pudo entender la voz")
    except sr.RequestError as e:
        print("Error en la solicitud a la API de Google: {0}".format(e))


@app.route('/')
def index():
    return render_template('index-speech.html')


@app.route('/', methods=['POST'])
def get_recommendation():
    speech_recognized = reconocer_voz()
    #time.sleep(5)
    print("speech_recognized: "+speech_recognized)
    #user_input = request.form['user_input']
    user_input = speech_recognized
    print("user_input: "+user_input)

    # Implementing the NLP logic.
    # Processing user input with spaCy.
    # Matching user input with menu items,
    #  and returning a recommendation.
    user_doc = nlp(user_input.lower())
    #user_doc = nlp(user_input)

    # Find matches with the PhraseMatcher
    matches = matcher(user_doc)
    print(" ".join([token.lemma_ for token in user_doc]))
    
    if matches:
        print(matches)
        # Get the category with the most matches
        # best_match = max(matches, key=lambda x: len(x[0]))
        # best_match = max(matches)
        def most_frequent(List):
            return max(set(List), key = List.count)

        best_match = most_frequent(matches)

       
        # Extract the category name
        category_id_string = nlp.vocab.strings[best_match[0]]
        print("best categoy: ", category_id_string)

        # Get a random recommendation from the selected category
        recommendation = "(" + category_id_string + ") " + random.choice(menu[category_id_string])
    else:
        # No match found, provide a default recommendation
        recommendation = "Sorry, we couldn't find a match. Please try again."

    return render_template('index-speech.html', recommendation=recommendation, user_input=user_input)

if __name__ == '__main__':
    app.run(debug=True)
