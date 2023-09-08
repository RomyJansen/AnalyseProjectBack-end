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
id int,
naam varchar(50),
objectType int,
locatieX int,
locatieY int,
grootteX int,
grootteY int,
jaar int,
primary key(id, jaar),
foreign key (objectType) references objectTypes(id)
);

CREATE TABLE standaardVariabelen(
id int,
naam varchar(30),
objectLink int null,
waarde int,
jaar int,
primary key (id, jaar),
foreign key (objectLink) references objecten(id)
);

CREATE TABLE afstandVariabelen(
id int,
naam varchar(30),
objectLink int,
doelObjectType int,
jaar int,
primary key (id, jaar),
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
id int primary key auto_increment,
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

CREATE TABLE objectGebeurtenissen(
id int,
naam varchar(30),
jaar int,
locatieX int,
locatieY int,
primary key(id, jaar));

CREATE TABLE scenario(
naam varchar(30) primary key,
startjaar int, 
eindjaar int);

ALTER TABLE berekendeVariabelen
ADD foreign key (var1Id)  references gebeurtenissen(id),
ADD foreign key (var2Id) references gebeurtenissen(id);

DELIMITER //
CREATE TRIGGER add_afstandVar_to_allevariabelen
after insert ON afstandvariabelen
FOR EACH ROW
BEGIN
	IF(new.id NOT IN (select afstandVarId from alleVariabelen))
    THEN
		INSERT INTO alleVariabelen(typeId, afstandVarId, objectLink)
		values(2, new.id, new.objectLink);
	END IF;
END;
//
DELIMITER ;

DELIMITER //
CREATE TRIGGER add_berekendeVar_to_allevariabelen
after insert ON afstandvariabelen
FOR EACH ROW
BEGIN
	IF(new.id NOT IN (select berVarId from alleVariabelen))
    THEN
		INSERT INTO alleVariabelen(typeId, berVarId, objectLink)
		values(3, new.id, new.objectLink);
	END IF;
END;
//
DELIMITER ;

DELIMITER //
CREATE TRIGGER add_standaardVar_to_allevariabelen
after insert ON afstandvariabelen
FOR EACH ROW
BEGIN
	IF(new.id NOT IN (select standaardVarId from alleVariabelen))
    THEN
		INSERT INTO alleVariabelen(typeId, standaardVarId, objectLink)
		values(1, new.id, new.objectLink);
	END IF;
END;
//
DELIMITER ;

DELIMITER //
CREATE TRIGGER add_new_value_from_gebeurtenis_to_var_table
after insert ON gebeurtenissen
FOR EACH ROW
BEGIN
	IF EXISTS (SELECT 1 FROM alleVariabelen WHERE new.id = id AND typeId = 2)
    THEN
		INSERT INTO afstandVariabelen 
        values(
        (select afstandVarId from alleVariabelen WHERE id = new.id), 
        (select naam from afstandvariabelen af join allevariabelen av where av.afstandVarId = af.id and av.id = new.id),
        (select objectLink from alleVariabelen WHERE id =  new.id),
        new.waarde, 
        new.jaar);
	ELSE IF EXISTS (SELECT 1 FROM allevariabelen WHERE new.id AND typeId = 1)
	THEN
		INSERT INTO standaardvariabelen
		values(
		(select standaardVarId from alleVariabelen WHERE id = new.id),
		(select naam from standaardvariabelen sv join allevariabelen av where av.standaardVarId = sv.id and av.id = new.id),
		(select objectLink from alleVariabelen WHERE id =  new.id),
		new.waarde, 
		new.jaar
		);
	END IF; /* end first else if */
	END IF; /* end first if */
END;
//
DELIMITER ;

DELIMITER //
CREATE TRIGGER add_new_value_from_objectgebeurtenis_to_object_table
after insert ON objectgebeurtenissen
FOR EACH ROW
BEGIN
	INSERT INTO objecten
    values(new.id, 
    (select o.naam from objecten o join objecten obj where o.id = obj.id and obj.id = new.id LIMIT 1),
    (select o.objectType from objecten o join objecten obj where o.id = obj.id and obj.id = new.id LIMIT 1),
    new.locatieX,
    new.locatieY,
    (select o.grootteX from objecten o join objecten obj where o.id = obj.id and obj.id = new.id LIMIT 1),
    (select o.grootteY from objecten o join objecten obj where o.id = obj.id and obj.id = new.id LIMIT 1),
    new.jaar);
END;
//
DELIMITER ;