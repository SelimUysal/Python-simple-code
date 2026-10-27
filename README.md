# Python Programming Exercises 🐍

A small collection of **four standalone Python exercises** covering text processing, functions, recursion, collections, and basic parsing.

These scripts were written for programming practice. They are best suited to learners who already know basic Python syntax and want to explore how common programming concepts work through examples.

## 📂 Explore the Exercises

| Exercise | What it does | Concepts |
| --- | --- | --- |
| [Array Declaration Parser](EBNF%20programining%20language%20.py) | Reads a Pascal-style array declaration and extracts its type and dimensions into a descriptor. | Regular expressions, string parsing, lists |
| [Recursive Digit Processing](function%20.py) | Turns an integer into a list of digits using recursion, then transforms the list based on its length. | Functions, recursion, global variables, lists |
| [Student Exam Score Analysis](function%20global%202%20.py) | Scores three students against an answer key, calculates the class average, and supports name lookup. | Functions, dictionaries, tuples, loops |
| [Text and Word-Frequency Analysis](simple%20game%20.py) | Removes selected stop words and punctuation, counts words, extracts unique words, and groups the results. | Strings, sets, dictionaries, `collections.Counter` |

> **Note:** The original filenames have been preserved. In particular, `simple game .py` is a **text-processing exercise**, not an interactive game.

## 🚀 Getting Started

**Requirements:** Python 3. All four exercises use the Python standard library; no third-party packages are required.

Clone the repository:

```bash
git clone https://github.com/SelimUysal/Python-simple-code.git
cd Python-simple-code
```

Run an exercise from your terminal. Filenames contain spaces, so **keep the quotation marks**:

```bash
python "simple game .py"
```

On systems where `python` does not refer to Python 3, use `python3` instead.

### Example: Text Processing

Run:

```bash
python "simple game .py"
```

Enter a short phrase, such as:

```text
The cat and the dog. The cat!
```

The script prints intermediate results, including the cleaned word list, word frequencies, unique words, and grouped words. Stop-word filtering currently covers only `a`, `an`, and `the`.

### Example: Parsing an Array Declaration

Run:

```bash
python "EBNF programining language .py"
```

Example input:

```text
DATA: array [1..5] of integer;
```

The parser produces a list describing the array declaration, including its element type and dimensions. Its accepted syntax is deliberately limited; it is **not a complete EBNF or Pascal parser**.

## 🧠 How to Practice

1. Open a script and identify its inputs, functions, and outputs.
2. Run it using the suggested example.
3. Try changing the input and predicting the result.
4. Improve error handling, variable naming, or code structure as an exercise.

## ⚠️ Important Limitations

- These are **learning exercises**, not production-ready utilities; input validation and edge-case handling are limited.
- `function .py` uses `eval(input(...))`, which can execute arbitrary Python expressions. **Run it only with trusted input**; replacing `eval` with safe parsing is a recommended improvement.
- The exam-scoring exercise assumes the entered answer strings are compatible in length with the answer key.
- Some implementations may produce unexpected results for boundary cases. Review and test them before reusing the code in other projects.

---

**Purpose:** Learn by running, inspecting, and improving small Python programs.
