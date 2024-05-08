import sys
import open3d
import numpy as np
import pickle
from visual_utils.open3d_vis_utils import draw_scenes

def load_points_and_visualize(file_path):
    with open(file_path, 'rb') as f:
        data = pickle.load(f)
    
    points = data['points'][0]
    pred_dicts = data['pred_dicts'][0]
    
    draw_scenes(points, gt_boxes=None, ref_boxes=pred_dicts[0]['pred_boxes'], ref_labels=pred_dicts[0]['pred_labels'], ref_scores=pred_dicts[0]['pred_scores'], point_colors=None, draw_origin=True)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python visualize.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    load_points_and_visualize(file_path)
