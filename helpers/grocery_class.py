import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
import uuid

from scipy.stats import skewnorm
import grocery_fns

# Customer 

class Customer:
    
    def __init__(self, store):
        
        self.store = store
        self.register = None
        self.name = uuid.uuid1().hex
        self.items = sample_skew(size=1)
        self.position = random.randint(0, store.n_registers)
        self.vessel = random.choice(["cart", "basket"])

    def register_attributes(self):
        
        active_registers = [reg for reg in self.store.registers if reg.active]

        # DISTANCE IS RELATIVE TO CUSTOMER
        distance_arr = np.array([np.abs(self.position - reg.index) for reg in active_registers]) 
        distance_arr = norm_array(1/(distance_arr+0.1))

        #cart_basket_arr = np.array([reg.vessel for reg in self.store.registers])

        line_arr = np.array([reg.line_length for reg in active_registers])
        line_arr = norm_array(1/(line_arr+0.1))

        item_arr = np.array([reg.items for reg in active_registers])
        item_arr = norm_array(1/(item_arr+0.1))

        speed_arr = np.array([reg.cashier.speed for reg in active_registers])
        speed_arr = norm_array(speed_arr)

        return np.column_stack((distance_arr, line_arr, item_arr, speed_arr))

    def ability_weight(self, attr_matrix):
        
        # TODO: design ability vector (i.e., each distribution) 
        attr_matrix += np.random.normal(0, 0.1, 4)
        #               dist, line, items, speed

        # TODO: design weights vector 
        weighted_attrs = np.multiply(attr_matrix, np.random.normal(1, 0.2, 4))
        
        return weighted_attrs
    
    def register_scores(self, weighted_attrs):
        # Sum up attribute values by 
        return np.sum(weighted_attrs, axis=1)

    def choose_register(self, verbose=True):
        
        active_registers = [reg for reg in self.store.registers if reg.active]
        attr_matrix = self.register_attributes()

        weighted_attrs = self.ability_weight(attr_matrix)

        summed = self.register_scores(weighted_attrs)
        chosen_register = np.argmax(summed)
        
        # Join chosen register
        register = active_registers[chosen_register]

        register.line_length += 1
        register.items += self.items
        register.vessel.append(self.vessel)
        register.customers.append(self.name)
        self.register = register
        if verbose: return chosen_register