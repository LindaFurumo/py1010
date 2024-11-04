# -*- coding: utf-8 -*-
"""
# Arbeidskrav 1
## Kostnadsdifferanse mellom elbil og bensinbil

Created on Mon Nov  4 08:22:40 2024

@author: lindafurumo
"""

# Antall kjorte kilometer per ar
km_per_ar = 10000

# Forsikring og trafikkforsikringsavgift
forsikring_elbil = 5000       # Arlig forsikring for elbil
forsikring_bensinbil = 7500   # Arlig forsikring for bensinbil
trafikkforsikringsavgift = 8.38 * 365  # Arlig trafikkforsikringsavgift

# Kostnader per km
kost_elbil_per_km = 0.2 * 2.00 + 0.1  # Elbil: drivstoff og bom
kost_bensin_per_km = 1.0 + 0.3        # Bensinbil: drivstoff og bom

# Totalkostnader per ar
kost_elbil = forsikring_elbil + trafikkforsikringsavgift + (kost_elbil_per_km * km_per_ar)
kost_bensinbil = forsikring_bensinbil + trafikkforsikringsavgift + (kost_bensin_per_km * km_per_ar)

# Kostnadsdifferanse
differanse = kost_bensinbil - kost_elbil

# Resultater
print("Arlige totalkostnader for elbil:", kost_elbil, "kr")
print("Arlige totalkostnader for bensinbil:", kost_bensinbil, "kr")
print("Arlig kostnadsdifferanse (bensinbil - elbil):", differanse, "kr")