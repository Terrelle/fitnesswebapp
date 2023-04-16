from flask import Flask, render_template, request
import csv


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/event')
def events():
    return render_template('events.html')

@app.route('/membership', methods=['GET', 'POST'])
def membership():
    if request.method == 'POST':
        full_name = request.form['full_name']
        phone_number = request.form['phone_number']
        with open('membership.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([full_name, phone_number])
        return render_template('confirmation.html', full_name=full_name, phone_number=phone_number)
    else:
        return render_template('membership.html')


if __name__ == '__main__':
    app.run(debug=True)
