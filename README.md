# Currency Converter App

A web application for real-time currency conversion using the CurrencyLayer API.

## Features
- Real-time currency conversion
- Clean, responsive interface
- Docker container support
- Flask backend with RESTful API

## Tech Stack
- **Frontend**: HTML5, CSS3
- **Backend**: Python, Flask
- **Deployment**: Docker
- **API**: [CurrencyLayer API](https://currencylayer.com/)

## Prerequisites
- Python 3.8+
- Docker (optional for containerized deployment)
- CurrencyLayer API key (free tier available)

## Setup & Installation

### Local Development
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/currency-converter.git
   cd currency-converter
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure API key:
   - Option 1: Create `.env` file:
     ```bash
     echo "API_KEY=your_currencylayer_api_key" > .env
     ```
   - Option 2: Edit `main.py` directly:
     ```python
     API_KEY = "your_currencylayer_api_key"
     ```

4. Run the application:
   ```bash
   python main.py
   ```

5. Access the app at: `http://localhost:5000`

### Docker Deployment
1. Pull the Docker image:
   ```bash
   docker pull preygle/currency-converter-app
   ```

2. Run the container (replace `your_api_key`):
   ```bash
   docker run -p 5000:5000 -e API_KEY=your_api_key preygle/currency-converter-app
   ```

3. Access the app at: `http://localhost:5000`

## Usage
1. Select base currency from dropdown
2. Enter amount to convert
3. Select target currency
4. Click "Convert" to see results

## Project Structure
```
.
├── main.py              # Flask application
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker configuration
├── static/              # Static files (CSS, JS)
│   └── style.css
├── templates/           # HTML templates
│   ├── index.html
│   └── result.html
├── .env                 # Environment variables
└── README.md            # This file
```

## Contributing
Pull requests welcome. For major changes, please open an issue first.

## License
[MIT](https://choosealicense.com/licenses/mit/)
