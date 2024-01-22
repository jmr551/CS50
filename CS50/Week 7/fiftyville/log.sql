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

-- My list of possible thiefs is

SELECT activity, license_plate, hour, minute, month, year
FROM bakery_security_logs
WHERE month = 7 AND day = 28
AND license_plate NOT IN (
    SELECT license_plate
    FROM bakery_security_logs
    WHERE (activity = 'entrance' AND hour > 10 )
)
AND license_plate NOT IN (
    SELECT license_plate
    FROM bakery_security_logs
    WHERE (activity = 'exit' AND hour < 10)
));

-- I want to see what is in the Interviews table
SELECT *
FROM interviews
WHERE day = 28 AND month = 7;
-- 1. Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away.
--    If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.                                                   |
-- 2. I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery,
--    I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.                                                                                               |
-- 3. As the thief was leaving the bakery, they called someone who talked to them for less than a minute.
--    In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow.
-- 4. The thief then asked the person on the other end of the phone to purchase the flight ticket.

-- According to 1.
SELECT license_plate
FROM (SELECT activity, license_plate, hour, minute, month, year
FROM bakery_security_logs
WHERE month = 7 AND day = 28
AND license_plate NOT IN (
    SELECT license_plate
    FROM bakery_security_logs
    WHERE (activity = 'entrance' AND hour > 10 )
)
AND license_plate NOT IN (
    SELECT license_plate
    FROM bakery_security_logs
    WHERE (activity = 'exit' AND hour < 10)
))
WHERE activity = 'exit' AND hour = 10 AND minute < 25;

-- So, the people with these license plates are
SELECT *
FROM people
WHERE license_plate IN (
    SELECT license_plate
    FROM (
        SELECT activity, license_plate, hour, minute, month, year
        FROM bakery_security_logs
        WHERE month = 7 AND day = 28
        AND license_plate NOT IN (
            SELECT license_plate
            FROM bakery_security_logs
            WHERE (activity = 'entrance' AND hour > 10 )
        )
        AND license_plate NOT IN (
            SELECT license_plate
            FROM bakery_security_logs
            WHERE (activity = 'exit' AND hour < 10)
        )
    )
    WHERE activity = 'exit' AND hour = 10
    );
-- So, I have 9 people.

-- Acording to 2.
.schema atm_transactions

SELECT *
FROM atm_transactions
WHERE month = 7 AND day = 28
AND atm_location = 'Leggett Street';
-- I need to see how to connect with the account_number

.schema bank_account

-- I need the ID from the people at the ATM
SELECT person_id
FROM bank_accounts
WHERE account_number IN (
    SELECT account_number
    FROM atm_transactions
    WHERE month = 7 AND day = 28
    AND atm_location = 'Leggett Street'
);

-- So, according to 1 and 2
SELECT *
FROM people
WHERE license_plate IN (
    SELECT license_plate
    FROM (
        SELECT activity, license_plate, hour, minute, month, year
        FROM bakery_security_logs
        WHERE month = 7 AND day = 28
        AND license_plate NOT IN (
            SELECT license_plate
            FROM bakery_security_logs
            WHERE (activity = 'entrance' AND hour > 10 )
        )
        AND license_plate NOT IN (
            SELECT license_plate
            FROM bakery_security_logs
            WHERE (activity = 'exit' AND hour < 10)
        )
    )
    WHERE activity = 'exit' AND hour = 10
    )
AND id in (
    SELECT person_id
    FROM bank_accounts
    WHERE account_number IN (
        SELECT account_number
        FROM atm_transactions
        WHERE month = 7 AND day = 28
        AND atm_location = 'Leggett Street'
    )
);
-- So I have 5 people

-- According to 3.
.schema phone_calls
SELECT *
FROM phone_calls
WHERE month = 7 AND day = 28 AND duration <=60;


-- So, the phone number from the people involved in a phone call are
SELECT phone_number
FROM people
WHERE phone_number IN (
    SELECT caller
    FROM phone_calls
    WHERE month = 7 AND day = 28 AND duration <=60
)
OR phone_number IN (
    SELECT receiver
    FROM phone_calls
    WHERE month = 7 AND day = 28 AND duration <=60
);

-- According to 1, 2 and 3
SELECT *
FROM people
WHERE license_plate IN (
    SELECT license_plate
    FROM (
        SELECT activity, license_plate, hour, minute, month, year
        FROM bakery_security_logs
        WHERE month = 7 AND day = 28
        AND license_plate NOT IN (
            SELECT license_plate
            FROM bakery_security_logs
            WHERE (activity = 'entrance' AND hour > 10 )
        )
        AND license_plate NOT IN (
            SELECT license_plate
            FROM bakery_security_logs
            WHERE (activity = 'exit' AND hour < 10)
        )
    )
    WHERE activity = 'exit' AND hour = 10
    )
AND id in (
    SELECT person_id
    FROM bank_accounts
    WHERE account_number IN (
        SELECT account_number
        FROM atm_transactions
        WHERE month = 7 AND day = 28
        AND atm_location = 'Leggett Street'
    )
)
AND phone_number IN (
    SELECT phone_number
    FROM people
    WHERE phone_number IN (
        SELECT caller
        FROM phone_calls
        WHERE month = 7 AND day = 28 AND duration <=60
    )
    OR phone_number IN (
        SELECT receiver
        FROM phone_calls
        WHERE month = 7 AND day = 28 AND duration <=60
    )
)
;
-- So, I have four people.

-- According to 4.
.schema flights

-- So, I need the ids from these flights
SELECT id
FROM flights
WHERE day = 29 AND month = 7;

-- So I need the passport number from the people who flu next day.
.schema passengers
SELECT passport_number
FROM passengers
WHERE flight_id IN (
    SELECT id
    FROM flights
    WHERE day = 29 AND month = 7 and hour < 9
);

-- According to 1, 2, 3 and 4
SELECT *
FROM people
WHERE license_plate IN (
    SELECT license_plate
    FROM (
        SELECT activity, license_plate, hour, minute, month, year
        FROM bakery_security_logs
        WHERE month = 7 AND day = 28
        AND license_plate NOT IN (
            SELECT license_plate
            FROM bakery_security_logs
            WHERE (activity = 'entrance' AND hour > 10 )
        )
        AND license_plate NOT IN (
            SELECT license_plate
            FROM bakery_security_logs
            WHERE (activity = 'exit' AND hour < 10)
        )
    )
    WHERE activity = 'exit' AND hour = 10 AND minute < 25
    )
AND id in (
    SELECT person_id
    FROM bank_accounts
    WHERE account_number IN (
        SELECT account_number
        FROM atm_transactions
        WHERE month = 7 AND day = 28
        AND atm_location = 'Leggett Street'
    )
)
AND phone_number IN (
    SELECT phone_number
    FROM people
    WHERE phone_number IN (
        SELECT caller
        FROM phone_calls
        WHERE month = 7 AND day = 28 AND duration <60
    )
    OR phone_number IN (
        SELECT receiver
        FROM phone_calls
        WHERE month = 7 AND day = 28 AND duration <60
    )
)
AND passport_number IN (
    SELECT passport_number
    FROM passengers
    WHERE flight_id IN (
        SELECT id
        FROM flights
        WHERE day = 29 AND month = 7 and hour < 9
    )
)
;
