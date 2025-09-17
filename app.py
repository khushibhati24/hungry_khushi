from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')  # Your main page

@app.route('/signup')
def login():
    return render_template('signup.html')  # Example login page

@app.route('/restaurant')
def restaurant():
    return render_template('restaurant.html')  # Restaurant donation page

@app.route('/ngo')
def ngo():
    return render_template('ngo.html')  # NGO dashboard page


if __name__ == '__main__':
    app.run(debug=True)
