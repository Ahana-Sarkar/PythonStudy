from flask import Flask, render_template, request, flash
from pymongo import MongoClient
from forms import InputForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '9a662daf6682268761d0f8a7c264a363'

client = MongoClient('localhost', 27017)
mydb = client["FlaskAPPdb"]
mycoll = mydb["UserTable"]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/input", methods=['GET', 'POST'])
def user_input():
    form = InputForm()
    if request.method == 'POST':
        usr_name = request.form.get("username")
        usr_email = request.form.get("email")
        usr_passwrd = request.form.get("password")
        print("The details", usr_name, usr_email, usr_passwrd)
        mycoll.insert_one({'username': usr_name, 'email': usr_email, 'password': usr_passwrd})
        # return render_template('display.html', name = usr_name, email_add = usr_email, password = usr_passwrd)
        all_results = mycoll.find()
        return render_template('display.html', users=all_results)
    return render_template('usr_input.html', title='Input', form=form)


if __name__ == '__main__':
    app.run(debug=True)