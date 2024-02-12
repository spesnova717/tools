import pandas as pd
import matplotlib.pyplot as plt
import sys
import os

def plot_individual_cpu_metrics(file_path, output_dir):
    # ファイルを読み込み、DataFrameに変換
    df = pd.read_csv(file_path, sep='\s+', 
                     names=['Time', 'CPU', '%user', '%nice', '%system', '%iowait', '%steal', '%idle'],
                     skiprows=[0])
    
    # 出力ディレクトリが存在しない場合は作成
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    metrics = ['%user', '%nice', '%system', '%iowait', '%steal', '%idle']
    
    # 各CPUごとに処理
    for cpu in df['CPU'].unique():
        cpu_df = df[df['CPU'] == cpu]
        
        for metric in metrics:
            fig, ax = plt.subplots(figsize=(10, 8))
            ax.plot(cpu_df['Time'], cpu_df[metric], label=metric)
            ax.set_xlabel('Time')
            ax.set_ylabel('Usage (%)')
            ax.set_title(f'{metric} Over Time - CPU {cpu}')
            ax.legend()
            plt.xticks(rotation=45)
            plt.tight_layout()
            output_path = os.path.join(output_dir, f'CPU_{cpu}_{metric}.png')
            plt.savefig(output_path)
            plt.close()
            print(f"{metric} graph for CPU {cpu} saved to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <path_to_file> <output_directory>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    output_dir = sys.argv[2]
    plot_individual_cpu_metrics(file_path, output_dir)

