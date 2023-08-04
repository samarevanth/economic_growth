from flask import Flask, render_template, request  # Flask is a application
# used to run/serve our application
# request is used to access the file which is uploaded by the user in out application
# render_template is used for rendering the html pages
import pickle  # pickle is used for serializing and de-serializing Python object structures
from sklearn.preprocessing import StandardScaler
import numpy as np

app = Flask(__name__, static_folder='static',template_folder='templates')   # our flask app
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')  # rendering the html template
def home():
    return render_template('home.html')


@app.route('/predict')  # rendering the html template
def index():
    return render_template("predict.html")


@app.route('/pred', methods=['POST'])  # route for our prediction
def predict():
    # loading model which we saved
    Region = request.form['Region']
    Population = request.form['Population']
    Area = request.form['Area']
    Pop = request.form['Pop']
    Coastline = request.form['Coastline']
    Phones = request.form['Phones']
    Arable = request.form['Arable']
    Crops = request.form['Crops']
    Climate = request.form['Climate']
    Birthrate = request.form['Birthrate']
    Deathrate = request.form['Deathrate']
    Agriculture = request.form['Agriculture']
    Industry = request.form['Industry']
    Service = request.form['Service']
    total = [[Region, Population, Area, Pop, Coastline, Phones, Arable, Crops, Climate, Birthrate, Deathrate, Agriculture, Industry, Service]]
    print(total)
    prediction = model.predict(total)
    print(prediction)
    return render_template('gdp_pred.html', prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True)