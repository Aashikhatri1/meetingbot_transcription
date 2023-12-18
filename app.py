from flask import Flask, request, jsonify
from pymongo import MongoClient
import datetime

app = Flask(__name__)

# Connect to MongoDB (Update with your connection string)
client = MongoClient("mongodb+srv://admin:admin@mygitdb.v0gnkoy.mongodb.net")
db = client.Meeting_automation
collection = db.user_data

@app.route('/save_user_info', methods=['POST'])
def save_user_info():
    # Extracting data from request
    data = request.json

    # Extracting each piece of data from the request
    request_id = data.get('request_id')
    meet_link = data.get('meetLink')
    user_id = data.get('user_id')
    status = data.get('status')
    create_date = data.get('create_date', datetime.datetime.now().strftime("%d-%m-%y"))
    created_by = data.get('created_by')

    # Preparing the user_info dictionary
    user_info = {
        "request_id": request_id,
        "meetLink": meet_link,
        "user_id": user_id,
        "status": status,
        "create_date": create_date,
        "created_by": created_by
    }

    # Saving data to MongoDB
    collection.insert_one(user_info)

    return jsonify({"message": "User info saved successfully"}), 201


@app.route('/get_link', methods=['GET'])
def get_link():
    # Extracting id from query parameter
    user_id = request.args.get('id')

    # Generating the link
    if user_id:
        link = 'https://salescrm247.s3.amazonaws.com/' + user_id
        return jsonify({"link": link}), 200
    else:
        return jsonify({"error": "Missing id parameter"}), 400

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)
