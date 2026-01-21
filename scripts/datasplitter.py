import os
import shutil
import random

# ---------------- CONFIG ----------------
SOURCE_DIR = "stages"  # Folder containing Stage 0 to Stage 4
DEST_DIR = "output"    # Folder to create train/val/test splits
SPLITS = {"train": 0.7, "val": 0.15, "test": 0.15}
STAGES = ["Stage 0", "Stage 1", "Stage 2", "Stage 3", "Stage 4"]
RANDOM_SEED = 42
# ---------------------------------------

random.seed(RANDOM_SEED)

# Create directory structure
for split in SPLITS:
    for i in range(len(STAGES)):
        os.makedirs(os.path.join(DEST_DIR, split, str(i)), exist_ok=True)

# Split files
for idx, stage in enumerate(STAGES):
    stage_path = os.path.join(SOURCE_DIR, stage)
    files = [f for f in os.listdir(stage_path) if os.path.isfile(os.path.join(stage_path, f))]
    random.shuffle(files)
    
    n_total = len(files)
    n_train = int(SPLITS["train"] * n_total)
    n_val = int(SPLITS["val"] * n_total)
    n_test = n_total - n_train - n_val  # ensure all images are included

    splits_files = {
        "train": files[:n_train],
        "val": files[n_train:n_train+n_val],
        "test": files[n_train+n_val:]
    }

    for split, split_files in splits_files.items():
        for f in split_files:
            src = os.path.join(stage_path, f)
            dst = os.path.join(DEST_DIR, split, str(idx), f)
            shutil.copy2(src, dst)

print("Data split complete!")
