
INSERT INTO dojos (name, location) VALUES ('Dojo A', 'Location A'), ('Dojo B', 'Location B'), ('Dojo C', 'Location C');

DELETE FROM dojos WHERE name IN ('Dojo A', 'Dojo B', 'Dojo C');


INSERT INTO dojos (name, location) VALUES ('Dojo D', 'Location D'), ('Dojo E', 'Location E'), ('Dojo F', 'Location F');


INSERT INTO ninjas (first_name, last_name, dojo_id) VALUES ('Ninja 1A', 'Ninja 1B', 1), ('Ninja 2A', 'Ninja 2B', 1), ('Ninja 3A', 'Ninja 3B', 1);


INSERT INTO ninjas (first_name, last_name, dojo_id) VALUES ('Ninja 1C', 'Ninja 1D', 2), ('Ninja 2C', 'Ninja 2D', 2), ('Ninja 3C', 'Ninja 3D', 2);


INSERT INTO ninjas (first_name, last_name, dojo_id) VALUES ('Ninja 1E', 'Ninja 1F', 3), ('Ninja 2E', 'Ninja 2F', 3), ('Ninja 3E', 'Ninja 3F', 3);


SELECT * FROM ninjas WHERE dojo_id = 1;


SELECT * FROM ninjas WHERE dojo_id = (SELECT id FROM dojos ORDER BY id DESC LIMIT 1);

SELECT dojos.* FROM dojos JOIN ninjas ON dojos.id = ninjas.dojo_id ORDER BY ninjas.id DESC LIMIT 1;

SELECT ninjas.*, dojos.* FROM ninjas JOIN dojos ON ninjas.dojo_id = dojos.id WHERE ninjas.id = 6;

SELECT ninjas.*, dojos.* FROM ninjas JOIN dojos ON ninjas.dojo_id = dojos.id;
