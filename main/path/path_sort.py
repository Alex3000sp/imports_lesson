from pathlib import Path

tree = Path('directory/')
for i in tree.iterdir():
    stm = i.stem.replace('-', '/')
    path = i.parent / (stm + i.suffix)
    path.parent.mkdir(parents=True, exist_ok=True)
    i.rename(path)
    
    