Use Northwind;
-- Create a single query to list the product id, product name, unit price and category name of all products. Order by category name and within that, by product name
Select productid, productname, unitprice, categoryname from products join categories on products.categoryid = categories.categoryid order by categories.categoryname, products.productname;
-- Create a single query to list the product id, product name, unit price and supplier name of all products that cost more than $75. Order by product name
Select productid, productname, unitprice, companyname from products join suppliers on products.supplierid = suppliers.supplierid where products.unitprice > 75 order by products.productname asc; 
-- Create a single query to list the product id, product name, unit price, category name, and supplier name of every product. Order by product name
select productid, productname, unitprice, categoryname, companyname from products join categories on products.categoryid = categories.categoryid join suppliers on suppliers.supplierid = products.supplierid order by productname asc;
-- Create a single query to list the order id, ship name, ship address, and shipping
-- company name of every order that shipped to Germany. Assign the shipping company
-- name the alias ‘Shipper.’ Order by the name of the shipper, then the name of who it
-- shipped to
Select orderid, shipname, shipaddress, suppliers.companyname shipper from orders join suppliers on orders.shipvia = suppliers.supplierid where orders.shipcountry = 'Germany' order by shipper asc, orders.shipname asc;
-- Start from the same query as above (#4), but omit OrderID and add logic to group by ship name, with a count of how many orders were shipped for that ship name.
SELECT orders.ShipName, orders.ShipAddress, suppliers.CompanyName AS Shipper, COUNT(*) AS OrderCount FROM orders JOIN suppliers ON orders.ShipVia = suppliers.SupplierID WHERE orders.ShipCountry = 'Germany' GROUP BY  orders.ShipName, orders.ShipAddress, suppliers.CompanyName ORDER BY Shipper ASC, orders.ShipName ASC;
-- Create a single query to list the order id, order date, ship name, ship address of all orders that included Sasquatch Ale
Select orders.orderid, orders.orderdate, orders.shipname, orders.shipaddress from orders join `order details` on orders.orderid = `order details`.orderid join products on `order details`.productid = products.productId where products.productname = 'Sasquatch Ale';