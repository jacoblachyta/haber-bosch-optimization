from constants import (
    N_N2_FEED,
    N_H2_FEED,
    N_NH3_FEED,
)

def calculate_moles(extent):
    """Calculate ending mole amounts from reaction extent."""

    if not 0 <= extent <= 1:
        raise ValueError("Extent must be between 0 and 1.")

    n_n2 = N_N2_FEED - extent
    n_h2 = N_H2_FEED - 3 * extent
    n_nh3 = N_NH3_FEED + 2 * extent

    n_total = n_n2 + n_h2 + n_nh3

    return {
        "N2": n_n2,
        "H2": n_h2,
        "NH3": n_nh3,
        "Total": n_total,
    }
