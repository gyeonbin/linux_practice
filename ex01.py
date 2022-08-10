from flask import Flask,render_template,request
import diabetes

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method=="GET":
        model = diabetes.getModel()
        당뇨여부 = model.predict([[6.0,148.0,72.0,35.0,0.0,33.6,0.6,50.0],
                                  [1.0,89.0,66.0,23.0,94.0,28.1,0.2,21],
                                  [6.0,148.0,72.0,35.0,0.0,33.6,0.6,50.0],
                                  [1.0,89.0,66.0,23.0,94.0,28.1,0.2,21]])
        
    return render_template("index.html",당뇨여부=당뇨여부)


app.run(debug=True)