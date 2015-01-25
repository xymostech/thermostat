CREATE TABLE temp_data (
    id INTEGER PRIMARY KEY ASC,
    time INTEGER,
    temperature REAL
);

CREATE TABLE schedule (
    weekday INTEGER,
    hour INTEGER,
    minute INTEGER,
    desired_temp REAL
);

INSERT INTO schedule VALUES
    (0, 7, 0, 22),
    (0, 11, 0, 17),
    (0, 18, 0, 22),
    (0, 23, 0, 17),

    (1, 7, 0, 22),
    (1, 11, 0, 17),
    (1, 18, 0, 22),
    (1, 23, 0, 17),

    (2, 7, 0, 22),
    (2, 11, 0, 17),
    (2, 18, 0, 22),
    (2, 23, 0, 17),

    (3, 7, 0, 22),
    (3, 11, 0, 17),
    (3, 18, 0, 22),
    (3, 23, 0, 17),

    (4, 7, 0, 22),
    (4, 11, 0, 17),
    (4, 18, 0, 22),
    (4, 23, 0, 17),

    (5, 7, 0, 22),
    (5, 23, 0, 17),

    (6, 7, 0, 22),
    (6, 23, 0, 17);

.quit
