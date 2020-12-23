from flask import Flask,jsonify
from flask_restful import Api, Resource
import sqlite3

app = Flask(__name__)
api = Api(app)

conn = sqlite3.connect('testDB.sqlite',check_same_thread=False)
cur = conn.cursor()

class Home(Resource):
    def get(self):
        return jsonify({'data':'welcome'})
    def post(self):
        return jsonify({'data':'welcome'})

class Search(Resource):
    def get(self,name):
        if name.lower()=='all':
            cur.execute('select name from Universities')
            r=[row[0] for row in cur]
            return jsonify({'countries':r})
        cur.execute('Select * from Universities where name like ?', (name,))
        row=cur.fetchone()
        if row is None: return jsonify({name:'not found'})
        else:
            keys = ['name','address','lat','lon']
            data = dict(zip(keys,row))
            return jsonify({row[0]:data})

class Country(Resource):
    def get(self,cname):
        r=[]
        if cname.lower()=='all':
            cur.execute('select address from Universities')
            r=[(row[0].split(','))[-1].strip() for row in cur]
            return jsonify({'countries':r})
        cur.execute('select name,address from Universities where address like ?',(f'%{cname}',))
        r=[row[0] for row in cur]
        if len(r) <1: return jsonify({cname:'not found'})
        return jsonify({cname:r})
                
api.add_resource(Home, '/','/univ/','/country/')
api.add_resource(Search,'/univ/<string:name>/')
api.add_resource(Country,'/country/<string:cname>/')

if __name__ == '__main__':
    app.run(debug=True)