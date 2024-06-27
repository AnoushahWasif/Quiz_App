# Quiz Application

This is a Python-based quiz application that fetches quiz questions from the Open Trivia Database API and allows users to take quizzes interactively.

## Features

- Fetches quiz questions from the Open Trivia Database API.
- Supports multiple choice questions with shuffled options.
- Provides interactive quiz-taking experience.
- Displays final score after completing the quiz.

## Requirements

- Python 3.x
- `requests` library (to fetch data from APIs)

## Usage

1. Navigate to the project directory:
   ```
   cd quiz-application
   ```

2. Run the main script:
   ```
   python main.py
   ```

3. Follow the prompts to enter your name and answer quiz questions.

## Customization

- Modify `get_questions` function in `main.py` to fetch questions from different categories, difficulties, or types by adjusting API parameters.
- Extend functionality by adding features such as saving quiz results, adding more quiz types, or implementing a graphical user interface (GUI).

## API Reference

- [Open Trivia Database API](https://opentdb.com/): Provides trivia questions in various categories.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.
