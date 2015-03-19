'''
Created on 2015-03-19

https://class.coursera.org/principlescomputing1-002/assignment/part_results?part_id=12
'''

import simpleplot # @UnresolvedImport
import math
import random

# Used to increase the timeout, if necessary
import codeskulptor # @UnresolvedImport
codeskulptor.set_timeout(20)

import poc_clicker_provided as provided # @UnresolvedImport

# Constants
SIM_TIME = 10000000000.0

class ClickerState:
    """
    Simple class to keep track of the game state.
    """
    
    def __init__(self):
        """
        Initialize internal variables
        """
        self.__total_number_of_cookies = 0.0
        self.__current_number_of_cookies = 0.0
        self.__current_time = 0.0
        self._current_cps = 1.0
        self.__history_record = []
        self.__history_record.append((0.0, None, 0.0, 0.0))
        
    def __str__(self):
        """
        Return human readable state
        """
        return "".join(["\ntotal_number_of_cookies\n", str(self.__total_number_of_cookies), "\ncurrent_number_of_cookies\n", str(self.__current_number_of_cookies), "\ncurrent_time\n", str(self.__current_time), "\ncurrent_CPS\n", str(self._current_cps)])
        
    def get_cookies(self):
        """
        Return current number of cookies 
        (not total number of cookies)
        
        Should return a float
        """
        return self.__current_number_of_cookies
    
    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self._current_cps
    
    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self.__current_time
    
    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: [(0.0, None, 0.0, 0.0)]

        Should return a copy of any internal data structures,
        so that they will not be modified outside of the class.
        """
        return self.__history_record

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0.0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        if cookies < self.__current_number_of_cookies:
            return 0.0
        
        return math.ceil((cookies - self.__current_number_of_cookies) / self._current_cps)
    
    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0.0
        """
        if time > 0.0:
            self.__total_number_of_cookies += self._current_cps * time
            self.__current_number_of_cookies += self._current_cps * time
            self.__current_time += time
    
    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if cost <= self.__current_number_of_cookies:
            self.__current_number_of_cookies -= cost
            self._current_cps += additional_cps
            self.__history_record.append((self.__current_time, item_name, cost, self.__total_number_of_cookies))
    
def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """

    # Add until reaching the deadline
    items_info = build_info.clone()
    cookie_clicker = ClickerState()
    while cookie_clicker.get_time() < duration:
        item_name = strategy(cookie_clicker.get_cookies(), cookie_clicker.get_cps(), cookie_clicker.get_history(), duration - cookie_clicker.get_time(), items_info)
        if item_name is None:
            cookie_clicker.wait(duration - cookie_clicker.get_time())
        else:
            if (cookie_clicker.get_time() + cookie_clicker.time_until(items_info.get_cost(item_name))) <= duration:
                cookie_clicker.wait(cookie_clicker.time_until(items_info.get_cost(item_name)))               
                cookie_clicker.buy_item(item_name, items_info.get_cost(item_name), items_info.get_cps(item_name))
                items_info.update_item(item_name)
            else:
                cookie_clicker.wait(duration - cookie_clicker.get_time())
    # Can still add item .... -_-b
    while cookie_clicker.get_time() == duration:
        item_name = strategy(cookie_clicker.get_cookies(), cookie_clicker.get_cps(), cookie_clicker.get_history(), 0, items_info)
        if item_name == None:
            break
        else:
            if items_info.get_cost(item_name) <= cookie_clicker.get_cookies():
                cookie_clicker.buy_item(item_name, items_info.get_cost(item_name), items_info.get_cps(item_name))
                items_info.update_item(item_name)
            else:
                break
    return cookie_clicker

def strategy_cursor_broken(cookies, cps, history, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic (and broken) strategy does not properly
    check whether it can actually buy a Cursor in the time left.  Your
    simulate_clicker function must be able to deal with such broken
    strategies.  Further, your strategy functions must correctly check
    if you can buy the item in the time left and return None if you
    can't.
    """
    return "Cursor"

def strategy_none(cookies, cps, history, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that will never buy anything, but
    that you can use to help debug your simulate_clicker function.
    """
    return None

def strategy_cheap(cookies, cps, history, time_left, build_info):
    """
    Always buy the cheapest item you can afford in the time left.
    """
    min_cost = float('inf')
    min_item = None
    for item in build_info.build_items():
        if build_info.get_cost(item) < min_cost:
            min_cost = build_info.get_cost(item)
            min_item = item
    if min_cost <= cookies + cps * time_left:
        return min_item
    else:
        return None

def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    max_cost = float('-inf')
    max_item = None
    for item in build_info.build_items():
        if (build_info.get_cost(item) > max_cost) and (build_info.get_cost(item) <= cookies + cps * time_left):
            max_cost = build_info.get_cost(item)
            max_item = item
    return max_item

def build_history_record(history):
    """
    Helper function to build a dict containing items and occurrence
    """
    history_record = dict()
    for tup in history:
        if tup[1] is not None:
            if tup[1] not in history_record:
                history_record[tup[1]] = 1.0
            else:
                history_record[tup[1]] += 1.0
    return history_record

def strategy_best(cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    """
    # Get basic data
    # weight_dict = {'Cursor' : 0.12, 'Grandma' : 0.12, 'Farm' : 0.11, 'Factory' : 0.11, 'Mine' : 0.11, 'Shipment' : 0.10, 'Alchemy Lab' : 0.10, 'Portal' : 0.09, 'Time Machine' : 0.07, 'Antimatter Condenser' : 0.07}
    history_record = build_history_record(history)
    valid_items = []
    for item in build_info.build_items():
        if build_info.get_cost(item) <= cookies + cps * time_left:
            valid_items.append(item)
    # Get uniform distribution first
    if len(history_record) < len(build_info.build_items()):
        for item in valid_items:
            if item not in history_record:
                return item
    else:
        # At least we have one item for every category
        candidate_list = []
        history_len = float(len(history) - 1)
        # Try to achieve uniform
        for item in valid_items:
            if round((history_record[item] / history_len), 2) <= round((float(1) / float(len(build_info.build_items()))), 2):
                candidate_list.append(item)
        if len(candidate_list) == 1:
            return candidate_list[0]
        elif len(candidate_list) > 1:
            return random.choice(candidate_list)
    return None

def strategy_random(cookies, cps, history, time_left, build_info):
    """
    The random selection strategy that you are able to implement. 
    With Weight
    """
    weight_dict = {'Cursor' : 11, 'Grandma' : 11, 'Farm' : 11, 'Factory' : 11, 'Mine' : 11, 'Shipment' : 10, 'Alchemy Lab' : 10, 'Portal' : 9, 'Time Machine' : 8, 'Antimatter Condenser' : 8}
    weight = 0
    candidate_with_weight = []
    for item in build_info.build_items():
        if build_info.get_cost(item) <= cookies + cps * time_left:
            weight += weight_dict[item]
            candidate_with_weight.append((weight, item))
    if len(candidate_with_weight) == 0:
        return None
    seed = random.randrange(0, weight)
    for tup in candidate_with_weight:
        if seed <= tup[0]:
            return tup[1]      
        
def strategy_greedy(cookies, cps, history, time_left, build_info):
    """
    The greedy strategy that you are able to implement.
    """
    # Get all feasible items
    potential_item_candidate = dict()
    for item in build_info.build_items():
        if build_info.get_cost(item) <= cookies + cps * time_left:
            potential_item_candidate[item] = build_info.get_cost(item)   
    # Get the one with the max potential
    max_earnings = float('-inf')
    target_item = None   
    for feasible_item in potential_item_candidate.keys():
        earnings = 0.0
        # Can buy immediately
        if cookies >= potential_item_candidate[feasible_item]:
            earnings = time_left * (cps + build_info.get_cps(feasible_item))
        else:
            wait_period = math.ceil((potential_item_candidate[feasible_item] - cookies) / cps)
            earnings = (potential_item_candidate[feasible_item] - cookies) + (time_left - wait_period) * (cps + build_info.get_cps(feasible_item))
        if earnings > max_earnings:
            max_earnings = earnings
            target_item = feasible_item
    return target_item
       
def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation for the given time with one strategy.
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print(strategy_name, ":", state)

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    history = state.get_history()
    # history = [(item[0], item[3]) for item in history]
    # simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)
    
    record = dict()
    for tup in history:
        if tup[1] is not None:
            if tup[1] not in record:
                record[tup[1]] = 1
            else:
                record[tup[1]] += 1
    for key in record.keys():
        print(key)
        print(record[key])
        print(float(record[key])/float(len(history)))
        
def run():
    """
    Run the simulator.
    """    
    # run_strategy("Cursor", SIM_TIME, strategy_cursor_broken)

    # Add calls to run_strategy to run additional strategies
    # run_strategy("Cheap", SIM_TIME, strategy_cheap)
    # run_strategy("Expensive", SIM_TIME, strategy_expensive)
    run_strategy("Best", SIM_TIME, strategy_best)
    
run()

if __name__ == '__main__':
    pass