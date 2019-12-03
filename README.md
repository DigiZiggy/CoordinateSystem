**Project title**

Program that converts from WGS84 to L-Est97 coordinate system and vice versa.

**Project description**

Locations on earth are often expressed in geographic degrees (latitude and longitude). But when you are surveying you need to talk in meters (or feet). This is because - depending on the application - you use a geographic or projected coordinate system.

A geographic coordinate system (GCS) is a coordinate system which uses a three-dimensional spherical surface (ellipsoid) to define locations on the earth. A common choice of coordinates is latitude and longitude. For example, main entrance of Taltech IT College is located on 59Â°23'43.02" North and 24Â°39'50.78" East in the WGS84 coordinate system. 

In a projected coordinate system (PCS) you project the geographic coordinate that you have measured, to, for example, a cylinder which you roll out easily on two-dimensional surface (the map). There exist many different projections. For example, main entrance of Taltech IT College is located on X=6584335.6 and Y=537731.1 in the Estonian L-Est97 coordinate system. 
NB X-axe direction is to North and Y-axe direction is to East. https://xgis.maaamet.ee/xGIS/XGis?app_id=UU82&user_id=at&punkt=537731.1,6584335.6&zoom=95.2690129536204&LANG=2

Task: You need to wrote program which converts coordinates from WGS84 coordinates to L-Est97 and vice versa.
Additional requirements: Python 2.7 and 3.x, documentation and testing are mandatory.
GUI is recommended.

Hints
* use pyproj  library (https://pypi.org/project/pyproj/)
* Estonian coordinate system: http://spatialreference.org/ref/epsg/3301/
* WGS84 coordinate system: http://spatialreference.org/ref/epsg/4326/


**Screenshots**

![Alt text](Screenshot 2019-04-15 at 18.28.48.png?raw=true "Optional Title")



**Code Example**

The following library helps to converts coordinates from WGS84 coordinates to L-Est97 and vice versa. 
Library consists of following classes:  

*CoordinateConverter* 
    - converts decimal coordinates from WGS84 to L-Est97 and vice versa
    
*CoordinateValidator* 
    - validates that user input is valid and in allowed bounds
    
*DecimalDegreeConverter*
    - converts decimal values into degrees and vice versa

**Installation**

Provide step by step series of examples and explanations about how to get a development env running.

**Tests**

Install PyTest in root folder
```angular2
pip install pytest
```

Before being able to run all tests, some Tkinter Labels need to be commented out:

    def l_est97to_wgs_84
        # Tk.Label(main, text=longitude_in_degrees).grid(row=0, column=3, padx=0, pady=10)
        # Tk.Label(main, text=latitude_in_degrees).grid(row=1, column=3, padx=0, pady=10)
        
    def wgs_84to_l_est97   
        # Tk.Label(main, text=l_est97_latitude).grid(row=3, column=3, padx=0, pady=10)
        # Tk.Label(main, text=l_est97_longitude).grid(row=4, column=3, padx=0, pady=10)

    def validate_user_input_is_valid
        # Tk.Label(main, text='Your input ' + input_value + ' was not valid because you entered letters '
        #                                                   'instead of numbers or left the input blank, try again!',
        #          fg="red").grid(row=6, column=1, padx=50, pady=20)

    def wgs_84_validate_user_input_in_bounds
        # Tk.Label(main, text='Your input ' + str(input_value) + ' is out of bounds!', fg="red")\
        #     .grid(row=7, column=1, padx=50, pady=20)
        
        # Tk.Label(main, text='Your input ' + str(input_value) + ' is out of bounds!', fg="red")\
        #     .grid(row=7, column=1, padx=50, pady=20)
        
    def l_est97_validate_user_input_in_bounds
        # Tk.Label(main, text='Your input ' + str(input_value) + ' is out of bounds!', fg="red")\
        #     .grid(row=7, column=1, padx=50, pady=20)
        
        # Tk.Label(main, text='Your input ' + str(input_value) + ' is out of bounds!', fg="red")\
        #     .grid(row=7, column=1, padx=50, pady=20)


Run tests
```angular2
pytest test_converter.py
```


**How to use?**

Go into the CoordinateSystem folder
```angular2
cd CoordinateSystem
```

Make sure PyProj library is installed
```angular2
pip install pyproj
```

Run the converter with python version 2 or 3
```angular2
python converter.py  OR python3 converter.py
```

GUI window should open up. 
Enter decimal values and press button to convert.

**Credits**

Inspiration for Decimal-Degrees (DD) to Degrees-Minutes-Seconds (DMS) with Python

https://glenbambrick.com/2015/06/24/dd-to-dms/

**License**

MIT © Sigrid Närep