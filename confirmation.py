from flask import Flask, render_template, request, jsonify
from supabase import create_client, Client

SUPABASE_URL = "https://lxbyasmuewlppfbvqvkq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imx4Ynlhc211ZXdscHBmYnZxdmtxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDAxODMxNDMsImV4cCI6MjA1NTc1OTE0M30.TT_ev1z60HZ5gB8KzL2qvtxPzuOKQ1TxyUTRfbThyC8"

# Initialize Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
def confirm(ID):
    def fetch_data(table_name):
        print('Fetching data from:', table_name)
        response = supabase.table(table_name).select('*').execute()
        return response

    data = fetch_data("CustomerDB").data
    data1=fetch_data("BusinessDB").data
    venue,v = '',''
    app = Flask(__name__)
    # Sample booking data
    for i in data:
        if i['id']==ID:
            booking_data = {
                "customer_name": i['cust_name'],
                "booking_status": i["status"],
                "event_name": i["business"],
                "venue": "",
                "date_time": i["booking_dt"],
                "email": i["email"]
            }
            v=i["business"]
            
    for i in data1:
        if i['name']==v:
            booking_data["venue"] = i["address"]
    print(booking_data)
    @app.route('/')
    def index():
        return render_template('Confirmation.html', **booking_data)

    @app.route('/submit_data', methods=['POST'])
    def submit_data():
        data = request.get_json()
        if data:
            return jsonify({"message": "Data received successfully!", "received_data": data})
        return jsonify({"message": "No data received!"}), 400

    if __name__ == '__main__':
        app.run(debug=True)
confirm(2)