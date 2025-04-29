# Finds optimal configuration of pieces from dxf onto a 24x36 cut space
import rpack

def group_dxfs(dxf_names, sheet_size):
    """Takes a folder containing only dxfs and groups them into the best arrangement
    
    Assumptions: rectangular shapes
    Units: inches"""
    sizes = []
    for dxf in dxf_names:
        dxf_path = dxf
        size = dxf_path
        sizes.append(size)
        
    positions = rpack.pack(sizes)
    print(positions)