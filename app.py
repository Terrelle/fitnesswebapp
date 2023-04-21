from flask import Flask, render_template, request, send_from_directory
import csv


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/event')
def event():
    return render_template('event.html')


@app.route('/testimonial')
def testimonial():
    return render_template('testimonial.html')

@app.route('/articles')
def articles():
    return render_template('articles.html')

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
    
@app.route('/assets/<path:path>')
def send_static(path):
    return send_from_directory('assets', path)


if __name__ == '__main__':
    app.run(debug=True)
