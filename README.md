# Golf Tracker
Record a round of golf from the command line, using:
```bash
python main.py --save-dir <directory to save round in>
```
and following the printed instructions.

Alternatively, run within a Python console, using:
```python
from golf_tracker.main import play_golf

play_golf(save_path='<directory to save round in>')
```
All round data will be saved as a csv file in the specified directory. 

Default save directory is the root of the repo, in `saved_rounds/` (not tracked by git).

Example usage notebook can be found at 
[notebooks/main.ipnb](https://github.com/J-Curwell/golf-tracker/tree/master/notebooks/main.ipynb).