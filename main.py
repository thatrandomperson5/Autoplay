from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
  if not "id" in request.args:
    return redirect("/info")
  else:
    return redirect(url_for("main", **request.args.to_dict()))
@app.route("/play")
def main():
  return render_template("index.html")
