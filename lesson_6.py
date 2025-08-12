import json

with open("lesson_6.ipynb", "r", encoding="utf-8") as f:
    notebook = json.load(f)

if "widgets" in notebook.get("metadata", {}):
    del notebook["metadata"]["widgets"]

with open("lesson_6.ipynb", "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=2)
