-- lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.
-- INSERT INTO second_table ('name', 'score') VALUES ('Aria', 18);
-- INSERT INTO second_table ('name', 'score') VALUES ('Aria', 12);
-- DELETE FROM second_table WHERE name = 'George';
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
