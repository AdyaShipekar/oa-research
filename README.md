## Two-Stage Osteoarthritis Classification Model

Two-stage ResNet18 pipeline:
1. Binary classification: OA vs No OA
2. Severity classification: KL grades 1–4

### Dataset
Knee X-ray images organized as:
data/train/0–4  
data/val/0–4  

Dataset not included.

### Training
Run `two_stage_oa.ipynb` in Google Colab with GPU enabled.

### Framework
PyTorch + torchvision
