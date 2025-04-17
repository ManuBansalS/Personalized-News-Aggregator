from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/news')
def get_news():
    query = request.args.get('q')
    api_key = "bccf553fb72a4370ad6117c590ea43c0"  # Replace this with your real API key

    if not query:
        return jsonify({'error': 'No query provided'}), 400

    try:
        url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}"
        print(f"Requesting: {url}")  # Debug URL
        response = requests.get(url)
        print("Status Code:", response.status_code)
        print("Response Text:", response.text)

        if response.status_code == 200:
            articles = response.json().get('articles', [])
            return jsonify({'articles': articles})
        else:
            return jsonify({'error': f"News API Error: {response.json().get('message', 'Unknown error')}"}), 500

    except Exception as e:
        print(f"Exception occurred: {e}")
        return jsonify({'error': 'Failed to load news articles. Please try again later'}), 500

if __name__ == '__main__':
    app.run(debug=True)
