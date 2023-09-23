_base_ = [
    '../_base_/models/fpn_r50.py',
    '../_base_/datasets/ade20k.py',
    '../_base_/default_runtime.py'
]
# model settings
model = dict(
    type='EncoderDecoder',
    # pretrained='https://docs-assets.developer.apple.com/ml-research/models/fastvit/image_classification_distilled_models/fastvit_t8.pth.tar', # for old version of mmsegmentation
    backbone=dict(
        type='fastvit_t8_feat',
        style='pytorch',
        init_cfg=dict(
            type='Pretrained', 
            checkpoint=\
                'https://docs-assets.developer.apple.com/ml-research/models/fastvit/image_classification_distilled_models/fastvit_t8.pth.tar',
            ),
        ),
    neck=dict(in_channels=[64, 128, 320, 512]),
    decode_head=dict(num_classes=150))

# optimizer
optimizer = dict(type='AdamW', lr=0.0001, weight_decay=0.0001)
optimizer_config = dict()
# learning policy
lr_config = dict(policy='poly', power=0.9, min_lr=0.0, by_epoch=False)
# runtime settings
runner = dict(type='IterBasedRunner', max_iters=80000)
checkpoint_config = dict(by_epoch=False, interval=8000)
evaluation = dict(interval=8000, metric='mIoU')
