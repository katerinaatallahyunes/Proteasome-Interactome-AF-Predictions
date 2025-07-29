#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 10:00:52 2025

@author: atallahyuneska
"""

import pandas as pd

def calculate_confidence_averages(file_path, output_path):
    # Load the TSV file
    df = pd.read_csv(file_path, sep='\t')
    
    # Extract unique protein pairs
    df['protein_pair'] = df['prediction_name'].apply(lambda x: '_'.join(x.split('_')[:3]))
    protein_pairs = df['protein_pair'].unique()
    
    results = []
    for pair in protein_pairs:
        # Filter rows for this protein pair
        subset = df[df['protein_pair'] == pair]
        
        # Ensure only the relevant top 3 ranked entries are considered
        top3 = subset[subset['model_id'].str.endswith(('ranked_0', 'ranked_1', 'ranked_2'))]
        
        # Compute averages
        avg_top3 = top3['model_confidence'].mean()
        avg_all = subset['model_confidence'].mean()
        
        # Store results
        results.append({'protein_pair': pair, 'avg_top3': avg_top3, 'avg_all': avg_all})
    
    # Convert to DataFrame and save
    result_df = pd.DataFrame(results)
    result_df.to_csv(output_path, sep='\t', index=False)
    print(f"Results saved to {output_path}")

input_tsv = '/mnt/csbms_scratch/Proteasome_Missing_Predictions/High_Priority/template_indep_info.tsv'
output_tsv = '/mnt/csbms_scratch/Proteasome_Missing_Predictions/High_Priority/average_model_confidence_Proteasome_High_Priority.tsv'
calculate_confidence_averages(input_tsv, output_tsv)
