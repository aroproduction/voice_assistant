# Import the time and hashlib modules
import time
import hashlib

# Define a function to calculate the factorial of a number
def factorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * factorial(n-1)

# Define a function to calculate the SHA1 hash of a string
def sha1_hash(s):
  return hashlib.sha1(s.encode()).hexdigest()

# Define a list of tasks to perform
tasks = [
  ("Factorial of 100", lambda: factorial(100)),
  ("SHA1 hash of 'Hello, world!'", lambda: sha1_hash("Hello, world!")),
  ("SHA1 hash of 'The quick brown fox jumps over the lazy dog'", lambda: sha1_hash("The quick brown fox jumps over the lazy dog"))
]

# Loop through the tasks and measure the execution time
for task_name, task_func in tasks:
  # Get the start time
  start_time = time.time()
  # Execute the task
  task_result = task_func()
  # Get the end time
  end_time = time.time()
  # Calculate the elapsed time
  elapsed_time = end_time - start_time
  # Print the task name, result and elapsed time
  print(f"{task_name}: {task_result} ({elapsed_time:.6f} seconds)")
