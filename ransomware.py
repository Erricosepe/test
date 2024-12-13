import sys
import os

# Add the dependencies ZIP file to Python's path
current_dir = os.path.dirname(os.path.abspath(__file__))
zip_path = os.path.join(current_dir, "dependencies.zip")
sys.path.insert(0, zip_path)

# Import your dependencies
import your_dependency

# Your main logic here
if __name__ == "__main__":
    print("Dependencies loaded successfully!")