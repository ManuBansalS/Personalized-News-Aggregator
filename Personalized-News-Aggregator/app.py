from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/news')
def get_news():
    query = request.args.get('q')
    api_key = "bccf553fb72a4370ad6117c590ea43c0"  
    try:
        response = requests.get(f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}")
        if response.status_code == 200:
            articles = response.json().get('articles', [])
            return jsonify({'articles': articles})
        else:
            return jsonify({'error': 'Failed to load news articles. Please try again later'}), 500
    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({'error': 'Failed to load news articles. Please try again later'}), 500

if __name__ == '__main__':
    app.run(debug=True)

