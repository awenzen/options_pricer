import pricer_cpp
import time
import random

# --- Benchmark Parameters ---
NUM_CONTRACTS = 1_000_000  # Price ONE MILLION contracts
S = 100.0
K = 100.0
T = 1.0
r = 0.05
v = 0.20
# ----------------------------

def run_benchmark():
    print(f"Preparing to price {NUM_CONTRACTS:,} contracts...")
    
    # Create a list of 1M identical contracts
    inputs = []
    for _ in range(NUM_CONTRACTS):
        inputs.append((S, K, T, r, v))
        
    print("Starting benchmark...")
    start_time = time.perf_counter()
    
    # --- THE HOT LOOP ---
    # Run all 1M calculations
    for params in inputs:
        greeks = pricer_cpp.calculate_greeks(
            params[0], params[1], params[2], params[3], params[4]
        )
    # --- END HOT LOOP ---
    
    end_time = time.perf_counter()
    
    total_time = end_time - start_time
    options_per_sec = NUM_CONTRACTS / total_time
    
    print("\n--- Benchmark Complete ---")
    print(f"Total time: {total_time:.4f} seconds")
    print(f"Total options priced: {NUM_CONTRACTS:,}")
    print(f"OPTIONS PER SECOND: {options_per_sec:,.0f}")
    print("--------------------------")

if __name__ == "__main__":
    run_benchmark()