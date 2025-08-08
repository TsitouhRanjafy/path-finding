
- in `interface` file

_mylib_path = os.path.join(path, "_internal/lib/graph.so")


- in `path-finding` file
 
icon = PhotoImage(file="_internal/reload.png")

- build an executable
  
  - in unix
```bash
pyinstaller --add-binary "lib/graph.so:lib" --add-data "reload.png:." path-finding.py
```

  - in wondows
```bash
pyinstaller --add-binary "lib\\graph.dll;lib" --add-data "reload.png;." path-finding.py
```