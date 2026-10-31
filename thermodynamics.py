import math

from constants import (
    R,
    DELTA_H_RXN,
    T_REF,
    KP_REF,
)

def calculate_kp(temperature_k):
    """Estimates Kp using the van 't Hoff equation."""

    if temperature_k <= 0:
        raise ValueError("Temperature must be positive Kelvin.")

    exponent = (-DELTA_H_RXN / R) * (1 / temperature_k - 1 / T_REF)

    return KP_REF * math.exp(exponent)
