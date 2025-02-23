import supabase

def remove_customer(customer_name):
    response = supabase.table("CustomerDB").delete().eq("name", customer_name).execute()

    if response.error:
        print(f"Error: {response.error['message']}")
    else:
        print(f"Customer '{customer_name}' removed successfully!")
    
    return 0


def add_cuhzz(customer_info):
    # Ensure the list has correct values
    if len(customer_info) != 9:
        print("Error: customer_info must have exactly 9 values (id, name, email, phone, address).")
        return
    
    # Convert list to dictionary for Supabase

    fields_cust = ["id","business","cust_name","cust_addr","party_size","status","email","booking_dt"]

    customer_data = dict(zip(fields_cust,customer_info))

    # Insert into Supabase
    response = supabase.table("CustomerDB").insert(customer_data).execute()
    
    if response.error:
        print(f"Error: {response.error['message']}")
    else:
        print(f"Customer '{customer_info[2]}' added successfully!")

    return


def add_bez(business_info):
    if len(business_info) != 11:
        print("Error: business_info must have exactly 11 values (id, name, email, phone, address).")
        return
    
    # Convert list to dictionary for Supabase

    fields_bus = ["username","password","type","address","latitude","longitude",\
                  "wait_time","capacity","email","phone","name"]
    business_data = dict(zip(fields_bus,business_info))

    # Insert into Supabase
    response = supabase.table("CustomerDB").insert(business_data).execute()
    
    if response.error:
        print(f"Error: {response.error['message']}")
    else:
        print(f"Customer '{business_info[2]}' added successfully!")
    return

def mycuhzz(bus_name):
    response = supabase.table("CustomerDB").select("*").eq("business", bus_name).execute()

    if not response.data:
        print("No reservations found for this business.")
        return []

    return response.data


def increase_wait_time():
    response = supabase.table("BusinessDB").select("busid, wait_time").execute()
    
    if response.data:
        for row in response.data:
            delay_waittime = row["avg_wait_time"] * 1.1  # Increase by 10%
            supabase.table("BusinessDB").update({"wait_time": delay_waittime}).eq("busid", row["busid"]).execute()
    
    print("Wait times updated successfully!")


def get_waitinfo(id):
    booking = supabase.table("CustomerDB").select("created_at", "business").eq("id", id).single().execute()
    if not booking.data:
        print("Invalid booking ID")
        return None
    customer_time = booking.data["created_at"]
    bus_name = booking.data["business"]

    response = supabase.table("CustomerDB").select("count", count="exact").eq("business", bus_name).eq("status", "waiting") \
        .lt("created_at", customer_time).execute()
    
    people_ahead = response.data[0]["count"] if response.data else 0

    business_info = supabase.table("BusinessDB").select("wait_time").eq("name", bus_name).single().execute()
    ppwait = business_info.data["wait_time"] if business_info.data else 10  # Default 10 mins if not found

    est_time = people_ahead * ppwait

    print(f"People ahead: {people_ahead}")
    print(f"Estimated wait time: {est_time} minutes")

    return people_ahead, est_time





def leaving_time(customer_id, travel_time):
    wait_time = get_waitinfo(customer_id)[1]

    if wait_time <= travel_time():
        print("Time to leave NOW!")
    else:
        leave_in = wait_time - travel_time()
        print(f"Wait time now is {wait_time} minutes.")
        print(f"You can choose to leave in {leave_in} minutes.")

    return wait_time,leave_in
