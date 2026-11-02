Use northwind;
-- What is the product name of the most expensive products?
Select * from products where unitprice = (Select MAX(unitprice) from products);
-- What is the product name(s) and categories of the least expensive products?
SELECT ProductName, UnitPrice FROM products WHERE UnitPrice = (SELECT MIN(UnitPrice) FROM products);
-- What is the order id, shipping name and shipping address of all orders shipped via "Federal Shipping"?
Select orderid, shipname, shipaddress from orders where shipvia =(select shipperid from shippers where companyname = 'federal shipping');
-- What are the order ids of the orders that included "Sasquatch Ale"?
Select orderid from `order details` where productId =(select productid from products where productname ='Sasquatch Ale');
-- What is the name of the employee that sold order 10266?
Select FirstName from employees where employeeID = (select employeeid from orders where orderid = 10266);
-- What is the name of the customer that bought order 10266?
Select ContactName from customers where customerId = (Select customerid from orders where orderid =10266);


