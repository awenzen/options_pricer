import pricer_cpp
import time
import random
from collections import namedtuple

Contract = namedtuple('Contract', ['strike', 'time_to_expiry'])

STARTING_STOCK_PRICE = 200.0
VOLATILITY = 0.30
RISK_FREE_RATE = 0.05
NUM_CONTRACTS = 5_000
TIME_TICK_PER_LOOP = 0.0001

def generate_contracts(num):
    contracts = []
    for _ in range(num):
        strike = STARTING_STOCK_PRICE * random.uniform(0.7, 1.3)
        expiry = random.uniform(0.02, 2.0)
        contracts.append(Contract(strike, expiry))
    return contracts

def run_simulation():
    print(f"Generating {NUM_CONTRACTS} option contracts...")
    contracts = generate_contracts(NUM_CONTRACTS)
    print("Starting real-time simulation... (Press Ctrl+C to stop)")
    current_price = STARTING_STOCK_PRICE
    
    while True:
        try:
            price_change = random.uniform(-0.05, 0.05)
            current_price += price_change
            
            start_time = time.perf_counter()
            
            for i in range(len(contracts) - 1, -1, -1): # Iterate backwards to safely remove
                c = contracts[i]
                new_expiry = c.time_to_expiry - TIME_TICK_PER_LOOP
                
                if new_expiry <= 0:
                    contracts.pop(i) # Remove expired contract
                    continue
                
                contracts[i] = c._replace(time_to_expiry=new_expiry)

                greeks = pricer_cpp.calculate_greeks(
                    current_price, c.strike, new_expiry,
                    RISK_FREE_RATE, VOLATILITY
                )
                
            end_time = time.perf_counter()
            duration_ms = (end_time - start_time) * 1000
            
            print(f"Stock Price: ${current_price:,.2f} | "
                  f"Priced {len(contracts):,} contracts in {duration_ms:.2f} ms")
            
            time.sleep(0.05)

        except KeyboardInterrupt:
            print("\nSimulation stopped.")
            break

if __name__ == "__main__":
    run_simulation()