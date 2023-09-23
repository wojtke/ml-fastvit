_base_ = [
    './fpn_fastvit_t8_ade20k_80k.py'
]
# model settings
model = dict(
    backbone=dict(
        type='fastvit_sa12_feat',
        init_cfg=dict(
            checkpoint='https://docs-assets.developer.apple.com/ml-research/models/fastvit/image_classification_distilled_models/fastvit_sa12.pth.tar',
            ),
        ),
    neck=dict(in_channels=[64, 128, 256, 512]),
)