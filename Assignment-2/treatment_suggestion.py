# Assignment 2 - Lina, Amelia, Liam, and Chris
'''
Strategy to find rate of optimal perscribing:
We compared the probability of recovery given the patient is of type
W = 0, and M = 0 and what drugs they were given. The greater one is the
preferred treatment.

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
    pred_a0 = exp_model.predict_proba({"M": "0", "W": "0", "X": "0"})[1].parameters[0].get("1")
    pred_b0 = exp_model.predict_proba({"M": "0", "W": "0", "X": "1"})[1].parameters[0].get("1")

    if (pred_a0 > pred_b0):
        print("Optimal treatment for a patient of type W = 0, M = 0 is (X = 0) with a probable rate of recovery of: ", pred_a0)
    else:
        print("Optimal treatment for a patient of type W = 0, M = 0 is (X = 1) with a probable rate of recovery of: : ",pred_b0)

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
