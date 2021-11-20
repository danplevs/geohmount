"""Helper functions to read and wrangle data."""
import json
from pathlib import Path
import pandas as pd

def read_inventory(sheet="Rio", version=7):
    """Return a specific sheet and version of the inventory."""
    config_file = Path("config.json")

    with config_file.open(mode="r", encoding="utf-8") as config:
        inventory_path = json.load(config)["inventory_path"]

    inventory_path = inventory_path.replace("$", str(version))
    data_file = Path(inventory_path)
    inventory = pd.read_excel(data_file, sheet_name=sheet)
    return inventory


def manipulate_data(inventory, subset_cols=None):
    """Return a cleaned dataset."""
    if subset_cols is None:
        subset_cols = [
            "Amostra",
            "Ponto",
            "H+",
            "Condutividade",
            "Vazao",
            "Temperatura",
            "Na_CI",
            "NH4_CI",
            "K_CI",
            "Mg_CI",
            "Ca_CI",
            "F",
            "Cl",
            "NO2_CI",
            "Br",
            "NO3_CI",
            "SO4",
            "NID_CI",
            "PO4_ESP",
            "HCO3_AUTO",
            "Si",
            "Fe",
            "Al",
            ]

    corr_dataframe = inventory.drop([19, 43]).drop(inventory.index[66:74])
    corr_dataframe = (corr_dataframe.loc[:, subset_cols])
    corr_dataframe.columns = corr_dataframe.columns.str.replace("(_).*", "", regex=True)

    return corr_dataframe

def split_data(dataframe, split_column='Ponto', stations=("BM", "SB", "SM")) -> tuple:
    """Split the dataframe according to the sample station"""
    return tuple(dataframe.loc[dataframe[split_column] == station] for station in stations)

if __name__ == "__main__":
    read_inventory()
    print("Success!")
