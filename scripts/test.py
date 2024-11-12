from pathlib import Path
path = Path('').home() / 'Documents/The Py50 Guide/PyGuide/static'
print(path)
correct_path = path 
print(correct_path)
print(correct_path.is_dir())
for gif in correct_path.glob('*.gif'):
    print(gif)