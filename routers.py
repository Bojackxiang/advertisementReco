from flask import Flask
from flask import request
from flask_restplus import Resource, Api
from flask_restplus import fields
from flask_restplus import reqparse
from flask_restplus import inputs
from pymongo import *
from preprocessing import dispose
# from preprocessing import predict
from preprocessing import top10
from preprocessing import findUniqueCate
from flask_cors import CORS


import json
app = Flask(__name__)
CORS(app)
api = Api(app)
MONGODB_URI = 'mongodb://watermelon:zoe123@ds129344.mlab.com:29344/ass3user'
client = MongoClient(MONGODB_URI, connectTimeoutMS=30000)
db = client.get_database('ass3user')
user_db = db.user
parser = reqparse.RequestParser()
parser.add_argument('type',type = str)

data_model = api.model('type',{
    "Genres": fields.String})
@api.route('/register/<string:userName>/<string:password>')
class uploadData(Resource):
 #Create a user
    @api.response(201, 'Created')
    @api.response(202, 'Existed')
    def post(self, userName, password):
     registed = user_db.find_one({'userName': userName})
     if registed:
      return {'message': 'User name has existed.'},202
     else:
      record = {
       'userName': userName,
       'password': password
      }
      user_db.insert_one(record)
      data = user_db.find_one({'userName': userName})
      return {'message': 'You created a new user.'},201

    @api.response(200, 'OK')
    @api.response(400, 'Wrong password')
    @api.response(404, 'No user')
    def get(self, userName, password):
     registed = user_db.find_one({'userName': userName})
     if registed:
      user = user_db.find_one({'userName': userName})
      if user['password'] != password:
       return {'message': 'You inputted a wrong password'},400
      else:
       return {'message': 'Success'},200
     else:
      return {'message': 'Can not find user name'},404

@api.route('/genres')
class find(Resource):
    @api.response(201,'Found')
    @api.response(404,'Not Found')
    @api.expect(parser)
    def get(self):
        args = parser.parse_args()
        type1 = args.get('type')
        data = (top10(type1))
        
        #data = json.dumps(data)
        return data,201

@api.route('/predict')
class predict(Resource):
    @api.response(201,'Found')
    @api.response(404,'Not Found')
    @api.expect(parser)
    def get(type):
        cate = request.args.get('type')
        size = request.args.get('size')
        review = request.args.get('review')
        rating = request.args.get('rating')
        predictdata = dispose(cate,rating,size,review)
        print((predictdata))
        return predictdata
@api.route('/catelist')
class find(Resource):
    @api.response(201,'Found')
    @api.response(404,'Not Found')
    
    def get(self):
        data = findUniqueCate()
        dict_data = {}
        for item in data:
            dict_data[item] = 1
        return dict_data

if __name__ == '__main__':
   app.run(debug=True)
