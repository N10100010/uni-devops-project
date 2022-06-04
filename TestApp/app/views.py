from app import app
from flask import Flask, request, jsonify, render_template


@app.route('/getmsg/', methods=['GET'])
def respond():

    name = request.args.get("name", None)

    response = {}

    if not name:
        response["ERROR"] = "No name found. Please send a name."

    elif str(name).isdigit():
        response["ERROR"] = "The name can't be numeric. Please send a string."
    else:
        response["MESSAGE"] = f"Welcome {name} to our awesome API!"

    return jsonify(response)


@app.route('/post/', methods=['POST'])
def post_something():
    param = request.form.get('name')
    # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
    if param:
        return jsonify({
            "Message": f"Welcome {name} to our awesome API!",

            "METHOD": "POST"
        })
    else:
        return jsonify({
            "ERROR": "No name found. Please send a name."
        })


@app.route('/')
def index():

    return render_template('index.html')
