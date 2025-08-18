from app import create_app, extensions
from app.models import *

app = create_app()

with app.app_context():
    extensions.db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
