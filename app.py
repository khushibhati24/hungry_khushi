from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():  # main login page
    return render_template('Home.html')

@app.route('/login')
def login():  # main login page
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/restaurant')
def restaurant():
    return render_template('restaurant.html')

@app.route('/ngo')
def ngo():
    return render_template('ngo.html')


# if __name__ == '__main__':
#     app.run(debug=True)
