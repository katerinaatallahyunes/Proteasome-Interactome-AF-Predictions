#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import pandas as pd

def process_model_statistics(root_folder, output_file):
    results = []
    
    for subfolder in os.listdir(root_folder):
        subfolder_path = os.path.join(root_folder, subfolder)
        csv_file = os.path.join(subfolder_path, "model_statistics.csv")
        
        if os.path.isdir(subfolder_path) and os.path.isfile(csv_file):
            try:
                df = pd.read_csv(csv_file)
                
                avg_plddt = df['plddt'].mean()
                avg_pdockq = df['pdockq'].mean()
                
                results.append([subfolder, avg_pdockq, avg_plddt])
            except Exception as e:
                print(f"Error processing {csv_file}: {e}")
    
    result_df = pd.DataFrame(results, columns=["Subfolder", "Average_pdockq", "Average_plddt"])
    result_df.to_excel(output_file, index=False)
    print(f"Results saved to {output_file}")

# Example usage
root_folder = "/root/folder/path"  
output_file = "output/file/path/average_plddt_and_pdockq.xlsx"         
process_model_statistics(root_folder, output_file)
