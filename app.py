from flask import Flask, render_template,request,url_for
# ['age', 'sex', 'bmi', 'children', 'smoker', 'weight', 'region_northeast','region_northwest', 'region_southeast', 'region_southwest']

import joblib
# model1 = joblib.load("linear_model.lb")
# model2 = joblib.load("decisionTree.lb")
# model3 = joblib.load("randomForest.lb")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/project")
def project():
    return render_template("project.html")

@app.route("/prediction",methods=["GET","POST"])
def prediction():
    if request.method=="POST":
        age = request.form["age"]
        sex =request.form["sex"]
        bmi =request.form["bmi"] 
        children =request.form["children"] 
        smoker =request.form["smoker"] 
        weight =request.form["weight"] 
        region =request.form["region"] 
        
        
    user_data = [[age, sex, bmi, children, smoker, weight, region]]
    return user_data
        
        
        
         

if __name__ == "__main__":
    app.run(debug=True)
    

    
