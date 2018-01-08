
# coding: utf-8

# In[9]:

import os
from keras.preprocessing import image
from keras.models import Sequential
from keras.layers import Flatten, Dense, Input
from keras.optimizers import Nadam, Adam, SGD
from keras.callbacks import TensorBoard, ModelCheckpoint
from keras.applications.resnet50 import ResNet50
from keras.applications.xception import Xception
from keras.applications.vgg16 import VGG16
from keras.models import Model
from python_code.ResNet_Keras import ResnetBuilder

batch_size = 512

# 控制 Res18 每 10 分钟验证一次
step_per_epoch = 512 * 1000 / batch_size 
# 验证仅使用五分之一的步数，刚好符合训练集和测试集的比例 8:2
step_per_valid = step_per_epoch / 5
# 按照每个 epoch 10 分钟计算，1000 个 epoch 刚好跑一周，按照比赛的情况，这应该是最大值了
max_epoch = 512 * 1000 / batch_size


# In[2]:

train_dir = '/aiml/data/train/'
test_dir = '/aiml/data/test/'
log_dir = '/aiml/dfs/checkpoint/'
pix = 64


# In[3]:

train_data = image.ImageDataGenerator(rescale=1./255)
test_data = image.ImageDataGenerator(rescale=1./255)
train_gen = train_data.flow_from_directory(train_dir, color_mode='grayscale', target_size=(pix, pix), batch_size=batch_size)
test_gen = train_data.flow_from_directory(test_dir, color_mode='grayscale', target_size=(pix, pix), batch_size=batch_size)
# 类别数量
if hasattr(train_gen, 'num_classes'):
    num_class = train_gen.num_classes
else:
    num_class = train_gen.num_class
# 训练样本数量
num_train = train_gen.n
# 测试样本数量
num_test = test_gen.n
# 确认读取的图片的格式正确
image_shape = train_gen.next()[0].shape
# 查看返回的标签类型，“categorical” 表示为 one-hot 标签
print(train_gen.class_mode)
print(num_class, num_train, num_test, image_shape)


# In[8]:

model_dir_name = 'Resnet18'
param_rate = 1
model = ResnetBuilder.build_resnet_18((pix, pix, 1), num_class)
model.compile(Adam(), loss='categorical_crossentropy', metrics=['accuracy'])s


# In[ ]:

# 定义存储目录
train_dir_name = os.path.join(log_dir, model_dir_name, 'v.02')

# 通用代码，无需更改
if os.path.exists(train_dir_name):
    os.system('rm -rf %s' % (train_dir_name));
print(train_dir_name)
weights_name = os.path.join(train_dir_name , 'weights.hdf5')
check_cb = ModelCheckpoint(filepath=weights_name, verbose=1, save_best_only=True)
board_cb = TensorBoard(log_dir=train_dir_name, histogram_freq=False, write_graph=False, write_images=False)
step_per_epoch /= param_rate
step_per_valid /= param_rate
max_epoch /= param_rate
print("Batch_size: %d\nStep_per_epoch: %d\nstep_per_valid: %d\nMax_epoch: %d" % (batch_size, step_per_epoch, step_per_valid, max_epoch))

# 开始训练
model.fit_generator(train_gen, steps_per_epoch=step_per_epoch, epochs=max_epoch, 
                    validation_data=test_gen, validation_steps=step_per_valid, 
                    callbacks=[check_cb, board_cb])

