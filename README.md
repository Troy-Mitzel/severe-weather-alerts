# Weather Alert System

A simple Flask web application that fetches live severe weather alerts from the National Weather Service (NWS) and displays them in an easy-to-read format. Users can select a state from a dropdown or use their device's GPS location to see alerts relevant to them. The app also features a modern gradient background, color-coded alert boxes, and a mobile-friendly layout.

## Features

- Displays current severe weather alerts by state
- Color-coded alerts based on severity and type
- Option to use your current location to see local alerts
- Refresh button for the latest updates
- Mobile-friendly and responsive design

## Technologies Used

- Python (Flask)
- HTML / CSS / JavaScript
- Requests library for API calls
- National Weather Service API for live alerts

## Setup / Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<username>/<repo>.git
   cd weather-alert-system
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # macOS/Linux
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask app:
   ```bash
   python app.py
   ```

5. Open your browser and go to `http://127.0.0.1:5000/`

## Notes

- The app displays alerts exactly as provided by the NWS, including the text in special weather statements.
- Requires an internet connection to fetch live alerts.

## License

MIT License
