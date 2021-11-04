# weather-dashboard

This app uses below Tools technologies.

```
H2o Wave
Python
```

# Installation steps

# Clone the repo
Use the following command to clone the repo
```
https://github.com/sanjeepan23/weather-dashboard.git
```
# Start the Wave server
After Cloning, move the dir to inside existing conda environment. then use the `./waved` command to start the server in Linux and use `waved` in Windows

# Set up a working directory
Next, let's set up a working directory to author our program.
## Create a directory
`mkdir  $HOME/wave-apps`
 `cd $HOME/wave-apps`

## Set up a virtual environment

A [virtual environment](https://docs.python.org/3/tutorial/venv.html) helps us manage our program's dependencies without interfering with system-wide packages.
For Linux,
`python3 -m venv venv`
`source venv/bin/activate`
For Windows,
`python3 -m venv venv`
`venv\bin\activate`

## Install the Wave Python driver
`pip install h2o_wave`

# Run your program
`python covid_tracker.py`


##Screen Shots
![alt text](https://github.com/sanjeepan23/weather-dashboard/blob/main/assets/.h2o.png?raw=true)
![alt text](https://github.com/sanjeepan23/weather-dashboard/blob/main/assets/2.h2o.png?raw=true)


