from src.math_operations import add, sub

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_sub():
    assert sub(5, 3) == 2
    assert sub(4, 3) == 1
    assert sub(3, 3) == 0
    assert sub(2, 3) == -1
```

---

## How to do it step by step:

1. In your terminal type:
```
   notepad src\math_operations.py
```
2. Notepad opens (it may ask "Create new file?" — click **Yes**)
3. **Copy the code above** and paste it into notepad
4. Press **Ctrl+S** to save
5. Close notepad

6. Then type:
```
   notepad tests\test_operation.py
```
7. Notepad opens → paste the second code block
8. Press **Ctrl+S** to save
9. Close notepad

After both files are saved, come back to the terminal and run:
```
git init
git add .
git commit -m "feat: initial project setup with CI workflow"
git branch -M main
git remote add origin https://github.com/<your-username>/appgithubaction.git
git push -u origin main