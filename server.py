from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
class TimezoneList(Resource):
    def __init__(self) -> None:
      self.Timezone = {
        "Vietnam": 'GMT +7',
        "China": 'GMT+8'
      }
    def get_data(self, country: str):
        return self.Timezone[country]
    
    def getAll(self):
        return self.Timezone

    def set_data(self, newDict: dict):
        self.Timezone.update(newDict)

timezone = TimezoneList()

@app.route("/get/<string:key>", methods=['GET'])
def get(key):
    resp = {}
    try:       
        content = timezone.get_data(key)
        resp = {str(key): content}
    except KeyError as e:
        resp = str(e)
    return jsonify(resp)

@app.route("/set", methods=['POST'])
def set():
    try:
        data = request.get_json()
        timezone.set_data(data)
        return timezone.getAll()
    except Exception as e:
        return str(e)
   

if __name__ == "__main__":
  app.run(debug=True)
