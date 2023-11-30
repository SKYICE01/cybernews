from flask import Flask, render_template
from cybernews.cybernews import *

app = Flask(__name__)
news_api = CyberNews()

# Define categories as a global variable
categories = [
    "general", "dataBreach", "cyberAttack", "vulnerability",
    "malware", "security", "cloud", "tech", "iot", "bigData",
    "business", "mobility", "research", "corporate", "socialMedia"
]

@app.route('/')
def home():
    return render_template('home.html', categories=categories)

@app.route('/<category>')
def show_news(category):
    # No need to define valid_categories again, just use the global categories list
    if category not in categories:
        return "Category not found", 404

    articles = news_api.get_news(category)
    return render_template('news.html', articles=articles, category=category.capitalize())

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
