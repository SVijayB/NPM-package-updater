from src.app import *

# Initializing the flask app and running it
app = create_app()
if __name__ == "__main__":
    app.run()
