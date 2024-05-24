from pathlib import Path
#path=Path("email")
#print(path.rmdir())
#print(path.mkdir())
#print(path.exists())
path=Path()
for file in path.glob("*"):
    print(file)