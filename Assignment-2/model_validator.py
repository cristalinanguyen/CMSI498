# Assignment 2 - Lina, Amelia, Liam, and Chris
''' 
Our strategy: We identified the backdoor admissable set as the variable "W". We didn't include "M" because there are
edges directing into "M" which creates a sink and blocks any spurious paths. The script performs a backdoor adjustment 
on the admissable set to get the causal effects of both drugs from both expirimental data and observational data.
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

    pred_a0 = exp_model.predict_proba({"X": "0", "W": "1"})[1].parameters[0].get("1")
    pred_b0 = exp_model.predict_proba({"W": "1"})[4].parameters[0].get('1')
    pred_c0 = exp_model.predict_proba({"X": "0", "W": "0"})[1].parameters[0].get("1")
    pred_d0 = exp_model.predict_proba({"W": "0"})[4].parameters[0].get('0')

    x_0 = (pred_a0 * pred_b0) + (pred_c0 * pred_d0)
    print("Experimental Data X = 0: " + str(x_0))


    pred_a1 = exp_model.predict_proba({"X": "1", "W": "1"})[1].parameters[0].get("1")
    pred_b1 = exp_model.predict_proba({"W": "1"})[4].parameters[0].get('1')
    pred_c1 = exp_model.predict_proba({"X": "1", "W": "0"})[1].parameters[0].get("1")
    pred_d1 = exp_model.predict_proba({"W": "0"})[4].parameters[0].get('0')

    x_1 = (pred_a1 * pred_b1) + (pred_c1 * pred_d1)
    print("Experimental Data X = 1: " + str(x_1))


    pred_a0 = obs_model.predict_proba({"X": "0", "W": "1"})[1].parameters[0].get("1")
    pred_b0 = obs_model.predict_proba({"W": "1"})[4].parameters[0].get('1')
    pred_c0 = obs_model.predict_proba({"X": "0", "W": "0"})[1].parameters[0].get("1")
    pred_d0 = obs_model.predict_proba({"W": "0"})[4].parameters[0].get('0')

    x_0 = (pred_a0 * pred_b0) + (pred_c0 * pred_d0)
    print("Observational Data X = 0: " + str(x_0))


    pred_a1 = obs_model.predict_proba({"X": "1", "W": "1"})[1].parameters[0].get("1")
    pred_b1 = obs_model.predict_proba({"W": "1"})[4].parameters[0].get('1')
    pred_c1 = obs_model.predict_proba({"X": "1", "W": "0"})[1].parameters[0].get("1")
    pred_d1 = obs_model.predict_proba({"W": "0"})[4].parameters[0].get('0')

    x_1 = (pred_a1 * pred_b1) + (pred_c1 * pred_d1)
    print("Observational Data X = 1: " + str(x_1))
