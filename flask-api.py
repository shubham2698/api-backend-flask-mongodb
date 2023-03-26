from flask import Flask, request
import pymongo

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yamahar15v2'

def db_con():
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client["navantrix"]
    con = db.product_collection
    return con

con = db_con()

def generate_res(con):
    data = con.find()
    res = {}
    for each in data:
        res[each["_id"]] = each
    return res


@app.route('/insert', methods=['POST'])
def insert():
    if request.method == "POST":
        name = request.json["name"]
        type = request.json["type"]
        unit = request.json["unit"]
        unit = unit.split(",")
        subproduct = []
        for each in unit:
            ins = f"{name} {each}"
            subproduct.append(ins)

        data = {
            "_id": name,
            "PRODUCT_TYPE": type,
            "PRODUCT_UNIT": unit,
            "SUB_PRODUCT": subproduct
        }
        con.insert_one(data)
        res = generate_res(con)
        return res


@app.route('/update', methods=['POST'])
def update():
    key, col, new_value = request.json["key"],request.json["col"],request.json["value"]
    if col == "PRODUCT_UNIT":
        subproduct = []
        for each in new_value:
            ins = f"{key} {each}"
            subproduct.append(ins)
        con.update_one({"_id":key},{"$set":{f"{col}":new_value}})
        con.update_one({"_id": key}, {"$set": {f"SUB_PRODUCT": subproduct}})
    else:
        con.update_one({"_id": key}, {"$set": {f"{col}": new_value}})
    res = generate_res(con)
    return res


@app.route('/delete', methods=['POST'])
def delete():
    key = request.json["key"]
    con.delete_one({"_id":key})
    res = generate_res(con)
    return res


@app.route('/view', methods=['POST',"GET"])
def view():
    res = generate_res(con)
    if request.method == "POST":
        return res
    if request.method == "GET":
        return res


if __name__ == '__main__':
    app.run(debug=True)






