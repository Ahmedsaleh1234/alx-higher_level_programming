--  a script that creates the database hbtn_0d_usa

create database if not exists hbtn_0d_usa;
create table if not exists hbtn_0d_usa.states
(
	id int unique not null auto_increment primary key,
	name varchar(256)
);
