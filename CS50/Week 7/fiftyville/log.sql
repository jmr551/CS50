-- Keep a log of any SQL queries you execute as you solve the mystery.
.tables -- Because I would like to know what tables are in the database
.schema crime_scene_reports

-- I want to know the crime scene reports from that day
SELECT description
FROM crime_scene_reports
WHERE month = 7 AND day = 28
AND street = 'Humphrey Street';


