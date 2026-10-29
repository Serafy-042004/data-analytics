USe Northwind;
-- Write a query to find the price of the cheapest item that Northwind sells. Then write a second query to find the name of the product that has that price
select Min(unitprice) from products; 
select * from products where unitprice = 2.50;
-- Write a query to find the average price of all items that Northwind sells
Select round(avg(unitprice), 2) from products;
-- Write a query to find the price of the most expensive item that Northwind sells. Then
-- write a second query to find the name of the product with that price, plus the name of
-- the supplier for that product
Select max(unitprice) from products;
Select productid, productname, suppliers.companyname, unitprice from products join suppliers on products.supplierid = suppliers.supplierid where products.unitprice =263.50;
-- Write a query to find total monthly payroll
Select Sum(Salary) from employees;
-- Write a query to identify the highest salary and the lowest salary amounts which any employee makes.
Select min(salary), max(salary) from employees;
-- Write a query to find the name and supplier ID of each supplier and the number of items they supply.
Select suppliers.companyname, suppliers.supplierid, count(distinct products.productid) as items from products join suppliers on products.supplierid = suppliers.supplierid group by suppliers.companyname, suppliers.supplierId order by items asc; 
-- Write a query to find the list of all category names and the average price for items in each category
Select categories.categoryname, round(avg(products.unitprice),2) from categories join products on categories.categoryid = products.categoryid group by categoryname;
-- Write a query to find, for all suppliers that provide at least 5 items to Northwind, what
-- is the name of each supplier and the number of items they supply
Select suppliers.companyname, suppliers.supplierid, count(distinct products.productid) as items from products join suppliers on products.supplierid = suppliers.supplierid group by suppliers.companyname, suppliers.supplierId having count(distinct products.productid) >= 5;
-- Write a query to list products currently in inventory by the product id, product name,
-- and inventory value (calculated by multiplying unit price by the number of units on
-- hand). Sort the results in descending order by value. If two or more have the same
-- value, order by product name. If a product is not in stock, leave it off the list
SELECT ProductID, ProductName, UnitPrice * UnitsInStock AS inventory_value FROM products Where unitsinstock > 0 ORDER BY inventory_value DESC, ProductName ASC;


