-- a script that creates the table unique_id on your MySQL server.

create table if not exists unique_id
(
	id int default 1,
	unique(id),
	name varchar(256)
);
