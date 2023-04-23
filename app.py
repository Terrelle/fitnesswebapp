from flask import Flask, redirect, render_template, request, send_from_directory
import csv
import os
from werkzeug.utils import secure_filename


app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')



from database import get_events
@app.route('/event')
def events():
    events = get_events()

    return render_template('event.html', events = events)

@app.route('/video')
def videos():
    return render_template('video.html')

@app.route('/recipe')
def recipes():
    return render_template('recipe.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/article')
def article():
    return render_template('article.html')

@app.route('/about')
def about():
    return render_template('about.html')

from database import get_products
@app.route('/products')
def products():
    products = get_products()

    return render_template('product.html', products = products)





@app.route('/testimonial')
def testimonial():
    return render_template('testimonial.html')

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

#############################################################################
@app.route('/assets/<path:path>')
def send_static(path):
    return send_from_directory('assets', path)

@app.route('/products_uploads/<filename>')
def uploaded_product_file(filename):
    return send_from_directory('products_uploads', filename)

@app.route('/events_uploads/<filename>')
def uploaded_event_file(filename):
    return send_from_directory('events_uploads', filename)
#############################################################################



from database import add_product_db
@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        # get form data
        name = request.form['name']
        price = request.form['price']
        description = request.form['description']
        
        # handle file upload
        file = request.files['image']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join('products_uploads', filename))
        else:
            filename = ''
        
        # insert product into database
        add_product_db(name, price, description, filename)
        
        return redirect('/products')

from database import remove_product_db
@app.route('/delete_product/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    remove_product_db(product_id)

    return redirect('/products')





# For EVENTS
from database import add_event_db
@app.route('/add_event', methods=['GET', 'POST'])
def add_event():
    if request.method == 'POST':
        # get form data
        name = request.form['name']
        location = request.form['location']
        description = request.form['description']
        
        # handle file upload
        file = request.files['image']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join('events_uploads', filename))
        else:
            filename = ''
        
        # insert event into database
        add_event_db(name, location, description, filename)
        
        return redirect('/event')
    
from database import remove_event_db
@app.route('/delete_event/<int:event_id>', methods=['POST'])
def delete_event(event_id):
    remove_event_db(event_id)

    return redirect('/event')



if __name__ == '__main__':
    app.run(debug=True)
