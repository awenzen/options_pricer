#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "BlackScholes.h" // Include our engine

namespace py = pybind11;

// This is the module definition
PYBIND11_MODULE(pricer_cpp, m) {
    m.doc() = "High-performance C++ options pricer"; // Optional module docstring

    // Bind the OptionGreeks struct
    py::class_<OptionGreeks>(m, "OptionGreeks")
        .def(py::init<>())
        .def_readwrite("call_price", &OptionGreeks::call_price)
        .def_readwrite("put_price", &OptionGreeks::put_price)
        .def_readwrite("call_delta", &OptionGreeks::call_delta)
        .def_readwrite("put_delta", &OptionGreeks::put_delta)
        .def_readwrite("gamma", &OptionGreeks::gamma)
        .def_readwrite("vega", &OptionGreeks::vega)
        .def_readwrite("call_theta", &OptionGreeks::call_theta)
        .def_readwrite("put_theta", &OptionGreeks::put_theta)
        .def("__repr__",
            [](const OptionGreeks &g) {
                return "<OptionGreeks: Call=" + std::to_string(g.call_price) +
                       ", Put=" + std::to_string(g.put_price) + ">";
            }
        );

    // Bind the main calculation function
    m.def(
        "calculate_greeks",
        &calculate_greeks,
        "Calculates Black-Scholes prices and greeks",
        py::arg("S"),
        py::arg("K"),
        py::arg("T"),
        py::arg("r"),
        py::arg("v")
    );
}