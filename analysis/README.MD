# vehicles-power-to-weight data analysis
## Overview of the data
### Summary
The raw data has three tab delimited columns: <code>make</code>, <code>model</code> and <code>specs</code>.<br>
The <code>specs</code> column contains two semicolon ":" delimited values.<br>
The value before the semicolon is more specific information about the vehicle, past just make and model.<br>
The value after the semicolon is the power to weight ratio for that specific vehicle.
### Columns
<code>Column name</code> (example)<br>
<code>make</code> (acura)<br>
<code>model</code> (acura-ilx)<br>
<code>specs</code> (2013 Acura ILX)<br>
<code>specs1</code> (0.052)

## Objectives
### For your consideration
When it comes to writing computer programs that leverage data, you are only ever doing one of two things at a time.<br>
The first is that you see the data as a sample of measurements from an existing system and you want to gain insight into that system.<br>
The second is that you see the data as examples for how you want a piece of software to behave. It is likely you want to leverage these examples because it makes more sense to do so than to write a heuristic or algorithm by hand.<br>
The technical techniques used to perform these two things are largely the same. Arguably, the first is within the real of Data Science and the second within the real of AI Engineering. However, these two things are not mutually exclusive and both may be done, to some degree, during any tasking that involves data and computers.
### Objective #1
What does a 'high power to weight ratio' versus a 'low power to weight ratio' mean in the context of this data?
### Objective #2
Apply the methodology from Objective #1 to the data by model year instead of as a whole.
### Objective #3
Create a model to predict whether a given power to weight ratio is a 'high power to weight ratio' or a 'low power to weight ratio', given a power to weight ratio and a model year, including for future model years.
