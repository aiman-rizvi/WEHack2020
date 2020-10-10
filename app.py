from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/user_home', methods=['GET'])
def user_home():
    return 'Welcome to the user-home page!'

@app.route('/network', methods=['GET'])
def network():
    return 'Welcome to the page where users can find people to connect with!'

@app.route('/user_profile', methods=['GET'])
def user_profile():
    return 'Welcome to the users profile!'





if __name__ == '__main__':
    app.run()
