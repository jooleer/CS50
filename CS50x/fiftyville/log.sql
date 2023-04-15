-- Keep a log of any SQL queries you execute as you solve the mystery.
.schema -- check db layout
SELECT * FROM crime_scene_reports WHERE year = 2021 AND month = 7 AND day = 28 AND street = 'Humphrey Street';
-- look for reports at exact date and location of theft
-- Results:
-- Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery.
-- Interviews were conducted today with three witnesses who were present at the time
-- each of their interview transcripts mentions the bakery

SELECT * FROM interviews WHERE year = 2021 AND month = 7 AND day = 28;
-- check interviews of witnesses to see if we can get more information from them
-- | 161 | Ruth    | 2021 | 7     | 28  | Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away. If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.
-- | 162 | Eugene  | 2021 | 7     | 28  | I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.
-- | 163 | Raymond | 2021 | 7     | 28  | As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked the person on the other end of the phone to purchase the flight ticket.

-- From the data provided from the interviews we can make a query combining all of them together
SELECT name FROM people
WHERE people.license_plate IN
(
    SELECT license_plate FROM bakery_security_logs
    WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute BETWEEN 15 AND 25
)
AND people.id IN
(
    SELECT person_id FROM bank_accounts
    JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number
    AND atm_transactions.year = 2021 AND atm_transactions.month = 7 AND atm_transactions.day = 28
    AND atm_transactions.transaction_type = 'withdraw' AND atm_transactions.atm_location = 'Leggett Street'
)
AND people.phone_number IN
(
    SELECT caller FROM phone_calls
    WHERE phone_calls.caller = people.phone_number
    AND year = 2021 AND month = 7 AND day = 28
    AND phone_calls.duration < 60
)
AND people.passport_number IN
(
    SELECT passport_number FROM passengers
    JOIN flights ON flights.id = passengers.flight_id
    JOIN airports ON airports.id = flights.origin_airport_id
    AND flights.year = 2021 AND flights.month = 7 AND flights.day = 29
    AND airports.city = 'Fiftyville'
);


-- We get 2 results, Diana and Bruce. We will check their flight times and see who left the earliest.
SELECT flights.hour, flights.minute FROM flights
JOIN passengers ON passengers.flight_id = flights.id
JOIN people ON passengers.passport_number = people.passport_number
AND flights.year = 2021 AND flights.month = 7 AND flights.day = 29
AND people.name = 'Bruce';


-- Bruce leaves at 8h20 in the morning

SELECT flights.hour, flights.minute FROM flights
JOIN passengers ON passengers.flight_id = flights.id
JOIN people ON passengers.passport_number = people.passport_number
AND flights.year = 2021 AND flights.month = 7 AND flights.day = 29
AND people.name = 'Diana';

-- Diana leaves at 16h00 in the afternoon

-- We now consider Bruce our main suspect for this case

/* below sort of broken attempt to print result for both bruce and diana at same time in same table
SELECT DISTINCT flights.id, flights.hour, flights.minute, people.name
FROM (SELECT DISTINCT flights.id, flights.hour, flights.minute FROM flights WHERE flights.year = 2021 AND flights.month = 7 AND flights.day = 29) AS flights
JOIN (SELECT DISTINCT people.name FROM people WHERE people.name = 'Bruce' OR people.name='Diana') AS people
JOIN passengers ON passengers.flight_id = flights.id
AND passengers.passport_number IN
(
    SELECT DISTINCT passport_number FROM people
    WHERE name = 'Bruce' OR name = 'Diana'
);
*/


-- Now we find out what city Bruce fled to
SELECT city FROM airports
JOIN flights ON flights.destination_airport_id = airports.id
JOIN passengers ON flights.id = passengers.flight_id
JOIN people ON people.passport_number = passengers.passport_number
AND flights.year = 2021 AND flights.month = 7 AND flights.day = 29 AND flights.hour = 8 AND flights.minute = 20
AND people.passport_number IN
(
    SELECT passport_number FROM people
    WHERE name = 'Bruce'
);

-- He fled to New York City

-- Now we just need to find out who his accomplice was.
SELECT name FROM people
JOIN phone_calls ON people.phone_number = phone_calls.receiver
AND phone_calls.caller IN
(
    SELECT phone_number FROM people
    WHERE name = 'Bruce'
)
AND phone_calls.duration < 60
AND phone_calls.year = 2021 AND phone_calls.month = 7 AND phone_calls.day = 28;

--Robin