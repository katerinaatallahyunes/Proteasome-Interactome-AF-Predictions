#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import pandas as pd

def process_model_statistics(root_folder, output_file):
    results = []
    
    # Iterate through each subfolder in the root folder
    for subfolder in os.listdir(root_folder):
        subfolder_path = os.path.join(root_folder, subfolder)
        csv_file = os.path.join(subfolder_path, "model_statistics.csv")
        
        if os.path.isdir(subfolder_path) and os.path.isfile(csv_file):
            try:
                # Read CSV file
                df = pd.read_csv(csv_file)
                
                # Compute averages
                avg_plddt = df['plddt'].mean()
                avg_pdockq = df['pdockq'].mean()
                
                # Append results
                results.append([subfolder, avg_pdockq, avg_plddt])
            except Exception as e:
                print(f"Error processing {csv_file}: {e}")
    
    # Create a DataFrame and save to Excel
    result_df = pd.DataFrame(results, columns=["Subfolder", "Average_pdockq", "Average_plddt"])
    result_df.to_excel(output_file, index=False)
    print(f"Results saved to {output_file}")

# Example usage
root_folder = "/root/folder/path"  # Change this to your actual folder path
output_file = "output/file/path/average_plddt_and_pdockq.xlsx"         # Output file name
process_model_statistics(root_folder, output_file)
