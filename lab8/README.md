### Question 1
**What are the denominations of the US coins from the green, blue, and orange distributions?**
    - Dime, nickel, dollar
    
**Can you think why the coins from the same denomination might show variation in weight, although they are specified to be of the same weight?**
    - Maybe like being worn down as they are used by different people with different usage patterns

**If your vending machine had a weight sensor, how would you use the weight of a coin that was just inserted to find the denomination?**
    - Match the measured weight of the inserted coin to the closest known denomination weight.

### Question 2
**We can shine light on the coin and measure the reflected amount of light, which should be proportional (directly or in some non-linear way) to the size/area of the coin. Can you reason which sensor on the Grove Pi Kit can be used for this purpose?**
    - The Grove Light Sensor. It uses a photoresistor to measure light intensity and to detect the varying amounts of light reflected by coins

### Question 3
**Which of the following datasets are linearly separable? Justify your answer**
    - A,C,D, as one can draw a line that separates the two colors of points perfectly

### Question 4
**Sometimes we need more than a simple hyperplane to separate the datasets of the two classes. What are some other simple geometric entities other than a simple plane/line that can be used to separate some of the data points that were not linearly separable?**
    - Circles, ellipses, parabolas, or other polynomial curves.

### Question 5
**For the example shown in the figure, what is approximately the output of the neuron? The bias is -2 [if anybody has any confusion]**
    - 1/(1+e^{-4}) = 0.982
