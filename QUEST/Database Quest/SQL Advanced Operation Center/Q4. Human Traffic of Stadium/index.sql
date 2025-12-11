WITH HighAttendance AS (
    -- Step 1: Filter only the rows where people >= 100
    SELECT
        *,
        -- Step 2: Create a synthetic group ID (groupId)
        -- We subtract the row number (ordered by id) from the id itself.
        -- If the id's are consecutive (e.g., 5, 6, 7), the row_num will also be consecutive (1, 2, 3).
        -- The difference (5-1=4, 6-2=4, 7-3=4) will be constant, forming a unique group ID.
        id - ROW_NUMBER() OVER (ORDER BY id) AS group_id
    FROM
        Stadium
    WHERE
        people >= 100
),
ConsecutiveGroups AS (
    -- Step 3: Identify the groups that have at least 3 consecutive rows
    SELECT
        group_id
    FROM
        HighAttendance
    GROUP BY
        group_id
    HAVING
        COUNT(id) >= 3
)
-- Step 4: Retrieve all original records that belong to the identified groups
SELECT
    t1.id,
    t1.visit_date,
    t1.people
FROM
    HighAttendance t1
INNER JOIN
    ConsecutiveGroups t2
ON
    t1.group_id = t2.group_id
ORDER BY
    t1.visit_date ASC;