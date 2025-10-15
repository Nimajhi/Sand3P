# -----------------------------
# Parameter Definitions
# -----------------------------
FIELD_GROUPS = {
    "Initial Stresses": {
        "fields": {
            "sigma_v": {"full_name": "Vertical Stress", "unit": "Psi"},
            "sigma_H": {"full_name": "Maximum Horizontal Stress", "unit": "Psi"},
            "sigma_h": {"full_name": "Minimum Horizontal Stress", "unit": "Psi"}
        }
    },
    "Reservoir Pressures": {
        "fields": {
            "p_i": {"full_name": "Initial Reservoir Pressure", "unit": "Psi"},
            "p_res": {"full_name": "Current Reservoir Pressure", "unit": "Psi"},
            "p_well": {"full_name": "Wellbore Pressure", "unit": "Psi"}
        }
    },
    "Rock Properties": {
        "fields": {
            "theta": {"full_name": "Failure Angle", "unit": "Degree"},
            "UCS": {"full_name": "UCS", "unit": "Psi"}
        }
    },
    "Time Settings": {
        "fields": {
            "time_step": {"full_name": "Time Step", "unit": "Second"},
            "until": {"full_name": "Until", "unit": "Dimensionless"}
        }
    },
    "Well Orientation": {
        "fields": {
            "i": {"full_name": "Inclination", "unit": "Degree"},
            "alpha": {"full_name": "Azimuth", "unit": "Degree"}
        }
    },
    "Elastic Properties": {
        "fields": {
            "alphap": {"full_name": "Poroelastic Constant", "unit": "Dimensionless"},
            "nu": {"full_name": "Poisson Ratio", "unit": "Dimensionless"}
        }
    },
    "Porosity": {
        "fields": {
            "phi": {"full_name": "Porosity", "unit": "Fraction"},
            "phi_c": {"full_name": "Critical Porosity", "unit": "Fraction"}
        }
    },
    "Permeability": {
        "fields": {
            "k": {"full_name": "Permeability", "unit": "Darcy"},
            "beta": {"full_name": "Sand Production Coefficient", "unit": "Sec/m³"}
        }
    },
    "Critical Pressures": {
        "fields": {
            "p_crit_res": {"full_name": "Critical Reservoir Pressure", "unit": "Psi"},
            "p_crit_well": {"full_name": "Critical Well Pressure", "unit": "Psi"}
        }
    },
    "Geometry": {
        "fields": {
            "r_well": {"full_name": "Wellbore Radius", "unit": "ft"},
            "r_ext": {"full_name": "External Radius", "unit": "ft"},
            "h_res": {"full_name": "Reservoir Thickness", "unit": "ft"},
            "rho_s": {"full_name": "Solid Density", "unit": "Kg/m³"}
        }
    },
    "Other Parameters": {
        "fields": {
            "mu": {"full_name": "Viscosity", "unit": "cP"},
            "COPR": {"full_name": "COPR", "unit": "Dimensionless"},
            "ISP": {"full_name": "ISP", "unit": "Kg"},
            "failure_method": {"full_name": "Failure Method", "unit": ""}
        }
    }
}

# -----------------------------
# Utility Functions
# -----------------------------
def get_parameter_full_name(short_name):
    """Return the full field name for a short parameter name"""
    for group_name, group_data in FIELD_GROUPS.items():
        fields = group_data.get("fields", {})
        if short_name in fields:
            return fields[short_name]["full_name"]
    return None

def get_parameter_unit(short_name):
    """Return the unit for a short parameter name"""
    for group_name, group_data in FIELD_GROUPS.items():
        fields = group_data.get("fields", {})
        if short_name in fields:
            return fields[short_name]["unit"]
    return None

def get_all_short_names():
    """Return all available short parameter names"""
    short_names = []
    for group_name, group_data in FIELD_GROUPS.items():
        fields = group_data.get("fields", {})
        short_names.extend(fields.keys())
    return short_names

def validate_parameter_value(short_name, value):
    """Basic validation based on parameter type"""
    unit = get_parameter_unit(short_name)

    if unit == "Fraction" and not (0 <= float(value) <= 1):
        return False, f"{short_name} should be between 0 and 1"
    elif unit == "Degree" and not (0 <= float(value) <= 360):
        return False, f"{short_name} should be between 0 and 360 degrees"
    elif unit in ["Psi", "ft", "Kg/m³", "Darcy", "cP", "Second"] and float(value) < 0:
        return False, f"{short_name} should be positive"

    return True, "Valid"
