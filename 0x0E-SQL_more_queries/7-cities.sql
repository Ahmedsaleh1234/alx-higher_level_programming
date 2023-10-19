-- a script that creates the database hbtn_0d_usa

create database if not exists hbtn_0d_usa;
create table if not exists hbtn_0d_usa.cities
(
	id int unique auto_increment primary key,
	state_id int not null ,
	foreign key(state_id) references hbtn_0d_usa.states(id),
	name varchar(256) not null
);
