# Classes-Quiz-Exercise

A small command line quiz written with basic object oriented Python, used as a classes exercise.

## Running it

Run the script from the repository root, because the question file is opened by its relative path:

```
python3 main.py
```

The quiz prints each question with numbered choices, re-prompts until the input is a number inside the valid range, then reports the number answered and the score at the end.

## Question file format

`questions.txt` holds one question per line, skipped if blank or unparseable. Each line is a Python tuple literal read with `ast.literal_eval`, in the order `(question text, list of choices, correct answer)`:

```
"What is the capital of France?", ["London", "Paris", "Berlin", "Madrid"], 2
```

The correct answer is the 1-based position of the choice in the list, matching what the user types at the prompt, so `2` above means Paris.

## Structure

- `Question` holds one question's text, choices and answer position, and checks a submitted answer.
- `Quiz` tracks the current question index, prompts, validates input and keeps the score.
- `load_questions_from_file` reads the question file and reports line numbers it could not parse.
