$ Help me to implement a NLP logic in python, using libraries like spaCy or NLTK. Match user input with menu items and return a recommendation, finding the closest match.
>>>>>>
Certainly! I'll provide you with a basic example of how you can use spaCy for NLP and find the closest match between the user input and menu items. Make sure to install spaCy before running this example:

```bash
pip install spacy
```
NOTA JORGE begin
With spaCy installed in your virtual environment, you’re almost ready to get started with NLP. But there’s one more thing you’ll have to install:
```bash
python -m spacy download en_core_web_sm
```
end

Now, let's modify the `app.py` script to include spaCy for NLP:

```python
from flask import Flask, render_template, request
import spacy
from spacy.matcher import PhraseMatcher

app = Flask(__name__)

# Define your menu dataset
menu = {
    "appetizers": ["Bruschetta", "Spinach Artichoke Dip", "Stuffed Mushrooms"],
    "main_courses": ["Chicken Alfredo", "Grilled Salmon", "Vegetarian Pasta"],
    "desserts": ["Chocolate Lava Cake", "Cheesecake", "Tiramisu"],
}

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Create a PhraseMatcher with menu items
matcher = PhraseMatcher(nlp.vocab)
for category, items in menu.items():
    patterns = [nlp(item) for item in items]
    matcher.add(category, None, *patterns)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def get_recommendation():
    user_input = request.form['user_input']

    # Process user input with spaCy
    user_doc = nlp(user_input.lower())

    # Find matches with the PhraseMatcher
    matches = matcher(user_doc)

    if matches:
        # Get the category with the most matches
        best_match = max(matches, key=lambda x: len(x[1]))

        # Extract the category name
        category = best_match[0]

        # Get a random recommendation from the selected category
        recommendation = menu[category][0]
    else:
        # No match found, provide a default recommendation
        recommendation = "Sorry, we couldn't find a match. Please try again."

    return render_template('index.html', recommendation=recommendation)


if __name__ == '__main__':
    app.run(debug=True)
```

In this example, we use spaCy's `PhraseMatcher` to find matches between the user input and the menu items. The `en_core_web_sm` model is used for English language processing. If a match is found, the system selects the category with the most matches and recommends the first item from that category.

Remember to adjust the logic based on your specific requirements and use a larger and more diverse menu dataset for better results.