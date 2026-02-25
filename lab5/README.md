# Lab 5

## Team Members
- Junsoo Kim <junsooki@usc.edu>
- Mo Jiang <mojiang@usc.edu>
- repo: https://github.com/Ruuuuuush2027/ee-250.git

## Lab Question Answers

### Part1
Answer for Question 1: 
**Question 1: What is dBm? What values are considered good and bad for WiFi signal strength?**
dBm is the unit used to measure WiFi signal strength, and since it's negative, a number closer to zero is better. 
Anything around -50 dBm is good, but once you drop to -80 dBm or lower, your connection is basically dead.

**Question 2: Why do we need to check the OS? What is the difference between the commands for each OS?**
We have to check the OS because Mac, Windows, and Linux all use completely different terminal commands to pull network info.

**Question 3: In your own words, what is subprocess.check_output doing? What does it return?**
**HINT: https://docs.python.org/3/library/subprocess.html#subprocess.check_output**
subprocess.check_output captures a command's standard output and returns it as a byte string. Normally, 
you had have to manually manage and read these output streams yourself, but this function does the heavy lifting for you.

**Question 4: In your own words, what is re.search doing? What does it return?**
**HINT: https://docs.python.org/3/library/re.html#re.search**
re.search scans through a string until it finds the first location where your regex pattern matches. 
It returns a match object containing the data if it finds something, or None if there is no match.

**Question 5: In the Windows case, why do we need to convert the signal quality to dBm?**
**HINT: https://learn.microsoft.com/en-us/windows/win32/api/wlanapi/ns-wlanapi-wlan_association_attributes?redirectedfrom=MSDN**
Windows prints a signal quality percentage instead of standard dBm. Because of this, we have to run a 
separate math formula to convert that percentage into dBm so our data is consistent.

**Question 6: What is the standard deviation? Why is it useful to calculate it?**
The standard deviation is useful because it shows how spread out the values are 
and how far they typically differ from the mean.

**Question 7: What is a dataframe? Why is it useful to use a dataframe to store the data?**
**HINT: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html**
**HINT: print the dataframe to see what it looks like**
print(df)
A dataframe is a tabular data structure with rows and columns.
It is useful because it provides flexibility, efficient data handling, and convenient built-in operations for analysis and manipulation.

**Question 8: Why is it important to plot the error bars? What do they tell us?**
Error bars show the variability/uncertainty in the measurements.
They indicate how stable or inconsistent the signal strength is at each location.

**Question 9: What did you observe from the plot? How does the signal strength change as you move between locations?**
**Why do you think signal strength is weaker in certain locations (e.g. kitchen)?**
Signal strength typically decreases as distance from the router increases or when obstacles
(walls, floors, appliances) interfere. Locations farther away or blocked by thick walls
often show weaker and more variable signals.

### Part2
**Question 1: How does distance affect TCP and UDP throughput?**
As distance increases, TCP throughput tends to decrease, yet according to the experiment the UDP throughput is not changing, or as noticeably.

**Question 2: At what distance does significant packet loss occur for UDP?**
In theory it should occur at around 15 meters, yet it's not occuring in my experiment. Maybe I should introduce some obstacles at 15 meter distance.

**Question 3: Why does UDP experience more packet loss than TCP?**
In theory it should, this is because UDP is like "single fire and don't care." It just fires up the packets without checking message correctness and re-transmit - lacking handshake like TCP.

**Question 4: What happens if we increase the UDP bandwidth (-b 100M)?**
In theory we should expect more packets being dropped due to network bottleneck and limit in receiver buffers. We might also expect some network latency for other devices in the same network as UDP is knwon to be "selfish" and won't adjust transmission rate based on network bandwidth like TCP does.

**Question 5: Would performance be different on 5 GHz Wi-Fi vs. 2.4 GHz?**
5GHz Wi-Fi should have better performance than 2.4 GHz Wi-Fi because 5GHz have wider transmission channels. Also 5GHz will likely experience less interference as 2.4GHz tends to be saturated by Bluetooth, microwaves, and neighboring Wi-Fi.