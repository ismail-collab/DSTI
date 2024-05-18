/*
Provide a list of count of customers per city
Output:
City	Count of Customers
Nice	2
Paris	1
*/

-- See blackboard for extra comments
SELECT City, COUNT(*) AS CountOfCustomers
FROM Customers
GROUP BY City -- Create "groups" of equal valued "City", so that COUNT can be applied on
			-- these groups, rather than the whole resultset