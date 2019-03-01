# Assignment 2 - Lina, Amelia, Liam, and Chris
'''
Strategy to find rate of optimal perscribing:
We took the total number of patients of type W = 0, M = 0 and divided
it by the number of patients of that type which were perscribed an optimal
treatment. 
'''
import pandas as pd
import numpy as np
from pomegranate import *

class Naive_Bayes_Classifier:

    def __init__ (self, data_file):
        self.data_file = data_file
    exp_data = pd.read_csv("med_ex_exp.csv", header = None, delimiter = ' *, *', engine = 'python')
    obs_data = pd.read_csv("med_ex_obs.csv", header = None, delimiter = ' *, *', engine = 'python')

    exp_model = BayesianNetwork.from_samples(exp_data, state_names = ["X", "Z", "Y", "W", "M"])
    obs_model = BayesianNetwork.from_samples(obs_data, state_names = ["X", "Z", "Y", "W", "M"])


    M_0 = exp_data[3] == "0"
    W_0 = exp_data[4] == "0"
    X_1 = exp_data[0] == "1"

    MW_0f = exp_data[M_0]
    MW_0f = exp_data[W_0]

    num = MW_0f.shape[0]
    MW_0f = exp_data[X_1]
    den = MW_0f.shape[0]

    rate = num / den
    print("Rate at which doctors are teating patients optimally: ", rate)
