##ADD COUNTRY
USE baies;
EXPLAIN countrys;
INSERT INTO countrys(name) VALUES ('CN');
INSERT INTO countrys(name) VALUE ('EN');
INSERT INTO countrys(name) VALUE ('US');
SELECT * FROM countrys;

##ADD TABLEx

EXPLAIN socioeconomic_tables;
INSERT INTO socioeconomic_tables(name, cn_alis, en_alis) VALUES ('A','表1','table1');
INSERT INTO socioeconomic_tables(name, cn_alis, en_alis) VALUES ('B','表2','table2');
INSERT INTO socioeconomic_tables(name, cn_alis, en_alis) VALUES ('C','表3','table3');
SELECT * FROM socioeconomic_tables;

#ADD INDEX

EXPLAIN socioeconomic_indexes;
INSERT INTO socioeconomic_indexes(name, unit, cn_alis, en_alis, table_id) VALUES ('a','yuan','指标a','indexa',1);
INSERT INTO socioeconomic_indexes(name, unit, cn_alis, en_alis, table_id) VALUES ('b','yuan','指标b','indexb',1);
INSERT INTO socioeconomic_indexes(name, unit, cn_alis, en_alis, table_id) VALUES ('c','yuan','指标c','indexc',1);
INSERT INTO socioeconomic_indexes(name, unit, cn_alis, en_alis, table_id) VALUES ('d','yuan','指标d','indexb',2);
INSERT INTO socioeconomic_indexes(name, unit, cn_alis, en_alis, table_id) VALUES ('a','yuan','指标a','indexb',2);

SELECT * FROM socioeconomic_indexes;

#ADD FACT
EXPLAIN socioeconomic_facts;
INSERT INTO socioeconomic_facts(country_id, time, time_stamp, index_id, value) VALUES (1,'2016-12-31 23:59:59','2018-12-31 23:59:59',1,100);
INSERT INTO socioeconomic_facts(country_id, time, time_stamp, index_id, value) VALUES (1,'2015-12-31 23:59:59','2018-12-31 23:59:59',1,200);
INSERT INTO socioeconomic_facts(country_id, time, time_stamp, index_id, value) VALUES (1,'2016-12-31 23:59:59','2018-12-31 23:59:59',2,100);
INSERT INTO socioeconomic_facts(country_id, time, time_stamp, index_id, value) VALUES (1,'2015-12-31 23:59:59','2018-12-31 23:59:59',2,200);
INSERT INTO socioeconomic_facts(country_id, time, time_stamp, index_id, value) VALUES (1,'2016-12-31 23:59:59','2018-12-31 23:59:59',4,100);
INSERT INTO socioeconomic_facts(country_id, time, time_stamp, index_id, value) VALUES (1,'2015-12-31 23:59:59','2018-12-31 23:59:59',5,200);

INSERT INTO socioeconomic_facts(country_id, time, time_stamp, index_id, value) VALUES (2,'2016-12-31 23:59:59','2018-12-31 23:59:59',1,1000);
INSERT INTO socioeconomic_facts(country_id, time, time_stamp, index_id, value) VALUES (2,'2015-12-31 23:59:59','2018-12-31 23:59:59',1,2000);
INSERT INTO socioeconomic_facts(country_id, time, time_stamp, index_id, value) VALUES (2,'2016-12-31 23:59:59','2018-12-31 23:59:59',2,1000);
INSERT INTO socioeconomic_facts(country_id, time, time_stamp, index_id, value) VALUES (2,'2015-12-31 23:59:59','2018-12-31 23:59:59',2,2000);
INSERT INTO socioeconomic_facts(country_id, time, time_stamp, index_id, value) VALUES (2,'2016-12-31 23:59:59','2018-12-31 23:59:59',4,1000);
INSERT INTO socioeconomic_facts(country_id, time, time_stamp, index_id, value) VALUES (2,'2015-12-31 23:59:59','2018-12-31 23:59:59',5,2000);

SELECT * FROM socioeconomic_facts;

SELECT * FROM post_logs;

# SELECT concat('DROP TABLE IF EXISTS ', table_name, ';')
# FROM information_schema.tables
# WHERE table_schema = 'baies';


ALTER DATABASE baies DEFAULT CHARACTER SET utf8 ;

## ADD KIND

INSERT INTO kinds(name, cn_alis, en_alis) VALUES ('农业发展政策信息','农业发展政策信息','Agricultural Development');
INSERT INTO kinds(name, cn_alis, en_alis) VALUES ('农业贸易政策信息','农业贸易策信息','Agricultural Trade');

INSERT INTO kinds(name, cn_alis, en_alis) VALUES ('农业科技政策信息','农业科技策信息','Agricultural Science and Technology');

INSERT INTO kinds(name, cn_alis, en_alis) VALUES ('鱼林政策信息','鱼林政策信息','Fishery & Aquaculture Policies');

