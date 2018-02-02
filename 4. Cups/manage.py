from flask import Flask

from controls.blog import blogController
from controls.user import userController

app = Flask(__name__)

app.register_blueprint(blogController)
app.register_blueprint(userController)

if __name__ == '__main__':
    app.run(debug=True)
