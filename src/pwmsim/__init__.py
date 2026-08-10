"""Minimal pulse-width-modulation simulation helpers."""

from __future__ import annotations

from math import isfinite

__all__ = ["__version__", "pwm_state"]
__version__ = "0.0.1"


def pwm_state(
    time: float,
    frequency: float,
    duty_cycle: float,
    phase: float = 0.0,
) -> bool:
    """Return whether an ideal trailing-edge PWM signal is high.

    Args:
        time: Simulation time in seconds.
        frequency: Switching frequency in hertz; must be positive.
        duty_cycle: High-time fraction in the inclusive range ``[0, 1]``.
        phase: Phase offset in cycles.
    """
    values = (time, frequency, duty_cycle, phase)
    if not all(isfinite(value) for value in values):
        raise ValueError("time, frequency, duty_cycle, and phase must be finite")
    if frequency <= 0:
        raise ValueError("frequency must be positive")
    if not 0 <= duty_cycle <= 1:
        raise ValueError("duty_cycle must be between 0 and 1")
    if duty_cycle == 0:
        return False
    if duty_cycle == 1:
        return True
    position = (time * frequency + phase) % 1.0
    return position < duty_cycle
