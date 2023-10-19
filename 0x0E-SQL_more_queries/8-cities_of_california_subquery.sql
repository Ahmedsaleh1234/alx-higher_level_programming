-- lists all the cities of California in the database hbtn_0d_usa
   -- states table contains only one record where name = California
   -- Results must be sorted in ascending order by cities.id
   -- The database name will be passed as an argument of the mysql command

select id, name from cities
where state_id = 
(
	select id from states 
	where name = "California"
)
order by id;
