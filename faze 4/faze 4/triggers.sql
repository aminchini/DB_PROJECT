-- FIRST TRIGGER FUNCTION
/*
    It is used to check Participate_count to be 0 to 3 per month
    Also CHECK( Participate_count BETWEEN 0 AND 3 ) in creating
    the tabel helps us
*/
CREATE OR REPLACE FUNCTION UP_FUNC()
  RETURNS trigger AS
$BODY$
BEGIN  
    IF EXISTS 
	(
		SELECT * FROM participate WHERE 
        participate.user_id = NEW.user_id AND participate.camp_id = NEW.camp_id
        AND EXTRACT(MONTH FROM participate.p_date) = EXTRACT(MONTH FROM NEW.p_date)
        ORDER BY participate.Participate_count DESC
        LIMIT 1
	)
	THEN
        NEW.Participate_count = 
        (
            SELECT Participate_count FROM participate WHERE 
            participate.user_id = NEW.user_id AND participate.camp_id = NEW.camp_id
            AND EXTRACT(MONTH FROM participate.p_date) = EXTRACT(MONTH FROM NEW.p_date)
            ORDER BY participate.Participate_count DESC
            LIMIT 1
	    ) + 1;
    END IF;

	RETURN NEW;
END;
$BODY$ 
LANGUAGE plpgsql VOLATILE;

CREATE TRIGGER Participate_count_update
    BEFORE INSERT ON participate
    FOR EACH ROW EXECUTE PROCEDURE UP_FUNC();


-- SECOND TRIGGER FUNCTION
CREATE OR REPLACE FUNCTION DELETE_FUNC()
  RETURNS trigger AS
$BODY$
BEGIN  
    DELETE FROM be_exist
    WHERE be_exist.branch_id = OLD.branch_id;
    RETURN NEW;
END;
$BODY$ 
LANGUAGE plpgsql VOLATILE;

CREATE TRIGGER delete_branch
    BEFORE DELETE ON branch
    FOR EACH ROW EXECUTE PROCEDURE DELETE_FUNC();


-- THIRD TRIGGER FUNCTION
/*
    The branch "folani" with branch_id = 11 is a very luxury
    brach in the system and always wants to have cloths with 
    the price more than 300. So this trigger is written fro this purpose.
*/
CREATE OR REPLACE FUNCTION ADD_TO_BRANCH()
  RETURNS trigger AS
$BODY$
BEGIN
    IF NEW.price > 300 THEN
        INSERT INTO be_exist VALUES
        (NEW.c_id, 11);
    END IF;
    RETURN NEW;
END;
$BODY$ 
LANGUAGE plpgsql VOLATILE;

CREATE TRIGGER high_price_cloth
    AFTER INSERT ON cloth
    FOR EACH ROW EXECUTE PROCEDURE ADD_TO_BRANCH();