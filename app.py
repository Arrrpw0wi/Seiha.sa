from flask import Flask, request, jsonify, render_template
import csv

app = Flask(__name__)

# Function to verify username and password from CSV
def verify_credentials(username, password):
    with open('users.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row['username'] == username and row['password'] == password:
                return {"status": "success", "data": row}
    return {"status": "failed", "message": "Invalid username or password"}

# Route to handle POST request for verification
@app.route('/check', methods=['POST'])
def check():
    username = request.form.get('username')
    password = request.form.get('password')
    result = verify_credentials(username, password)
    return jsonify(result)

# Route to serve the HTML file
@app.route('/')
def index():
    return render_template('spk.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)), debug=False)

