from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample event data
events = [
    {
        "id": 1,
        "name": "Python Workshop",
        "location": "Nairobi",
        "date": "2026-07-01"
    },
    {
        "id": 2,
        "name": "Tech Meetup",
        "location": "Mombasa",
        "date": "2026-07-10"
    }
]


# Home route
@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Event Catalog API"})


# GET all events
@app.route("/events", methods=["GET"])
def get_events():
    return jsonify(events)


# POST a new event
@app.route("/events", methods=["POST"])
def add_event():
    data = request.get_json()

    # Validate input
    if not data:
        return jsonify({"error": "Missing JSON data"}), 400

    required_fields = ["name", "location", "date"]

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"'{field}' is required"}), 400

    new_event = {
        "id": len(events) + 1,
        "name": data["name"],
        "location": data["location"],
        "date": data["date"]
    }

    events.append(new_event)

    return jsonify(new_event), 201


if __name__ == "__main__":
    app.run(debug=True)