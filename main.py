from flask import Flask, render_template, request, redirect, url_for, abort
import requests, re
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
  if not "id" in request.args:
    return redirect("/info")
  else:
    return redirect(url_for("main", **request.args.to_dict()))
@app.route("/play")
def main():
  return render_template("index.html")
@app.route("/tools/getVid-<id>")
def getvid(id):
  ytid = re.compile(r'\A([^"&?/\s]{11})$')
  if ytid.match(id):
    req = requests.get(f"https://www.youtube.com/embed/{id}?enablejsapi=1&controls=0&disablekb=1&fs=0&modestbranding=1&origin={request.host}&playsinline=1&rel=0")
    return req.content
  else:
    abort(400)
