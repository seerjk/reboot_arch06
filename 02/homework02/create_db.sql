-- create_db.sql
-- create db testdb
create database if not exists testdb default charset utf8;

use testdb;
create table employee (
    first_name char(20) not null,
    last_name char(20),
    age int,
    sex char(1),
    income float
);

insert into employee values ('kun','jiang',25,'m',1000);
insert into employee (first_name, age, sex, income) values ('Lily', 26, 'f', 10000);

-- grant all on testdb.* to 'testuser'@"%" identified by "test123";
-- grant all on testdb.* to 'testuser'@"192.168.3.%" identified by "test123";
-- source /home/jiangk/reboot_arch06/02/homework02/create_db.sql;