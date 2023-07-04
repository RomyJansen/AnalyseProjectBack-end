DROP DATABASE IF EXISTS Arnhem;

CREATE DATABASE Arnhem;

USE Arnhem;

CREATE TABLE VarTypes(
naam varchar(50) primary key
);

CREATE TABLE alleVariabelen(
id int primary key,
waarde int,
varType varchar(30),
foreign key (varType) references VarTypes(naam)
);

CREATE TABLE Startvariabelen(
id int primary key,
naam varchar(30),
waarde int,
foreign key (id) references AlleVariabelen(id)
);

CREATE TABLE Objecttypes(
id int primary key,
naam varchar(30)
);

CREATE TABLE Object(
id int primary key,
naam varchar(50),
objecttype int,
foreign key (objecttype) references Objecttypes(id) 
);

CREATE TABLE Objectvariabelen(
varId int primary key,
objectId int,
naam varchar(50),
waarde int,
foreign key (objectId) references Object(id),
foreign key (varId) references AlleVariabelen(id)
);

CREATE TABLE StandaardvariabelenVoorType(
varId int primary key,
typeId int,
naam varchar(50),
waarde int,
foreign key (typeId) references Objecttypes(id)
);

CREATE TABLE BerekendeVariabelen(
id int primary key,
naam varchar(50),
var1Id int,
var2Id int,
operator varchar(1),
waarde int,
objectBerekening bool,
foreign key (var1Id) references AlleVariabelen(id),
foreign key (var2Id) references AlleVariabelen(id)
);

CREATE TABLE Gebeurtenissen(
id int,
naam varchar(50),
varId int,
jaar int, 
waarde int,
primary key(id, varId),
foreign key (varId) references AlleVariabelen(id)
);

CREATE TABLE Regels(
id int primary key,
naam varchar(50),
waarde int,
vergelijkingOperator varchar(2),
varId int,
foreign key (varId) references alleVariabelen(id)
);

INSERT INTO VarTypes (naam) VALUES
('FantasyType'),
('SuperType'),
('MegaType');

INSERT INTO alleVariabelen (id, waarde, varType) VALUES
(1, 10, 'FantasyType'),
(2, 20, 'SuperType'),
(3, 30, 'MegaType'),
(4, 40, 'FantasyType'),
(5, 50, 'SuperType');

INSERT INTO Startvariabelen (id, naam, waarde) VALUES
(1, 'StartVarKnight', 100),
(2, 'StartVarHero', 200),
(3, 'StartVarLegend', 300);

INSERT INTO Objecttypes (id, naam) VALUES
(1, 'DragonType'),
(2, 'MagicType'),
(3, 'TreasureType');

INSERT INTO Object (id, naam, objecttype) VALUES
(1, 'Dragon1', 1),
(2, 'MagicObject2', 2),
(3, 'TreasureChest', 3);

INSERT INTO Objectvariabelen (varId, objectId, naam, waarde) VALUES
(1, 1, 'DragonVar1', 50),
(2, 2, 'MagicVar2', 60),
(3, 3, 'TreasureVar3', 70),
(4, 1, 'DragonVar4', 80),
(5, 2, 'MagicVar5', 90);

INSERT INTO StandaardvariabelenVoorType (varId, typeId, naam, waarde) VALUES
(1, 1, 'StandardVarDragon', 100),
(2, 2, 'StandardVarMagic', 200),
(3, 3, 'StandardVarTreasure', 300),
(4, 1, 'StandardVarDragon2', 400),
(5, 2, 'StandardVarMagic2', 500);

INSERT INTO BerekendeVariabelen (id, naam, var1Id, var2Id, operator, waarde, objectBerekening) VALUES
(1, 'CalcVar1', 1, 2, '+', 110, true),
(2, 'CalcVar2', 3, 4, '-', 150, false),
(3, 'CalcVar3', 5, 1, '*', 200, false),
(4, 'CalcVar4', 2, 3, '/', 240, false),
(5, 'CalcVar5', 4, 5, '+', 350, true);

INSERT INTO Gebeurtenissen (id, naam, varId, jaar, waarde) VALUES
(1, 'Event1', 1, 2022, 120),
(2, 'Event2', 3, 2022, 140),
(3, 'Event3', 5, 2023, 160),
(4, 'Event4', 2, 2023, 180),
(5, 'Event5', 4, 2024, 200);

INSERT INTO Regels (id, naam, waarde, vergelijkingOperator, varId) VALUES
(1, 'Rule1', 100, '>', 1),
(2, 'Rule2', 200, '<', 3),
(3, 'Rule3', 300, '>=', 5),
(4, 'Rule4', 400, '<=', 2),
(5, 'Rule5', 500, '=', 4);


SELECT * FROM AlleVariabelen;
SELECT * FROM BerekendeVariabelen;
SELECT * FROM Gebeurtenissen;
SELECT * FROM Object;
SELECT * FROM ObjectTypes;
SELECT * FROM ObjectVariabelen;
SELECT * FROM Regels;
SELECT * FROM StandaardvariabelenVoorType;
SELECT * FROM StartVariabelen;
SELECT * FROM VarTypes;