from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
@app.route('/main')
def hello_world():
     #return 'Hello, World!'
     return render_template('main.html')


@app.route('/cars')
def cars():
     model = 'Volvo'
     price = 1.5
     data = {
             'model': 'Volvo',
             'price': 1.5}
     #return 'This is contact page'
     #return render_template('cars.html', model = model, price = price)
     return render_template('cars.html', data=data)

@app.route('/cars_form', methods = ['POST'])
def cars_form():
     brand = request.form['brand']
     price = request.form['price']
     #print(brand, price)
     data = {
             'model': brand,
             'price': price}
     #return 'This is contact page'
     #return render_template('cars.html', model = model, price = price)
     return render_template('cars_form.html', data=data)


@app.route('/moto')
def motos():

     data = {
             'model': 'BMW',
             'price': 0.8}
     return render_template('moto.html', **data)


if __name__ == "__main__":
    app.run(debug = True)