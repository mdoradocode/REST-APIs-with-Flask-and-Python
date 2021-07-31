from flask import Flask, json, jsonify, request, render_template
app = Flask(__name__)

stores = [
            {
                'name': 'My Store', 
                'items': 
                    [
                        {
                            'name': 'An Item', 
                            'price': 15
                        }
                    ]
            }
        ]

##Remember the different HTTP variables to communicate
##We are the server in this scenario

##This is rendering the HTML code from within the flask application, good for flask web app, bad for flask web api
##Flask auto looks in the template folder
@app.route('/')
def home():
    return render_template('index.html')

#POST /store data: {name:}
##@app.route('/store') is a default GET request
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    ##Return a string instead of the dictionary data structure
    return jsonify(new_store)
    
#GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    ##Iterate of store and return the one that matches, else display and error
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'Error: No store found'})

#GET /store
@app.route('/store')
def get_stores():
    ##Make your list of stores into a dictionary of stores with one entry in it, the stores list.
    ##jsonify does the conversion
    return jsonify({'stores': stores})

#POST /store<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            print(jsonify(store))
            return jsonify(new_item)

    return jsonify({'message': 'Error: No store found'})
#GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'Error: No store found'})

app.run(port=5000)

##A JSON is a hex/string that acts likea dictionary used to send data between programs. It looks similar to the "store" dictionary above. Have to convert a JSON string to a dictionary. CANNOT BE A LIST