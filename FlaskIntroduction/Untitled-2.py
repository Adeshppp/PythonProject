
from flask import Flask


# setup application
app = Flask(__name__)


# create a index route
@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(debug=True)

# In this code, we have created a simple Flask application. 
# The app is initialized with the Flask class, 
# and then we define a route ('/') to respond with 'Hello, World!'. 
# Finally, we run the Flask application in debug mode, allowing it to automatically reload changes to the code and display the changes in real-time.