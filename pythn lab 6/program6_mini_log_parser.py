import re

log = """
[2024-06-01 08:15:32] ERROR  user=jsmith  msg="Disk quota exceeded"
[2024-06-01 08:16:05] INFO   user=agarcia msg="Login successful"
[2024-06-01 08:17:44] WARN   user=jsmith  msg="High memory usage"
"""

# Pattern for the log
pattern = (
    r"\[(?P<timestamp>[\d-]+ [\d:]+)\]\s+"
    r"(?P<level>\w+)\s+"
    r"user=(?P<user>\w+)\s+"
    r'msg="(?P<msg>[^"]*)"'
)


# Store all log entries
entries = []

for x in re.finditer(pattern, log):
    entries.append(x.groupdict())

print("Log entries:")

for entry in entries:
    print(entry)


# Count ERROR, WARN and INFO
error = len(re.findall(r"\bERROR\b", log))
warn = len(re.findall(r"\bWARN\b", log))
info = len(re.findall(r"\bINFO\b", log))

print("\nLog summary:")
print("ERROR:", error)
print("WARN:", warn)
print("INFO:", info)


# Hide usernames
result = re.sub(r"user=\w+", "user=<hidden>", log)

print("\nRedacted log:")
print(result)


# Bonus - Sort entries by username
entries.sort(key=lambda x: x["user"])

print("ERROR entries:")

for entry in entries:
    if entry["level"] == "ERROR":
        print(entry["user"], ":", entry["msg"])

'''output:
Log entries:
{'timestamp': '2024-06-01 08:15:32', 'level': 'ERROR', 'user': 'jsmith', 'msg': 'Disk quota exceeded'}
{'timestamp': '2024-06-01 08:16:05', 'level': 'INFO', 'user': 'agarcia', 'msg': 'Login successful'}
{'timestamp': '2024-06-01 08:17:44', 'level': 'WARN', 'user': 'jsmith', 'msg': 'High memory usage'}

Log summary:
ERROR: 1
WARN: 1
INFO: 1

Redacted log:

[2024-06-01 08:15:32] ERROR  user=<hidden>  msg="Disk quota exceeded"
[2024-06-01 08:16:05] INFO   user=<hidden> msg="Login successful"
[2024-06-01 08:17:44] WARN   user=<hidden>  msg="High memory usage"

ERROR entries:
jsmith : Disk quota exceeded  '''

