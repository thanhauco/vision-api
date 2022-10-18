class EnhancedDataset(Dataset):
    def __init__(self, transforms=None):
        self.transforms = transforms