from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split,cross_val_score
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
pl2122 = pd.read_csv("C:/Users/HP/Downloads/p21-22.csv")
pl2223 = pd.read_csv("C:/Users/HP/Downloads/p22-23.csv")
pl2324 = pd.read_csv("C:/Users/HP/Downloads/p23-24.csv")
print(pl2122.info())
print(pl2223.info())
print(pl2324.info())




