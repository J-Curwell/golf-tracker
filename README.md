# Golf Tracker
Record a round of golf from the command line, using:
```bash
python main.py --save-dir <directory to save round in>
```
and following the printed instructions.

Alternatively, run within a Python console, using:
```python
from beta.main import play_golf

play_golf(save_path='<directory to save round in>')
```
All round data will be saved as a csv file in the specified directory. 

Default directory is `./rounds/`.
