INSERT INTO users (first_name, last_name)
VALUES 
('Amy', 'Giver'),
('Eli', 'Byers'),
('Kermit', 'The Frog'),
('Big', 'Bird'),
('Marky', 'Mark'),
('Fozzie', 'Bear');
-----------------------------------------------------------------
INSERT INTO friendships (user_id, friend_id)
VALUES 
(1, 2),
(1, 4),
(1, 6),
(2, 1),
(2, 3),
(2, 5),
(3, 2),
(3, 5),
(4, 3),
(5, 1),
(5, 6),
(6, 2),
(6, 3);
---------------------------------------------- 
SELECT 
  u1.first_name AS first_name,
  u1.last_name AS last_name,
  u2.first_name AS friend_first_name,
  u2.last_name AS friend_last_name
FROM users u1
JOIN friendships f ON u1.id = f.user_id
JOIN users u2 ON f.friend_id = u2.id;
------------------------------------------------------
SELECT 
  u2.first_name AS friend_first_name,
  u2.last_name AS friend_last_name
FROM users u1
JOIN friendships f ON u1.id = f.user_id
JOIN users u2 ON f.friend_id = u2.id
WHERE u1.id = 1;
---------------------------------------------------------
SELECT COUNT(*) AS total_friendships
FROM friendships;
--------------------------------------------------------
SELECT 
  u1.first_name,
  u1.last_name,
  COUNT(f.friend_id) AS total_friends
FROM users u1
JOIN friendships f ON u1.id = f.user_id
GROUP BY u1.id
ORDER BY total_friends DESC
LIMIT 1;
---------------------------------------------------------------
SELECT 
  u2.first_name AS friend_first_name,
  u2.last_name AS friend_last_name
FROM users u1
JOIN friendships f ON u1.id = f.user_id
JOIN users u2 ON f.friend_id = u2.id
WHERE u1.id = 3
ORDER BY u2.first_name, u2.last_name;