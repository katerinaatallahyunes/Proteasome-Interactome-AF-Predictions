#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd

def calculate_confidence_averages(file_path, output_path):
    df = pd.read_csv(file_path, sep='\t')
    
    df['protein_pair'] = df['prediction_name'].apply(lambda x: '_'.join(x.split('_')[:3]))
    protein_pairs = df['protein_pair'].unique()
    
    results = []
    for pair in protein_pairs:
        subset = df[df['protein_pair'] == pair]

        top3 = subset[subset['model_id'].str.endswith(('ranked_0', 'ranked_1', 'ranked_2'))]

        avg_top3 = top3['model_confidence'].mean()
        avg_all = subset['model_confidence'].mean()
        
        results.append({'protein_pair': pair, 'avg_top3': avg_top3, 'avg_all': avg_all})
    
    result_df = pd.DataFrame(results)
    result_df.to_csv(output_path, sep='\t', index=False)
    print(f"Results saved to {output_path}")

input_tsv = '/input/tsv/path/template_indep_info.tsv'
output_tsv = 'output/tsv/path/average_model_confidence.tsv'
calculate_confidence_averages(input_tsv, output_tsv)
