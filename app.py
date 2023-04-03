from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello_ghw():
    return "<p>Hello, My name is Esther!</p>"

@app.route('/getHackathons', methods=['GET'])
def getHackathons():
  return hackathons_list

if __name__=="__main__":
    app.run(debug = True)

