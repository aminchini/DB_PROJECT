import psycopg2

q ={
    '1': 
    """
    SELECT sl.seller_id, sl.seller_name, sl.telephone AS seller_telephone, 
    br.branch_id, br.branch_name, br.branch_address, br.telephone AS branch_telephone
    FROM seller AS sl JOIN branch AS br ON sl.seller_id = br.seller_id;
    """ ,
    '2': 
    """
    WITH data AS (SELECT o.order_date, b.c_id FROM buy AS b 
    JOIN orders AS o ON o.buy_id = b.buy_id)

    SELECT cl.c_id, cl.pic, cl.price FROM 
    data AS ord JOIN cloth AS cl
    ON ord.c_id = cl.c_id
    WHERE ord.order_date = '2020-01-29' :: DATE; 
    """,
    '3': 
    """
    SELECT user_id, COUNT(Participate_count) FROM participate
    WHERE result = true
    GROUP BY user_id
    """,
    '4': 
    """
    SELECT cl.c_id, cl.pic, cl.price FROM 
    buy AS bu JOIN cloth AS cl ON bu.c_id = cl.c_id
    WHERE bu.payed_money < cl.price AND 
    bu.buy_id IN 
    (
        SELECT buy_id FROM orders
        WHERE order_id IN 
        (
            SELECT order_id FROM RECEIVING
        )
    )
    """,
    '5':
    """
    WITH data AS
    (
        SELECT user_id, COUNT(p_id) FROM participate
        WHERE result = true AND camp_id IN
        (
            SELECT camp_id FROM campaign
            WHERE seller_id = 1004
        )
        GROUP BY user_id
        HAVING COUNT(p_id) > 1
    )
    SELECT COUNT(user_id) FROM data;
    """,
    '6': 
    """
    WITH data AS
    (
        SELECT be.branch_id, cl.* FROM 
        be_exist AS be JOIN cloth AS cl
        ON be.c_id = cl.c_id
    )

    SELECT SUM(price) FROM data AS dd 
    JOIN branch AS br ON dd.branch_id = br.branch_id
    WHERE br.seller_id = 1008 AND br.branch_id = 13;
    """ ,
    '7': 
    """
    WITH option_ AS
    (
        WITH data AS
        (
            SELECT be.branch_id, cl.* FROM 
            be_exist AS be JOIN cloth AS cl
            ON be.c_id = cl.c_id
        )
        SELECT seller_id, c_id , price FROM branch AS br JOIN data AS d ON d.branch_id = br.branch_id
    )
    SELECT SUM(price), seller_id FROM option_ 
    WHERE c_id IN 
    (
        SELECT c_id FROM buy 
        WHERE EXTRACT(MONTH FROM buy_date) = EXTRACT(MONTH FROM '2020-06-22' :: DATE)
    )
    GROUP BY seller_id
    ORDER BY SUM(price) DESC
    LIMIT 1;
    """ ,
    '8': 
    """
    WITH data AS
    (
        SELECT user_id, COUNT(p_id) FROM participate
        WHERE result = true
        GROUP BY user_id
        ORDER BY COUNT(p_id) DESC
        LIMIT 1
    )
    SELECT * FROM users
    WHERE users.user_id = (SELECT user_id FROM data)
    """ ,
    '9': 
    """
    WITH data AS
    (
        SELECT be.branch_id, cl.* FROM 
        be_exist AS be JOIN cloth AS cl
        ON be.c_id = cl.c_id
    )
    SELECT DISTINCT(c_id) FROM branch AS br JOIN data AS d ON d.branch_id = br.branch_id
    WHERE seller_id = 1005 AND c_id IN 
    (
        SELECT c_id FROM branch AS br JOIN data AS d ON d.branch_id = br.branch_id
        WHERE seller_id = 1008
    ) OR seller_id = 1008 AND c_id IN 
    (
        SELECT c_id FROM branch AS br JOIN data AS d ON d.branch_id = br.branch_id
        WHERE seller_id = 1005
    )    
    """ ,
    '10': 
    """
    SELECT ex_id , COUNT(ex_id) FROM receiving
    WHERE order_id IN
    (
        SELECT order_id FROM orders
        WHERE buy_id IN
        (
            SELECT buy_id FROM buy
            GROUP BY buy_id
            HAVING COUNT(c_id) > 2
        )
    )
    GROUP BY ex_id;
    """ ,
    '11': 
    """
    WITH data AS
    (
        SELECT clc_id AS id, c_id AS checked_item, checker_id, clc_date AS date 
        FROM cloth_check 
        WHERE checker_id = 147
        UNION ALL
        SELECT sec_id AS id, seller_id AS checked_item, checker_id, sec_date AS date 
        FROM seller_check 
        WHERE checker_id = 147
    )
    SELECT * FROM data
    ORDER BY date;
    """ ,
    '12': 
    """
    WITH data AS
        (
            SELECT be.branch_id, cl.* FROM 
            be_exist AS be JOIN cloth AS cl
            ON be.c_id = cl.c_id
        )
    SELECT DISTINCT seller_id, c_id , price FROM branch AS br JOIN data AS d ON d.branch_id = br.branch_id
    WHERE seller_id = 1008
    ORDER BY price;
    """ ,
    '13': 
    """
    WITH found_users AS
    (
        WITH option_ AS
        (
            WITH data AS
            (
                SELECT be.branch_id, cl.* FROM 
                be_exist AS be JOIN cloth AS cl
                ON be.c_id = cl.c_id
            )
            SELECT seller_id, c_id FROM branch AS br JOIN data AS d 
            ON d.branch_id = br.branch_id
            WHERE seller_id = 1008
        )
        SELECT user_id FROM option_ AS op JOIN buy AS b 
        ON op.c_id = b.c_id
    )
    SELECT * FROM users
    WHERE user_id IN 
    (
        SELECT fu.user_id FROM found_users AS fu JOIN participate AS p
        ON p.user_id = fu.user_id
        WHERE p.result = false

    )
    """ ,
    '14': 
    """
    WITH raw_ AS
    (
        SELECT b.user_id, SUM(c.price) AS raw_price FROM buy AS b JOIN cloth AS c
        ON c.c_id = b.c_id
        WHERE b.user_id = 4012
        GROUP BY b.user_id
    ),
    codes AS
    (
        SELECT jsonb_object_keys(dis_codes) FROM users 
        WHERE user_id = 4012
    ),
    dis AS(
        SELECT user_id, supply, 
        CASE
            WHEN (SELECT COUNT(*) FROM codes) > 0 THEN true
            ELSE false
        END AS has_dis
        FROM users 
        WHERE user_id = 4012
    )
    SELECT r.*, d.supply, d.has_dis,
    CASE
        WHEN d.has_dis = true THEN raw_price*0.9
        ELSE raw_price
    END AS total_price,
    CASE
        WHEN d.has_dis = true AND raw_price*0.9 < d.supply THEN true
        WHEN d.has_dis = false AND raw_price < d.supply THEN true
        ELSE false
    END AS can_buy
    FROM raw_ AS r JOIN dis AS d
    ON d.user_id = r.user_id;
    """ ,
    '15': 
    """
    WITH branch_cloth AS
    (
        SELECT be.branch_id, c.* FROM 
        be_exist AS be JOIN cloth AS c
        ON be.c_id = c.c_id
    ),
    seller_cloth AS
    (
        SELECT s.seller_id, bc.* FROM
        branch AS s JOIN branch_cloth AS bc
        ON s.branch_id = bc.branch_id
    )
    SELECT * FROM seller_cloth
    WHERE seller_id = 1008
    """ ,
    }

connection = psycopg2.connect(user="postgres",
                                password="asdf",
                                host="127.0.0.1",
                                port="5432",
                                database="DB_project")
cursor = connection.cursor()

def query(N):
    try:
        cursor.execute(q[N])
        return cursor.fetchall()
    except (Exception, psycopg2.Error) as error :
        print ("Error while fetching data from PostgreSQL", error)
        return [('Error')]
