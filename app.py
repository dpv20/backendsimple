from flask import Flask
from flask_cors import CORS
from api.email.send_email import email_bp  # Import the email blueprint

# Load configuration settings from config.py
def create_app():
    app = Flask(__name__)

    # Load the configuration from the Config class in config.py
    app.config.from_object('config.Config')

    # Register the email blueprint
    app.register_blueprint(email_bp, url_prefix='/api/email')

    return app

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=8080, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app = create_app()

    # Enable CORS for the frontend to access the backend
    CORS(app, resources={r"/*": {"origins": ['http://localhost:3000', 'http://localhost:3002', 'http://ec2-3-142-160-157.us-east-2.compute.amazonaws.com/']}})

    app.run(host='0.0.0.0', port=port, debug=True)
