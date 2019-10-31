## Happy Halloween!

![image](https://i.pinimg.com/236x/9f/7d/ec/9f7decd4ce463890fdc37741bf77dd61--carved-pumpkins-pumpkin-carvings.jpg)

Also,
![image](https://previews.123rf.com/images/christitze/christitze1611/christitze161138480/66332637-happy-birthday-isabel-card-with-balloon-text-3d-rendered-stock-image-this-image-can-be-used-for-a-ec.jpg)

Today we are going to cut our data down once and for all.  Slight change: instead of using the file we have been using, sea_velocity_19930101.nc, which contains *ugos* and *vgos*, we are going to move forward with a different (but very similar file), ssh_1572033769470.nc. Instead of containing the velocities, this file contains just the *sea surface height* of the ocean. Why are we using a new file?? What is going on??

**********
Big picture of what we are doing:
* We need to calculate the **ageostrophic** velocity vectors of the ocean, particularly the vertical (w) velocity. (Pause, draw, make sure we are on the same page) 
* ugos and vgos (from the file we were looking at in the past) are the **geostrophic** velocities.

Geostrophic and ageostrophic are types of currents.  Scientists (us) use models of geostrophic and ageostrophic velocities to calculate ocean current velocities from sea surface height. The geostrophic velocity is more commonly used because it is easier to calcuate and it is correct/good enough for most purposes.  
We are interested in using the ageostrophic velocity because the ageostrophic model is more accurate for dealing with eddies. 

Before the plan was to go from geostrophic velocities --> ageostrophic velocities, but now we are using code from a Spanish collaborator that goes from sea surface height --> ageostrophic velocities. 

This code is written in fortran77 (as in a programming language developed in 1977) :sob: and commented in :sob: Catalan :sob: 
This is what a computer looked like in 1977:

![image](https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTExaxVhuEjf0oFMRzuuVJu0avZ3GG-QuSVyfw6HkfxXpPH7K9H)
:see_no_evil::see_no_evil:

Som-hi! (Catalan for "let's go!") 
***********

So now our input data is **sea surface heights**. And despite all of this complicated mess, we still need to cut down our data.

In our file, sea surface height data is under the header 'adt' for absolute dynmaic typography, and it covers the whole globe. 

# Our goal: create a variable BATS_adt that just covers the BATS data range:

<img src="https://raw.githubusercontent.com/madesai22/ocean-ml/master/images/BATS_data.png" width="400" height="450" />

The adt data field has dimension (time, latitude, longitude). 
The other data fields that are important to us are latitude and longitude. 

In Sublime, open the file cutting_data.py. 
Other resources:
* [NumPy cheatsheet](https://github.com/madesai22/ocean-ml/blob/master/cheat-sheets-resources/numpy-cheat-sheet.pdf)

Quick NetCDF notes:
* to import netCDF4 library: `from netCDF4 import Dataset`
* to import netCDF file: `dataset = Dataset(r'/path/to/file')`
* to access a data element: `lat = dataset['latitude']`

Start by importing the file ssh_1572470095877 as a dataset object and creating variables with the lat, lon, and adt. Then, with a partner, discuss what the next steps are. (10 minutes)

Now, we will discuss as a group and map out an aproach. 

Finally, you and your partner have the rest of the session to code the approach you choose. At the end, run `print(BATS_adt.shape)`
You should get (1, 78, 25). 



