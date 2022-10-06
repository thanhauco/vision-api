import torch
def quantize(model):
    return torch.quantization.quantize_dynamic(model)