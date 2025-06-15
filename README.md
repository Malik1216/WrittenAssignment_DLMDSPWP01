# Function Matching and Evaluation System

This project solves a function-matching task using Python. It compares training data to a set of ideal functions, selects the best matches using least-squares error, evaluates test data against those ideal functions, stores all results in a SQLite database, and visualizes everything using interactive Bokeh plots.

This project was developed as part of the *Programming with Python* course at IU International University of Applied Sciences.

**Submitted by:** Mehboob Hassan  
**Matriculation Number:** 10246609  
**Course Code:** DLMDSPWP01  
**Study Program:** Master of Computer Science  
**Submission Date:** 21 May 2025  

---

## Folder Structure

```
Assignment/
├── data/                  # CSV input files
│   ├── training_data.csv
│   ├── ideal_functions.csv
│   └── test_data.csv
│
├── db/                    # SQLite database output
│   └── data.db
│
├── src/                   # Source code
│   ├── main.py
│   ├── matcher.py
│   ├── data_loader.py
│   ├── visualizer.py
│   └── database.py
│
├── tests/                 # Unit tests
│   └── test_matcher.py
│
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

---

## Installation

1. Clone the repository or download the project files.
2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

Python 3.8 or higher is recommended (tested with Python 3.12 on Windows 11).

---

## How to Run

Run the main program from the root folder:

```bash
python src/main.py
```

This will:
- Load input data from `data/`
- Match training functions to ideal functions using least-squares error
- Map test data using the max deviation × √2 rule
- Generate interactive Bokeh plots in your browser
- Save all processed results into `db/data.db`

---

## How It Works

### 1. Training to Ideal Function Matching  
Each of the 4 training functions is compared against 50 ideal functions. The ideal function with the smallest sum of squared differences is selected using the least-squares method.

### 2. Test Data Mapping  
Each test data point is checked against the 4 chosen ideal functions. A point is mapped if its deviation is within the allowed threshold (max deviation from training × √2).

### 3. Database Storage  
All outputs are stored in a local SQLite database:
- `training_data` — x values and 4 training y columns
- `ideal_functions` — x values and 50 ideal y columns
- `test_results` — test x, y, delta, ideal function number, and test column

---

## Technologies Used

- Python 3.12
- pandas
- numpy
- bokeh
- sqlalchemy
- unittest

---

## Output

- Interactive visualizations using Bokeh (`.html`)
- A SQLite database: `db/data.db`
- Code is structured with object-oriented programming
- Includes one subclass (`TrainingMatcher`) and a basic unit test

---

## Submission Notes

- All Python scripts are in `src/` and `tests/`
- Input CSV files are under `data/`
- The generated database is stored in `db/`
- Unit test script is inside `tests/`
- This project was built and submitted for the DLMDSPWP01 assignment
