USE northwind;
-- Write a query to list the product id, product name, and unit price of every product. This time, display them in ascending order by price
Select productid, productname, unitprice from products order by unitprice asc;
-- What are the products that we carry where we have at least 100 units on hand? Order them in descending order by price.
Select * from products where unitsinstock >= 100 order by unitprice desc;
-- If two or more have the same price, list those in ascending order by product name.(note litterly the same question and it changes nothing
Select * from products where unitsinstock >= 100 order by unitprice desc,productName Asc;
-- Write a query against the orders table that displays the total number of distinct customers who have placed orders, based on customer ID. Use an alias to label the count calculation as CustomerCount.
Select count(distinct customerid) as coustercount from orders;
-- Write a query against the orders table that displays the total number of distinct
-- customers who have placed orders, by customer ID, for each country where orders
-- have been shipped. Again, use an alias to label the count as CustomerCount. Order
-- the list by the CustomerCount, largest to smallest
Select shipcountry, count(distinct customerid) as customercount from orders group by shipcountry order by customercount desc;
-- What are the products that we carry where we have less than 25 units on hand, but 1
-- or more units of them are on order? Write a query that orders them by quantity on
-- order (high to low), then by product name.
Select * from products where unitsinstock < 25 and unitsonorder > 1 order by unitsinstock asc, productname;
-- Write a query to list each of the job titles in employees, along with a count of how
-- many employees hold each job title.
Select title, count(*) as employeecount from employees group by title;
-- What employees have a monthly salary that is between $2000 and $2500? Write a query that orders them by job title.
Select * from employees where salary > 2000 and salary < 2500;

