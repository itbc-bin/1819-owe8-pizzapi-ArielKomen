from flask import Flask, jsonify, request

app = Flask(__name__)

pizzaDB = [
            {'name': 'tonno', 'prijs': 10},
            {'name': 'salami', 'prijs': 5},
            {'name': 'hawaii', 'prijs': 8}
          ]
@app.route("/<string:name>", methods=['GET'])
def getOnePizza(name):
    resultPizza = []
    for pizza in pizzaDB:
        if pizza['name'] == name:
            resultPizza.append(pizza)
    return jsonify({'pizzaDB':resultPizza})

@app.route("/", methods=['POST'])
def addOnePizza():
    pizza = {'name' : request.json['name'], 'prijs' : request.json['prijs']}
    pizzaDB.append(pizza)
    return jsonify({'pizzaDB' : pizzaDB})

@app.route("/<string:name>", methods=['DELETE'])
def delPizza(name):
    resultPizza = []
    for pizza in pizzaDB:
        if pizza['name'] == name:
            resultPizza.append(pizza)
    pizzaDB.remove(resultPizza[0])
    return jsonify({'pizzaDB': pizzaDB})

@app.route("/", methods=['GET'])
def getPizza():
    return jsonify({'pizzaDB':pizzaDB})


if __name__ == "__main__":
    app.run(debug=True, port=8080)
