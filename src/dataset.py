from torch.utils.data import Dataset
class ImageDataset(Dataset):
    def __len__(self): return 100
    def __getitem__(self, idx): return 0