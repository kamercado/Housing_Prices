#import dependencies
import numpy as np
import pickle
from flask import Flask, jsonify, render_template

#app setup
app = Flask(__name__)

##########################
# Web pages of interface #
##########################

#App routes to render HTML templates/web pages
@app.route("/")
def index():
    #Return the homepage/form
    return render_template("index.html")

@app.route("/nlp")
def nlp():
    #Return the How to Improve Your Ratings page
    return render_template("nlp.html")
    
@app.route("/geomap")
def geomap():
    #Return the Geomap displaying other Airbnbs in the area
    return render_template("geomap.html")

##############################################################
# Predicting the host Airbnb rating based on characteristics #
# of their airbnb input by the user                          #
##############################################################

#load the trained model
airbnb_model = pickle.load(open('model.pkl','rb'))

#app route to create API to predict Airbnb host's rating
@app.route('/predict',methods=['POST'])
def predict():
	data = request.get_json(force=True)
	#make prediction of rating using the airbnb_model that was pickled
	prediction = airbnb_model.predict([[np.array(data['exp'])]])
	#rating (output) is first value of prediction
	rating = prediction[0]
	return jsonify(rating)




if __name__ == '__main__':
    app.run(debug=True)