from flask import Flask, request, jsonify, render_template
import requests
from bs4 import BeautifulSoup
import json
app = Flask(__name__)

def scrape_website(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.text

def parse_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup

def format_output(data, output_format='html'):
    if output_format == 'html':
        return str(data)
    elif output_format == 'json':
        return json.dumps(data, indent=4)
    else:
        raise ValueError("Unsupported format. Please choose either 'html' or 'json'.")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    data = request.get_json()
    urls = data['urls'].split(',')
    output_format = data['outputFormat']

    results = []
    for url in urls:
        url = url.strip()
        try:
            html_content = scrape_website(url)
            soup = parse_html(html_content)
            if output_format == 'json':
                result_data = {
                    'title': soup.title.string if soup.title else '',
                    'body': soup.body.get_text() if soup.body else ''
                }
            else:
                result_data = soup.prettify()
            formatted_output = format_output(result_data, output_format)
            results.append(formatted_output)
        except Exception as e:
            return jsonify({'error': str(e)}), 400

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
