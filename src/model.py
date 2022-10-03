import timm
def get_vit():
    return timm.create_model('vit_base_patch16_224', pretrained=True)