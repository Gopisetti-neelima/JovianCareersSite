from flask import Flask, jsonify, render_template

app = Flask(__name__, template_folder="templates/")
job_details=[
        {'id':1, 'title':"Associate Software Engineer", 'location': "Visakhapatnam", 'salary': "$3200"},
        {'id':2, 'title':"Software Engineer", 'location': "Visakhapatnam", 'salary': "$4100"},
        {'id':3, 'title':"Python Developer - AWS", 'location': "Hyderabad", 'salary': "$5500"}
    ]

@app.route("/")
def home():
    return render_template("index.html", jobs = job_details)

@app.get("/jobs/")
def getJobs():
    return jsonify(job_details)


@app.get("/user/<string:name>")
def getUser(name):
    if name =="Neelima":
        return jsonify({
            "name" : "Neelima Gopisetti",
            "age":24,
            "experience": 1,
            "isSearchingForJob": True
        })
    elif name=="srinija":
        return '"name" : "Katta Srinija","age":24,"experience": 2.5,"isSearchingForJob": False'

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

