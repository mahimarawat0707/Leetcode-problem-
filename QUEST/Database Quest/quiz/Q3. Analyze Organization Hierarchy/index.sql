WITH RECURSIVE EmployeeHierarchy AS (
    -- Base Case: The CEO (Level 1)
    SELECT
        employee_id,
        employee_name,
        manager_id,
        salary,
        1 AS level
    FROM Employees
    WHERE manager_id IS NULL

    UNION ALL

    -- Recursive Case: Find direct reports of the previous level (level + 1)
    SELECT
        e.employee_id,
        e.employee_name,
        e.manager_id,
        e.salary,
        eh.level + 1 AS level
    FROM Employees e
    INNER JOIN EmployeeHierarchy eh
        ON e.manager_id = eh.employee_id
),
Subordinates AS (
    -- Base Case: Each employee is a 'subordinate' of themselves (to include own salary/count)
    SELECT
        employee_id AS manager_id,
        employee_id AS subordinate_id,
        salary AS subordinate_salary
    FROM Employees

    UNION ALL

    -- Recursive Case: Map the subordinates of the current level to the original manager
    SELECT
        s.manager_id,
        e.employee_id AS subordinate_id,
        e.salary AS subordinate_salary
    FROM Subordinates s
    INNER JOIN Employees e
        ON e.manager_id = s.subordinate_id
    -- Stop when a cycle is detected, though typically not needed for standard org charts
    -- WHERE s.manager_id != e.employee_id 
)

-- Final Aggregation and Calculation
SELECT
    eh.employee_id,
    eh.employee_name,
    eh.level,
    -- Team Size: COUNT(DISTINCT subordinates) - 1 (to exclude the manager themselves)
    -- COALESCE handles cases where an employee is not a manager (COUNT will be 1, resulting in 0)
    COALESCE(COUNT(DISTINCT s.subordinate_id) - 1, 0) AS team_size,
    -- Budget: Manager's salary (always included) + SUM of all subordinates' salaries (direct/indirect)
    SUM(s.subordinate_salary) AS budget
FROM EmployeeHierarchy eh
LEFT JOIN Subordinates s
    ON eh.employee_id = s.manager_id
GROUP BY
    eh.employee_id, eh.employee_name, eh.level, eh.salary
ORDER BY
    eh.level ASC,
    budget DESC,
    eh.employee_name ASC;