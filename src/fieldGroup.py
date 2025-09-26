#Field to use 
FIELD_GROUPS = {
    "Initial Stresses": {
        "Vertical Stress": "Psi",
        "Maximum Horizontal Stress": "Psi",
        "Minimum Horizontal Stress": "Psi"
    },
    "Reservoir Pressures": {
        "Initial Reservoir Pressure": "Psi",
        "Current Reservoir Pressure": "Psi",
        "Wellbore Pressure": "Psi"
    },
    "Rock Properties": {
        "Failure Angle": "Degree",
        "UCS": "Psi"
    },
    "Time Settings": {
        "Time Step": "Second",
        "Until": "Dimensionless"
    },
    "Well Orientation": {
        "Inclination": "Degree",
        "Azimuth": "Degree"
    },
    "Elastic Properties": {
        "Poroelastic Constant": "Dimensionless",
        "Poisson Ratio": "Dimensionless"
    },
    "Porosity": {
        "Porosity": "Fraction",
        "Critical Porosity": "Fraction"
    },
    "Permeability": {
        "Permeability": "Darcy",
        "Sand Production Coefficient": "Sec/m³"
    },
    "Critical Pressures": {
        "Critical Reservoir Pressure": "Psi",
        "Critical Well Pressure": "Psi"
    },
    "Geometry": {
        "Wellbore Radius": "ft",
        "External Radius": "ft",
        "Reservoir Thickness": "ft",
        "Solid Density": "Kg/m³"
    },
    "Other Parameters": {
        "Viscosity": "cP",
        "COPR": "Dimensionless",
        "ISP": "Kg",
        "Failure Method": "-"
    },
}

# You can also add helper functions
def get_all_field_names():
    """Return a flat list of all field names"""
    all_fields = []
    for group in FIELD_GROUPS.values():
        all_fields.extend(group.keys())
    return all_fields

def get_field_unit(field_name):
    """Get the unit for a specific field"""
    for group in FIELD_GROUPS.values():
        if field_name in group:
            return group[field_name]
    return None