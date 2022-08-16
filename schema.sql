DROP TABLE IF EXISTS vehicles;

CREATE TABLE vehicles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    manufacturer TEXT(100),
    model TEXT(100)
);