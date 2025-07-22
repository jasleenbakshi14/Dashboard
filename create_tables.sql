CREATE TABLE logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    user TEXT,
    event_type TEXT,
    status TEXT,
    ip_address TEXT
);
