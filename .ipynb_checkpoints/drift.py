import matplotlib.pyplot as plt
import numpy as np
import math


class GBM:

    def simulate(self):
        while(self.total_time > 0):
            dS = self.current_price*self.drift*self.time_period + self.current_price*self.volatility*np.random.normal(0, math.sqrt(self.time_period))
            self.prices.append(self.current_price + dS)
            self.current_price += dS
            self.total_time -= self.time_period

    def __init__(self, initial_price, drift, volatility, time_period, total_time):
        # Initialize fields
        self.initial_price = initial_price
        self.current_price = initial_price
        self.drift = drift
        self.volatility = volatility
        self.time_period = time_period
        self.total_time = total_time
        self.prices = []
        # Simulate the diffusion process
        self.simulate()   # Simulate the diffusion proces

simulations = []
n = 10
initial_price = 500
drift = .24
volatility = .4
time_period = 1/365 # Daily
total_time = 1

for i in range(0, n):
    simulations.append(GBM(initial_price, drift, volatility, time_period, total_time))

for sim in simulations:
    plt.plot(np.arange(0, len(sim.prices)), sim.prices)

plt.show()