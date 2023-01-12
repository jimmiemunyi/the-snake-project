# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_core.ipynb.

# %% auto 0
__all__ = ['ds_path', 'get_species']

# %% ../nbs/00_core.ipynb 4
from pandas import Series

# %% ../nbs/00_core.ipynb 7
ds_path = '../dataset/ai-crowd-snake-dataset/'

# %% ../nbs/00_core.ipynb 9
def get_species(
        row # pandas dataframe row.
    )->Series: # pandas dataframe series
    """Add a species column in the series"""
    _, species = row.binomial.split()
    return species