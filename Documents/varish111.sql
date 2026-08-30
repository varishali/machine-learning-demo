CREATE DATABASE IF NOT EXISTS june_sql_db;
USE june_sql_db;
DROP TABLE IF EXISTS user_table;

CREATE TABLE user_table(
   id INT,
   naam VARCHAR(100),
   gmail VARCHAR(100),
   gender ENUM('Male', 'Female', 'other'),
   account_id  VARCHAR(100)
   );
   
   INSERT INTO user_table (id,naam,gmail,gender,account_id)
    VALUES
    (1, 'Varish','varish@gmail.com','Male',835767),
   (2, 'Zainul','apnacollage@gamil.com','Male',498974);
         SELECT * FROM user_table;
   
   
   
   
