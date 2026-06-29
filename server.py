from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample events data
events = [
    {
        "id": 1,
        "title": "Python Workshop"
    },
    {
        "id": 2,
        "title": "Web Development Bootcamp"
    },
    {
        "id": 3,
        "title": "Tech Meetup"
    }
]

# Home Route
@app.route("/")
def home():
    return jsonify({"message": "Welcome To Event Catalogue API"})


# GET all events
@app.route("/events", methods=["GET"])
def get_events():
    return jsonify(events)


# POST new event
@app.route("/events", methods=["POST"])
def add_event():
    data = request.get_json()

    # Validate input
    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400

    new_event = {
        "id": len(events) + 1,
        "title": data["title"]
    }

    events.append(new_event)

    return jsonify(new_event), 201


if __name__ == "__main__":
    app.run(debug=True)