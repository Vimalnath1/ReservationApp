import supabase

def rm_cuhzz(cuh_name):
    return 0

def add_cuhzz(cuh_name):
    return 0

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





def leaving_time(customer_id, customer_address, business_address):
    wait_time = get_waitinfo(customer_id)[1]
    #travel_time = get_travel_time(customer_address, business_address) GET FROM SIVARAJ

    if wait_time <= travel_time():
        print("Time to leave NOW!")
    else:
        leave_in = wait_time - travel_time()
        print(f"Leave in {leave_in} minutes.")

    return leave_in