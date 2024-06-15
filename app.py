from flask_bcrypt import Bcrypt
from app import create_app, db

app = create_app()
bcrypt = Bcrypt(app)

if __name__ == '__main__':
    app.run(debug=True, host = "0.0.0.0")


