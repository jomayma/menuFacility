Certainly! To create an interactive chat for a menu recommendation system, you can use a combination of natural language processing (NLP) and a predefined menu dataset. You'll need a programming language like Python and a framework like Flask for a basic web application. Here's a simplified example using Python and Flask:

1. Install Flask:
   ```
   pip install Flask
   ```

2. Create a Python script (e.g., `app.py`):
   ```python
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
   ```

3. Create a templates folder with an `index.html` file:
   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Menu Recommender</title>
   </head>
   <body>
       <h1>Menu Recommender</h1>
       <form method="post">
           <label for="user_input">Ask for a menu recommendation:</label>
           <input type="text" name="user_input" id="user_input" required>
           <button type="submit">Get Recommendation</button>
       </form>
       {% if recommendation %}
           <p>Your recommendation: {{ recommendation }}</p>
       {% endif %}
   </body>
   </html>
   ```

4. Run your app:
   ```
   python app.py
   ```

Now, when you visit `http://127.0.0.1:5000/` in your browser, you can input a natural language request, and the app will provide a menu recommendation based on your predefined logic.

Keep in mind that this is a basic example, and you may need to enhance the NLP logic and expand your dataset for a more robust system.