import numpy as np
import pandas as pd

np.random.seed(7)
N = 500

# CITYA
citya_elev = np.random.normal(loc=80, scale=30, size=N)
citya_price = np.random.normal(loc=1100, scale=180, size=N)
citya_sqft = np.random.normal(loc=900, scale=120, size=N)
citya_beds = np.random.randint(1, 5, size=N)


# CITYB
cityb_elev = np.random.normal(loc=50, scale=25, size=N)
cityb_price = np.random.normal(loc=950, scale=150, size=N)
cityb_sqft = np.random.normal(loc=800, scale=80, size=N)
cityb_beds = np.random.randint(1, 4, size=N)

df = pd.DataFrame(
    {
        "elevation": np.concatenate([citya_elev, cityb_elev]),
        "price": np.concatenate([citya_price, cityb_price]),
        "sqft": np.concatenate([citya_sqft, cityb_sqft]),
        "bedrooms": np.concatenate([citya_sqft, cityb_sqft]),
        "city": ["CITYA"] * N + ["CITYB"] * N,
    }
)
