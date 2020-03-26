from flask import Flask,jsonify,request


app = Flask(__name__)

from product import productos

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message":"pong"})


#get products
@app.route('/products', methods=['GET'])
def getProducts():
     return jsonify({
        "products":productos 
     })


#get one products
@app.route('/products/<string:product_name>')
def getOneProduct(product_name):
     productFound = [product for product in productos if product['name'] == product_name ]
     if(len(productFound) > 0):
         return jsonify({"products":productFound})
     return jsonify({"message":"product not found"})
     

#create product
@app.route('/products', methods=['POST'])
def createProduct():
    newProduct = {
        "name" :request.json['name'],
        "price" : request.json['price'],
        "cuantity" : request.json['cuantity']
    }

    productos.append(newProduct)
    return jsonify({"message":"product added success", "products":productos})


#update products
@app.route('/products/<string:product_name>', methods=['PUT'])
def updateProduct(product_name):
    productFound = [product for product in productos if product['name'] == product_name]
    if(len(productFound) > 0):
        productFound[0]['name'] = request.json['name']
        productFound[0]['price'] = request.json['price']
        productFound[0]['cuantity'] = request.json['cuantity']
        return jsonify({"message":"product updated successfulli", "products":productos})
    return jsonify({"messaga":"product no found"})



@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    productFound = [product for product in productos if product['name'] == product_name]
    if len(productFound) > 0 :
        productos.remove(productFound[0])
        return jsonify({
            "message":"product deleted",
            "products":productos
        })
    return jsonify({"message":"product not found"})



#server initializando
if __name__ == '__main__':
    app.run(debug=True, port=4000)
