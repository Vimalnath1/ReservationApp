from flask import Flask, render_template,request

app = Flask(__name__)

def get_coordinates():

    @app.route('/')
    def index():
        # Provide the address to the frontend (this can be dynamic)
        address = "Golden Gate Bridge, San Francisco, CA 94129"
        return render_template('testing2.html', address=address)

    @app.route('/submit_data', methods=['POST'])
    def submit_data():
        # Get the JSON data sent from the JavaScript front-end
        coord = request.get_json()
        return_coord(coord)
        return {"message": "List received successfully!", "received_list": []}


    if __name__ == '__main__':
        app.run(debug=True)

def return_coord(coord):
    print(coord)
get_coordinates()