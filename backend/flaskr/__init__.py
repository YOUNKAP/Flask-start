# Import your dependencies
from flask import Flask, jsonify


# Define the create_app function
def create_app(test_config=None):

    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return jsonify({'message':'Hello, World!'})

    @app.route('/smiley')
    def smiley():
        return ':)'

     # Return the app instance
    return app
