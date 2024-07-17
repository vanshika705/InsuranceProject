from flask import Flask, url_for, render_template,request
# ['age', 'sex', 'bmi', 'children', 'smoker', 'weight', 'region_northeast','region_northwest', 'region_southeast', 'region_southwest']

import joblib
# model1 = joblib.load("linear_model.lb")
# model2 = joblib.load("decisionTree.lb")
# model3 = joblib.load("randomForest.lb")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
    

    
