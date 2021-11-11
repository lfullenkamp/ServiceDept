import mysql.connector
from flask import Flask, render_template, request

# Starts app and initializes secret key
app = Flask(__name__)
app.secret_key = "12345"

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    database="service"
)


# Index routing to main index page
@app.route('/')
def index():
    return render_template('index.html')


# Manufacturing Package
@app.route('/manufacturing', methods=['GET', 'POST'])
def manufacturing():
    if request.method == "POST":
        # Create variables for easy access of all form data entries
        instrument = request.form['instrument']
        serial_number = request.form['serial number']
        customer_name = request.form['customer name']
        date = request.form['date']
        warranty_life = request.form['warranty life']
        co = request.form['co']
        co_warranty = request.form['co warranty']
        co_date = request.form['co date']
        o2 = request.form['o2']
        o2_warranty = request.form['co warranty']
        o2_date = request.form['o2 date']
        h2s = request.form['h2s']
        h2s_warranty = request.form['h2s warranty']
        h2s_date = request.form['h2s date']
        h2n = request.form['h2n']
        h2n_warranty = request.form['h2n warranty']
        h2n_date = request.form['h2n date']
        # Initializes database cursor
        cursor = db.cursor()
        # Inserts every user entry into the database
        cursor.execute('INSERT INTO service.service (`instrument`, `serial number`, `customer name`,`date`, '
                       '`warranty life`, `co`, `co warranty`, `co date`, `o2`,`o2 warranty`, `o2 date`, `h2s`, '
                       '`h2s warranty`, `h2s date`, `h2s`, `h2s warranty`, `h2s date`) '
                       'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                       (instrument, serial_number, customer_name, date, warranty_life, co, co_warranty, co_date, o2,
                        o2_warranty, o2_date, h2s, h2s_warranty, h2s_date, h2n, h2n_warranty, h2n_date))
        # Commits user input into database
        db.commit()
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
