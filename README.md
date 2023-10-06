# ASTRO OBSERVER PLAN - PySide6

![header](https://github.com/krmerdem/Astro-Observer-Plan/assets/115490296/06b5baa8-9c8d-4419-9ad1-a7f8db797a71)

Astronomy software built with Python and PySide 6 for astronomical observations.

IMPORTANT NOTE: Please read the information part of the program before you start using the program. 

## Download and Installing Software

The software is compatible with 64-bit versions of Windows 10 and Windows 11. Currently, the program has a ZIP extension. The setup version will be added soon. After downloading the ZIP, extract the archive and run AstroObserverPlan.exe

[Astro Observer Plan v1.0.0 Download](https://github.com/krmerdem/Astro-Observer-Plan/releases/download/v1.0.0/Astro.Observer.Plan.zip)

## Installing Dependencies

**INFO** | When the program is downloaded, the dependencies that it needs are available in the program. The program has been tested and works on Windows 10 and Windows 11 operating systems.

**Dependencies used in the program** | PySide6, Matplotlib, NumPy, Astroquery, Astropy, Ephem

## Introduction

The program calculates the daily or annual altitude of the selected star or object according to its position on Earth and its angular distance to the Moon and displays it on the graph. It also calculates the observable phase range for binary stars or multiple star systems. It also displays astronomical times depending on the location. There is a degree-minute-second or hour-minute-second converter required for astronomy in the program. In the program, you can search Simbad, 2MASS, WISE, Gaia DR3 and ZTF DR19 catalogs at the same time.

Optionally, it also performs elevation correction at sunrise and sunset, but it is important to know the requirements to use this option. Be sure to read the explanations on this subject in the information section of the program or in the gettings started section below.


## Getting Started

### OBJECT VISIBILITY AND OBSERVABLE PHASE RANGE

For object visibility, our program includes 138 observatories. The information of the observatories other than the few observatories we have added is taken from https://github.com/astropy/astropy-data/tree/gh-pages/coordinates. The existing observatory settings cannot be changed. Please select the manual option to make your own settings or edit the settings. You can click the "Edit Settings" button in the location, timezone and telescope limits settings section, fill in the relevant fields and edit the settings with the confirm button. When you open the program again, please click the "Save Settings" button to open the program with the settings you entered before. Please make sure you have entered the correct UTC. If you do not want to see the limits of the telescope on the object visibility graph, you can leave the minimum altitude and maximum altitude values of the telescope blank.

![locset](https://github.com/krmerdem/Astro-Observer-Plan/assets/115490296/679cd93c-888f-4379-962e-f87dc9824fdc)

![obs](https://github.com/krmerdem/Astro-Observer-Plan/assets/115490296/11d22bad-4dcd-4c68-bf76-e2a2ea223b88)


You can select the day you will observe from the Date section. 
The program opens with today's date by default. Date is valid for both object visibility and Observable Phase Range part.

In the Observable Phase Range on Selected Date section, period should be in days, and reference time should be in julian date. Phase range shows the phase range of the star you selected during the night hours of the date you selected. (for example, binary or multiple star systems). If astronomical night is not available for the current location, if astronomical twilight is available, the phase range is calculated according to the hours of the astronomical twilight interval.
For example, the result in Phase Range:

0.5161 - 0.5330 (1.0168)

![phase](https://github.com/krmerdem/Astro-Observer-Plan/assets/115490296/2efe7e3e-77b2-4655-9685-e862fabde98e)


Here 0.5161 is the beginning of the phase and 0.5330 is the end of the phase. The 1.0168 written in parentheses is the completed phase. For example, if the period of the star is 0.3864975 days (9.27594 hours) and the night interval on that day is 9.26 hours, the observable phase for that night is 9.27594 / 9.26 = 1.0168. Of course the phase range is always in the 0-1 range, we just show it so you can see the phase you've completed. According to the sample result, you completed one full phase and started to complete a new phase again.
In the "Coordinates of the object" section, enter the coordinates in RA (right ascension) and DEC (declination) formats. Enter the coordinate of only 1 object per line. For example, you should add the coordinates of the star Vega and Rigel as follows (hh:mm:ss dd:mm:ss):

18 36 56.3363 +38 47 01.280

05 14 32.2721 -08 12 05.898

![add](https://github.com/krmerdem/Astro-Observer-Plan/assets/115490296/9358e355-ea37-4e49-ac7a-37dc72d2dfcd)

You can change the theme and two properties of the object visibility graph. You can adjust the theme and these features according to your desire by clicking the button with the settings icon on the far right in the object visibility section. In addition, after the graphic appears, you can adjust the settings related to appearance and naming from the upper part according to your desire.

![graphset](https://github.com/krmerdem/Astro-Observer-Plan/assets/115490296/082fc156-f63a-464d-8d90-7675e4b06c92)

Also, when you search from Simbad, you will see informations about the relevant object. When you click the "+" button, Simbad will add the coordinates of the object you are searching from the database to the "Coordinates of the object" part. You can search the Simbad database by object name or coordinate. The query region option shows the objects in the area you specify. If you want to see only the information of the main object while searching (especially with the name), we recommend that you search in the range of 5-10 arcmin in the query region option. Apart from that, when you search in degrees, if there are too many objects in the area, the search may take a long time. For this reason, we have set a 1 degree limit for this program to work efficiently and properly for now. In the future, we will find a solution to this depending on the situation.

![add](https://github.com/krmerdem/Astro-Observer-Plan/assets/115490296/92b1aabc-0088-4375-a2e1-a469765a407e)

The Staralt option gives the altitude of the related object or objects on the date you selected. When Staralt is selected, when you click the "Show Object Visibility" button, the values written on the related object or objects every hour on the graph that comes before you are the angular distance value of the related object to the Moon. It also automatically adds the name of the relevant object to the chart. It gets the names from the simbad database. 

![staralt](https://github.com/krmerdem/Astro-Observer-Plan/assets/115490296/d2240b32-5ede-4ca5-8d3d-5404ca29bc64)

Starobs, on the other hand, gives the one-year altitude values of the related object or objects.

![starobs](https://github.com/krmerdem/Astro-Observer-Plan/assets/115490296/cb66934d-a83b-42e5-8c12-36c3a464f012)

In the astronomical times section, there are important hours for observation. Elevation(for sea level) correction option should be used under certain conditions. For example, for an observer on a mountain, it would be correct to use this option if the horizon line is below its current position. In summary, consider the horizon line at sea level and consider an observer on the mountain at this position. This option corrects for sunrise and sunset, taking into account elevation in addition to atmospheric refraction and solar disk diameter.
It also contains information about the Moon. You can see the Moon's rise, sunset, percent illuminated and phase for the relevant location and date. The position and phase of the Moon in the sky is very important in scientific observations and astrophotography.

### ASTRONOMICAL CATALOGS SEARCH

When you click on the search button on the 2nd line of the main menu, you will see the astronomical catalogs search section. You can search in SIMBAD, 2MASS All-Sky Point Source Catalog, AllWise Source Catalog, Gaia DR3 and ZTF DR 19 catalogues. You can also search in more than one catalogue. You can also limit the SIMBAD search to stars.

![catalog](https://github.com/krmerdem/Astro-Observer-Plan/assets/115490296/a7cca9fc-eeba-452b-bee3-1f57652b7693)

Apart from this, when you search in degrees, the search may take a long time if there are many objects in the area. For this reason, we have set a 1 degree limit for now in order for this program to work efficiently and properly. We will find a solution to this in the future, depending on the situation. Enter the area seen by your CCD or CMOS into the FOV value. For now the FOV is limited to a square area. We plan to customize this a lot in the future. After entering the FOV value and selecting the catalogs you want, click on the "Search and Show FOV" button and the search will start and when the search is finished, the results screen will open. The results screen includes an area image depending on your FOV value. You can see the results by clicking on the icons of the catalogs you searched in the vertical menu. Objects that you click or select with arrows in the grid are marked with a red square in the FOV area.

![catalog2](https://github.com/krmerdem/Astro-Observer-Plan/assets/115490296/0b85d75d-9ff7-43b1-a402-fc7b720ef0aa)

In the SIMBAD section, you can filter the results according to color B-V, G-V, U-B, g-r and i-z color indices. In the 2MASS section, you can filter the results according to J-H, H-K, J-K color indices. The reason why we put color indices is that they have an important place in astronomy. It is most commonly used in analysis and is used in the selection of check and comparison stars for observations of double stars or multiple star systems.

![filtered](https://github.com/krmerdem/Astro-Observer-Plan/assets/115490296/1e787b16-a97e-423a-82f7-bb9aaf5fea83)

For example, when J-H is selected in the 2MASS section, you must enter the J-H value of your main star in the "Index Value" box and then enter a value for a range in the "Range ±" box. For example, let's say the J-H index of our main star is 0.366. When we filter by entering 0.01 in the "Range ±" box, you will only see objects with J-H index between 0.356 and 0.376. These indices and filtering options will help you, but apart from these indices, the characteristics of the main star, the comparison star and the check star, such as their spectral type, object type and whether they show period change or not, whether they show brightness change or not, are also very important. Therefore, do not just stick to this program. We always recommend you analyze in more detail.



## Icons
The icons used in the program are taken from these addresses:

https://icons8.com
https://www.clipartmax.com/
https://feathericons.com/
https://brandeps.com/
https://cds.unistra.fr/
https://irsa.ipac.caltech.edu/
https://wise2.ipac.caltech.edu/
https://www.cosmos.esa.int/web/gaia/data-release-3
https://www.ztf.caltech.edu/

## Contact

For your comments, suggestions, questions or bug reports

```
Kerem ERDEM:  keremdive@gmail.com  
Korhan KARA:  korhankara98@gmail.com
``` 
