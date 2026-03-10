# ServiceNow Practice Challenge: Highest Priority Open Incident Count

## Overview

In ServiceNow and IT operations environments, teams often need to quickly understand how many **open incidents** exist at each priority level, especially for escalation and reporting.

Your task is to write a Python function that processes a list of incident records and returns the **priority with the highest number of open incidents**, along with its count.

This challenge simulates the kind of logic used in:

- ServiceNow reporting
- incident escalation dashboards
- operations summaries
- queue health monitoring

---

## Assignment

Write a function:

```python
def highest_priority_open_incident_count(incidents):
```

The function should return a tuple in this format:

```python
("P1", 4)
```

Where:

- the first value is the priority with the highest number of **open incidents**
- the second value is the count of open incidents for that priority

---

## Open Incident Rule

Only count incidents whose `"state"` is considered **open**.

Open states are:

- `"New"`
- `"In Progress"`

Do **not** count incidents whose state is:

- `"Resolved"`
- `"Closed"`

---

## Incident Record Format

Each incident is a dictionary that may contain:

- `"number"` – incident number (example: `"INC0012345"`)
- `"priority"` – example: `"P1"`, `"P2"`, `"P3"`
- `"state"` – example: `"New"`, `"In Progress"`, `"Resolved"`, `"Closed"`

---

## Example Input

```python
[
    {"number": "INC001", "priority": "P1", "state": "New"},
    {"number": "INC002", "priority": "P2", "state": "In Progress"},
    {"number": "INC003", "priority": "P1", "state": "Resolved"},
    {"number": "INC004", "priority": "P1", "state": "New"},
    {"number": "INC005", "priority": "P2", "state": "New"}
]
```

---

## Expected Output

```python
("P1", 2)
```

Explanation:

- `P1` has 2 open incidents
- `P2` has 2 open incidents

If there is a tie, return the priority that comes **first alphabetically**.

So between:

```python
"P1" and "P2"
```

you return:

```python
"P1"
```

---

## Rules

Only count incidents that have:

- a non-empty `"priority"`
- a non-empty `"state"`

If either field is missing or empty, **skip that record**.

Additional requirements:

- Use **loops and dictionaries**
- Do **not use external libraries**
- Preserve the exact priority string
- Do **not print inside the function**
- Return a tuple

---

## Edge Cases to Consider

Your function should correctly handle:

- an empty incident list
- incidents missing `"priority"`
- incidents missing `"state"`
- incidents with empty values for those fields
- ties between priorities

---

## Empty Result Rule

If there are **no valid open incidents**, return:

```python
(None, 0)
```

---

## Example Invalid Records (Should Be Skipped)

```python
{"number": "INC010", "priority": "", "state": "New"}
{"number": "INC011", "priority": "P1", "state": ""}
{"number": "INC012", "state": "In Progress"}
{"number": "INC013", "priority": "P2"}
```

---

## Goal

Your goal is to identify which priority currently has the greatest number of open incidents.

This type of transformation is common when building scripts for:

- ServiceNow incident summaries
- escalation dashboards
- queue analysis
- operational reporting

---

## Starter Function

```python
def highest_priority_open_incident_count(incidents):
    pass
```

---

## Hint

A good way to think about this problem is in two phases:

1. Count open incidents by priority using a dictionary
2. Find the priority with the largest count

Conceptually, the counting step looks like:

```python
priority_counts[priority] += 1
```

Then you loop through the counts and track the best result seen so far.