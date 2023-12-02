from flask import Flask, render_template, request

app = Flask(__name__)

# Define your menu dataset
menu = {
    "appetizers": ["Bruschetta", "Spinach Artichoke Dip", "Stuffed Mushrooms"],
    "main_courses": ["Chicken Alfredo", "Grilled Salmon", "Vegetarian Pasta"],
    "desserts": ["Chocolate Lava Cake", "Cheesecake", "Tiramisu"],
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def get_recommendation():
    user_input = request.form['user_input']

    # Implement your NLP logic to interpret user input and recommend a menu item
    recommendation = recommend_menu_item(user_input)

    return render_template('index.html', recommendation=recommendation)

def recommend_menu_item(user_input):
    # Implement your NLP logic here (you can use libraries like spaCy or NLTK)
    # Match user input with menu items and return a recommendation
    # This can be as simple as finding the closest match

    # For simplicity, just return a fixed recommendation for now
    return "Grilled Salmon"

if __name__ == '__main__':
    app.run(debug=True)
