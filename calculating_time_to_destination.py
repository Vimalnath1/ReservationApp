from flask import Flask, render_template,request, Blueprint
from supabase import create_client, Client
import cust_table as cust
app = Flask(__name__)
another_blueprint = Blueprint('another', __name__)
SUPABASE_URL = "https://lxbyasmuewlppfbvqvkq.supabase.co"  # Replace with your Supabase project URL
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imx4Ynlhc211ZXdscHBmYnZxdmtxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDAxODMxNDMsImV4cCI6MjA1NTc1OTE0M30.TT_ev1z60HZ5gB8KzL2qvtxPzuOKQ1TxyUTRfbThyC8"  # Replace with your Supabase API key

# Initialize Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def calculating_time_to_destination():
    def fetch_data(table_name): # Fetch data from a specific table
        response = supabase.table(table_name).select("name","latitude","longitude").execute()
        return(response)

    def calculate(coordinates,main_data):
        @app.route('/')
        def index():
            # List of five destinations with longitude and latitude
            destinations = coordinates
            
            # Render the HTML page and send the destinations list to it
            return render_template('testing1.html', destinations=destinations)

        @app.route('/submit_data', methods=['POST'])
        def submit_data():
            # Get the JSON data sent from the JavaScript front-end
            data = request.get_json()
            if len(data)==len(main_data):
                print('hello')
                print(data,'ffffhjbjbjhjhbjhbjbf')
                cust.cust_table(data)
            return {"message": "List received successfully!", "received_list": []}

#        def calculation():
        app.run(debug=True)

#        calculation()
#    def try_it_out(data):
        
    data1=fetch_data("BusinessDB")
    main_data=data1.data
    coordinates=[]
    for i in main_data:
        coordinates.append([[i["longitude"],i["latitude"]],i["name"]])
    calculate(coordinates,main_data)
calculating_time_to_destination()