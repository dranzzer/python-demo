
-- see initial outlay of databases
show databases

-- checking if database from previous testing
drop database if exists python_demo


-- creating new db
create database python_demo


-- creating tabel headers

use python_demo;
create table covid(
tag varchar(10),
continent varchar(50),
location varchar(50),
date date,
population int,
total_cases int,
new_cases int,
new_cases_smoothed float,
total_deaths int,
new_deaths int,
new_deaths_smoothed float)

select * from covid

