from flask import Flask, render_template, request, url_for
import sqlite3
import joblib

random_forest = joblib.load("./models/randomForest.lb")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/project")
def project():
    return render_template("project.html")

@app.route("/predict",methods=["GET","POST"])
def predict():
    if request.method == "POST":
        # to recieve the data 
        age = int(request.form["age"])
        sex = int(request.form["gender"])
        bmi = int(request.form["bmi"]) 
        children = int(request.form["children"] )
        smoker = int(request.form["smoker"]) 
        weight = int(request.form["weight"]) 
        region = (request.form["region"]) 
        
        region_southeast = 0
        region_northeast = 0
        region_northwest = 0
        region_southwest = 0
        
        if region == "se":
            region_southeast = 1
        elif region == "sw":
            region_southwest = 1
        elif region == "ne":
            region_northeast = 1
        elif region == "nw":
            region_northwest = 1
            
    unseen_data = [[age, sex, bmi, children, smoker, weight, region_northeast, region_northwest, region_southeast, region_southwest]]
    
    prediction = random_forest.predict(unseen_data)[0]
    print(prediction)
    
    return (unseen_data)
    
if __name__ == "__main__":
    app.run(debug=True)
    

    
