CREATE TABLE users (
    id INT AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255),
    birthday DATE,
    interests VARCHAR(255),
    PRIMARY KEY (id)
);