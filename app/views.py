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


# Sales Package
@app.route('/sales', methods=['GET', 'POST'])
def manufacturing():
    if request.method == "POST":
        # Create variables for easy access of all form data entries
        instrument = request.form['instrument']
        serial_number = request.form['serial number']
        customer_name = request.form['customer name']
        date = request.form['date']
        warranty_life = request.form['warranty life']

        # Creates variable for request form data
        co = request.form['co']
        # Checks if the length of variable is equal to 0, if so sensor is None
        if len(co) == 0:
            co = None
        # Creates variable for request form data
        co_warranty = request.form.get('co warranty')
        # Checks if there is no co_warranty selected, if so warranty is None
        if not co_warranty:
            co_warranty = None
        # Creates variable for request form data
        co_date = request.form['co date']
        # Checks if the length of variable is equal to 0, if so data is None
        if len(co_date) == 0:
            co_date = None

        o2 = request.form['o2']
        if len(o2) == 0:
            o2 = None
        o2_warranty = request.form.get('o2 warranty')
        if not o2_warranty:
            o2_warranty = None
        o2_date = request.form['o2 date']
        if len(o2_date) == 0:
            o2_date = None

        h2s = request.form['h2s']
        if len(h2s) == 0:
            h2s = None
        h2s_warranty = request.form.get('h2s warranty')
        if not h2s_warranty:
            h2s_warranty = None
        h2s_date = request.form['h2s date']
        if len(h2s_date) == 0:
            h2s_date = None

        hcn = request.form['hcn']
        if len(hcn) == 0:
            hcn = None
        hcn_warranty = request.form.get('hcn warranty')
        if not hcn_warranty:
            hcn_warranty = None
        hcn_date = request.form['hcn date']
        if len(hcn_date) == 0:
            hcn_date = None

        # Initializes database cursor
        cursor = db.cursor()
        # Inserts every user entry into the database
        insert_data = 'INSERT INTO service.service (`instrument`, `serial number`, `customer name`,`date`,' \
                      '`warranty life`, `co`, `co warranty`, `co date`, `o2`,`o2 warranty`, `o2 date`, `h2s`, ' \
                      '`h2s warranty`, `h2s date`, `hcn`, `hcn warranty`, `hcn date`) ' \
                      'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        values = (instrument, serial_number, customer_name, date, warranty_life, co, co_warranty, co_date, o2,
                  o2_warranty, o2_date, h2s, h2s_warranty, h2s_date, hcn, hcn_warranty, hcn_date)
        cursor.execute(insert_data, values)
        # Commits user input into database
        db.commit()
    return render_template("index.html")


# Service Package
@app.route('/service', methods=['GET', 'POST'])
def service():
    if request.method == "POST":
        # Create variables for easy access of instrument and serial number
        instrument = request.form['instrument']
        serial_number = request.form['serial number']
        # Initializes database cursor
        cursor = db.cursor()
        # Selects instrument and serial number if found in the database
        select_data = 'SELECT * FROM service.service WHERE `instrument`=%s AND `serial number`=%s'
        values = (instrument, serial_number)
        cursor.execute(select_data, values)
        # Uses cursor to fetch all the contents
        result = cursor.fetchall()
        # Displays the results
        return render_template("service.html", result=result)
    else:
        return render_template('service.html')


if __name__ == '__main__':
    app.run()
