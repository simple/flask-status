# Simple Flask Status Code Responder
This project is a straightforward Flask application designed to respond with HTTP status codes based on the path parameter provided. By passing a valid status code as part of the URL path, the application returns the corresponding HTTP response with that status code.

## Features
### Dynamic Status Code Response:
The app extracts the first three digits from the URL path and attempts to match them to a list of predefined valid HTTP status codes.
### Supported Status Codes:
The application recognizes and responds with the following status codes:
* 200: OK
* 201: Created
* 400: Bad Request
* 401: Unauthorized
* 403: Forbidden
* 404: Not Found
* 500: Internal Server Error
* 502: Bad Gateway
* 503: Service Unavailable
### Fallback Handling:
If an invalid status code is provided or the format doesn't match, the application defaults to returning a 404 Not Found status.
