from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

templates = [
    {
        "inputs": 13,
        "category": "Historical Figures",
        "word": "Nelson Mondela"
    },
    {
        "inputs": 13,
        "category": "Country",
        "word": "United Kingdom"
    },


]

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/get-template")
def get_template():
  return jsonify({
        "status": "success",
        "word": random.choice(templates)
  })

if __name__ == '__main__':
  app.run()
