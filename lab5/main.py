# team members: Junsoo Kim, Mo Jiang
# link: https://github.com/Ruuuuuush2027/ee-250.git
import platform
import time
import pandas as pd
import plotly.express as px
import numpy as np
import subprocess
import re

def get_wifi_signal_strength() -> int:
    """Get the signal strength of the wifi connection.
    
    Returns:
        The signal strength in dBm.
    """

    if platform.system() == 'Linux': # Linux, mine is WSL
        output = subprocess.check_output("netsh.exe wlan show interfaces", shell=True)
        match = re.search(r"Signal\s*:\s*(\d+)%", output.decode('utf-8', errors='ignore'))
        signal_quality = int(match.group(1))
        signal_strength = -100 + signal_quality / 2
    elif platform.system() == 'Windows': # Windows
        output = subprocess.check_output("netsh wlan show interfaces", shell=True)
        match = re.search(r"Signal\s*:\s*(\d+)%", output.decode('utf-8'))
        signal_quality = int(match.group(1))
        signal_strength = -100 + signal_quality / 2
    elif platform.system() == 'Darwin': # Mac
        output = subprocess.check_output("wdutil info", shell=True, stderr=subprocess.STDOUT)
        # The new regex looks for "RSSI" (Received Signal Strength Indicator).
        match = re.search(r"RSSI\s+:\s*(-?\d+)", output.decode('utf-8', errors='ignore'))        
        signal_strength = int(match.group(1))
        print(signal_strength)
    else:
        raise Exception("Unknown OS")

    return signal_strength

def main():
    # Choose at least 5 locations to sample the signal strength at
    # These can be rooms in your house, hallways, different floors, outside, etc. (as long as you can get a WiFi signal)
    locations = ['bedroom', 'living room', 'kitchen', 'bathroom', 'garage']
    samples_per_location = 10 # number of samples to take per location
    time_between_samples = 1 # time between samples (in seconds)

    data = [] # list of data points
    for location in locations:
        print(f"Go to the {location} and press enter to start sampling")
        input() # wait for the user to press enter
        signal_strengths = [] # list of signal strengths at this location

        # TODO: collect 10 samples of the signal strength at this location, waiting 1 second between each sample
        # HINT: use the get_wifi_signal_strength function
        for i in range(10):
            signal_strengths.append(get_wifi_signal_strength())
        time.sleep(1)

        # TODO: calculate the mean and standard deviation of the signal strengths you collected at this location
        signal_strength_mean = sum(signal_strengths) / len(signal_strengths)
        signal_strength_std = (sum((x - signal_strength_mean) ** 2 for x in signal_strengths) / (len(signal_strengths) - 1)) ** 0.5

        data.append((location, signal_strength_mean, signal_strength_std))

    # create a dataframe from the data
    df = pd.DataFrame(data, columns=['location', 'signal_strength_mean', 'signal_strength_std'])

    # TODO: plot the data as a bar chart using plotly
    # HINT: https://plotly.com/python/bar-charts/
    # NOTE: use the error_y parameter of px.bar to plot the error bars (1 standard deviation)
    #   documentation: https://plotly.com/python-api-reference/generated/plotly.express.bar.html
    fig = px.bar(
        df,
        x='location',
        y='signal_strength_mean',
        error_y='signal_strength_std',
        title="WiFi Signal Strength by Location (Mean ± 1 Std Dev)",
        labels={
            'signal_strength_mean': 'Mean Signal Strength (dBm)',
            'location': 'Location'
        }
    )

    # write the plot to a file - make sure to commit the PNG file to your repository along with your code
    fig.write_image("signal_strength.png")

if __name__ == "__main__":
    main()
