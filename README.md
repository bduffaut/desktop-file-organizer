# desktop-file-organizer
A Python + Bash script that organizes desktop files into semester and course-based folders using creation dates and filename parsing.



# Desktop File Organizer

This repository contains a Python script and a Bash launcher that automatically organizes files from your desktop into folders by semester and course code. It is designed for students who want to keep their academic files sorted by term and class.

## Features

- Scans desktop for visible files
- Detects course codes using regex (e.g., -COP3503)
- Extracts file creation dates to determine semester and year
- Creates directories as needed (e.g., Fall_2025/COP3503)
- Moves matching files into correct folders
- Moves unmatched files into an "Extras" folder

## Technologies

- Python (os, datetime, re, shutil)
- Bash script to trigger Python script
