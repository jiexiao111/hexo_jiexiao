import os
from keras.preprocessing import image
from keras.models import Sequential
from keras.layers import Flatten, Dense
from keras.optimizers import Nadam, Adam, SGD
from keras.callbacks import TensorBoard, ModelCheckpoint
batch_size = 64

train_dir = '/aiml/data/train/'
test_dir = '/aiml/data/test/'
log_dir = '/aiml/dfs/checkpoint/train'
pix = 28

train_data = image.ImageDataGenerator(samplewise_std_normalization=True)
test_data = image.ImageDataGenerator(samplewise_std_normalization=True)
train_gen = train_data.flow_from_directory(train_dir, color_mode='grayscale', target_size=(pix, pix), batch_size=batch_size)
test_gen = train_data.flow_from_directory(test_dir, color_mode='grayscale', target_size=(pix, pix), batch_size=batch_size)

# 类别数量
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

# 每个 epoch 的回调
check_cb = ModelCheckpoint(filepath=os.path.join(log_dir, 'sigle_dense_model.hdf5'), verbose=1, save_best_only=True)
board_cb = TensorBoard(log_dir=log_dir, histogram_freq=0, write_graph=True, write_images=False)

# 测试模型，用于检测 TensorBoard、ModelCheckpoint 能够正常被调用
def sigle_dense_model():
    model = Sequential([
        Flatten(input_shape=(pix, pix, 1)),
        Dense(512, activation='softmax'),
        Dense(num_class, activation='softmax')
    ])
    model.compile(Adam(), loss='categorical_crossentropy', metrics=['accuracy'])
    return model
s_d_model = sigle_dense_model()
s_d_model.fit_generator(train_gen, steps_per_epoch=2, epochs=4, validation_data=test_gen, validation_steps=1, callbacks=[check_cb, board_cb])
