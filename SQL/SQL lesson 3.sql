USE NORTHWND

--SELECT OD.OrderID,
--       OD.ProductID,
--	   OD.Quantity,
--	   OD.UnitPrice,
--	   OD.Quantity * OD.UnitPrice AS Total
--FROM [Order Details] AS OD



--SELECT p.ProductName,
--       P.UnitPrice,
--	   P.UnitPrice * 3.5 AS PriceSh...,
--FROM Products AS P


--SELECT E.*
--FROM Employees AS E
--WHERE EmployeeId = 5 OR EmployeeId = 6


--SELECT E.*
--FROM Employees AS E
--WHERE EmployeeId <= 5


--SELECT *
--FROM Employees AS E
--WHERE EmployeeId >= 3 AND EmployeeId <= 8

--SELECT *
--FROM Employees AS E
--WHERE EmployeeId BETWEEN 3 AND 8


--SELECT *
--FROM Employees AS E
--WHERE E.FirstName = 'гег'

--SELECT E.*
--FROM Employees AS E
--WHERE E.FirstName = 'Nancy'

--SELECT E.*
--FROM Employees AS E
--WHERE E.FirstName LIKE 'Nancy'


--SELECT C.*
--FROM Customers AS C
--WHERE C.Country LIKE 'USA' OR C.Country LIKE 'CANADA' OR C.Country LIKE 'MEXICO'

--SELECT C.*
--FROM Customers AS C
--WHERE C.Country IN ('USA', 'CANADA', 'MEXICO')


--SELECT E.*
--FROM Employees AS E
--WHERE E.HireDate = '03/15/1995'


--SELECT E.*
--FROM Employees AS E
--WHERE E.HireDate BETWEEN  '06/01/1992' AND '12/31/1993'


--SELECT C.*
--FROM Customers AS C
--WHERE CustomerId > 200 AND DEPTID=14


-------  Page 27 -----


--SELECT C.CustomerID,
--       C.CompanyName,
--	   C.City,
--	   C.Country,
--	   C.ContactTitle
--FROM Customers AS C
--WHERE C.Country = 'FRANCE' AND ContactTitle = 'Owner'


--SELECT C.CustomerID,
--       C.CompanyName,
--	   C.City,
--	   C.Country,
--	   C.ContactTitle
--FROM Customers AS C
--WHERE C.Country IN ('USA', 'FRANCE')



--SELECT DISTINCT C.Country
--FROM Customers AS C
--ORDER BY C.Country DESC


--SELECT C.*
--FROM Customers AS C
--WHERE C.City LIKE 'jerusalem'

--SELECT C.*
--FROM Customers AS C
--WHERE C.City LIKE 'London'

--SELECT E.EmployeeID,
--       E.Title,
--	   E.FirstName,
--	   E.LastName
--FROM Employees AS E
--WHERE E.Country LIKE 'USA'

--SELECT E.*
--FROM Employees AS E
--WHERE E.EmployeeID < 10

--SELECT P.ProductID,
--       P.ProductName,
--	   P.QuantityPerUnit
--FROM Products AS P
--WHERE P.ProductName LIKE '[ABC]%'
--ORDER BY P.ProductName 

--SELECT *
--FROM Orders AS O
--WHERE O.Freight < 35


--SELECT????
--FROM Orders AS O
--WHERE MONTH ????


--SELECT O.OrderID,
--       O.OrderDate,
--	   DATEPART(QUARTER, O.OrderDate) AS Q1
--FROM Orders AS O
--WHERE DATEPART(QUARTER, O.OrderDate)% 2 = 0


--SELECT *
--FROM Orders AS O
--WHERE DATEPART(YEAR, O.OrderDate)= 1998 
--AND O.Freight <15

--SELECT *
--FROM Orders AS O
--WHERE  O.Freight NOT BETWEEN 10 AND 35

--SELECT *
--FROM Employees AS E
--WHERE E.City = 'London' AND DATEPART(YEAR, E.BirthDate) > 1950
--OR E.City LIKE '%Seattle%'
--ORDER BY E.City

--SELECT *
--FROM Products AS P
--WHERE P.UnitPrice BETWEEN 50 AND 100
--OR P.QuantityPerUnit LIKE '%BOXES%'
--ORDER BY P.UnitPrice

--SELECT O.OrderID,
--       O.OrderDate,
--	   DATEPART (MONTH, O.OrderDate) AS Month,
--	   O.Freight * 3.5 AS InShekel
--FROM Orders AS O
--WHERE DATEPART (YEAR, O.OrderDate) BETWEEN 1996 AND 1997
--AND DATEPART (MONTH, O.OrderDate) % 2 =0
--ORDER BY MONTH, InShekel


--SELECT O.OrderID,
--       DATEPART(MONTH, O.OrderDate) AS Month,
--	   DATEPART(QUARTER, O.OrderDate),
--	   O.OrderDate,
--	   O.Freight
--FROM Orders AS O
--WHERE DATEPART(QUARTER,	O.OrderDate)% 2 = 0
--ORDER BY MONTH, o.Freight


--SELECT O.OrderID,
--       DATEPART(MONTH, O.OrderDate) AS MONTH,
--	   DATEPART(QUARTER, O.OrderDate) AS QUARTER,
--	   O.OrderDate,
--	   O.Freight,
--	   O.ShipCountry
--FROM Orders AS O
--WHERE O.ShipCountry IN ('USA', 'MEXICO', 'CANADA')
--AND DATEPART(QUARTER ,O.OrderDate)% 2 = 0
--AND O.Freight > 20
--ORDER BY MONTH, O.ShipCountry