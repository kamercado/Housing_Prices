#import dependencies
import numpy as np
import pickle
from flask import Flask, request, jsonify, render_template

#app setup
app = Flask(__name__)

##########################
# Web page(s) of interface #
##########################

#App routes to render HTML templates/web pages
@app.route("/")
def index():
    #Return the homepage/form
    return render_template("userinput.html")

#######################################################
# Predicting the house price based on characteristics #
# of house input by the user                          #
#######################################################

#load the trained model
house_model = pickle.load(open('model.pkl','rb'))

#app route to create API to predict Airbnb host's rating
@app.route('/predict',methods=['POST'])
def predict():
	# store the input from the form
	form_input = [int(x) for x in request.form.values()]
	#convert input into numpy array to feed into prediction model
	input_list = [np.array(form_input)]
	#put values list into prediction model
	prediction = house_model.predict(input_list)
	#variable for output (predicted price), round for decimals
	price = round(prediction[0],2)
	#populate webpage with price predictioin
	return render_template('userinput.html', prediction_text = 'Your house in Ames, Iowa will sell for approx. $ {}'.format(price))



@app.route('/results',methods=['POST'])
def result():
	data = request.get_json(force=True)
	#make prediction of price using the house_model that was pickled
	prediction = house_model.predict([[np.array(list(data.values()))]])
	#price (output) is first value of prediction
	output = prediction[0]
	return jsonify(output)


if __name__ == '__main__':
    app.run(debug=True)