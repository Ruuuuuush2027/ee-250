# team members: Junsoo Kim, Mo Jiang
# link: https://github.com/Ruuuuuush2027/ee-250.git
import pandas as pd
import matplotlib.pyplot as plt
import argparse
import os
import sys

def create_distance_plot(tcp_csv: str, udp_csv: str):
    """
    Reads TCP and UDP iPerf results CSV files, calculates average throughput per distance,
    and generates a comparison plot of Throughput vs Distance.
    """
    for f in [tcp_csv, udp_csv]:
        if not os.path.exists(f):
            print(f"Error: File not found at {f}")
            sys.exit(1)

    try:
        df_tcp = pd.read_csv(tcp_csv)
        df_udp = pd.read_csv(udp_csv)
        
        if df_tcp.empty or df_udp.empty:
            print("Error: One of the CSV files is empty.")
            sys.exit(1)
            
    except Exception as e:
        print(f"Error reading or processing CSV files: {e}")
        sys.exit(1)

    # Identify run columns (assuming they start with 'Run')
    run_cols_tcp = [col for col in df_tcp.columns if col.startswith('Run')]
    run_cols_udp = [col for col in df_udp.columns if col.startswith('Run')]

    # Calculate average throughput for each row (Distance)
    df_tcp['Avg_Throughput'] = df_tcp[run_cols_tcp].mean(axis=1)
    df_udp['Avg_Throughput'] = df_udp[run_cols_udp].mean(axis=1)
    
    # Sort by Distance to ensure the line plot connects points correctly
    df_tcp = df_tcp.sort_values('Distance')
    df_udp = df_udp.sort_values('Distance')

    # --- Plotting ---
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots(figsize=(10, 6))

    # TCP Line (Solid)
    ax.plot(df_tcp['Distance'], df_tcp['Avg_Throughput'], label='TCP Throughput', linestyle='-', marker='o')
    
    # UDP Line (Dashed)
    ax.plot(df_udp['Distance'], df_udp['Avg_Throughput'], label='UDP Throughput', linestyle='--', marker='s')

    ax.set_title('TCP & UDP Throughput vs Distance', fontsize=16)
    ax.set_xlabel('Distance (m)', fontsize=12)
    ax.set_ylabel('Average Throughput (Mbps)', fontsize=12)
    
    ax.legend()

    # --- Saving the file ---
    output_filename = "iperf_throughput_vs_distance.png"
    plt.savefig(output_filename)
    print(f"Plot saved to {output_filename}")

def main():
    parser = argparse.ArgumentParser(description="Generate a Throughput vs Distance plot from TCP and UDP iPerf CSV log files.")
    parser.add_argument("tcp_csv", type=str, help="Path to the TCP iPerf CSV file.")
    parser.add_argument("udp_csv", type=str, help="Path to the UDP iPerf CSV file.")
    args = parser.parse_args()
    create_distance_plot(args.tcp_csv, args.udp_csv)

if __name__ == "__main__":
    main()