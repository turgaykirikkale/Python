import pandas as pd
from collections import Counter
import re

# Read log file
log_file = "system_logs.txt"

log_entries = []
with open(log_file, "r") as file:
    for line in file:
        match = re.match(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)", line.strip())
        if match:
            timestamp, level, message = match.groups()
            log_entries.append([timestamp, level, message])

# Convert to DataFrame
df = pd.DataFrame(log_entries, columns=["timestamp", "level", "message"])
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Count errors in the last 30 seconds
error_counts = Counter(df[df["level"] == "ERROR"]["timestamp"].dt.floor("30S"))

# Threshold for detecting an anomaly (too many errors in a short time)
threshold = 3

# Detect error spikes
for time, count in error_counts.items():
    if count > threshold:
        print(f"🚨 Anomaly detected! {count} ERROR logs in 30 seconds at {time}")

# Show logs with anomalies
print("\nFull Log Analysis:")
print(df)



# there are some many issues with this script if count is bigger then threshold just print anomoly we dont use any ML algorithm
#everytime there is an error this particular script writes that anomaly detected maybe error that you can ignore or important is that this 
#script also ignores warning messages and info messages it will also ignore critical messages sometimes your log level might be application
#is leaking memory or application response time is 10s that might come with info log but its a strange pattern which this particular script 
#might not detect if you use AI ıt will detect this strange particular behaving 