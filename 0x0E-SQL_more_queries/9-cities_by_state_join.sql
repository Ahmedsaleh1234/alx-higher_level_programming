-- script that lists all cities contained in the database

select cities.id, cities.name, states.name from cities
join states on cities.state_id = states.id
order by cities.id;
