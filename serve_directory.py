from flask import Flask, send_from_directory, abort
import os

# Initialize the Flask app
app = Flask(__name__)

# Get the current working directory
current_directory = os.getcwd()

@app.route('/<path:filename>', methods=['GET'])
def serve_file(filename):
    """Serve files from the current directory."""
    try:
        # Ensure file exists
        return send_from_directory(current_directory, filename)
    except FileNotFoundError:
        # Return 404 if the file does not exist
        abort(404)

@app.route('/')
def index():
    """List all files in the current directory."""
    try:
        files = os.listdir(current_directory)
        return "<br>".join(f"<a href='/{file}'>{file}</a>" for file in files)
    except Exception as e:
        return f"Error: {e}", 500

if __name__ == '__main__':
    # Run the app on port 5000
    app.run(host='0.0.0.0', port=8880, debug=True)
