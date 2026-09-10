-- SELECT*FROM longlist;
-- SELECT title,author FROM longlist WHERE year=2023
-- SELECT title FROM longlist limit 5
-- SELECT*FROM longlist LIMIT 5;
-- ═════════════════════════════════════════════════════════════════════════════
-- NOTE: sql is un senstive language => select is SELECT but we used upercase for a commands to organize our code
-- Topic: important and sample commands
-- Select = extract data
--
-- هنا انا بقوله هاتلي title من longlist بس بدون تكرار للعناوين 
SELECT DISTINCT title FROM longlist;

SELECT count(DISTINCT title) FROM longlist;
--we can count the number of unique tilte

--FROM = atatchment distnation
--UPDATE - updates data in a database
-- DELETE - deletes data from a database
-- INSERT INTO - inserts new data into a database
-- CREATE DATABASE - creates a new database
-- ALTER DATABASE - modifies a database
-- CREATE TABLE - creates a new table
-- ALTER TABLE - modifies a table
-- DROP TABLE - deletes a table
-- CREATE INDEX - creates an index (search key)
-- DROP INDEX - deletes an index

