from flask import Flask, render_template, request, jsonify, Blueprint
from supabase import create_client, Client
SUPABASE_URL = "https://lxbyasmuewlppfbvqvkq.supabase.co"  # Replace with your Supabase project URL
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imx4Ynlhc211ZXdscHBmYnZxdmtxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDAxODMxNDMsImV4cCI6MjA1NTc1OTE0M30.TT_ev1z60HZ5gB8KzL2qvtxPzuOKQ1TxyUTRfbThyC8"  # Replace with your Supabase API key

# Initialize Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
another_blueprint = Blueprint('another', __name__)
def fetch_data(table_name): # Fetch data from a specific table
    response = (supabase.table(table_name).select('*').execute())
    return(response)
resteraunt_data=[]
data=fetch_data("BusinessDB").data
def cust_table(timeTaken={'Ambar Indian Restaurant': 114,'Cheesecake Factory': 10}):
    app = Flask(__name__)
    def fetch_data(table_name): # Fetch data from a specific table
        response = (supabase.table(table_name).select('*').execute())
        return(response)
    resteraunt_data=[]
    data=fetch_data("BusinessDB").data
    est_time={'Ambar Indian Restaurant': 10,'Cheesecake Factory': 114}
    for i in data:
        resteraunt_data.append([i['name'],timeTaken[i['name']],est_time[i['name']]])
    print(resteraunt_data)
    @app.route('/') 
    def index():
        # Pass the list of lists to the HTML template
        print("here too")
        return render_template('buttons.html', restaurant_data=resteraunt_data)
    @app.route('/select-restaurant', methods=['POST'])
    def select_restaurant():
        print('here 3')
        data = request.get_json()
        selected_restaurant = data.get('name')
        # You can add additional logic here if needed, such as saving the selection or further processing
        print(f"Selected Restaurant: {selected_restaurant}")
        
        return jsonify({'name': selected_restaurant})
    def start():
#        if __name__ == '__main__':
        print('here')
        app.run(debug=True)
    start()
cust_table()