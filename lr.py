import warnings
warnings.simplefilter('ignore')
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression




# load model

survey_data_df = pd.read_csv('class_survey.csv')

survey_data_df.head()

model = joblib.load("HR_LRmodel_trained.h5")



