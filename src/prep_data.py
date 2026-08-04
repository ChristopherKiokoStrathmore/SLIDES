"""Compact the boundary + county data into a single payload the web app can embed."""
import json
import re

import geopandas as gpd
import pandas as pd

norm = lambda s: re.sub(r"[^A-Z]", "", str(s).upper())

geo = gpd.read_file("kenya_counties.geojson")
geo = geo[geo.COUNTY_NAM.notna()].dissolve(by="COUNTY_NAM").reset_index()
geo["ckey"] = geo.COUNTY_NAM.map(norm).replace(
    {"ELEGEYOMARAKWET": "ELGEYOMARAKWET", "NAIROBI": "NAIROBICITY"})

# simplify hard - this renders at ~700px, sub-kilometre detail is wasted bytes
geo["geometry"] = geo.geometry.simplify(0.008, preserve_topology=True)

cap = pd.read_csv("county_capacity.csv")
census = pd.read_csv("census_county.csv")
census["ckey"] = census["name"].map(norm)
cap = cap.merge(census[["ckey", "households", "density"]], on="ckey", how="left")
cap["hh_size"] = cap["pop"] / cap["households"]

gdf = geo.merge(cap, on="ckey", validate="one_to_one")
pts = gdf.to_crs(21037).centroid.to_crs(4326)
gdf["lon"], gdf["lat"] = pts.x, pts.y

fields = ["county", "ckey", "pop", "beds", "beds_public", "n_bedded", "facilities",
          "lvl4plus", "lvl5plus", "largest_share", "hhi", "density", "hh_size",
          "beds_per_10k", "pub_beds_per_10k", "lon", "lat"]

features = []
for _, r in gdf.iterrows():
    geom = json.loads(gpd.GeoSeries([r.geometry]).to_json())["features"][0]["geometry"]
    # 3dp of latitude is about 110 m - far finer than this map can show
    geom["coordinates"] = json.loads(
        json.dumps(geom["coordinates"]).replace("]", "]"))
    props = {}
    for f in fields:
        v = r[f]
        props[f] = round(float(v), 4) if isinstance(v, float) else v
    features.append({"type": "Feature", "properties": props, "geometry": geom})

payload = {"type": "FeatureCollection", "features": features}
raw = json.dumps(payload, separators=(",", ":"))
raw = re.sub(r"(\d+\.\d{4})\d+", r"\1", raw)      # trim coordinate precision

open("web_data.json", "w").write(raw)
print(f"payload: {len(raw)/1024:.0f} KB, {len(features)} counties")
print("national beds:", int(gdf.beds.sum()), "pop:", int(gdf["pop"].sum()))
