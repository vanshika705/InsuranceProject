from flask import Flask, render_template, request, url_for
import sqlite3
import joblib

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
        gender = (request.form["gender"])
        bmi = int(request.form["bmi"]) 
        children = int(request.form["children"] )
        smoker = (request.form["smoker"]) 
        health = (request.form["health"]) 
        region = (request.form["region"]) 
        
        region_southeast = 0
        region_northeast = 0
        region_northwest = 0
        region_southwest = 0
        
        if region == "southeast":
            region_southeast = 1
        elif region == "southwest":
            region_southwest = 1
        elif region == "northeast":
            region_northeast = 1
        elif region == "northwest":
            region_northwest = 1
           
            
        if gender == "Female":
            gender_type = 0
        else:
            gender_type = 1
            
        if smoker == "":
            smoker_type = 1
        else:
            smoker_type = 0
            
        if health == "Underweight":
            health_type = 1
        elif health == "Healthyweight":
            health_type = 2  
        elif health == "Overweight":
            health_type = 3  
        elif health == "Obese":
            health_type = 4      
            
            
            
            
    unseen_data = [[age, gender_type, bmi, children, smoker_type, health_type, region_northeast, region_northwest, region_southeast, region_southwest]]
    
    prediction = str(random_forest.predict(unseen_data)[0])
    print(prediction)
    
    connection = sqlite3.connect("insurance.db")
    cur = connection.cursor()
    
    Data = (age, gender, bmi, children, region, smoker, health, prediction)
    cur.execute(data_insert_query, Data)
    print("Your data is inserted into database : ",Data)
    connection.commit()
    cur.close()
    connection.close()
    
    return render_template("final.html", output = prediction)
    
if __name__ == "__main__":
    app.run(debug=True)
    

    
