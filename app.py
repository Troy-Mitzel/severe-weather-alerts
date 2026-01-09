from flask import Flask, render_template, request
import requests

app = Flask(__name__)

NWS_URL = "https://api.weather.gov/alerts/active"

STATES = ['All States', 'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut',
          'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas',
          'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota',
          'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey',
          'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon',
          'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah',
          'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

@app.route("/")
def index():
    selected_state = request.args.get('state', 'All States')
    lat = request.args.get('lat')
    lon = request.args.get('lon')

    if lat and lon:
        try:
            # Reverse geocode lat/lon to get state name
            nominatim_url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}&zoom=5&addressdetails=1"
            response = requests.get(nominatim_url, headers={"User-Agent": "WeatherAlertApp"})
            location_data = response.json()
            state_from_geo = location_data.get('address', {}).get('state')
            if state_from_geo and state_from_geo in STATES:
                selected_state = state_from_geo
            else:
                selected_state = 'All States'
        except Exception:
            selected_state = 'All States'

    headers = {
        "User-Agent": "WeatherAlertApp (example@example.com)"
    }
    response = requests.get(NWS_URL, headers=headers)
    data = response.json()

    alerts = data.get("features", [])

    # Filter out test alerts or those with unknown severity or event containing 'test'
    filtered_alerts = []
    for alert in alerts:
        props = alert.get('properties', {})
        event = props.get('event', '').lower()
        severity = props.get('severity', '').lower()

        if "test" in event or severity == "unknown":
            continue

        if selected_state != 'All States':
            if selected_state.lower() not in props.get('areaDesc', '').lower():
                continue

        filtered_alerts.append(alert)

    return render_template("index.html", alerts=filtered_alerts, states=STATES, selected_state=selected_state)

if __name__ == "__main__":
    app.run(debug=True)
