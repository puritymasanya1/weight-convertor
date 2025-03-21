# Weight Converter

A simple Python script that converts weight between kilograms and pounds.

## Description

This program allows users to convert their weight between the imperial (pounds) and metric (kilograms) systems. The user enters their weight value and specifies the unit they're entering (kilograms or pounds), and the program converts it to the other unit.

## Features

- Convert weight from kilograms to pounds
- Convert weight from pounds to kilograms
- Round the result to 1 decimal place for readability
- Input validation for unit selection

## How to Use

1. Run the script in your Python environment
2. Enter your weight when prompted
3. Specify the unit by entering:
   - `K` or `k` for kilograms
   - `L` or `l` for pounds
4. The program will display your weight in the converted unit


## Technical Details

- The program uses a conversion factor of 2.205 pounds per kilogram
- Input handling is case-insensitive and strips whitespace
- Error handling is included for invalid unit inputs

## Requirements

- Python 3.x
