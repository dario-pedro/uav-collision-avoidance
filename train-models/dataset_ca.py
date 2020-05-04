from dataset import load_cached
import os


# Set common constants

######################### Cap Functions

# Directory where you want to download and save the data-set.
# Set this before you start calling any of the functions below.
data_dir = "data/images/"

# Directory for the training-set after copying the files using copy_files().
train_dir = os.path.join(data_dir, "train/")

# Directory for the test-set after copying the files using copy_files().
test_dir = os.path.join(data_dir, "test/")

# define width / height / deepth images target size
target_size = (198*3 , 108*3 , 3)

def load():
    """
    Load the Colission data-set into memory.

    This uses a cache-file which is reloaded if it already exists,
    otherwise the Knifey-Spoony data-set is created and saved to
    the cache-file. The reason for using a cache-file is that it
    ensure the files are ordered consistently each time the data-set
    is loaded. This is important when the data-set is used in
    combination with Transfer Learning as is done in Tutorial #09.

    :return:
        A DataSet-object for the Knifey-Spoony data-set.
    """

    # Path for the cache-file.
    cache_path = os.path.join(data_dir, "collisions.pkl")

    # If the DataSet-object already exists in a cache-file
    # then load it, otherwise create a new object and save
    # it to the cache-file so it can be loaded the next time.
    dataset = load_cached(cache_path=cache_path,
                          in_dir=data_dir)

    return dataset

def copy_files():
    """
    Copy all the files in the training-set to train_dir
    and copy all the files in the test-set to test_dir.

    This creates the directories if they don't already exist,
    and it overwrites the images if they already exist.

    The images are originally stored in a directory-structure
    that is incompatible with e.g. the Keras API. This function
    copies the files to a dir-structure that works with e.g. Keras.
    """

    # Load the Knifey-Spoony dataset.
    # This is very fast as it only gathers lists of the files
    # and does not actually load the images into memory.
    dataset = load()

    # Copy the files to separate training- and test-dirs.
    dataset.copy_files(train_dir=train_dir, test_dir=test_dir)
####################
#   START CODE
####################




# Load the data-set.
dataset = load()

#print(dataset.output_types)  # ==> "tf.float32"
#print(dataset.output_shapes)  # ==> "(10,)"

# Get the file-paths for the images and their associated class-numbers
# and class-labels. This is for the training-set.
image_paths_train, cls_train, labels_train = dataset.get_training_set()

# Get the file-paths for the images and their associated class-numbers
# and class-labels. This is for the test-set.
image_paths_test, cls_test, labels_test = dataset.get_test_set()

# Check if the training-set looks OK.

# Print some of the file-paths for the training-set.
for path in image_paths_train[0:5]:
    print(path)

# Print the associated class-numbers.
print(cls_train[0:5])

# Print the class-numbers as one-hot encoded arrays.
print(labels_train[0:5])

# Check if the test-set looks OK.

# Print some of the file-paths for the test-set.
for path in image_paths_test[0:5]:
    print(path)

# Print the associated class-numbers.
print(cls_test[0:5])

# Print the class-numbers as one-hot encoded arrays.
print(labels_test[0:5])