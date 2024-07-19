from flask import Flask, render_template, request, url_for
import sqlite3
import joblib

# connection = sqlite3.connect("insurance.db")
# cur = connection.cursor()

random_forest = joblib.load("./models/randomForest.lb")

app = Flask(__name__)

data_insert_query = """ insert into project 
(age, sex, bmi, children, region, smoker, weight, prediction)
values(?,?,?,?,?,?,?,?)"""

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
    
    prediction = str(random_forest.predict(unseen_data)[0])
    print(prediction)
    connection = sqlite3.connect("insurance.db")
    cur = connection.cursor()
    
    Data = (age, sex, bmi, children, region, smoker, weight, prediction)
    cur.execute(data_insert_query, Data)
    print("Your data is inserted into database : ",Data)
    connection.commit()
    cur.close()
    connection.close()
    
    return render_template("final.html", output = prediction)
    
if __name__ == "__main__":
    app.run(debug=True)
    

    
