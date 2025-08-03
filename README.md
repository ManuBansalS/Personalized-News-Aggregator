# Personalized News Aggregator

A web-based personalized news aggregator built using **Flask**, **HTML**, **CSS**, **JavaScript**, and the **News API**. This application allows users to search for news based on different categories or specific keywords and view relevant news articles in an attractive and responsive interface.

## Features

- **Category-based News**: Get news from specific categories like IPL, Finance, and Politics.
- **Search Functionality**: Search for news based on any topic (e.g., Science, Technology).
- **Responsive Design**: Mobile-friendly design that adapts to various screen sizes.
- **Dynamic News Cards**: News articles are dynamically fetched and displayed in card format with images, titles, descriptions, and sources.
- **News API Integration**: The app fetches the latest articles from NewsAPI, ensuring real-time news updates.

## Prerequisites

- **Python 3.x**
- **Flask** (`pip install flask`)
- **Requests** (`pip install requests`)
- **News API Key** (Free API key from [NewsAPI](https://newsapi.org/))

## Setup and Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <project-folder>
```

### 2. Install Dependencies

Make sure you have Python installed, then install the required packages:

```bash
pip install -r requirements.txt
```

### 3. Create a `requirements.txt`

If you don't already have a `requirements.txt`, create one and add the following:

```
Flask==2.1.1
requests==2.27.1
```

### 4. Get Your NewsAPI Key

- Go to [NewsAPI](https://newsapi.org/) and create an account.
- Get your API key and replace `YOUR_API_KEY` in the `app.py` file with your actual API key.

### 5. Run the Application

Once everything is set up, run the Flask application:

```bash
python app.py
```

The app will be hosted locally at `http://127.0.0.1:5000/`.

Open the URL in your browser to start using the app.

## Usage

- **Home Page**: The main page displays the categories like IPL, Finance, and Politics, along with a search bar.
- **Category Selection**: Clicking on a category will display relevant news articles.
- **Search**: Enter a topic in the search bar (e.g., "Science") and click the search button to fetch news articles related to the topic.
- **News Cards**: Each news card displays an image, title, description, and the source with the published date. Clicking on a card will open the article in a new tab.

## Code Overview

### Frontend

- **HTML**: The structure of the webpage, including navigation and news cards.
- **CSS**: Styles for the webpage, providing a clean and responsive layout.
- **JavaScript**: Handles fetching data from the Flask backend and populating the webpage with news articles dynamically.

### Backend

- **Flask**: The Python web framework used to host the app and handle requests.
- **NewsAPI**: Fetches the latest news articles based on the search query or category.

### Flask API Route

- `/news?q=<query>`: Fetches news articles based on the search query or category using NewsAPI and returns the articles in JSON format.

### JavaScript Fetch

- **fetchNews(query)**: Sends a GET request to the backend and updates the news cards on the webpage.

### Error Handling

- If an error occurs while fetching news (e.g., invalid API key or network issues), the app displays an alert with a message: `Failed to load news articles. Please try again later`.

## Folder Structure

```
Personalized-News-Aggregator/
│
├── app.py                # Flask backend
├── templates/            # HTML files
│   └── index.html        # Main HTML template
├── static/               # Static files (CSS, JS, images)
│   ├── css/
│   │   └── style.css     # Styles for the app
│   ├── js/
│   │   └── script.js     # JavaScript for dynamic functionality
│   └── favicon.ico       # Favicon for the app
├── requirements.txt      # List of dependencies
└── README.md             # Project documentation
```
