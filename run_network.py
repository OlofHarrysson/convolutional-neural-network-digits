from mist_loader import load_data_wrapper
import sys
import numpy as np

training_data, validation_data, test_data = load_data_wrapper()

for image, digit in zip(training_data[0], training_data[1]):
    print(image)
    print(len(image))
    sys.exit(1)