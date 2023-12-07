#pip install geopandas matplotlib topojson contextily
#!pip install requests py7zr geopandas openpyxl tqdm s3fs PyYAML xlrd !pip install git+https://github.com/inseefrlab/cartiflette@80b8a5a28371feb6df31d55bcc2617948a5f9b1a

import geopandas as gpd
import contextily as ctx
import matplotlib.pyplot as plt

import cartiflette.s3 as s3


shp_region = s3.download_vectorfile_url_all(
    values = "metropole",
    crs = 4326,
    borders = "REGION",
    vectorfile_format="topojson",
    filter_by="FRANCE_ENTIERE",
    source="EXPRESS-COG-CARTO-TERRITOIRE",
    year=2022)
    
fig,ax = plt.subplots(figsize=(10, 10))
shp_region.to_crs(5070).plot(ax = ax)
ax