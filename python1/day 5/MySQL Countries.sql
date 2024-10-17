SELECT country.Name AS Country, countrylanguage.Language, countrylanguage.Percentage
FROM country
JOIN countrylanguage ON country.CountryCode = countrylanguage.CountryCode
WHERE countrylanguage.Language = 'Slovene'
ORDER BY countrylanguage.Percentage DESC;
-------------------------------------------------------------------------------
SELECT country.Name AS Country, COUNT(city.ID) AS TotalCities
FROM country
JOIN city ON country.CountryCode = city.CountryCode
GROUP BY country.Name
ORDER BY TotalCities DESC;
----------------------------------------------------------------------------------
SELECT Name AS City, Population
FROM city
WHERE CountryCode = (SELECT CountryCode FROM country WHERE Name = 'Mexico')
AND Population > 500000
ORDER BY Population DESC;
----------------------------------------------------------------------------------------
SELECT country.Name AS Country, countrylanguage.Language, countrylanguage.Percentage
FROM country
JOIN countrylanguage ON country.CountryCode = countrylanguage.CountryCode
WHERE countrylanguage.Percentage > 89
ORDER BY countrylanguage.Percentage DESC;
----------------------------------------------------------------------------------------
SELECT Name AS Country
FROM country
WHERE SurfaceArea < 501 AND Population > 100000;
--------------------------------------------------------------
SELECT Name AS Country
FROM country
WHERE GovernmentForm = 'Constitutional Monarchy' AND Capital > 200 AND LifeExpectancy > 75;
-----------------------------------------------------------------------------------------------
SELECT country.Name AS Country, city.Name AS City, city.District, city.Population
FROM city
JOIN country ON city.CountryCode = country.CountryCode
WHERE country.Name = 'Argentina' AND city.District = 'Buenos Aires' AND city.Population > 500000;
----------------------------------------------------------------------------------------------------
SELECT Region, COUNT(Name) AS NumberOfCountries
FROM country
GROUP BY Region
ORDER BY NumberOfCountries DESC;