import os
import tensorflow as tf
# Filtering out corrupt files. 
num_skipped = 0
for fname in os.listdir("Dataset_Maker/downloads/fish(kaggle)/Fish_Data/images/raw_images"):
    fpath = os.path.join("Dataset_Maker/downloads/fish(kaggle)/Fish_Data/images/raw_images", fname)
    try:
        fobj = open(fpath, "rb")
        is_jfif = tf.compat.as_bytes("JFIF") in fobj.peek(10)
    finally:
        fobj.close()
    if not is_jfif:
        num_skipped += 1
        # Delete corrupted image
        os.remove(fpath)
print("Deleted %d fish images" % num_skipped)
num_skipped = 0
for fname in os.listdir("Dataset_Maker/downloads/people(kaggle)/images"):
    fpath = os.path.join("Dataset_Maker/downloads/people(kaggle)/images", fname)
    try:
        fobj = open(fpath, "rb")
        is_jfif = tf.compat.as_bytes("JFIF") in fobj.peek(10)
    finally:
        fobj.close()
    if not is_jfif:
        num_skipped += 1
        # Delete corrupted image
        os.remove(fpath)
print("Deleted %d people images" % num_skipped)