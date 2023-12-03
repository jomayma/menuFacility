from flask import Flask, render_template, request
import spacy
import random
from spacy.matcher import PhraseMatcher

app = Flask(__name__)

# Define your menu dataset
menu = {
    "appetizers": ["Bruschetta", "Spinach Artichoke Dip", "Stuffed Mushrooms"],
    "main_courses": ["Chicken Alfredo", "Grilled Salmon", "Vegetarian Pasta"],
    "desserts": ["Chocolate Lava Cake", "Cheesecake", "Tiramisu", "Apple"]
}

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Create a PhraseMatcher with menu items
matcher = PhraseMatcher(nlp.vocab, attr='LOWER')
for category, items in menu.items():
    patterns = [nlp.make_doc(item.lower()) for item in items]
    matcher.add(category, None, *patterns)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def get_recommendation():
    user_input = request.form['user_input']

    # Implementing the NLP logic.
    # Processing user input with spaCy.
    # Matching user input with menu items,
    #  and returning a recommendation.
    user_doc = nlp(user_input.lower())
    #user_doc = nlp(user_input)

    # Find matches with the PhraseMatcher
    matches = matcher(user_doc)

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

    return render_template('index.html', recommendation=recommendation)

if __name__ == '__main__':
    app.run(debug=True)
