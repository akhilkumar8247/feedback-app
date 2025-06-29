from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        with open('feedback.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, message])
        return redirect('/')
    return render_template('index.html')
