from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')
@app.route('/', methods=['POST'])
def getvalue():
    user_guess_number = request.form['guessNumber']
    return render_template('pass.html', num=user_guess_number)

if __name__ == '__main__':
    app.run()
