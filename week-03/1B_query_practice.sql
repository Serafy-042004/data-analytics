Use northwind;
-- Write a query to list the product id, product name, and unit price of every product that Northwind sells. 
Select productid, productname, unitprice from products;
-- Write a query to identify the products where the unit price is $7.50 or less
Select productname, productid, unitprice from products where unitprice < 7.50;
-- What are the products that we carry where we have no units on hand, but 1 or more units are on backorder? Write a query that answers this question.
Select productname, unitsinstock, unitsonorder from products where unitsinstock = 0 and unitsonorder >= 1;
-- How does it identify the type (category) of each item sold? Where can you find a list of all categories?
Select * from products where categoryid=8;
-- Write a set of queries to find the specific identifier for "Tokyo Traders" and then find all products from that supplier
Select * from products where supplierid = 4;
-- How many employees work at northwind? 
Select count(*) as numberofemployees from employees;
-- What employees have "manager" somewhere in their job title?
Select * from employees where title like '%manager%';