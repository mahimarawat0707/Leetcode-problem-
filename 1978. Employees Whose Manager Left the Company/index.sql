SELECT employee_id
FROM Employees
WHERE manager_id NOT IN (
    SELECT employee_id FROM Employees
)
ORDER BY employee_id;
