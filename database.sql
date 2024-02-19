DROP TABLE IF EXISTS urls;

CREATE TABLE urls (
    id SERIAL PRIMARY KEY,
    url varchar(255),
    domain varchar(255),
    end_link varchar(255),
    abbreviated_url varchar(255) UNIQUE NOT NULL,
    created_at DATE DEFAULT CURRENT_TIMESTAMP
);
