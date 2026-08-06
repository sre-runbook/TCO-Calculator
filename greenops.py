def calculate_co2(power_kwh, carbon_intensity_g):
    """
    Berekent de totale CO2-uitstoot in kilogram.
    """
    total_grams = power_kwh * carbon_intensity_g
    total_kg = total_grams / 1000
    
    return total_kg
