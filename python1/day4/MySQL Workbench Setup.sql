SELECT * FROM names;
INSERT INTO names (first_name, last_name) VALUES ('YourFirstName', 'YourLastName');
INSERT INTO names (first_name, last_name) VALUES 
('FirstName1', 'LastName1'),
('FirstName2', 'LastName2'),
('FirstName3', 'LastName3');
UPDATE names SET first_name = 'UpdatedFirstName' WHERE id = 1;
DELETE FROM names WHERE id = 1;