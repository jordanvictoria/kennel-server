# import json
# from http.server import BaseHTTPRequestHandler, HTTPServer
# from views import get_all_animals, get_single_animal, create_animal, delete_animal, update_animal
# from views import get_all_locations, get_single_location, create_location, delete_location, update_location
# from views import get_all_employees, get_single_employee, create_employee, delete_employee, update_employee
# from views import get_all_customers, get_single_customer, create_customer, delete_customer, update_customer


# method_mapper = { 
#     "animals": {
#         "single": get_single_animal,
#         "all": get_all_animals
#     },
#     "locations": {
#         "single": get_single_location,
#         "all": get_all_locations
#     },
#     "employees": {
#         "single": get_single_employee,
#         "all": get_all_employees
#     },
#     "customers": {
#         "single": get_single_customer,
#         "all": get_all_customers
#     }
# }

# # Here's a class. It inherits from another class.
# # For now, think of a class as a container for functions that
# # work together for a common purpose. In this case, that
# # common purpose is to respond to HTTP requests from a client.
# class HandleRequests(BaseHTTPRequestHandler):
#     """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
#     """

#     def parse_url(self, path):
#         """Method docstring."""
#         # Just like splitting a string in JavaScript. If the
#         # path is "/animals/1", the resulting list will
#         # have "" at index 0, "animals" at index 1, and "1"
#         # at index 2.
#         path_params = path.split("/")
#         resource = path_params[1]
#         id = None

#         # Try to get the item at index 2
#         try:
#             # Convert the string "1" to the integer 1
#             # This is the new parseInt()
#             id = int(path_params[2])
#         except IndexError:
#             pass  # No route parameter exists: /animals
#         except ValueError:
#             pass  # Request had trailing slash: /animals/

#         return (resource, id)  # This is a tuple

#     # Here's a class function

#     # Here's a method on the class that overrides the parent's method.
#     # It handles any GET request.
#     def do_GET(self):
#         """Method docstring."""
#         response = None
#         (resource, id) = self.parse_url(self.path)
#         response = self.get_all_or_single(resource, id)
#         self.wfile.write(json.dumps(response).encode())

#     def get_all_or_single(self, resource, id):
#         """Method docstring."""
#         if id is not None:
#             response = method_mapper[resource]["single"](id)

#             if response is not None:
#                 self._set_headers(200)
#             else:
#                 self._set_headers(404)
#                 response = ''
#         else:
#             self._set_headers(200)
#             response = method_mapper[resource]["all"]()

#         return response

#     # def do_GET(self):
#     #     # This is a Docstring it should be at the beginning of all classes and functions
#     #     # It gives a description of the class or function
#     #     """Handles GET requests to the server
#     #     """
#     #     # Set the response code to 'Ok'
#     #     # self._set_headers(200)
#     #     response = {}

#     #     # Your new console.log() that outputs to the terminal
#     #     # Parse the URL and capture the tuple that is returned
#     #     (resource, id) = self.parse_url(self.path)

#     #     # It's an if..else statement
#     #     if resource == "animals":
#     #         if id is not None:
#     #             response = get_single_animal(id)
#     #             if response is None:
#     #                 self._set_headers(404)
#     #                 response = { "message": f"Animal {id} is out playing right now" }

#     #         else:
#     #             response = get_all_animals()

#     #     # It's an if..else statement
#     #     if resource == "locations":
#     #         if id is not None:
#     #             response = get_single_location(id)
#     #             if response is None:
#     #                 self._set_headers(404)
#     #                 response = { "message": f"Location {id} does not exist" }

#     #         else:
#     #             response = get_all_locations()

#     #     # It's an if..else statement
#     #     if resource == "employees":
#     #         if id is not None:
#     #             response = get_single_employee(id)
#     #             if response is None:
#     #                 self._set_headers(404)
#     #                 response = { "message": f"Employee {id} does not exist" }

#     #         else:
#     #             response = get_all_employees()

#     #     # It's an if..else statement
#     #     if resource == "customers":
#     #         if id is not None:
#     #             response = get_single_customer(id)
#     #             if response is None:
#     #                 self._set_headers(404)
#     #                 response = { "message": f"Customer {id} does not exist" }

#     #         else:
#     #             response = get_all_customers()
#     #     if response is not None:
#     #         self._set_headers(200)
#     #     # Send a JSON formatted string as a response
#     #     self.wfile.write(json.dumps(response).encode())

#     # # Here's a method on the class that overrides the parent's method.
#     # # It handles any POST request.
#     def do_POST(self):
#         """Handles POST requests to the server"""

#         # Set response code to 'Created'
#         self._set_headers(201)

#         content_len = int(self.headers.get('content-length', 0))
#         post_body = self.rfile.read(content_len)

#         # Convert JSON string to a Python dictionary
#         post_body = json.loads(post_body)

#         # Parse the URL
#         (resource, id) = self.parse_url(self.path)

#         # Initialize new animal
#         new_animal = None
#         new_location = None
#         new_employee = None
#         new_customer = None

#         # Add a new animal to the list. Don't worry about
#         # the orange squiggle, you'll define the create_animal
#         # function next.
#         if resource == "animals":
#             new_animal = create_animal(post_body)
#         # Encode the new animal and send in response
#             self.wfile.write(json.dumps(new_animal).encode())
#         if resource == "locations":
#             if "name" in post_body and "address" in post_body:
#                 self._set_headers(201)
#                 new_location = create_location(post_body)
#             else:
#                 self._set_headers(400)
#                 new_location = {
#                 "message": f'{"name is required" if "name" not in post_body else ""} {"address is required" if "address" not in post_body else ""}'
#                 }
#             self.wfile.write(json.dumps(new_location).encode())
#         if resource == "employees":
#             new_employee = create_employee(post_body)
#             self.wfile.write(json.dumps(new_employee).encode())
#         if resource == "customers":
#             new_customer = create_customer(post_body)
#             self.wfile.write(json.dumps(new_customer).encode())

#     def do_DELETE(self):
#         """Handles DELETE requests to the server"""
#         # Set a 204 response code
#         # self._set_headers(204)
#         response = None
#         # Parse the URL
#         (resource, id) = self.parse_url(self.path)

#         # Delete a single animal from the list
#         if resource == "animals":
#             self._set_headers(204)
#             delete_animal(id)
#             response = ""
#         # Encode the new animal and send in response
#         if resource == "locations":
#             self._set_headers(204)
#             delete_location(id)
#             response = ""
#         # Encode the new location and send in response
#         if resource == "employees":
#             self._set_headers(204)
#             delete_employee(id)
#             response = ""
#         # Encode the new employee and send in response
#         if resource == "customers":
#             self._set_headers(405)
#             response = { "message": "Deleting customers requires contacting the company directly." }
#         # Encode the new customer and send in response
#         self.wfile.write(json.dumps(response).encode())
#         # A method that handles any PUT request.
#     def do_PUT(self):
#         """Handles PUT requests to the server"""
#         self._set_headers(204)
#         content_len = int(self.headers.get('content-length', 0))
#         post_body = self.rfile.read(content_len)
#         post_body = json.loads(post_body)

#         # Parse the URL
#         (resource, id) = self.parse_url(self.path)

#         # Delete a single animal from the list
#         if resource == "animals":
#             update_animal(id, post_body)

#         # Encode the new animal and send in response
#         self.wfile.write("".encode())
#         if resource == "locations":
#             update_location(id, post_body)

#         # Encode the new animal and send in response
#         self.wfile.write("".encode())
#         if resource == "employees":
#             update_employee(id, post_body)

#         # Encode the new animal and send in response
#         self.wfile.write("".encode())
#         if resource == "customers":
#             update_customer(id, post_body)

#         # Encode the new animal and send in response
#         self.wfile.write("".encode())

#     def _set_headers(self, status):
#         # Notice this Docstring also includes information about the arguments passed to the function
#         """Sets the status code, Content-Type and Access-Control-Allow-Origin
#         headers on the response

#         Args:
#             status (number): the status code to return to the front end
#         """
#         self.send_response(status)
#         self.send_header('Content-type', 'application/json')
#         self.send_header('Access-Control-Allow-Origin', '*')
#         self.end_headers()

#     # Another method! This supports requests with the OPTIONS verb.
#     def do_OPTIONS(self):
#         """Sets the options headers
#         """
#         self.send_response(200)
#         self.send_header('Access-Control-Allow-Origin', '*')
#         self.send_header('Access-Control-Allow-Methods',
#                          'GET, POST, PUT, DELETE')
#         self.send_header('Access-Control-Allow-Headers',
#                          'X-Requested-With, Content-Type, Accept')
#         self.end_headers()


# # This function is not inside the class. It is the starting
# # point of this application.
# def main():
#     """Starts the server on port 8088 using the HandleRequests class
#     """
#     host = ''
#     port = 8088
#     HTTPServer((host, port), HandleRequests).serve_forever()


# if __name__ == "__main__":
#     main()
