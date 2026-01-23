# PyQuiz: Peer Tutor Logic Engine

## Overview
PyQuiz is a Command Line Interface (CLI) tool designed to help Python tutors check their students' knowledge. Instead of grading by hand, this tool streamlines the testing process. It ensures that students are tested on key logic, syntax, and data structures in a random and controlled setting.

## Features
- **Dynamic Question Loading:** Questions are retrieved from an external JSON file, which lets tutors update the curriculum without changing the code.
- **Randomized Sessions:** This prevents "screen peeking" by shuffling questions and options for each student.
- **Robust Error Handling:** It avoids crashes from invalid user inputs with structured try-except blocks.
- **Automated Reporting:** It saves each attempt to a local log file for long-term tracking of progress.

## Project Structure

- `project.py`: The main application logic.
- `questions.json`: The database of technical questions.
- `results.csv`: The persistent log of student scores.
- `test_project.py`: Pytest suite to ensure the grading logic is 100% correct.
