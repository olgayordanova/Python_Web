CREATE table hotel (
	hotel_id INTEGER NOT NULL PRIMARY KEY,
	hotel_name CHARACTER VARYING(25),
	hotel_stars INTEGER CHECK (hotel_stars BETWEEN 1 AND 5)
);

CREATE table pet_owner (
	owner_id INTEGER NOT NULL PRIMARY KEY,
	owner_name CHARACTER VARYING(15),
	owner_age INTEGER CHECK (owner_age BETWEEN 1 AND 110)
);

CREATE table cat (
	cat_id INTEGER NOT NULL PRIMARY KEY,
	owner_id INTEGER NOT NULL,
	cat_name CHARACTER VARYING(15),
	cat_age INTEGER CHECK (cat_age BETWEEN 1 AND 25),
	FOREIGN KEY (owner_id) REFERENCES pet_owner(owner_id) ON DELETE CASCADE
);

CREATE table dog (
	dog_id INTEGER NOT NULL PRIMARY KEY,
	owner_id INTEGER NOT NULL,
	dog_name CHARACTER VARYING(15),
	dog_age INTEGER CHECK (dog_age BETWEEN 1 AND 25),
	FOREIGN KEY (owner_id) REFERENCES pet_owner(owner_id) ON DELETE CASCADE
);

CREATE table cat_room (
	room_id INTEGER NOT NULL PRIMARY KEY,
	cat_id INTEGER NOT NULL,
	hotel_id INTEGER NOT NULL,
	registered_date DATE,
	unregistered_date DATE,
	FOREIGN KEY (cat_id) REFERENCES cat(cat_id) ON DELETE CASCADE,
	FOREIGN KEY (hotel_id) REFERENCES hotel(hotel_id) ON DELETE CASCADE
);

CREATE table dog_room (
	room_id INTEGER NOT NULL PRIMARY KEY,
	dog_id INTEGER NOT NULL,
	hotel_id INTEGER NOT NULL,
	registered_date DATE,
	unregistered_date DATE,
	FOREIGN KEY (dog_id) REFERENCES dog(dog_id) ON DELETE CASCADE,
	FOREIGN KEY (hotel_id) REFERENCES hotel(hotel_id) ON DELETE CASCADE
);

INSERT INTO pet_owner VALUES 
	(1, 'Peter', 26),
	(2, 'George', 32),
	(3, 'Amy', 67)
;

INSERT INTO dog VALUES 
	(1, 1, 'Fluffy', 2),
	(2, 3, 'Bully', 3),
	(3, 1, 'Rousey', 5)
;

INSERT INTO cat VALUES 
	(1, 2, 'Tommy', 1),
	(2, 3, 'Jessy', 7),
	(3, 2, 'Bubbles', 3)
;

INSERT INTO hotel VALUES 
	(1, 'Grand Pet Hotel', 5),
	(2, 'Pets Heaven', 2)
;

INSERT INTO dog_room VALUES 
	(1, 1, 1, '2020-06-08', '2020-06-10'),
	(2, 2, 2, '2020-06-10', '2020-06-15'),
	(3, 3, 2, '2020-06-20', '2020-06-23')
;

INSERT INTO cat_room VALUES 
	(1, 1, 1, '2020-06-08', '2020-06-10'),
	(2, 2, 2, '2020-06-10', '2020-06-15'),
	(3, 3, 2, '2020-06-20', '2020-06-23')
;

select * from dog_room;

select cat_id from cat_room where hotel_id=2;

select * from pet_owner ORDER BY owner_age desc;

select count(cat_id) from cat where cat_age>=3;

delete from cat where cat_age<=2;

delete from dog where dog_age<=2;

select * from cat_room;