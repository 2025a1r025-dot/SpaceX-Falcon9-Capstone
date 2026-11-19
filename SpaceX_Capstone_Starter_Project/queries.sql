-- Adjust table and column names to match your imported dataset.
SELECT COUNT(*) AS total_launches FROM SPACEXTBL;

SELECT class, COUNT(*) AS launch_count
FROM SPACEXTBL
GROUP BY class
ORDER BY class;

SELECT AVG([Payload Mass (kg)]) AS average_payload_kg
FROM SPACEXTBL;

SELECT [Launch Site], AVG(class) AS landing_success_rate
FROM SPACEXTBL
GROUP BY [Launch Site]
ORDER BY landing_success_rate DESC;
