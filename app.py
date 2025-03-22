from flask import Flask, request, render_template, jsonify

app = Flask(__name__, template_folder = 'template')

@app.route('/')
def hello_world():
    return 'Hello World!'

# TODO: re-build the Docker image after I'm done experimenting with POST requests

@app.route('/form', methods = ['GET', 'POST'])
def form_post():
    if request.method == 'POST':
        return jsonify(request.form)
    if request.method == 'GET':
        return render_template('form.html')
    
@app.route('/payload', methods = ['POST'])
def payload_post():
    print(request.json, type(request.json))
    print(request.data, type(request.data))
    result = request.json
    ret_str = f'item_1: {result['key1']}\nitem_2: {result['key2']}'
    return ret_str
    
if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5000)