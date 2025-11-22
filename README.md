# Sensor-Data-Logger
Python File Handling Practice

This mini-project is a collection of small Python scripts where I practiced different file-handling techniques.
It covers text files, JSON files, and binary files — the three core formats you’ll meet often in automation, data logging, embedded systems, and general backend work.

🔹 1. binary_write.py
This script focuses on writing and reading binary data.
It demonstrates:
  How to open files in "wb" and "rb" modes
  How binary data is stored
  How to verify the written bytes
Useful for: working with firmware dumps, sensor logs, or any low-level file.

🔹 2. filer.py (Text Writer)
This script handles normal text file writing using common modes like:
  "w" (write)
  "a" (append)
  "r+" (read/write combo)
It shows the basics of:
  Writing lines
  Appending new text
  Managing cursors with tell() and seek() (where possible)
Useful for: logs, notes, simple storage, automation scripts.

🔹 3. reader.py (Text Reader)
This file focuses on reading text files with:
  read(), readline(), readlines()
  Checking file size
  Navigating with the cursor
Useful for: processing files, parsing logs, CLI-based tools.

🔹 4. json_filer.py
This script works with JSON data — the most important structured file format in Python automation.
It demonstrates:
  Reading JSON (json.load)
  Updating dictionaries
  Appending items
  Writing back with json.dump(indent=10)
Useful for: config files, device settings, API-style data, project templates.
