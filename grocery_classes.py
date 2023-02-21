class Customer:
    
    def __init__(self, name: str, n: int, vessel: str):
        self.name = name
        self.items = n
        if vessel in ["cart", "basket"]:
            self.vessel = vessel
        else:
            raise ValueError("`vessel` must be one of 'cart' or 'basket'")

    def join_register(self, register):
        register.line_length += 1
        register.items += self.items
        register.vessel.append(self.vessel)
        register.customers.append(self.name)

class Cashier:
    def __init__(self, speed: int):
        """A Cashier instance

        Args:
            speed (int): number of items the cashier can process in a minute
        """
        self.speed = speed

class Register:
    
    bagger_multiplier = 1.5

    def __init__(self, index: int, cashier, bagger: bool):
        """A Register instance

        Args:
            index (int): unique identifier
            cashier (Cashier): instance of class Cashier
            bagger (bool): whether register includes a bagger
        """
        self.index = index
        # ! New register always has 0 items, 0 customers in line, and is active
        self.items = 0
        self.line_length = 0
        self.customers = []
        self.vessel = []
        self.active = True
    
        # ! A cashier is required when a register is opened
        if cashier is None:
            self.cashier = None
        else:
            self.cashier = cashier
        # A bagger is optional (you can always add one later with add_bagger())
            self.bagger = bagger
        # If a bagger is added, checkout speed increases
            if bagger:
                self.speed = cashier.speed * self.bagger_multiplier
            else:
                self.speed = cashier.speed

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False
    
    def add_bagger(self):
    # TODO: since baggers are just normal employees, add: check Store has enough employees free
        self.bagger = True
        self.speed = self.speed * self.bagger_multiplier

class Store:
    
    def __init__(self, n_registers: int, employees: int):
        
        registers = []
        free_employees = employees

        for i in range(n_registers):
            if free_employees <= 0:
                current_register = Register(index=i, cashier=None, bagger=False)
                current_register.deactivate()
                registers.append(current_register)

            else:
                cashier = Cashier(np.random.normal(30, 5))
                current_register = Register(index=i, cashier = cashier, bagger = False)
                registers.append(current_register)
            
            free_employees -= 1
        self.registers = registers