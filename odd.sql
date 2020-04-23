 drop table musician;
 drop table instrument;
 drop table plays;
 drop table songs;
 drop table performs;
 drop table album;
 
 
 create table musician
 (
 ssn integer primary key,
 name varchar(30),
 addr  varchar(30),
 phone integer
 );



create table instrument
(
id integer primary key,
iname varchar(30),
mkey  varchar(10)
);



 create table plays
 (
 ssn integer references musician(ssn),
 id integer references instrument(id), 
 primary key(ssn,id)
 );


create table album
(
aid integer primary key, 
atitle varchar(30), 
format varchar(5),
rdate date,
ssn integer references musician(ssn)
);

create table songs
(
title varchar(10) primary key, 
author varchar(20),
aid integer references album(aid)
);

 
create table performs
(
title varchar(10) references songs(title),
ssn integer references musician(ssn), 
primary key(title,ssn)
);





desc instrument;
desc musician;
desc plays;





insert into musician values(123,'rahaman','bangalore',232456);
insert into musician values(124,'shreya','mumbai',232477);
insert into musician values(125,'rahim','hubli',232458);
insert into musician values(126,'strusti','mumbai',232479);
insert into musician values(127,'neelendra','MP',232460);
insert into musician values(128,'nandish','khanpur',232478);
select * from musician;


insert into instrument values(1,'guitar','high');
insert into instrument values(2,'flute','low');
insert into instrument values(3,'synthesiezer','high');
select * from instrument;

insert into plays values(123,1);
insert into plays values(124,2);
insert into plays values(125,3);
insert into plays values(126,1);
insert into plays values(127,2);
insert into plays values(128,2);
insert into plays values(123,2);
select * from plays;


insert into album values(101,'abc','cd','20-3-2010',123);
insert into album values(102,'xyz','dvd','6-12-1999',124);
insert into album values(103,'nmp','cd','2-4-2011',125);
insert into album values(104,'kyc','dvd','6-12-1996',123);
insert into album values(105,'gfh','cd','20-3-2018',126);
insert into album values(106,'kle','dvd','6-12-1998',127);
insert into album values(107,'manju','dvd','6-12-1998',127);
select * from album;


insert into songs values('jaadu','kiran',102);
insert into songs values('sri sai','krishna',101);
insert into songs values('magic','kaveri',103);
insert into songs values('om shiv','shivu',104);
insert into songs values('ESCN','rcbian',105);
insert into songs values('nirab','nihal',106);
insert into songs values('india','modi',104);
insert into songs values('bean','raju',103);
select * from songs;


insert into performs values('jaadu',123);
insert into performs values('sri sai',124);
insert into performs values('magic',125);
insert into performs values('om shiv',126);
insert into performs values('ESCN',127);
insert into performs values('nirab',124);
insert into performs values('india',125);
insert into performs values('bean',128);
select * from performs;

commit;

##JOIN QUERIES

1.
select m.ssn,m.name,m.addr,i.iname
from musician m,plays p,instrument i
where m.ssn=p.ssn and p.id=i.id;


2.

select m.ssn,m.name,p.title 
from musician m,performs p,songs s
where m.ssn=p.ssn and  p.title=s.title;

3.
select m.ssn,m.name,a.aid
from musician m,album a
where m.ssn=a.ssn;

4.
select s.title,a.aid
from songs s,album a
where s.aid=a.aid;

5.

select m.ssn,m.name,p.title,a.aid
from musician m,performs p,songs s,album a
where m.ssn=p.ssn and  p.title=s.title and s.aid=a.aid;


###AGGREGATE FUNCTIONS QUERIES

6.
sql query for selecting number of mucisian who play more than one instrument 

select i.iname,count(m.ssn)
from musician m, plays p,instrument i
where m.ssn=p.ssn and p.id=i.id
group by iname
having count(m.ssn)>1;

7.
sql query for displaying name of musician who play only one instrument

select m.name,i.iname
from musician m, plays p,instrument i
where m.ssn=p.ssn and p.id=i.id
group by m.name,i.iname;

8.
sql query for displaying name of musician who perfrom more than one song 

select m.name,count(m.ssn)
from musician m,performs p,songs s
where m.ssn=p.ssn and  p.title=s.title
group by m.name
having count(m.ssn)>1;

9.
sql query for displaying name of musicain and number of albums he/she produces

select m.name,count(m.ssn)
from musician m,album a
where m.ssn=a.ssn
group by m.name;
having count(m.ssn)>1;

10.
sql query for counting no of songs in every album 

select a.atitle,count(a.aid)
from songs s,album a
where s.aid=a.aid
group by a.atitle;

###SIMPLE NESTED QUERIES 

11.
sql query for displaying data of musicians who have produces album KYC 

select *
from musician m,album a
where m.ssn=a.ssn and a.aid=( select a.aid from album a 
                                     where a.atitle='kyc');
                                     
                                     
12.display detail of musician who play Synthesiezer

select *
from musician m,plays p
where m.ssn=p.ssn and m.ssn=(select p.ssn
                            from instrument i ,plays p
                          where p.id=i.id and i.iname='synthesiezer');
                          
                          
                          
                          

13.  display detail of musician who have produces album in 2011

select * from musician
where ssn in (select ssn from album where rdate like '%-11');

14. display instrument information which is played by musicain rahim

select * from instrument 
where id in (select id from plays where ssn in(select ssn from musician where name='rahim')); 


15.display songs information which is performed by musician who ssn is 124

select * from songs
where title in (select title from performs where ssn=124);

##corelated queries

16.display musician information who plays more than one instrument

select *
from musician where ssn in (select ssn from plays 
                               group by ssn 
                               having count(ssn)>1);


17.display album details having more than 1 songs

select *
from album where aid in(select aid from songs 
                             group by aid
                             having count(aid)>1);
                             
                             
18.display misicain name who have produces album in the same year

select name 
from musician where ssn in (select s.ssn from album s
                               where s.rdate in(select r.rdate from album r
                                              where r.ssn=s.ssn));


19. display musician who play instrument in which mkey is HIGH

select * from musician 
where ssn in(select ssn from plays where id in (select id from instrument where mkey='high'));


20.display musician information who plays exactly one instrument

select *
from musician where ssn in (select ssn from plays 
                               group by ssn 
                               having count(ssn)=1); 



##VIEWS QUERIES

//21
create view musician_view as
select name 
from musician;
                          
select * from musician_view; 


//22
create view instrument_view as
select iname,mkey
from instrument;

select * from instrument;


//23
update instrument_view
set mkey='high';

select * from instrument;



//24
delete from instrument_view
where mkey='low';
select * from instrument_view;


//25
drop view instrument_view;

select *  from album;