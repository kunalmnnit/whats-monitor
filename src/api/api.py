import sys
from flask import Flask,jsonify


#api definition
app = Flask(__name__)


#get Status of user given phone number
@app.route('/monitor/<phone>',methods=['GET'])
def monitor(phone):
    from src.whatsapp import registerListener,getStatus
    registerListener(phone=phone)
    res = getStatus()
    return jsonify(res)


if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) # This is for a command-line input
    except:
        port = 12345 # If you don't provide any port the port will be set to 12345
    app.run(port=port, debug=True)

