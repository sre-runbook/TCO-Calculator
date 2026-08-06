import pytest
from greenops import calculate_co2

def test_calculate_co2_basic():
    # Arrange: Testdata staat klaar
    power_kwh = 100
    carbon_intensity_g = 200
    
    # Act: De functie aanroepen
    result = calculate_co2(power_kwh, carbon_intensity_g)
    
    # Assert: Controleren van de uitkomst
    assert result == 20.0
