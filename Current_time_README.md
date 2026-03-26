# Current Time Clock

`Current_time.py` is a simple Python GUI program that displays the current system time using `tkinter`.

## Features

- Shows the current time in `HH:MM:SS AM/PM` format
- Updates automatically every 500 milliseconds
- Uses a basic `tkinter` window with a styled label

## Requirements

- Python 3
- `tkinter` installed and available in your Python environment

## How It Works

The program:

1. Creates a `tkinter` window
2. Adds a label to display the time
3. Uses `time.strftime("%I:%M:%S %p")` to get the current time
4. Refreshes the label every 500 milliseconds using `after()`

## Run the Program

```bash
python Current_time.py
```

## Example Output

A window appears with a digital clock such as:

`10:45:32 PM`

## Files

- `Current_time.py` - main Python script for the clock application

## Notes

- The clock uses your computer's local system time.
- The GUI remains active until you close the window.
