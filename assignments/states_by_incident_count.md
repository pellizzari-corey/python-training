# Practice Challenge: States by Incident Count

## Overview

In environments, teams often need to generate summaries showing which incident states are the most common.

Your task is to analyze a list of incident records and return a **sorted list of states by incident count**.

This type of transformation is commonly used when building:

- operational dashboards
- incident trend reports
- monitoring summaries
- automation scripts

---

## Assignment

Write a function:

```python
def states_by_incident_count(incidents):
```

The function should return a **list of tuples** containing:

1. the state name
2. the number of incidents in that state

The list must be sorted in **descending order of incident count**.

---

## Example Input

```python
[
    {"number": "INC001", "state": "New"},
    {"number": "INC002", "state": "In Progress"},
    {"number": "INC003", "state": "Resolved"},
    {"number": "INC004", "state": "New"},
    {"number": "INC005", "state": "Closed"},
    {"number": "INC006", "state": "New"}
]
```

---

## Expected Output

```python
[
    ("New", 3),
    ("In Progress", 1),
    ("Resolved", 1),
    ("Closed", 1)
]
```

Explanation:

- `"New"` appears 3 times
- the others appear once

The list is sorted by count descending.

---

## Rules

Skip records that:

- do not contain `"state"`
- contain `"state": None`
- contain `"state": ""`

Additional requirements:

- Use loops, dictionaries, and sorting
- Do not use external libraries
- Do not print inside the function
- Return a list of tuples

---

## Edge Cases to Consider

Your function should handle:

- an empty incident list
- incidents missing `"state"`
- incidents with empty values

---

## Example Invalid Records (Skip These)

```python
{"number": "INC010", "state": ""}
{"number": "INC011"}
{"number": "INC012", "state": None}
```

---

## Goal

Return a sorted list showing which incident states appear most often.

This is similar to problems encountered when writing:

- reporting scripts
- monitoring pipelines
- analytics jobs
- log aggregation tools

---

## Starter Function

```python
def states_by_incident_count(incidents):
    pass
```

---

## Hint

The solution usually has **three phases**:

### Phase 1 — Count

Use a dictionary:

```python
counts[state] += 1
```

### Phase 2 — Convert

Convert the dictionary to a list of tuples:

```python
list(counts.items())
```

### Phase 3 — Sort

Sort by count descending:

```python
key=lambda item: item[1]
```