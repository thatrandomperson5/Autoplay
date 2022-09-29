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
  headers = {}
  if ytid.match(id):
    rq = requests.get(f"https://inv.riverside.rocks/api/v1/videos/{id}?fields=title,author,formatStreams&pretty=1")
    streamUrlDict = {}
    outjson = rq.json()
    for key, value in outjson["formatStreams"].items():
      streamUrlDict[value["resolution"]] = {"type":value["type"],"url":value["url"]}
    return render_template("player.html", 
                           vid144=streamUrlDict["144p"]["url"], 
                           vid144t = streamUrlDict["144p"]["type"],
                           vid360=streamUrlDict["360p"]["url"], 
                           vid360t = streamUrlDict["360p"]["type"],
                           vid720=streamUrlDict["720p"]["url"], 
                           vid720t = streamUrlDict["720p"]["type"],
                          )
  else:
    abort(400)
