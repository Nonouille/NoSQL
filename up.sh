#!/bin/bash

cqlsh
use basket;

CREATE TABLE IF NOT EXISTS players (id TEXT,firstName TEXT,middleName TEXT,lastName TEXT,fullGivenName TEXT,nameNick TEXT,pos TEXT,height FLOAT,weight FLOAT,college TEXT,birthDate DATE,birthCity TEXT,birthCountry TEXT,highSchool TEXT,hsCity TEXT,hsState TEXT,hsCountry TEXT, PRIMARY KEY(id) );
ALTER TABLE players WITH GC_GRACE_SECONDS = 0;
#CREATE INDEX btree_players_pos on players(pos);
COPY players(id,firstName,middleName,lastName,fullGivenName,nameNick,pos,height,weight,college,birthDate,birthCity,birthCountry,highSchool,hsCity,hsState,hsCountry) FROM 'data/Players.csv' WITH HEADER = true;

CREATE TABLE IF NOT EXISTS teams ( id TEXT, year INT, tmID TEXT, games INT, minutes INT, points INT, steals INT, blocks INT, PRIMARY KEY (id,year));
ALTER TABLE teams WITH GC_GRACE_SECONDS = 0
#CREATE INDEX btree_teams_year on teams(year);
COPY teams(id, year, tmID, games, minutes, points, steals, blocks) FROM 'data/Teams.csv' WITH HEADER = true;

CREATE TABLE awards (id TEXT,award TEXT,year INT,pos TEXT,PRIMARY KEY(id,award,year));
ALTER TABLE awards WITH GC_GRACE_SECONDS = 0;
#CREATE INDEX btree_awards_desc on awards(award);
COPY awards(id,award,year,pos) FROM 'data/Awards.csv' WITH HEADER = true;