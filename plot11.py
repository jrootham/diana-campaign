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

print(df["AREA_L_CD"])

df["WARD"] = df["AREA_L_CD"].map(ward)

print (df["WARD"])

list = []
index = 0
for longCode in df["AREA_L_CD"]: 
    index += 1
    if '11' == longCode[:2]: 
        list.append(index)

print(list)

df.iloc[list].plot()

print(df)
# df.plot("WARD")

plt.show()

