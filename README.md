**QFull Website**
- By Pranav, Vimal, Nihar, Nakul and லெப்ரான் ஜேம்ஸ்


Imagine walking into your favorite restaurant only to find a long wait time with no clear idea of when you'll be seated. For businesses, managing reservations manually can be chaotic, leading to frustrated customers and inefficient table turnover. Our reservation system bridges this gap by providing a seamless way for customers to book a spot while giving businesses a real-time overview of their queue. With integrated wait time tracking, Maps assistance, and Supabase-powered data management, our platform ensures smoother experiences for both customers and businesses.


**Features:**

For Customers:
1. Real-time booking
2. Wait Time Estimation
3. No. of people in front of you in queue
4. Maps Integration
5. Status of Reservation tracking

For Businesses:
1. Custom business profile
2. Queue Management
3. Automated Time Tracking
4. Security


We start off at the homepage, which allows us to select to access the website as a business or as a customer.

Business:
We either Sign In to an already exisiting account or Sign Up as a new account. 
When signing up, with Supabase and PostgreSQL, we edit and add to a table of various fields containing info about the businesses. 
If we sign in, the business owner can see the queue of customers, with info about their reservation bookings, and the status of their reservations(whether they are waiting or checked in). These are all dervied using SQL queries written in Python and then integrated to the website using JS.

Customer:
A customer can either make a reservation or check upon the status of their reservation. 
When making a reservation, the customer can enter their information, and their address, and then we get the customer address from IP. With the help of APIs, we track the address of customer and business, and find travel time. We can suggest the businesses in sorted order of distance from customer(sorted using SQL Queries). We display information about availability of seats to reserve for these establishments. We can then book the seat for a party of size n. These get collectively added to the SQL CustomerDB table. Then it directs to a site showing the booking confirmation. 
If we choose to view the status of reservation, we can view the waiting time, and the no of people ahead of us in the queue(calculated from business and customer table info using sql queries and python functions). There is also a suggestion on the apt time to depart, given the wait time and travel time.

The website is implemented using HTML/CSS. These features make reservations convenient and easy to track


**Tech Stack**

Frontend:
- JavaScript (for dynamic interaction)
- HTML & CSS (basic UI/UX)
- OpenStreetMap API, OpenRootService API (for travel time estimation)
  
Backend:
- Django (Handles business logic and API)
- Supabase (Cloud-based PostgreSQL for reservations & users)
  
Database:
- Supabase (PostgreSQL) (Stores business and reservation data)
  
Authentication:
- Django Auth (User authentication & session management)
