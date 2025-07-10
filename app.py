from flask import Flask, abort, make_response
import re

app = Flask(__name__)

@app.route('/<path:subpath>', methods=['GET', 'PUT', 'POST'])
def return_status(subpath):
    # Use regex to extract the first three digits
    match = re.match(r'^(\d{3})', subpath)
    if match:
        status_code = int(match.group(1))

        # Define valid status codes and their messages
        valid_status_codes = {
            200: "OK",
            201: "Created",
            400: "Bad Request",
            401: "Unauthorized",
            403: "Forbidden",
            404: "Not Found",
            500: "Internal Server Error",
            502: "Bad Gateway",
            503: "Service Unavailable"
        }

        # Check if the status code is valid
        if status_code in valid_status_codes:
            message = valid_status_codes[status_code]
            return make_response(message, status_code)

    # If the status code is not valid or no match, return 404
    abort(404)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
