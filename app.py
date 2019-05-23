from flask import Flask, jsonify, request

app = Flask(__name__)

pizzaDB = [
            {'name': 'tonno'},
            {'name': 'salami'},
            {'name': 'hawaii'}
          ]

@app.route("/", methods=['GET'])
def getPizza():
    return jsonify({'pizzaDB':pizzaDB})


if __name__ == "__main__":
    app.run(debug=True, port=8080)
