-- CHECKING FIRST TRIGGER FUNCTION
/*
    Note that this ↓ query will rais ERROR
    Because the last row violates 
    check constraint "participate_participate_count_check"
*/
INSERT INTO participate 
(p_id, user_id, camp_id, p_date, result) VALUES
(11111, 4011, 342, '2020-09-15', true),
(11112, 4011, 342, '2020-09-16', false),
(11113, 4011, 342, '2020-09-17', true),
(11114, 4011, 342, '2020-09-18', false),
(11115, 4011, 342, '2020-09-18', true);

-- CHECKING SECOND TRIGGER FUNCTION
/*
    It should the referenced record in be_exist
    table when deleting a record from branch table.
*/
SELECT * FROM branch;
SELECT * FROM be_exist;

DELETE FROM branch
WHERE branch_id = 14;

SELECT * FROM branch;
SELECT * FROM be_exist;

-- CHECKING THIRD TRIGGER FUNCTION
/*
    It should add the new cloth to the be_exist table
*/

SELECT * FROM be_exist;

INSERT INTO cloth VALUES
(121, '/Users/DB/Desktop/Slides/40.png', 300),
(122, '/Users/DB/Desktop/Slides/41.png', 320);

SELECT * FROM be_exist;