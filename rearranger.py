# Finds optimal configuration of pieces from dxf onto a 24x36 cut space
import rpack
import numpy as np

def group_dxfs(dxf_names):
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
    return positions

def positions_to_area(positions):
    max_width = np.max(positions[:, 0])
    max_height = np.max(positions[:, 1])
    return max_width * max_height

if __name__ == "__main__":
    dxf_names = [""]
    
    # try 12 random permutations of different shapes and find the one that uses the smallest area
    smallest_area = np.inf
    best_positions = 0
    for iter in range(10):
        positions = group_dxfs(dxf_names=dxf_names)
        total_area = positions_to_area(positions)
        if total_area < smallest_area:
            best_positions = positions
            smallest_area = total_area
    