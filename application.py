from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index_page():
    # Return this as a strange
    return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")

@app.route("/application-form")
def show_application_form():
	return render_template('application-form.html')

@app.route("/application", methods=["POST"])
def show_response():
	name = request.form.get('firstname') + " " + request.form.get('lastname')
	salary_requirement = request.form.get('salary')
	job_title = request.form.get('position')
	return "Thank you, %s for applying to be a %s. Your minimum salary requirement is %s dollars." \
	%(name, job_title, salary_requirement)

if __name__ == "__main__":
    app.run(debug=True)