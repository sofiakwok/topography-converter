# Converts bathymetry data to STL and DXF data. 

def tif_to_dxf():
    # https://github.com/ewandennis/geotiff2stl
    return None

if __name__ == "__main__":
    tif_file = "path/to/your/model"

    # bathymetry data: https://cmgds.marine.usgs.gov/data-releases/datarelease/10.5066-P9GVRZ3M/
    # https://www.ncei.noaa.gov/maps/bathymetry/

    try:
        tif_to_dxf(tif_file)
        print(f"Successfully converted {tif_file} to stl")
    except ValueError as e:
            print(f"Error: {e}")