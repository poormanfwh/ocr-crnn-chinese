#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Reference    :  https://github.com/MaybeShewill-CV/CRNN_Tensorflow
# @File    : global_config.py
# @IDE: PyCharm Community Edition
"""
Set some global configuration
"""
from easydict import EasyDict as edict

__C = edict()
# Consumers can get config by: from config import cfg

cfg = __C

__C.ARCH = edict()

# Number of units in each LSTM cell
__C.ARCH.HIDDEN_UNITS = 256
# Number of stacked LSTM cells
__C.ARCH.HIDDEN_LAYERS = 2
# Sequence length.  This has to be the width of the final feature map of the CNN, which is input size width / 4
__C.ARCH.SEQ_LENGTH = 70  # cn dataset
# Width x height into which training / testing images are resized before feeding into the network
__C.ARCH.INPUT_SIZE = (280, 32)                    # 输入图片宽高
# Number of channels in images
__C.ARCH.INPUT_CHANNELS = 3                        # 输入channel

# Train options
__C.TRAIN = edict()
# Set the shadownet training epochs
__C.TRAIN.EPOCHS = 500000                          # 训练终止步数
# Set the display step
__C.TRAIN.DISPLAY_STEP = 100                       # 训练过程中可视化步数

__C.TRAIN.VAL_DISPLAY_STEP = 1000                  # 训练过程中可视化步数
# Set the initial learning rate
__C.TRAIN.LEARNING_RATE = 0.01                    # 初始学习率
# Set the shadownet training batch size
__C.TRAIN.BATCH_SIZE = 64                          # batch_size
# Set the learning rate decay steps
__C.TRAIN.LR_DECAY_STEPS = 2000                    # 使用学习率指数衰减，衰减步幅
# Set the learning rate decay rate
__C.TRAIN.LR_DECAY_RATE = 0.97                     # 衰减值
# Set multi process nums
__C.TRAIN.CPU_MULTI_PROCESS_NUMS = 10              # 多线程
# Set moving average decay
__C.TRAIN.SAVE_STEPS = 1000                       # 每隔多少步保存一次模型
# Set the GPU resource used during training process
__C.TRAIN.GPU_MEMORY_FRACTION = 0.9                # 允许占用GPU运存的最大比例
# Set the GPU allow growth parameter during tensorflow training process
__C.TRAIN.TF_ALLOW_GROWTH = True

__C.TRAIN.LR_STAIRCASE = True


# Set Gpu nums
__C.TRAIN.GPU_NUM = 1

# Set moving average decay
__C.TRAIN.MOVING_AVERAGE_DECAY = 0.9999
