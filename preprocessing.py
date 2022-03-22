import numpy as np
import pandas as pd
import os
import torch
import pickle
from torch.utils.data import TensorDataset, DataLoader
from sklearn.model_selection import train_test_split



# Hyper-parameters
num_epochs = 700
batch_size = 35
learning_rate = 0.001


class Data:

    def __init__(self):
        filehandler = open('dataset.pth', 'rb')
        data = pickle.load(filehandler)

        # surprise has been changed from 8 to 0
        self.classes = {0: 'surprise', 1: 'calm', 2: 'happy', 3: 'sad', 4: 'angry', 5: 'fear', 6: 'disgust'}
        self.num_of_classes = 7

        x_dataset = [embedding[1] for embedding in data]
        y_dataset = [label[2] for label in data]
        train_x, test_x, train_y, test_y = train_test_split(np.array(x_dataset), np.array(y_dataset), test_size = 0.30)
        train_x = torch.from_numpy(train_x)
        train_y = torch.from_numpy(train_y)
        torch_train = TensorDataset(train_x, train_y)

        test_x = torch.from_numpy(test_x)
        test_y = torch.from_numpy(test_y)
        torch_test = TensorDataset(test_x, test_y)

        self.train_loader = DataLoader(torch_train, batch_size = 28, drop_last = True, shuffle = True)
        self.test_loader = DataLoader(torch_test, batch_size = 28, drop_last = True, shuffle = False)

