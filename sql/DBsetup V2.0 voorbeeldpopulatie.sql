USE Arnhem;

INSERT INTO vartypes
values(1, "standaard"),
(2, "afstand"),
(3, "berekend");

INSERT INTO objectTypes
values(1, "huis"),
(2, "park");

INSERT INTO objecten
values(1, "huis1", 1, 50, 50, 10, 10),
(2, "huis2", 1, 60, 50, 10, 10),
(3, "park1", 2, 250, 50, 20, 20),
(4, "park2", 2, 500, 200, 20, 20);

INSERT INTO afstandVariabelen
values (1, "afstand tot park", 1, 2),
(2, "afstand tot park", 2, 2),
(3, "park tot park", 3, 2);

INSERT INTO allevariabelen
values(1, 2, null, 1, null, 1),
(2, 2, null, 2, null, 2);

INSERT INTO regels
values (1, "park dichtbij", 190, "=>", 1),
(2, "park dichtbij", 190, "=>", 2);