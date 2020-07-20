CREATE TABLE seller
(
    seller_id INTEGER NOT NULL PRIMARY KEY,
    seller_name TEXT NOT NULL,
    telephone varchar(10) NOT NULL
);

CREATE TABLE branch
(
    branch_id INTEGER NOT NULL,
    seller_id INTEGER NOT NULL REFERENCES seller(seller_id),
    branch_name text NOT NULL,
    branch_address text NOT NULL,
    telephone varchar(10) NOT NULL,
    PRIMARY KEY (branch_id, seller_id),
    CONSTRAINT branch_PK UNIQUE (branch_id)
);

CREATE TABLE cloth
(
    c_id INTEGER NOT NULL PRIMARY KEY,
    pic TEXT NOT NULL,
    price INTEGER NOT NULL
);

CREATE TABLE users
(
    user_id INTEGER NOT NULL PRIMARY KEY,
    user_name TEXT NOT NULL,
    telephone varchar(10) NOT NULL,
    supply INTEGER NOT NULL,
    dis_codes jsonb
);

CREATE TABLE campaign
(
    camp_id INTEGER NOT NULL,
    seller_id INTEGER NOT NULL REFERENCES seller(seller_id),
    camp_name text NOT NULL,
    creation_date date NOT NULL,
    PRIMARY KEY (camp_id, seller_id),
    CONSTRAINT campaign_PK UNIQUE (camp_id)
);

CREATE TABLE checkers
(
    checker_id INTEGER NOT NULL PRIMARY KEY,
    checker_name TEXT NOT NULL,
    telephone varchar(10) NOT NULL
);

CREATE TABLE buy
(
    buy_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL REFERENCES users(user_id),
    c_id INTEGER NOT NULL REFERENCES cloth(c_id),
    payed_money INTEGER NOT NULL,
    buy_date date NOT NULL,
    PRIMARY KEY (buy_id, user_id, c_id)
);

CREATE TABLE orders
(
    order_id INTEGER NOT NULL,
    buy_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL REFERENCES users(user_id),
    order_date date NOT NULL,
    PRIMARY KEY (order_id, buy_id, user_id),
    CONSTRAINT orders_PK UNIQUE (order_id)
);

CREATE TABLE express
(
    ex_id INTEGER NOT NULL PRIMARY KEY,
    ex_name TEXT NOT NULL,
    telephone varchar(10) NOT NULL
);

CREATE TABLE receiving
(
    receive_id INTEGER NOT NULL,
    ex_id INTEGER NOT NULL REFERENCES express(ex_id),
    order_id INTEGER NOT NULL REFERENCES orders(order_id),
    receive_date date NOT NULL,
    PRIMARY KEY (receive_id, ex_id, order_id),
    CONSTRAINT receiving_PK UNIQUE (receive_id)
);

CREATE TABLE participate
(
    p_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL REFERENCES users(user_id),
    camp_id INTEGER NOT NULL REFERENCES campaign(camp_id),
    p_date date NOT NULL,
    Participate_count INTEGER NOT NULL
        CHECK(
            Participate_count BETWEEN 0 AND 3
            ),
    result BOOLEAN NOT NULL,
    PRIMARY KEY (p_id, user_id, camp_id),
    CONSTRAINT participate_PK UNIQUE (p_id)
);
ALTER TABLE participate 
ALTER COLUMN Participate_count SET DEFAULT 0;

CREATE TABLE cloth_check
(
    clc_id INTEGER NOT NULL,
    c_id INTEGER NOT NULL REFERENCES cloth(c_id),
    checker_id INTEGER NOT NULL REFERENCES checkers(checker_id),
    clc_date date NOT NULL,
    PRIMARY KEY (clc_id, c_id, checker_id),
    CONSTRAINT cloth_check_PK UNIQUE (clc_id)
);

CREATE TABLE seller_check
(
    sec_id INTEGER NOT NULL,
    seller_id INTEGER NOT NULL REFERENCES seller(seller_id),
    checker_id INTEGER NOT NULL REFERENCES checkers(checker_id),
    sec_date date NOT NULL,
    PRIMARY KEY (sec_id, seller_id, checker_id),
    CONSTRAINT seller_check_PK UNIQUE (sec_id)
);

CREATE TABLE be_exist
(
    c_id INTEGER NOT NULL REFERENCES cloth(c_id),
    branch_id INTEGER NOT NULL REFERENCES branch(branch_id),
    PRIMARY KEY (c_id, branch_id)
)
