import pandas as pd
import matplotlib.pyplot as plt
import sys
import os

def plot_active_cpu_usage(file_path, output_dir):
    # ファイルを読み込み、DataFrameに変換
    df = pd.read_csv(file_path, sep='\s+', 
                     names=['Time', 'CPU', '%user', '%nice', '%system', '%iowait', '%steal', '%idle'],
                     skiprows=[0])

    # 列が数値型であることを確認し、必要に応じて型変換
    for column in ['%user', '%nice', '%system', '%iowait', '%steal', '%idle']:
        df[column] = pd.to_numeric(df[column], errors='coerce')
    
    # 出力ディレクトリが存在しない場合は作成
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 各CPUごとに処理
    for cpu in df['CPU'].unique():
        # アクティブ利用率の計算と設定
        # .locを使用してDataFrameを直接更新
        df.loc[df['CPU'] == cpu, 'Active Usage'] = df.loc[df['CPU'] == cpu, '%user'] + df.loc[df['CPU'] == cpu, '%nice'] + df.loc[df['CPU'] == cpu, '%system'] + df.loc[df['CPU'] == cpu, '%iowait'] + df.loc[df['CPU'] == cpu, '%steal']
        
        # アクティブ利用率のグラフ化
        fig, ax = plt.subplots(figsize=(10, 8))
        cpu_df = df[df['CPU'] == cpu]
        ax.plot(cpu_df['Time'], cpu_df['Active Usage'], label='Active Usage (%)')
        ax.set_xlabel('Time')
        ax.set_ylabel('Usage (%)')
        ax.set_title(f'Active CPU Usage Over Time - CPU {cpu}')
        ax.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        # 画像として保存
        output_path = os.path.join(output_dir, f'CPU_{cpu}_active_usage.png')
        plt.savefig(output_path)
        plt.close()
        print(f"Active usage graph for CPU {cpu} saved to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <path_to_file> <output_directory>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    output_dir = sys.argv[2]
    plot_active_cpu_usage(file_path, output_dir)

