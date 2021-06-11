import psycopg2
from flask import Flask, request
from flask import render_template

app = Flask("Job site")

dbconn = psycopg2.connect("dbname=naukri")

@app.route("/")
def index():
	cursor = dbconn.cursor()
	cursor.execute("select count(*) from openings") #Query
	count_jobs = cursor.fetchall()[0][0] #Get data
	return render_template("main.html", njobs=count_jobs) #Render

@app.route("/jobs")
def jobs():
	cursor = dbconn.cursor()
	cursor.execute("select title, company_name, jd_text from openings")
	jobs = cursor.fetchall()
	return render_template("jobs.html", jobs = jobs)

if __name__ == "__main__":
	app.run(debug=True)
