import sys
import geopandas as gpd
import matplotlib.pyplot as plt

name = sys.argv[1]

df = gpd.read_file(name)

def ward(code):
    if code[:2] == "11":
        result = 0
    else: 
        result = 1
    return result

df["WARD"] = df["AREA_L_CD"].map(ward)

df = df[df["WARD"] == 0]

df.plot()

plt.show()

