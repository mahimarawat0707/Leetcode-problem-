WITH first_login AS (
    SELECT 
        player_id, 
        MIN(event_date) AS first_date
    FROM Activity
    GROUP BY player_id
),
next_day_login AS (
    SELECT 
        f.player_id
    FROM first_login f
    JOIN Activity a
      ON f.player_id = a.player_id
     AND a.event_date = DATE_ADD(f.first_date, INTERVAL 1 DAY)
)
SELECT 
    ROUND(COUNT(DISTINCT player_id) * 1.0 / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
FROM next_day_login;
