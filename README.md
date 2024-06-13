# Web Scraper

This project is a web scraper application that allows users to input URLs and receive the scraped content in the desired format (HTML or JSON). The application is built using Python, Flask, Bootstrap, and Tailwind CSS.

## Features

- Scrape web content from multiple URLs.
- Choose between HTML or JSON output formats.
- Display results in a user-friendly interface.
- Responsive design using Bootstrap and Tailwind CSS.

## Technologies Used

- Python
- Flask
- BeautifulSoup
- Requests
- Bootstrap
- Tailwind CSS

## Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- pip (Python package installer)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/your-repository-name.git
    cd your-repository-name
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    - On Windows:
        ```bash
        venv\Scripts\activate
        ```

    - On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```

4. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1. **Start the Flask app:**

    ```bash
    python app.py
    ```

2. **Open your browser and navigate to:**

    ```
    http://127.0.0.1:5000/
    ```

### Usage

1. **Enter URLs:** Input the URLs separated by commas in the provided textarea.
2. **Select Output Format:** Choose the desired output format (HTML or JSON) from the dropdown.
3. **Click Scrape:** Click the "Scrape" button to fetch and display the content.

### Project Structure
project/
│
├── templates/
│ └── index.html
├── static/
│ ├── css/
│ │ └── styles.css
│ ├── js/
│ │ └── script.js
│ └── bootstrap.min.css
├── app.py
├── requirements.txt
└── README.md
