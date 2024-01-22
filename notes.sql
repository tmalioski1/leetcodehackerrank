DROP TABLE puppiespup;
DROP TABLE owners;

CREATE TABLE puppiespup (
  id INTEGER PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  age_yrs NUMERIC(3,1),
  breed VARCHAR(100),
  weight_lbs INTEGER,
  microchipped BOOLEAN DEFAULT 0,
  owner_id INTEGER,
  FOREIGN KEY (owner_id) REFERENCES owners(id) ON DELETE CASCADE
);

INSERT INTO puppiespup (name, age_yrs, breed, weight_lbs, microchipped, owner_id) VALUES ('Apple', 11, 'Beagle', 15, 1, 2);
INSERT INTO puppiespup (name, age_yrs, breed, weight_lbs, microchipped, owner_id) VALUES ('Bubba', 13, 'Golden Retriever', 25, 0, 1);




CREATE TABLE owners (
  id INTEGER PRIMARY KEY,
  name VARCHAR(50) NOT NULL
);

INSERT INTO owners (name) VALUES ('Ron');
INSERT INTO owners (name) VALUES ('Randy');


