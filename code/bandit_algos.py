from __future__ import division
import numpy as np
import pandas as pd
import math
import random

#Uses ideas and some code from https://jeremykun.com/2013/11/08/adversarial-bandits-and-the-exp3-algorithm/

class adversary(object):
    '''Generate losses for our algorithms '''
    def __init__(self, n_rounds, flag, k=10,):
        self.gen_scheme = flag
        self.n_arms = k
        self.n_rounds = n_rounds
        self.biases = [1.0 / k for k in range(2,12)]
        self.rewardVector = [[1 if random.random() <self. bias else 0 for self.bias in self.biases] for _ in range(n_rounds)]

        
    def generate_loss(self, arm_i):
        return np.random.randint(0, self.n_arms)
     

    def return_best_action(self, time_step):
        best_act = max(
            range(self.n_rounds), key=lambda action: sum(
                [self.rewardVector[time_step][action] for t in range(self.n_rounds)]))
        return self.rewardVector[time_step][best_act]
        
        

class exp3(object):
    '''The exp3 algorithm for adversarial bandits'''
    def __init__(self, n_rounds,  eta=.1, k=10,  res_size = 100):
        self.n_arms = k
        self.eta = eta 
        self.loss_estimates = []
        self.weights = [1] * self.n_arms
        self.policy = [0] * k
        self.resevoir = np.array([[-1]*res_size]*k)
        self.n_rounds = n_rounds
        self.cum_loss = 0
        self.best_loss = 0 
        self.regret = []
     
    def add_to_resevoir(k, reward):
        if random.random() < 1.0 / self.n_rounds:
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
    
    def recieve_loss(self, loss_i, arm_i, best_loss):
        self.best_loss += best_loss
        self.cum_loss += loss_i
        self.regret.append(self.cum_loss - self.best_loss)
        estimated_reward = loss_i / self.policy[arm_i]
        w_prev = self.weights[arm_i]
        w_new = w_prev * math.exp((self.eta * estimated_reward) / self.n_arms)
        
        self.weights[arm_i] = w_new
    
        

class simulation():
    def __init__(self, algo_flag='exp3', adversary_flag='unif',  n_rounds=10):
        if algo_flag == 'exp3':
            self.algo = exp3(n_rounds = n_rounds);
        self.adversary = adversary(n_rounds, flag = adversary_flag)
        self.n_rounds = n_rounds

    def run_simulation(self):
        for t in range(self.n_rounds):
            arm_i = self.algo.pull_arm()
            loss_i = self.adversary.generate_loss(arm_i)
            best_loss = self.adversary.return_best_action(t)
            self.algo.recieve_loss(loss_i, arm_i, best_loss)
            



def main():
    sim = simulation()
    sim.run_simulation()



if __name__ == "__main__":
    main()
    
    
            


    



    
    
        
