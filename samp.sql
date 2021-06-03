-- Create table
create table character (
	id integer primary key,
	name text NOT NULL,
	gender varchar(1),
	nickname text,
	aff_id integer references affiliation(id) 
);--foriegn key

--Insert data
insert into character (name,gender,aff_id) values ("abhinav", "m",1);
insert into character (name,gender,nickname,aff_id) values
 ("Ruby", "f", "Queen",2);



create table affiliation(
	id integer primary key,
	name text not null,
	location text
);

insert into affiliation (name,location) values ("NITC", "India");
insert into affiliation (name,location) values
("Osaka university", "Japan");

select * from character;
select * from affiliation;
select name,gender from character where id=1;

.mode columns -- Arrange/show as a table

--updating data
update character set name = "Abhinav" where id = 1;

select c.name, c.gender,a.name, a.location from character c, affiliation a where c.aff_id = a.id and a.location = "India";
