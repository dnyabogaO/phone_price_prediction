# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the Random Forest CLassifier model
filename = '../model/kenya_phone_prices_model.pickle'
regressor = pickle.load(open(filename, 'rb'))

app = Flask(__name__, template_folder='../templates')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    if request.method == 'POST':

        phone_make = request.form['phone_make']
        phone_make = request.form['phone_make']
        if (phone_make == 'Samsung'):
            phone_make = 1
            ChestPainType_NAP = 0
            ChestPainType_TA = 0

        elif (ChestPainType == 'NAP'):
            ChestPainType_ATA = 0
            ChestPainType_NAP = 1
            ChestPainType_TA = 0
        elif (ChestPainType == 'TA'):
            ChestPainType_ATA = 0
            ChestPainType_NAP = 0
            ChestPainType_TA = 1
        if phone_make == 'Samsung':
            temp_array = temp_array + [1, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0]
        elif phone_make == 'Xiaomi':
            temp_array = temp_array + [0, 1, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0]
        elif phone_make == 'Huawei':
            temp_array = temp_array + [0, 0, 1, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0]
        elif phone_make == 'Infinix':
            temp_array = temp_array + [0, 0, 0, 1, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0]
        elif phone_make == 'Tecno':
            temp_array = temp_array + [0, 0, 0, 0, 1, 0, 0, 0,0,0,0,0,0,0,0,0,0]
        elif phone_make == 'Oppo':
            temp_array = temp_array + [0, 0, 0, 0, 0, 1, 0, 0,0,0,0,0,0,0,0,0,0]
        elif phone_make == 'Realme':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 1, 0,0,0,0,0,0,0,0,0,0]
        elif phone_make == 'Nokia':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 1,0,0,0,0,0,0,0,0,0]
        elif phone_make == 'HTC':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 0,1,0,0,0,0,0,0,0,0]
        elif phone_make == 'Apple':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 0,0,1,0,0,0,0,0,0,0]
        elif phone_make == 'Sony':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 0,0,0,1,0,0,0,0,0,0]
        elif phone_make == 'OnePlus':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 0,0,0,0,1,0,0,0,0,0]
        elif phone_make == 'LG':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,1,0,0,0,0]
        elif phone_make == 'Lenovo':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,1,0,0,0]
        elif phone_make == 'Google':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,1,0,0]
        elif phone_make == 'BlackBerry':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,1,0]
        elif phone_make == 'Motorola':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,1]

        OS = request.form['OS']
        if (OS == 'Android'):
            OS = 1
        else:
            OS=0



        ROM = int(request.form['ROM'])
        RAM = int(request.form['ROM'])
        screen_size = int(request.form['screen_size'])
        back_camera = int(request.form['back_camera'])
        front_camera = int(request.form['front_camera'])
        Battery = int(request.form['Battery'])
        Rating = float(request.form['Rating'])
        Likes = int(request.form['Likes'])
        specs_score = int(request.form['specs_score'])

        temp_array = temp_array + [OS, ROM, RAM, screen_size,back_camera,front_camera,Battery,Rating,Likes,specs_score]

        data = np.array([temp_array])
        my_prediction = int(regressor.predict(data)[0])

        return render_template('index.html',prediction_texts="Heart Disease Detected: {}".format(my_prediction))


if __name__ == '__main__':
    app.run(debug=True)