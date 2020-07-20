INSERT INTO seller VALUES
(1001, 'mohsen', '9124639289'),
(1002, 'mohadese', '9195263864'),
(1003, 'danial', '9367780945'),
(1004, 'tohid', '9144637689'),
(1005, 'ali', '9134639346'),
(1006, 'farzane', '9214245289'),
(1007, 'hushang', '9374667989'),
(1008, 'mahdi', '9123480589'),
(1009, 'mirtra', '9914667280'),
(1010, 'keyvan', '9358820983');

INSERT INTO branch VALUES
(11, 1001, 'folani', '59 Barrow Close, Marlborough, SN8 2BE', '88345678'),
(12, 1005, 'Draughting', 'Units 8-10, 6 Fairfields, Free Prae Rd, Chertsey, KT16 8EA', '70012159'),
(13, 1008, 'NameFitness', '59 Barrow Close, Marlborough, SN8 2BE', '88345678'),
(14, 1002, 'Logistics', 'Unit E, Lee Bridge, Dean Clough Industrial Park, Halifax, HX3 5AT', '16665071'),
(21, 1008, 'Antony', 'Unit E, Lee Bridge, Dean Clough', '17035080'),
(15, 1009, 'NamePEST', '260 Oatsheaf Road, Fleet, GU51 4BX', '40776248'),
(16, 1003, 'Shipping', 'Unit 26 Riverwalk Business Park, Riverwalk Road, Enfield, EN3 7QN', '26902725'),
(17, 1006, 'NameFinches', 'AddressUnit 8, Conway Industrial Estate, Skull House Lane, Wigan, WN6 9DW', '23155431'),
(18, 1004, 'Design Studio', '111 Gracehill Rd, Ballymoney, BT53 8JD', '31384058'),
(19, 1007, 'Millburn', '165 Galashiels Rd, Galashiels, TD1 2RE', '39670084'),
(20, 1010, 'Infocore Ltd', '2 Laurier Court, Laurier Rd, London, NW5 1SE', '41324825');

INSERT INTO cloth VALUES
(111, '/Users/DB/Desktop/Slides/81.png', 120),
(112, '/Users/DB/Desktop/Slides/82.png', 330),
(113, '/Users/DB/Desktop/Slides/83.png', 650),
(114, '/Users/DB/Desktop/Slides/84.png', 30),
(115, '/Users/DB/Desktop/Slides/85.png', 260),
(116, '/Users/DB/Desktop/Slides/86.png', 180),
(117, '/Users/DB/Desktop/Slides/87.png', 390),
(118, '/Users/DB/Desktop/Slides/88.png', 490),
(119, '/Users/DB/Desktop/Slides/89.png', 260),
(120, '/Users/DB/Desktop/Slides/90.png', 150);

INSERT INTO users VALUES
(4011, 'sadegh', '5767619364', 1200, '{"1":"$DLOCP"}'),
(4012, 'laleh', '3532329974', 300, '{"1":"$lIvBc"}'),
(4013, 'iman', '1319565524', 5600, '{"1":"$xZnsV"}'),
(4014, 'mobin', '8907666586', 7000, '{"1":"$zoppM"}'),
(4015, 'fatemeh', '3359809451', 100, '{"1":"$XSKCp"}'),
(4016, 'ali', '2422567034', 10, '{"1":"$dZWSk"}'),
(4017, 'hosein', '4406973590', 100, '{"1":"$MlFdr"}'),
(4018, 'foad', '1322502798', 6200, '{"1":"$dGIVQ"}'),
(4019, 'davud', '1044584472', 33200, '{"1":"$SHMQF"}'),
(4020, 'asghar', '8298037782', 5050, '{"1":"$WqOfj"}');

INSERT INTO campaign VALUES
(341, 1005, 'NEW DAY', '2020-08-04'),
(343, 1001, 'BE HAPPY', '2020-09-23'),
(345, 1007, 'GO WLAKING', '2020-10-13'),
(342, 1004, 'SEE YOU', '2020-11-17'),
(346, 1003, 'SEE', '2020-11-12'),
(344, 1010, 'HELLO', '2020-12-25');

INSERT INTO checkers VALUES
(146, 'hamed', '7406512149'),
(149, 'fariba', '5670195075'),
(147, 'sara', '6292638529'),
(148, 'mohammad', '7068158426'),
(145, 'reza', '5622548903');

INSERT INTO buy VALUES
(251, 4011, 114, 30, '2020-05-28'),
(252, 4020, 117, 380, '2020-06-22'),
(253, 4012, 111, 120, '2020-11-21'),
(253, 4012, 117, 390, '2020-11-21'),
(253, 4012, 115, 250, '2020-11-21'),
(254, 4014, 113, 600, '2020-01-17'),
(255, 4013, 115, 250, '2020-07-22'),
(256, 4015, 117, 390, '2020-06-30'),
(256, 4015, 119, 260, '2020-06-30'),
(256, 4015, 116, 180, '2020-06-30'),
(257, 4017, 112, 330, '2020-03-12'),
(258, 4018, 116, 100, '2020-08-28'),
(259, 4016, 118, 490, '2020-02-05'),
(260, 4018, 120, 130, '2020-08-06');

INSERT INTO orders VALUES
(41, 253, 4013, '2020-01-29'),
(42, 257, 4017, '2020-02-28'),
(43, 259, 4020, '2020-07-14'),
(47, 256, 4011, '2020-05-20'),
(44, 255, 4016, '2020-08-04'),
(45, 252, 4018, '2020-10-30'),
(46, 252, 4012, NOW() :: DATE);

INSERT INTO express VALUES
(52, 'hasan', '4501876653'),
(53, 'mehran', '6580321549'),
(51, 'navid', '8419559054'),
(55, 'hamid', '5878320343'),
(54, 'nima', '6622494070');

INSERT INTO receiving VALUES
(201, 53, 42, '2020-04-09'),
(203, 55, 41, '2020-06-08'),
(204, 51, 43, '2020-08-24'),
(206, 54, 47, '2020-08-24'),
(205, 51, 45, '2020-08-24');

INSERT INTO participate 
(p_id, user_id, camp_id, p_date, result) VALUES
(301, 4013, 342, '2020-07-15', true),
(302, 4014, 343, '2020-07-15', false),
(304, 4013, 342, '2020-07-16', true),
(305, 4013, 342, '2020-07-17', true),
(306, 4013, 342, '2020-07-15', true),
(307, 4013, 342, '2020-08-15', false),
(308, 4014, 341, '2020-08-15', true),
(309, 4017, 345, '2020-08-15', true),
(310, 4018, 342, '2020-08-15', true);

INSERT INTO cloth_check VALUES
(21, 113, 147, '2020-03-30'),
(22, 116, 145, '2020-02-14'),
(23, 111, 149, '2020-03-28'),
(24, 119, 147, '2020-05-14'),
(25, 120, 146, '2020-11-12');

INSERT INTO seller_check VALUES
(31, 1004, 147, '2020-11-15'),
(32, 1006, 145, '2020-11-15'),
(33, 1007, 149, '2020-11-15'),
(34, 1009, 148, '2020-11-15'),
(35, 1002, 146, '2020-11-15');

INSERT INTO be_exist VALUES
(113, 13),
(116, 14),
(115, 13),
(115, 12),
(119, 13),
(117, 15),
(117, 21),
(117, 12),
(119, 12),
(118, 13),
(118, 21),
(113, 21);
