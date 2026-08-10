# PWMSim

PWMSim is an early-stage Python package for pulse-width-modulation simulation.

## Install

```bash
pip install pwmsim
```

## Use

```python
from pwmsim import pwm_state

# A 100 kHz PWM signal at 25% duty cycle is high at t = 1 microsecond.
assert pwm_state(1e-6, frequency=100e3, duty_cycle=0.25)
```

`pwm_state()` accepts a time in seconds, frequency in hertz, duty cycle from
zero to one, and an optional phase offset measured in cycles.

This package is pre-alpha. Its API may change before version 1.0.
