Here I created a Python file `getting_and_printing_pid.py`. When run, it simply imports `os`, gets its own **PID** (= **P**rocess **Id**entifier), and prints it before exiting.

**OS** is a module in Python that allows the script to interact with the Operating System. Any Python process automatically gets a PID assigned by the kernel, but we need to import `os` to read it inside the script.

```bash
Projects/school-of-first-principles/workbench via 🐍 v3.12.3 
❯ python3 getting_pid.py 
64306
```


As you can see, the python file when run created its own process and cleanly outputted its own PID.