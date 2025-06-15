# Function Matching and Evaluation System

This project solves a function-matching task using Python. It compares training data to a set of ideal functions, selects the best matches using least-squares error, evaluates test data against those ideal functions, stores all results in a SQLite database, and visualizes everything using interactive Bokeh plots.

This project was developed as part of the IU Programming with Python assignment.

---

## Folder Structure

Assignment/
├── data/ # CSV input files
│ ├── training_data.csv
│ ├── ideal_functions.csv
│ └── test_data.csv
│
├── db/ # SQLite database output
│ └── data.db
│
├── src/ # Source code
│ ├── main.py
│ ├── Matcher.py
│ ├── data_loader.py
│ ├── visualizer.py
│ └── database.py
│
├── tests/ # Unit tests
│ └── test_matcher.py
│
├── requirements.txt # List of required Python packages
└── README.md # This file

## Installation

1. Clone the repository or copy the project files.
2. Install required Python packages:

Python 3.8+ is recommended.

---

## How to Run

Run the project from the root folder:

This will:

- Load the data from `data/`
- Match each training function to the best ideal function using least-squares error
- Map test data based on the max deviation × √2 rule
- Visualize the results with Bokeh (plots open in your browser)
- Save results into a SQLite database at `db/data.db`

---

## How It Works

### 1. Training to Ideal Matching
Each of the 4 training functions is compared against 50 ideal functions. The best match is selected using the sum of squared differences (least squares).

### 2. Test Data Mapping
Each test point is compared with the 4 selected ideal functions. If the difference is less than the maximum deviation from training × √2, it is assigned to that function.

### 3. Database Storage
- `training_data`: x and 4 y-values
- `ideal_functions`: x and 50 ideal functions
- `test_results`: test x, y, delta, and matched ideal function

---

## Technologies Used

- Python 3.12
- pandas
- numpy
- bokeh
- sqlalchemy
- unittest (for unit testing)

---

## Output

- Visuals open in browser (`.html` files)
- `data.db` stores the processed results
- All logic is OOP-structured
- Includes at least one inheritance and one test case

---

## Submission Notes

- All Python code is in `src/` and `tests/`
- All data files are in `data/`
- One SQLite file is created in `db/`
- Unit test file is located in `tests/`
- The code was developed and tested using Windows 10 and Python 3.12