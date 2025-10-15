import math
from fieldGroup import FIELD_GROUPS  # or whatever your field data object is called

class StressInputs:
    """Store the input stresses and angles for the model."""
    def __init__(self, sigma_h, sigma_H, sigma_v, alpha, inclination):
        self.sigma_h = sigma_h  # minimum horizontal stress
        self.sigma_H = sigma_H  # maximum horizontal stress
        self.sigma_v = sigma_v  # vertical stress
        self.alpha = math.radians(alpha)  # convert degrees → radians
        self.i = math.radians(inclination)  # deviation (0 for vertical well)


class NormalStresses:
    """Compute the normal stress components."""
    def __init__(self, inputs: StressInputs):
        self.inp = inputs

    def sigma_xx(self):
        return ((self.inp.sigma_H * math.cos(self.inp.alpha) ** 2 +
                 self.inp.sigma_h * math.sin(self.inp.alpha) ** 2) * math.cos(self.inp.i) ** 2 +
                 self.inp.sigma_v * math.sin(self.inp.i) ** 2)

    def sigma_yy(self):
        return (self.inp.sigma_H * math.sin(self.inp.alpha) ** 2 +
                self.inp.sigma_h * math.cos(self.inp.alpha) ** 2)

    def sigma_z(self):
        return ((self.inp.sigma_H * math.cos(self.inp.alpha) ** 2 +
                 self.inp.sigma_h * math.sin(self.inp.alpha) ** 2) * math.sin(self.inp.i) ** 2 +
                 self.inp.sigma_v * math.cos(self.inp.i) ** 2)


class ShearStresses:
    """Compute the shear stress components."""
    def __init__(self, inputs: StressInputs):
        self.inp = inputs

    def tau_xy(self):
        return 0.5 * (self.inp.sigma_h - self.inp.sigma_H) * math.sin(2 * self.inp.alpha) * math.cos(self.inp.i)

    def tau_yz(self):
        return 0.5 * (self.inp.sigma_h - self.inp.sigma_H) * math.sin(2 * self.inp.alpha) * math.sin(self.inp.i)

    def tau_xz(self):
        return 0.5 * ((self.inp.sigma_H * math.cos(self.inp.alpha) ** 2 +
                       self.inp.sigma_h * math.sin(self.inp.alpha) ** 2 - self.inp.sigma_v) *
                      math.sin(2 * self.inp.i))


class SandProductionModel:
    """Combine stresses for prediction framework."""
    def __init__(self, sigma_h, sigma_H, sigma_v, alpha, inclination):
        self.inputs = StressInputs(sigma_h, sigma_H, sigma_v, alpha, inclination)
        self.normal = NormalStresses(self.inputs)
        self.shear = ShearStresses(self.inputs)

    def compute_all(self):
        return {
            "sigma_xx": self.normal.sigma_xx(),
            "sigma_yy": self.normal.sigma_yy(),
            "sigma_z": self.normal.sigma_z(),
            "tau_xy": self.shear.tau_xy(),
            "tau_yz": self.shear.tau_yz(),
            "tau_xz": self.shear.tau_xz()
        }
