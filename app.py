from detection import detect_objects
from flask import Flask, request, url_for, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/predict/',methods=['POST'])
def predict():
    if request.method == 'POST':
        # if 'url' in request.json:
        #     url = request.json['url']
        url = request.form['urlofimage']
        print(url)
                      
        out = detect_objects(url)
        return render_template('index.html',response = out)
    
# @app.route('/predict/',methods=['POST'])
# def predict():
#     if request.method == 'POST':
#         if 'url' in request.json:
#             url = request.json['url']
                      
#             out = detect_objects(url)
#         return jsonify({'response':out})
    
    
if __name__=='__main__':
    app.run(debug=True,host='192.168.15.246')