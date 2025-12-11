SELECT
    -- Rename the request date to 'Day' as required by the output
    t.request_at AS Day,
    
    -- Calculate the Cancellation Rate: (Canceled Trips) / (Total Trips)
    -- 1. Use SUM and CASE to count canceled trips (status is not 'completed').
    -- 2. Divide by COUNT(*), which gives the total number of filtered trips.
    -- 3. Use ROUND to format the output to two decimal places.
    ROUND(
        SUM(CASE WHEN t.status != 'completed' THEN 1 ELSE 0 END) * 1.0 
        / COUNT(*),
        2
    ) AS "Cancellation Rate"
FROM
    Trips t
INNER JOIN
    -- Join with Users table (as Clients) to filter out banned clients
    Users c ON t.client_id = c.users_id AND c.banned = 'No'
INNER JOIN
    -- Join with Users table (as Drivers) to filter out banned drivers
    Users d ON t.driver_id = d.users_id AND d.banned = 'No'
WHERE
    -- Filter for the specific date range
    t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY
    t.request_at
HAVING 
    -- Requirement: 'with at least one trip'
    COUNT(*) > 0
ORDER BY
    t.request_at;