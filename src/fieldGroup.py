# -----------------------------
# Parameter Definitions
# -----------------------------
FIELD_GROUPS = {
    "Initial Stresses": {
        "sigma_v": "Vertical Stress (Psi)",
        "sigma_H": "Maximum Horizontal Stress (Psi)",
        "sigma_h": "Minimum Horizontal Stress (Psi)"
    },
    "Reservoir Pressures": {
        "p_i": "Initial Reservoir Pressure (Psi)",
        "p_res": "Current Reservoir Pressure (Psi)",
        "p_well": "Wellbore Pressure (Psi)"
    },
    "Rock Properties": {
        "theta": "Failure Angle (Degree)",
        "UCS": "UCS (Psi)"
    },
    "Time Settings": {
        "time_step": "Time Step (Second)",
        "until": "Until (Dimensionless)"
    },
    "Well Orientation": {
        "i": "Inclination (Degree)",
        "alpha": "Azimuth (Degree)"
    },
    "Elastic Properties": {
        "alphap": "Poroelastic Constant (Dimensionless)",
        "nu": "Poisson Ratio (Dimensionless)"
    },
    "Porosity": {
        "phi": "Porosity(Fraction)",
        "phi_c": "Critical Porosity (Fraction)"
    },
    "Permeability": {
        "k": "Permeability (Darcy)",
        "beta": "Sand Production Coefficient (Sec/m³)"
    },
    "Critical Pressures": {
        "p_crit_res": "Critical Reservoir Pressure (Psi)",
        "p_crit_well": "Critical Well Pressure (Psi)"
    },
    "Geometry": {
        "r_well": "Wellbore Radius (ft)",
        "r_ext": "External Radius (ft)",
        "h_res": "Reservoir Thickness (ft)",
        "rho_s": "Solid Density (Kg/m³)"
    },
    "Other Parameters": {
        "mu": "Viscosity (cP)",
        "COPR": "COPR (Dimensionless)",
        "ISP": "ISP (Kg)",
        "Failure Method": "Failure Method"
    }
}

# -----------------------------
# Utility Functions
# -----------------------------
def get_parameter(short_name):
    """Return the full field name for a short parameter name"""
    return FIELD_GROUPS.get(short_name, {}).get("full_name")

def get_parameter_unit(short_name):
    """Return the unit for a short parameter name"""
    return FIELD_GROUPS.get(short_name, {}).get("unit")

def get_parameter_info(short_name):
    """Return complete info (dict) for a parameter"""
    return FIELD_GROUPS.get(short_name)

def get_all_short_names():
    """Return all available short parameter names"""
    return list(FIELD_GROUPS.keys())

def validate_parameter_value(short_name, value):
    """Basic validation based on parameter type"""
    unit = get_parameter_unit(short_name)

    if unit == "Fraction" and not (0 <= value <= 1):
        return False, f"{short_name} should be between 0 and 1"
    elif unit == "Degree" and not (0 <= value <= 360):
        return False, f"{short_name} should be between 0 and 360 degrees"
    elif unit in ["Psi", "ft", "Kg/m³"] and value < 0:
        return False, f"{short_name} should be positive"

    return True, "Valid"


