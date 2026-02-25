# team members: Junsoo Kim, Mo Jiang
# link: https://github.com/Ruuuuuush2027/ee-250.git
import pandas as pd
import matplotlib.pyplot as plt
import argparse
import os
import sys

def create_plot(tcp_csv: str, udp_csv: str):
    """
    Reads TCP and UDP iPerf results CSV files, uses the last row to generate a comparison plot,
    and saves it as a PNG.

    Args:
        tcp_csv (str): The path to the TCP CSV file.
        udp_csv (str): The path to the UDP CSV file.
    """
    for f in [tcp_csv, udp_csv]:
        if not os.path.exists(f):
            print(f"Error: File not found at {f}")
            sys.exit(1)

    # Read the CSVs and get the last row (most recent run)
    try:
        df_tcp = pd.read_csv(tcp_csv)
        df_udp = pd.read_csv(udp_csv)
        if df_tcp.empty or df_udp.empty:
            print("Error: One of the CSV files is empty.")
            sys.exit(1)
        last_run_tcp = df_tcp.iloc[-1]
        last_run_udp = df_udp.iloc[-1]
    except Exception as e:
        print(f"Error reading or processing CSV files: {e}")
        sys.exit(1)

    distance = last_run_tcp['Distance']
    
    # Extract throughput data for runs
    run_cols = [col for col in df_tcp.columns if col.startswith('Run')]
    tcp_data = last_run_tcp[run_cols]
    udp_data = last_run_udp[run_cols]
    
    # --- Plotting ---
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots(figsize=(10, 6))

    # TCP Line (Solid)
    ax.plot(run_cols, tcp_data, label='TCP Throughput', linestyle='-', marker='o')
    
    # UDP Line (Dashed)
    ax.plot(run_cols, udp_data, label='UDP Throughput', linestyle='--', marker='s')

    ax.set_title(f'iPerf TCP vs UDP Throughput at {distance}m', fontsize=16)
    ax.set_xlabel('Run Number', fontsize=12)
    ax.set_ylabel('Throughput (Mbps)', fontsize=12)
    
    # Set Y limit to accommodate both
    max_val = max(max(tcp_data), max(udp_data))
    ax.set_ylim(0, max_val * 1.2 if max_val > 0 else 10)
    
    ax.legend()

    # --- Saving the file ---
    output_filename = f"iperf_compare_{distance}m.png"
    
    plt.savefig(output_filename)
    print(f"Plot saved to {output_filename}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate a comparison plot from the last run in TCP and UDP iPerf CSV log files."
    )
    parser.add_argument("tcp_csv", type=str, help="Path to the TCP iPerf CSV file.")
    parser.add_argument("udp_csv", type=str, help="Path to the UDP iPerf CSV file.")
    
    args = parser.parse_args()
    
    create_plot(args.tcp_csv, args.udp_csv)

if __name__ == "__main__":
    main()