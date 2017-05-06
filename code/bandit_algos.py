from __future__ import division
import numpy as np
import pandas as pd
import math

class adversary(object):
    '''Generate losses for our algorithms '''
    def __init__(self, flag, k=10):
        self.gen_scheme = flag
        self.n_arms = k

    def generate_loss(self):
        return np.random.randint(0, self.n_arms)
        
        
        

class exp3(object):
    '''The exp3 algorithm for adversarial bandits'''
    def __init__(self, eta=.1, k=10):
        self.n_arms = k
        self.eta = eta 
        self.loss_estimates = []
        self.weights = [1] * self.n_arms
        self.policy = [0] * k
                
    def pull_arm(self):
        '''request losses for an arm '''
        #Update our probabilities
        weight_sum = np.sum(self.weights)

        for i, probability in enumerate(policy):
            policy[i] = ((1 - eta) * (self.weights[i]/ denom)) + eta / self.n_arms
        
        sampled_arm = np.random.choice(numpy.arange(1, self.n_arms), p = self.policy)
        
        return sampled_arm
    
    def recieve_loss(self, loss_i, arm_i):
        estimated_reward = loss_i / self.policy[arm_i]
        w_prev = self.weights[arm_i]
        w_new = w_prev * math.exp((self.eta * estimated_reward) / self.n_arms)

        self.weights[arm_i] = w_new
    
        

class simulation():
    def __init__(self, algo_flag='exp3', adversary_flag='unif',  n_rounds=10):
        if algo_flag == 'exp3':
            self.algo = exp3();
        self.adversary = adversary(adversary_flag)
        self.n_rounds = n_rounds

    def run_simulation(self):
        for t in range(len(nrounds)):
            arm_i = self.algo.pull_arm()
            loss_i = self.adversary.get_loss(arm_i)
            self.algo.recieve_loss(loss_i)
            



def main():
    sim = simulation()
    print("done")


if __name__ == "__main__":
    main()
    
    
            


    



    
    
        
