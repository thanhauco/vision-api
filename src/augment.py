import albumentations as A
transform = A.Compose([A.HorizontalFlip(p=0.5)])