from flask import Flask, render_template

app = Flask(__name__)

JOBS=[
  {
    'id':1,
    'title':'Data Scientist',
    'location': 'Delhi India',
    'salary':'Rs. 1300000'
  },
  {
    'id':2,
    'title':'Frontend Engg.',
    'location':'Bengluru India',
    'salary':'Rs. 1300000'
  },
  {
    'id':3,
    'title':'Frontend Engg.',
    'location':'USA',
    'salary':'$ 13000'
  }
]

@app.route("/")
def hello_world():
    return render_template('home.html',jobs=JOBS)

if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)