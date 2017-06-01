from flask import Flask, render_template, redirect, url_for, request
from carrier import Carrier

CARRIERS = []
IDENTITY = 0

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def carriers_page():
	if request.method == "POST":
		carrier_name = request.form.get("name", "")
		global IDENTITY
		IDENTITY += 1
		carrier = Carrier(name = carrier_name, _id = IDENTITY)
		CARRIERS.append(carrier)

		return redirect(url_for("carriers_page"))

	return render_template("index.html", carriers = CARRIERS)

if __name__ == "__main__":
	app.run(debug=True)
