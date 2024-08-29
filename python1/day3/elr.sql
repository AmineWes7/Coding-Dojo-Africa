CREATE TABLE dojos (
  id INT AUTO_INCREMENT,
  name VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

CREATE TABLE ninjas (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(255),
  last_name VARCHAR(255),
  age INT,
  dojo_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (dojo_id) REFERENCES dojos(id)
);
INSERT INTO dojos (name) VALUES ('Dojo 1'), ('Dojo 2'), ('Dojo 3');
DELETE FROM dojos WHERE id IN (1, 2, 3);
INSERT INTO dojos (name) VALUES ('Dojo 4'), ('Dojo 5'), ('Dojo 6');
INSERT INTO dojos (name) VALUES ('Dojo 4'), ('Dojo 5'), ('Dojo 6');
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES 
  ('Ninja 1', 'Lastname 1', 25, 4),
  ('Ninja 2', 'Lastname 2', 30, 4),
  ('Ninja 3', 'Lastname 3', 20, 4);
  INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES 
  ('Ninja 4', 'Lastname 4', 25, 5),
  ('Ninja 5', 'Lastname 5', 30, 5),
  ('Ninja 6', 'Lastname 6', 20, 5);
  INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES 
  ('Ninja 7', 'Lastname 7', 25, 6),
  ('Ninja 8', 'Lastname 8', 30, 6),
  ('Ninja 9', 'Lastname 9', 20, 6);
SELECT * FROM ninjas WHERE dojo_id = 4;
SELECT dojos.name FROM dojos JOIN ninjas ON dojos.id = ninjas.dojo_id ORDER BY ninjas.id DESC LIMIT 1;
SELECT ninjas.*, dojos.name AS dojo_name FROM ninjas JOIN dojos ON ninjas.dojo_id = dojos.id WHERE ninjas.id = 6;
SELECT ninjas.*, dojos.name AS dojo_name FROM ninjas JOIN dojos ON ninjas.dojo_id = dojos.id;