### 4.1
git clone git@github.com:my-name/my-imaginary-repo.git
touch my_second_file.py
echo "print(\"Hello World\")" > my_second_file.py
git add .
git commit -m "xxx"
git push

### 4.2
We basically write the code in VS Code and use scp to copy files to RPI. This should be more efficient than git and github as I do not need to install git and github on RPI and when my device hotpot is disconnected from internet I can still pass my codes from my computer to RPI (as the hotspot or router is still working).

### 4.3
Even if I remove time.sleep(0.2) from my script, the library itself enforces a delay. Inside grovepi.py, specifically within the ultrasonicRead() function,  it has a time.sleep(0.06) which delays by 60 ms. RPI uses I2C protocol to connect with Atmega328P on the GrovePi.

### 4.4
The GrovePi uses an Analog-to-Digital Converter (ADC) to convert the voltage value to a range from 0 to 1023. RPI cannot do this directly because it just lacks the hardware to handle this ADC process.

### 4.5
1. it can due to hardware communication issues. I would run `i2cdetect -y 1` to check if I can find numbers like 0x3e for LCD. If it's only dash, then it could be that LCD is loose or is plugged in the wrong port
2. it could also be because the i2c module is not active so grovepi is failing silently. I can run `ls /dev/i2c*` to see if i2c is enabled. If not, I will enable it using `sudo raspi-config`