
import tensorflow as tf

new_model = tf.keras.models.load_model('my_model.h5')

new_model.summary()
