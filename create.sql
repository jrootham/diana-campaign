
CREATE TABLE race
(
	name UNIQUE
);

INSERT INTO race (name) VALUES ('Mayor');
INSERT INTO race (name) VALUES ('Councillor');
INSERT INTO race (name) VALUES ('Trustee');

CREATE TABLE candidate
(
	name UNIQUE
);

CREATE TABLE poll
(
	name UNIQUE
);

CREATE TABLE result
(
	race,
	candidate,
	poll,
	votes,
	PRIMARY KEY(race, candidate, poll)
);
