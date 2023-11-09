from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    number = random.randint(1, 100)
    if request.method == 'POST':
        guess = int(request.form['guess'])
        attempts = int(request.form['attempts']) + 1
        if guess > number:
            return render_template('index.html', number=number, message='Demasiado alto', attempts=attempts)
        elif guess < number:
            return render_template('index.html', number=number, message='Demasiado bajo', attempts=attempts)
        else:
            return render_template('index.html', number=number, message='Correcto', attempts=attempts)
    else:
        return render_template('index.html', number=number)

if __name__ == '__main__':
    app.run(debug=True)