import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from repository import all, retrieve, create, update, delete




# Here's a class. It inherits from another class.
# For now, think of a class as a container for functions that
# work together for a common purpose. In this case, that
# common purpose is to respond to HTTP requests from a client.
class HandleRequests(BaseHTTPRequestHandler):
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """

    def parse_url(self, path):
        """Method docstring."""
        # Just like splitting a string in JavaScript. If the
        # path is "/animals/1", the resulting list will
        # have "" at index 0, "animals" at index 1, and "1"
        # at index 2.
        path_params = path.split("/")
        resource = path_params[1]
        id = None

        # Try to get the item at index 2
        try:
            # Convert the string "1" to the integer 1
            # This is the new parseInt()
            id = int(path_params[2])
        except IndexError:
            pass  # No route parameter exists: /animals
        except ValueError:
            pass  # Request had trailing slash: /animals/

        return (resource, id)  # This is a tuple

    # Here's a class function

    # Here's a method on the class that overrides the parent's method.
    # It handles any GET request.
    # def do_GET(self):
    #     """Method docstring."""
    #     response = None
    #     (resource, id) = self.parse_url(self.path)
    #     response = self.get_all_or_single(resource, id)
    #     self.wfile.write(json.dumps(response).encode())

    # def get_all_or_single(self, resource, id):
    #     """Method docstring."""
    #     if id is not None:
    #         response = method_mapper[resource]["single"](id)

    #         if response is not None:
    #             self._set_headers(200)
    #         else:
    #             self._set_headers(404)
    #             response = ''
    #     else:
    #         self._set_headers(200)
    #         response = method_mapper[resource]["all"]()

    #     return response

    def do_GET(self):
        # This is a Docstring it should be at the beginning of all classes and functions
        # It gives a description of the class or function
        """Handles GET requests to the server
        """
        # Set the response code to 'Ok'
        # self._set_headers(200)
        response = {}

        # Your new console.log() that outputs to the terminal
        # Parse the URL and capture the tuple that is returned
        (resource, id) = self.parse_url(self.path)

        # It's an if..else statement
        if id is not None:
            response = retrieve(resource, id)

            if response is not None:
                self._set_headers(200)
            else:
                self._set_headers(404)
                response = ''

        else:
            self._set_headers(200)
            response = all(resource)
        # Send a JSON formatted string as a response
        self.wfile.write(json.dumps(response).encode())

    # # Here's a method on the class that overrides the parent's method.
    # # It handles any POST request.
    def do_POST(self):
        """Handles POST requests to the server"""

        # Set response code to 'Created'
        self._set_headers(201)

        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        # Convert JSON string to a Python dictionary
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Initialize new animal
        new_post = None

        # Add a new animal to the list. Don't worry about
        # the orange squiggle, you'll define the create_animal
        # function next.
        new_post = create(resource, post_body)
        self.wfile.write(json.dumps(new_post).encode())
    def do_DELETE(self):
        """Handles DELETE requests to the server"""
        # Set a 204 response code
        # self._set_headers(204)
        response = None
        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        if resource == "customers":
            self._set_headers(405)
            response = { "message": "Deleting customers requires contacting the company directly." }
        else:
            self._set_headers(204)
            delete(resource, id)
            response = ""
        # Encode the new customer and send in response
        self.wfile.write(json.dumps(response).encode())
        # A method that handles any PUT request.
    def do_PUT(self):
        """Handles PUT requests to the server"""
        self._set_headers(204)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Delete a single animal from the list
        update(resource, id, post_body)

        # Encode the new animal and send in response
        self.wfile.write("".encode())

    def _set_headers(self, status):
        # Notice this Docstring also includes information about the arguments passed to the function
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    # Another method! This supports requests with the OPTIONS verb.
    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                         'X-Requested-With, Content-Type, Accept')
        self.end_headers()


# This function is not inside the class. It is the starting
# point of this application.
def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
