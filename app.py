from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')


# Routes
@app.route('/')
def hello_world():
    return render_template('landing.html', title="landing")

@app.route('/user_home', methods=['GET'])
def user_home():
    return render_template('home.html', title="User - Home")

@app.route('/network', methods=['GET'])
def network():
    return render_template('network.html', title="Connect!")

@app.route('/user_profile', methods=['GET'])
def user_profile():
    return 'Welcome to the users profile!'



if __name__ == '__main__':
    app.run()
