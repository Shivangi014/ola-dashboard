USE ola;
SELECT *
FROM ola_rides
WHERE Booking_Status = 'Success';
SELECT Vehicle_Type,
AVG(Ride_Distance) AS avg_distance
FROM ola_rides
GROUP BY Vehicle_Type;
SELECT COUNT(*) AS cancelled_by_customer
FROM ola_rides
WHERE Booking_Status = 'Canceled by Customer';
SELECT Customer_ID,
COUNT(*) AS total_rides
FROM ola_rides
GROUP BY Customer_ID
ORDER BY total_rides DESC
LIMIT 5;
SELECT Canceled_Rides_by_Driver,
COUNT(*) AS total
FROM ola_rides
GROUP BY Canceled_Rides_by_Driver;
SELECT
MAX(Driver_Ratings) AS max_rating,
MIN(Driver_Ratings) AS min_rating
FROM ola_rides
WHERE Vehicle_Type = 'Prime Sedan';
SELECT *
FROM ola_rides
WHERE Payment_Method = 'UPI';
SELECT Vehicle_Type,
AVG(Customer_Rating) AS avg_customer_rating
FROM ola_rides
GROUP BY Vehicle_Type;
SELECT SUM(Booking_Value) AS total_revenue
FROM ola_rides
WHERE Booking_Status = 'Success';
SELECT Booking_ID,
Incomplete_Rides_Reason
FROM ola_rides
WHERE Incomplete_Rides = 'Yes';