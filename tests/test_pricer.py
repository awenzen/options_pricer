import pytest
import pricer_cpp  # Import our C++ module!

def test_pricer_against_known_values():
    """
    Test values checked against online calculator:
    https://www.option-price.com/black-scholes.php
    Inputs: S=100, K=100, T=1.0, r=0.05, v=0.20
    """
    S, K, T, r, v = 100.0, 100.0, 1.0, 0.05, 0.20

    greeks = pricer_cpp.calculate_greeks(S, K, T, r, v)

    assert greeks.call_price == pytest.approx(10.45058, abs=1e-5)
    assert greeks.put_price  == pytest.approx(5.57353, abs=1e-5)
    assert greeks.call_delta == pytest.approx(0.63683, abs=1e-5)
    assert greeks.put_delta  == pytest.approx(-0.36317, abs=1e-5)
    assert greeks.gamma == pytest.approx(0.01876, abs=1e-5)
    assert greeks.vega  == pytest.approx(37.52403, abs=1e-5)
    assert greeks.call_theta == pytest.approx(-6.41403, abs=1e-5)
    assert greeks.put_theta  == pytest.approx(-1.65788, abs=1e-5)