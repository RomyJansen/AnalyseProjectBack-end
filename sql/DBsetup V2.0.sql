DROP DATABASE IF EXISTS Arnhem;

CREATE DATABASE Arnhem;

USE Arnhem;

CREATE TABLE varTypes(
id int primary key,
naam varchar(30)
);

CREATE TABLE objectTypes(
id int primary key,
naam varchar(30)
);

CREATE TABLE objecten(
id int primary key,
naam varchar(50),
objectType int,
locatieX int,
locatieY int,
grootteX int,
grootteY int,
foreign key (objectType) references objectTypes(id)
);

CREATE TABLE standaardVariabelen(
id int primary key,
naam varchar(30),
objectLink int null,
beginwaarde int,
foreign key (objectLink) references objecten(id)
);

CREATE TABLE afstandVariabelen(
id int primary key,
naam varchar(30),
objectLink int,
doelObjectType int,
foreign key (objectLink) references objecten(id),
foreign key (doelObjectType) references objectTypes(id)
);

CREATE TABLE berekendeVariabelen(
id int primary key,
naam varchar(30),
var1Id int,
var2Id int,
operator varchar(2),
objectLink int null,
foreign key (objectLink) references objecten(id)
);

CREATE TABLE alleVariabelen(
id int primary key,
typeId int,
berVarId int null,
afstandVarId int null,
standaardVarId int null,
objectLink int null,
foreign key (typeId) references varTypes(id),
foreign key (berVarId) references berekendeVariabelen(id),
foreign key (afstandVarId) references afstandVariabelen(id),
foreign key (standaardVarId) references standaardVariabelen(id),
foreign key (objectLink)  references objecten(id)
);

CREATE TABLE gebeurtenissen(
id int,
naam varchar(30),
jaar int,
waarde int,
primary key (id, jaar),
foreign key (id) references allevariabelen(id)
);

CREATE TABLE regels(
id int primary key,
naam varchar(50),
waarde int,
vergelijkingOperator varchar(2),
varId int,
foreign key (varId) references alleVariabelen(id)
);

ALTER TABLE berekendeVariabelen
ADD foreign key (var1Id)  references gebeurtenissen(id),
ADD foreign key (var2Id) references gebeurtenissen(id);