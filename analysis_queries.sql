-- Failed logins per day
SELECT DATE(timestamp) AS day, COUNT(*) AS failed_logins
FROM logs
WHERE event_type = 'login' AND status = 'fail'
GROUP BY day;

-- Top 5 users by total events
SELECT user, COUNT(*) AS total_events
FROM logs
GROUP BY user
ORDER BY total_events DESC
LIMIT 5;
