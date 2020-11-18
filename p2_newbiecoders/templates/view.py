import projects #projects definitions are placed in different file
import data

# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template
#create a Flask instance
app = Flask(__name__)

#connects default URL of server to render home.html
@p2_newbiecodersbp.route('/')
def home_route():
return render_template("travel.html", projects=projects.setup())

@p2_newbiecodersbp.route("/portfolio/")
def portfolio_route():
return render_template("portfolio.html", projects=projects.setup())

#adds the app routes so we can have seprate sites for each of the locations where we can include information about them
@p2_newbiecodersbp.route("/greece/")
def greece_route():
return render_template("greece.html", projects=projects.setup())

@p2_newbiecodersbp.route("/italy/")
def italy_route():
return render_template("italy.html", projects=projects.setup())

@p2_newbiecodersbp.route("/spain/")
def spain_route():
return render_template("spain.html", projects=projects.setup())

@p2_newbiecodersbp.route("/france/")
def france_route():
return render_template("france.html", projects=projects.setup())

@p2_newbiecodersbp.route("/germany/")
def germany_route():
return render_template("germany.html", projects=projects.setup())

@p2_newbiecodersbp.route("/all/")
def all_route():
return render_template("all.html", datalist=data.alldata())

@p2_newbiecodersbp.route("/england/")
def england_route():
return "<h1 style='background-color:blue;color:white'>England!</h1>"

if __name__ == "__main__":
#runs the application on the repl development server
app.run(debug=True)