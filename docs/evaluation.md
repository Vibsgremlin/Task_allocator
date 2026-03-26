# Evaluation Logs and Outputs

## What was evaluated
- Adding tasks to local storage
- Score-based task ordering
- Marking tasks complete

## Example output
```text
--- Your Tasks ---
1. Submit project | Deadline: 2026-03-30 | Importance: High | x
2. Book tickets | Deadline: 2026-04-10 | Importance: Low | x
```

## Notes
- This is a small local CLI utility, so evaluation is primarily functional rather than benchmark-driven.
- The sorted display and completion indexing should be tested carefully because they do not use the same ordering source.
