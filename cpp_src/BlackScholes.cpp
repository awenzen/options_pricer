#include "BlackScholes.h"
#include <cmath>

// Define pi

// Helper function for the Cumulative Normal Distribution (CDF)
double cdf(double x) {
    return 0.5 * (1.0 + std::erf(x / std::sqrt(2.0)));
}

// Helper function for the Normal Probability Density (PDF)
double pdf(double x) {
    return (1.0 / std::sqrt(2.0 * M_PI)) * std::exp(-0.5 * x * x);
}

// Main calculation function
OptionGreeks calculate_greeks(
    const double S,
    const double K,
    const double T,
    const double r,
    const double v
) {
    OptionGreeks greeks;
    
    double v_sqrt_T = v * std::sqrt(T);
    double d1 = (std::log(S / K) + (r + 0.5 * v * v) * T) / v_sqrt_T;
    double d2 = d1 - v_sqrt_T;

    double exp_rT = std::exp(-r * T);

    // Calculate CDF and PDF values
    double n_d1 = cdf(d1);
    double n_d2 = cdf(d2);
    double n_neg_d1 = cdf(-d1);
    double n_neg_d2 = cdf(-d2);
    double pdf_d1 = pdf(d1);

    // --- Calculate Prices ---
    greeks.call_price = S * n_d1 - K * exp_rT * n_d2;
    greeks.put_price  = K * exp_rT * n_neg_d2 - S * n_neg_d1;

    // --- Calculate Greeks ---
    greeks.call_delta = n_d1;
    greeks.put_delta  = n_d1 - 1.0;
    greeks.gamma = pdf_d1 / (S * v_sqrt_T);
    greeks.vega = S * pdf_d1 * std::sqrt(T);
    greeks.call_theta = -(S * pdf_d1 * v) / (2 * std::sqrt(T)) - r * K * exp_rT * n_d2;
    greeks.put_theta  = -(S * pdf_d1 * v) / (2 * std::sqrt(T)) + r * K * exp_rT * n_neg_d2;
    
    return greeks;
}