 
import os

# create the main project directory
PROJ_DIR = "Real-Time-Data-Visualization"
os.makedirs(PROJ_DIR, exist_ok=True)

# create subdirectories for data processing and visualization
DATA_DIR = os.path.join(PROJ_DIR, "data-processing")
VIZ_DIR = os.path.join(PROJ_DIR, "visualization")
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(VIZ_DIR, exist_ok=True)

# create empty files for data processing
DATA_FILES = ["process_data.py", "kinesis.py", "lambda.py", "s3.py"]
for file in DATA_FILES:
    file_path = os.path.join(DATA_DIR, file)
    with open(file_path, "w") as f:
        pass

# create empty files for visualization
VIZ_FILES = ["app.py"]
for file in VIZ_FILES:
    file_path = os.path.join(VIZ_DIR, file)
    with open(file_path, "w") as f:
        pass
