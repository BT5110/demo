CREATE TABLE co2emission_reduced (
    imo BIGINT PRIMARY KEY,
    ship_name VARCHAR(64) NOT NULL,
    technical_efficiency_number REAL
);
