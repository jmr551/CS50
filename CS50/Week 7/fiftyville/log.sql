-- Keep a log of any SQL queries you execute as you solve the mystery.
.tables -- Because I would like to know what tables are in the database
.schema crime_scene_reports

-- I want to know the crime scene reports from that day
SELECT description
FROM crime_scene_reports
WHERE month = 7 AND day = 28
AND street = 'Humphrey Street';
-- Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery.
-- Interviews were conducted today with three witnesses who were present at the time –
-- each of their interview transcripts mentions the bakery.
-- Littering took place at 16:36. No known witness

-- "each of their interview transcripts mentions the bakery."
.schema bakery_security_logs

-- I need to see what info is there
SELECT activity, license_plate, hour, minute, month, year
FROM bakery_security_logs
WHERE month = 7 AND day = 28;

-- So I need to see who entered before 10:15 and has gone after that

(SELECT activity, license_plate, hour, minute, month, year
FROM bakery_security_logs
WHERE month = 7 AND day = 28)
