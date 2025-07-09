CREATE DATABASE pipeline_db;

CREATE TABLE IF NOT EXISTS artists (
    id BIGSERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    second_name VARCHAR(255),
    surname VARCHAR(255),
    artist_id BIGINT,
    link VARCHAR(255),
    extraction_date TIMESTAMP NOT NULL
);