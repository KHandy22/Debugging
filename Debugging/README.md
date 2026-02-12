# Debugging Challenge

## Instructions for Students

You have THREE debugging tasks. Each file has bugs that you need to fix.

### Task 1: Code Errors (task1.py)
These programs have common code mistakes. Just run the file to test - no typing needed!
Fix all 6 snippets.

### Task 2: Input Syntax Errors (task2.py)  
These programs have bugs in the input statements. Fix the syntax errors first, then test by running and entering values.
Fix all 4 programs.

### Task 3: Data Conversion Errors (task3.py)
These programs run but give wrong answers. You need to add the correct data conversions (int or float).
Fix all 6 programs.

**Rules:**
- DO NOT delete code - fix it!
- Run `pytest test_tasks.py -v` to check your progress
- Push when done

---

## For the Sub

Students should:
1. Clone their assignment from GitHub Classroom
2. Open the task files in PyCharm
3. Start with task1.py (easiest - just code errors, no input needed)
4. Move to task2.py (input syntax errors)
5. Finish with task3.py (data conversion - most challenging)
6. Run tests with `pytest test_tasks.py -v` in terminal
7. Commit and push when done

**Common hints you can give:**
- Task 1: Look for typos, missing colons, wrong brackets
- Task 2: Check the input() lines for missing quotes or wrong symbols
- Task 3: Remember input() always returns a string - they need int() or float()
