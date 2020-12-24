from flask import Flask,redirect,render_template,url_for,request
import requests

client_app = Flask(__name__)
url ='http://api:5000/'

@client_app.route('/')
@client_app.route('/home')
def home():
    r=(requests.get(url=url+'country/all').json())['countries']
    res = [] 
    [res.append(x) for x in r if x not in res] 
    #r= (urllib.request.urlopen(url+'country/all')).read()
    return render_template('index.html',countries=res)

@client_app.route('/university/')
def search():
    item= request.args.get('university')
    r=requests.get(url=url+'univ/'+item).json()
    item=list(r.keys())[0]
    dct=r[item]
    print(dct)
    if dct=='not found': return render_template('search.html',univ='N')
    else: return render_template('search.html',univ=dct)

@client_app.route('/country/')
def country():
    item = request.args.get('country')
    print(item)
    r = requests.get(url=url+'country/'+item).json()
    item=list(r.keys())[0]
    lst=r[item]
    print(lst)
    return render_template('search.html',values=lst)

if __name__ == '__main__':
    client_app.run(host='0.0.0.0',port=8000)