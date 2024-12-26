from flask import Flask, send_from_directory, abort
import os

# Initialize the Flask app
app = Flask(__name__)

# Define the directory containing your project files
project_directory = os.getcwd()

@app.route('/<path:filename>', methods=['GET'])
def serve_file(filename):
    """Serve static files from the project directory."""
    try:
        # Serve the requested file
        return send_from_directory(project_directory, filename)
    except FileNotFoundError:
        # Return 404 if the file does not exist
        abort(404)

@app.route('/')
def index():
    """Serve the main entry point (e.g., index.html)."""
    return send_from_directory(project_directory, 'index.html')

if __name__ == '__main__':
    # Run the app on your desired port
    app.run(host='0.0.0.0', port=8880, debug=True)
