# Quizlet Test Mode Clone

This repository contains a simple command-line clone of Quizlet's test mode for personal study.

## Features

- Load study cards from a JSON file containing terms and definitions
- Automatically generates written or multiple-choice questions
- Randomly asks for either the term or the definition
- Provides immediate feedback and a final score

## Usage

1. Prepare a JSON file of study cards, for example `quizlet_clone/cards_example.json`.
2. Run the test script:

```bash
python quizlet_clone/quizlet_test.py quizlet_clone/cards_example.json -n 5
```

Replace `-n 5` with the desired number of questions.
