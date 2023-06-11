# Date Normalizer- test

Date Normalizer is a Python script that converts various date formats into a standardized format. It utilizes regular expressions and datetime parsing to handle different date representations. The script demonstrates the use of first-class functions in Python.

## Usage

The script is executed from the command line using Python 3.

```shell
python3 transform-dates.py
#OR
chmod +x transform-dates.py && ./transform-dates.py
```

## Dependencies

The script requires the following dependencies:

- Python 3
- `re` module (built-in)
- `datetime` module (built-in)

## Features

- Converts dates in the format "Month-Year" (e.g., "Aug94", "January--23") to the standardized format (MM-DD-YYYY).
- Converts dates in the format "DD.MM.YYYY" (e.g., "26.08.1994") to the standardized format (MM-DD-YYYY).

## Implementation

The script showcases the concept of first-class functions through the use of function references stored in a list. The key components include:

1. Regular expressions and conversion functions:
   - `convert_month_year(match)`: Converts "Month-Year" format to the standardized format.
   - `convert_date(match)`: Converts "DD.MM.YYYY" format to the standardized format.

2. Normalization function:
   - `normalize_date(date)`: Normalizes the given date by matching it against the defined patterns and applying the appropriate conversion function.

3. Main function:
   - `main()`: Executes the date normalization process on a predefined list of dates, printing the raw dates and their normalized counterparts.

The list of patterns and actions in the `normalize_date` function demonstrates the use of first-class functions. Each pattern is associated with a corresponding action function, allowing for dynamic and reusable date normalization.

## Example

Here's an example usage of the script, highlighting the use of first-class functions:

```python
dates = ["January--23", "Aug94", "Febr-22", "26.08.1994"]
normalized_dates = [normalize_date(datum).strftime("%m-%d-%Y") for datum in dates]
print(f"Raw dates: {dates} \nNormalized dates: {normalized_dates}")

# Raw dates: ['January--23', 'Aug94', 'Febr-22', '26.08.1994']
# Normalized_dates: ['01-01-2023', '08-01-1994', '02-01-2022', '08-26-1994']
```

The output will display the raw dates followed by their normalized counterparts.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## Acknowledgments

This script was developed as a demonstration of date normalization techniques using regular expressions, datetime parsing, and the concept of first-class functions in Python.

The idea to do this occured during [a chat with ChatGPT.](https://chat.openai.com/share/f1bc2b2e-1888-4081-8610-0f1a6fb771fc)

Feel free to customize this README based on your specific needs, providing additional details or sections as necessary.
