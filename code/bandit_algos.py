from __future__ import division
import numpy as np
import pandas as pd
import math
import random

class adversary(object):
    '''Generate losses for our algorithms '''
    def __init__(self, flag, k=10):
        self.gen_scheme = flag
        self.n_arms = k

    def generate_loss(self, arm_i):
        return np.random.randint(0, self.n_arms)
        
        
        

class exp3(object):
    '''The exp3 algorithm for adversarial bandits'''
    def __init__(self, n_rounds,  eta=.1, k=10,  res_size = 100):
        self.n_arms = k
        self.eta = eta 
        self.loss_estimates = []
        self.weights = [1] * self.n_arms
        self.policy = [0] * k
        self.resevoir = np.array([[-1]*res_size]*k)
        self.T = n_rounds
     
    def add_to_resevoir(k, reward):
        if random.random() < 1.0 / self.T:
            if -1 in self.resevoir[k]:
                pos = self.resevoir[k].index(-1)
            else:
                pos = np.random.randint((0, self.n_arms))

            self.resevoir[pos] = reward

    def pull_arm(self):
        '''request losses for an arm '''
        #Update our probabilities
        weight_sum = np.sum(self.weights)

        for i, probability in enumerate(self.policy):
            self.policy[i] = ((1 - self.eta) * (self.weights[i]/ weight_sum)) + self.eta / self.n_arms
        
        sampled_arm = np.random.choice(np.arange(0, self.n_arms), p = self.policy)
        
        return sampled_arm
    
    def recieve_loss(self, loss_i, arm_i):
        estimated_reward = loss_i / self.policy[arm_i]
        w_prev = self.weights[arm_i]
        w_new = w_prev * math.exp((self.eta * estimated_reward) / self.n_arms)
        
        self.weights[arm_i] = w_new
    
        

class simulation():
    def __init__(self, algo_flag='exp3', adversary_flag='unif',  n_rounds=10):
        if algo_flag == 'exp3':
            self.algo = exp3(n_rounds = n_rounds);
        self.adversary = adversary(adversary_flag)
        self.n_rounds = n_rounds

    def run_simulation(self):
        for t in range(self.n_rounds):
            arm_i = self.algo.pull_arm()
            loss_i = self.adversary.generate_loss(arm_i)
            self.algo.recieve_loss(loss_i, arm_i)
            



def main():
    sim = simulation()
    sim.run_simulation()



if __name__ == "__main__":
    main()
    
    
            


    



    
    
        
