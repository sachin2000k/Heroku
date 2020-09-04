import pandas as pd
from flask import Flask, jsonify, request, render_template
import pickle
import json

model = pickle.load(open('model.pkl','rb'))

app = Flask(__name__)



@app.route('/', methods=['GET','POST'])

def predict():
    
    if request.method == 'POST':
        #data = request.get_json(force = True)
        Pclass = request.form.get('Pclass')
        Age = request.form.get('Age')
        SibSp = request.form.get('SibSp')
        Fare = request.form.get('Fare')
        print(Pclass,Age,SibSp,Fare)
       
        data = {
            'Pclass':int(Pclass),
            'Age':int(Age),
            'SibSp':int(SibSp),
            'Fare': int(Fare)
                    }
                    
        print(data)   
        data_df = pd.DataFrame()
        data_df = data_df.append({'Pclass':int(Pclass),
                                    'Age':int(Age),
                                    'SibSp':int(SibSp),
                                    'Fare': int(Fare)},ignore_index = True)

        
        result = model.predict(data_df)
        #output = {'results':int(result[0])}
        
        return render_template('index.html', prediction_text = '{}'.format(result))
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(port = 5000, debug = True)