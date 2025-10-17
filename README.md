# 💾 Flask Backend — Soil Moisture Monitoring System

## 📘 Overview
The **Flask backend** serves as the central data hub for the **Soil Moisture Monitoring System**.  
It receives live soil moisture data from the **ESP32**, processes it, and provides endpoints for the **web dashboard** to visualize readings in real time.

---

## ⚙️ Key Functions

| Function | Description |
|-----------|-------------|
| **Data Receiver** | Accepts live soil moisture readings from the ESP32 via HTTP POST requests (`/api/soil`). |
| **Data Provider** | Returns the latest stored data as JSON to the frontend via GET requests (`/api/data`). |
| **Dashboard Renderer** | Serves a web-based dashboard at `/dashboard` to display current moisture levels, alerts, and trends. |
| **Alert Logic** | Detects critical moisture levels and marks them for frontend visualization. |

---

## 🧠 How It Works

ESP32 ---> POST /api/soil ---> [Flask Server] ---> GET /api/data ---> Web Dashboard


- The **ESP32** continuously measures soil moisture and sends readings as JSON.  
- The **Flask server** receives and stores the latest reading.  
- The **Frontend Dashboard** fetches this data at intervals (e.g., every 2 seconds) for live updates.  

---

## 🧾 API Endpoints

| Method | Endpoint | Description |
|--------|-----------|-------------|
| `POST` | `/api/soil` | Receives JSON from ESP32: `{ "raw": <int>, "percent": <int>, "state": <string> }` |
| `GET` | `/api/data` | Returns the latest sensor data in JSON for the frontend |
| `GET` | `/dashboard` | Renders the live monitoring dashboard |

### Example POST Payload
```json
{
  "raw": 2785,
  "percent": 54,
  "state": "medium"
}

Example GET Response

{
  "raw": 2785,
  "percent": 54,
  "state": "medium",
  "timestamp": "2025-10-17T10:25:00Z"
}

💻 Installation & Setup
1️⃣ Install Dependencies

Make sure you have Python 3.10+ installed.

pip install flask flask-cors requests

2️⃣ Run the Server

python app.py

By default, Flask will start the backend on:

http://localhost:5000

3️⃣ Test API Endpoints

You can use Postman or curl to test:

curl -X POST http://localhost:5000/api/soil -H "Content-Type: application/json" -d '{"raw": 2500, "percent": 60, "state": "medium"}'

🌐 Communication Flow
Source	Destination	Protocol	Frequency
ESP32	Flask /api/soil	HTTP POST	Every 2 seconds
Flask	Frontend /api/data	HTTP GET	Every 2 seconds
📈 Future Enhancements

    Store readings in SQLite or Firebase

    Add timestamped logs for historical visualization

    Integrate AI prediction (e.g., soil dryness forecast)

    Support user authentication and multi-sensor nodes

👨🏽‍💻 Author

Backend Developer: Emmanuel Tigo5
🏁 License

This backend is part of the soil moisture monitoring system project and is licensed under the MIT License.
