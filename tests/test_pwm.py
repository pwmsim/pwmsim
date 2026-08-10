import math
import unittest

from pwmsim import __version__, pwm_state


class PWMStateTests(unittest.TestCase):
    def test_version(self):
        self.assertEqual(__version__, "0.0.1")

    def test_duty_cycle_edges(self):
        self.assertFalse(pwm_state(0.0, 100_000, 0.0))
        self.assertTrue(pwm_state(100.0, 100_000, 1.0))

    def test_trailing_edge_pwm(self):
        self.assertTrue(pwm_state(1e-6, 100_000, 0.25))
        self.assertFalse(pwm_state(3e-6, 100_000, 0.25))
        self.assertTrue(pwm_state(11e-6, 100_000, 0.25))

    def test_phase_is_measured_in_cycles(self):
        self.assertFalse(pwm_state(0.0, 1_000, 0.25, phase=0.5))
        self.assertTrue(pwm_state(0.0, 1_000, 0.25, phase=0.1))

    def test_invalid_values(self):
        for frequency in (0.0, -1.0):
            with self.assertRaises(ValueError):
                pwm_state(0.0, frequency, 0.5)
        for duty_cycle in (-0.1, 1.1):
            with self.assertRaises(ValueError):
                pwm_state(0.0, 1.0, duty_cycle)
        with self.assertRaises(ValueError):
            pwm_state(math.inf, 1.0, 0.5)


if __name__ == "__main__":
    unittest.main()
