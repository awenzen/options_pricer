#pragma once
#include <string>

// A struct to hold all our calculated values.
struct OptionGreeks {
    double call_price;
    double put_price;
    double call_delta;
    double put_delta;
    double gamma;
    double vega;
    double call_theta;
    double put_theta;
};

/**
 * Calculates the theoretical prices and Greeks for a European option
 */
OptionGreeks calculate_greeks(
    const double S, // Stock Price
    const double K, // Strike Price
    const double T, // Time to Expiry (Years)
    const double r, // Risk-free Rate
    const double v  // Volatility
);