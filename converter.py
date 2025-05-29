import ezdxf
import meshio

def stl_to_dxf(stl_filepath, dxf_filepath):
    """Converts an STL file to a DXF file, extracting the outline of the 3D model.
    """
    try:
        mesh = meshio.read(stl_filepath)
    except meshio._exceptions.ReadError:
        raise ValueError(f"Could not read the file: {stl_filepath}. Check if it is a valid STL file.")

    if len(mesh.cells) == 0 or mesh.cells[0].type != "triangle":
        raise ValueError("The STL file must contain triangle data.")

    doc = ezdxf.new()
    msp = doc.modelspace()

    for cell in mesh.cells[0].data:
        p1, p2, p3 = mesh.points[cell[0]], mesh.points[cell[1]], mesh.points[cell[2]]
        msp.add_lwpolyline([p1[:2], p2[:2], p3[:2], p1[:2]])

    doc.saveas(dxf_filepath)

if __name__ == "__main__":
    stl_file = "path/to/your/model.stl"
    dxf_file = "path/to/your/model.dxf"

    # data source: touchterrain (for non-bathymetry high resolution STLs): https://touchterrain.geol.iastate.edu/

    try:
        stl_to_dxf(stl_file, dxf_file)
        print(f"Successfully converted {stl_file} to {dxf_file}")
    except ValueError as e:
            print(f"Error: {e}")