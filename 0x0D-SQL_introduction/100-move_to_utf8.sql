-- Script that converts hbtn_0c_0 database to UTF8
-- (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.
USE hbtn_0c_0
-- FOR EACH DATABASE
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
-- FOR EACH TABLE 
ALTER TABLE	first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- FOR TEACH COLUMN
ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
