SELECT 
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM 
    Employee e
JOIN 
    Department d
    ON e.departmentId = d.id
JOIN 
    (
        -- Subquery to get the max salary per department
        SELECT departmentId, MAX(salary) AS max_salary
        FROM Employee
        GROUP BY departmentId
    ) m
    ON e.departmentId = m.departmentId AND e.salary = m.max_salary;
