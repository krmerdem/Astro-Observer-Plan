The new update will be released on February 17, 2025.

# ASTRO OBSERVER PLAN - PySide6

![header](https://github.com/krmerdem/Astro-Observer-Plan/assets/115490296/06b5baa8-9c8d-4419-9ad1-a7f8db797a71)

Astronomy software built with Python and PySide 6 for astronomical observations.

IMPORTANT NOTE: Please read the information part of the software before you start using the software. 

v24.1 Notes
- Windows 10/11 dark mode compatibility has been adjusted.
- Added summer and winter time correction, taking into account daylight saving time. All timezones added.
- Pecaut&Mamajek's EEM_dwarf_UBVIJHK_colors_Teff table has been added to the software, and you can find the appropriate color index values from this table, and view the star parameters depending on this table according to the color indexes of each star selected in the search results. Please note that this applies to main sequence stars.
- Improved the FOV display in search results. You can show all the objects in the Simbad, 2MASS and Gaia DR3 results on the FOV screen, and when you click on the marked objects on the image, the object is marked in the table in the relevant catalog.
- Necessary adjustments were made to make the simbad search results in the object visibility section more readable.
- Ubuntu version added. (currently being edited)

## Download and Installing Software

The software is compatible with 64-bit versions of Windows 10 and Windows 11. Currently, the software has a ZIP extension. After downloading the ZIP, extract the archive and run AstroObserverPlan.exe

[Astro Observer Plan v24.1 Download - (Windows 10/11 x64)](https://github.com/krmerdem/Astro-Observer-Plan/releases/download/v24.1/Astro.Observer.Plan.zip)

Instructions to run on Ubuntu:
Follow the necessary steps to make it work in two different window managers: x11 and wayland.
- Open the terminal and enter the following command.

  sudo apt install libxcb-*

- After the installation is completed, right-click on the AstroObserverPlan.tar.gz file and click extract.
- Alternatively, open a terminal where the AstroObserverPlan.tar.gz archive is located and enter the following command:

  tar -xvf AstroObserverPlan.tar.gz

- After the extraction process is completed, enter the folder and right-click on AstroObserverPlan. "Executable as Program" at the bottom of the window should be checked or open. After this stage, you can run the software by double-clicking on AstroObserverPlan.
- Alternatively, go into the AstroObserverPlan folder, right-click on an empty area and click "Open in terminal". You can open the software by typing ./AstroObserverPlan into the terminal.

[Astro Observer Plan v24.1 Download - (Ubuntu 22.04+) - (currently being edited)](https://github.com/krmerdem/Astro-Observer-Plan/releases/download/v23.2.1/AstroObserverPlan.tar.gz) 

## Installing Dependencies

**INFO** | When the software is downloaded, the dependencies that it needs are available in the software. The software has been tested and works on Windows 10, Windows 11, Ubuntu 22.04 and Ubuntu 23.10 operating systems.

**Dependencies used in the software** | PySide6, Matplotlib, NumPy, Astroquery, Astropy, Ephem, pytz

## Introduction

The software calculates the daily or annual altitude of the selected star or object according to its position on Earth and its angular distance to the Moon and displays it on the graph. It also calculates the observable phase range for binary stars or multiple star systems. It also displays astronomical times depending on the location. There is a degree-minute-second or hour-minute-second converter required for astronomy in the software. In the software, you can search Simbad, 2MASS, WISE, Gaia DR3 and ZTF DR19 catalogs at the same time.

Optionally, it also performs elevation correction at sunrise and sunset, but it is important to know the requirements to use this option. Be sure to read the explanations on this subject in the information section of the software or in the gettings started section below.

Some tables in Pecaut&Mamajek's 2013 article titled "Intrinsic Colors, Temperatures and Bolometric Corrections of Pre-Main Sequence Stars" and the table at "https://www.pas.rochester.edu/~emamajek/EEM_dwarf_UBVIJHK_colors_Teff.txt" have been added to the software. In the search results in the software, you can view the relevant star parameters from the EEM_dwarf_UBVIJHK_colors_Teff table according to the color indexes of each star. Detailed explanation is available in the usage section of the software.


## Getting Started

### OBJECT VISIBILITY AND OBSERVABLE PHASE RANGE

For object visibility, software includes 138 observatories. The information of the observatories other than the few observatories we have added is taken from https://github.com/astropy/astropy-data/tree/gh-pages/coordinates. The existing observatory settings cannot be changed. Please select the manual option to make your own settings or edit the settings. You can click the "Edit Settings" button in the location, timezone and telescope limits settings section, fill in the relevant fields and edit the settings with the confirm button. When you open the software again, please click the "Save Settings" button to open the software with the settings you entered before. Please make sure you choose the correct timezone. If you do not want to see the limits of the telescope on the object visibility graph, you can leave the minimum altitude and maximum altitude values of the telescope blank.

![1](https://github.com/krmerdem/Astro-Observer-Plan/assets/115490296/d28ccf23-ad02-437e-a986-99daaf3178a1)

![2](https://github.com/krmerdem/Astro-Observer-Plan/assets/115490296/94d7c40a-eac5-487d-a791-01e7dd8e40f0)

You can select the day you will observe from the Date section. 
The software opens with today's date by default. Date is valid for both object visibility and Observable Phase Range part.

In the Observable Phase Range on Selected Date section, period should be in days, and reference time should be in julian date. Phase range shows the phase range of the star you selected during the night hours of the date you selected. (for example, binary or multiple star systems). If astronomical night is not available for the current location, if astronomical twilight is available, the phase range is calculated according to the hours of the astronomical twilight interval.
For example, the result in Phase Range:

0.5161 - 0.5330 (1.0168)

![phase](https://github.com/krmerdem/Astro-Observer-Plan/assets/115490296/2efe7e3e-77b2-4655-9685-e862fabde98e)


Here 0.5161 is the beginning of the phase and 0.5330 is the end of the phase. The 1.0168 written in parentheses is the completed phase. For example, if the period of the star is 0.3864975 days (9.27594 hours) and the night interval on that day is 9.26 hours, the observable phase for that night is 9.27594 / 9.26 = 1.0168. Of course the phase range is always in the 0-1 range, we just show it so you can see the phase you've completed. According to the sample result, you completed one full phase and started to complete a new phase again.
In the "Coordinates of the object" section, enter the coordinates in RA (right ascension) and DEC (declination) formats. Enter the coordinate of only 1 object per line. For example, you should add the coordinates of the star Vega and Rigel as follows (hh:mm:ss dd:mm:ss):

18 36 56.3363 +38 47 01.280

05 14 32.2721 -08 12 05.898

![2](https://github.com/krmerdem/Astro-Observer-Plan/assets/115490296/6ba5c2c2-fdb8-4228-b25c-831c5c27771c)

You can change the theme and two properties of the object visibility graph. You can adjust the theme and these features according to your desire by clicking the button with the settings icon on the far right in the object visibility section. In addition, after the graphic appears, you can adjust the settings related to appearance and naming from the upper part according to your desire.

![3](https://github.com/krmerdem/Astro-Observer-Plan/assets/115490296/35b822e8-cf71-4535-8870-ee7bfe0f7114)

Also, when you search from Simbad, you will see informations about the relevant object. When you click the "+" button, Simbad will add the coordinates of the object you are searching from the database to the "Coordinates of the object" part. You can search the Simbad database by object name or coordinate. The query region option shows the objects in the area you specify. If you want to see only the information of the main object while searching (especially with the name), we recommend that you search in the range of 5-10 arcsec in the query region option. Apart from that, when you search in degrees, if there are too many objects in the area, the search may take a long time. For this reason, we have set a 1 degree limit for this software to work efficiently and properly for now. In the future, we will find a solution to this depending on the situation.

![4](https://github.com/krmerdem/Astro-Observer-Plan/assets/115490296/88311a7f-df80-46ac-8e8d-52a98f6db53c)

The Staralt option gives the altitude of the related object or objects on the date you selected. When Staralt is selected, when you click the "Show Object Visibility" button, the values written on the related object or objects every hour on the graph that comes before you are the angular distance value of the related object to the Moon. It also automatically adds the name of the relevant object to the chart. It gets the names from the simbad database. 

![5](https://github.com/krmerdem/Astro-Observer-Plan/assets/115490296/bf8b9f59-e0ca-4b0e-9476-acc834acc984)

Starobs, on the other hand, gives the one-year altitude values of the related object or objects.

![6](https://github.com/krmerdem/Astro-Observer-Plan/assets/115490296/7dab7b7e-f7b5-47a7-89d9-bc2dfc2d9ae2)

In the astronomical times section, there are important hours for observation. Elevation(for sea level) correction option should be used under certain conditions. For example, for an observer on a mountain, it would be correct to use this option if the horizon line is below its current position. In summary, consider the horizon line at sea level and consider an observer on the mountain at this position. This option corrects for sunrise and sunset, taking into account elevation in addition to atmospheric refraction and solar disk diameter.
It also contains information about the Moon. You can see the Moon's rise, sunset, percent illuminated and phase for the relevant location and date. The position and phase of the Moon in the sky is very important in scientific observations and astrophotography.

### ASTRONOMICAL CATALOGS SEARCH

When you click on the search button on the 2nd line of the main menu, you will see the astronomical catalogs search section. You can search in SIMBAD, 2MASS All-Sky Point Source Catalog, AllWise Source Catalog, Gaia DR3 and ZTF DR 19 catalogues. You can also search in more than one catalogue. You can also limit the SIMBAD search to stars.

![7](https://github.com/krmerdem/Astro-Observer-Plan/assets/115490296/bdb73cca-5b1e-4bd2-ae28-fa4e93ef0f7a)

Apart from this, when you search in degrees, the search may take a long time if there are many objects in the area. For this reason, we have set a 1 degree limit for now in order for this software to work efficiently and properly. We will find a solution to this in the future, depending on the situation. Enter the FOV value of the CCD and CMOS you use depending on the telescope. For now the FOV is limited to a square area. We plan to customize this a lot in the future. After entering the FOV value and selecting the catalogs you want, click on the "Search and Show FOV" button and the search will start and when the search is finished, the results screen will open. The results screen includes an area image depending on your FOV value. You can see the results by clicking on the icons of the catalogs you searched in the vertical menu.

![8](https://github.com/krmerdem/Astro-Observer-Plan/assets/115490296/32ea0f07-fae2-4145-80c3-b9a9f386e9a9)

On the search results screen you will see the options None, Mark all Simbad objects, Mark all 2MASS objects, and Mark all Gaia DR3 objects. For example, when you select the “Mark all Simbad objects” option, all objects in the Simbad table will be marked on the FOV screen according to your search results. When you click on the objects marked on the FOV screen, the relevant object is shown in the Simbad table. On the other hand, when you select an object in the table, the object you selected is marked on the FOV screen. If you selected "Mark all 2MASS objects" and clicked on a marked object in the FOV screen, the object you selected will be shown in the 2MASS table. Please be careful with it. All objects are marked with a red circle. The object you select from the table or FOV screen is marked with a cyan circle. You can adjust the color of the markings from the "Settings" section in the top menu. You can remove the markings you have made from the "Unmark Menu". You can rotate the x and y axes 180 degrees from "Chart Settings". You can turn the pointer on or off from "Pointer Settings".

![11](https://github.com/krmerdem/Astro-Observer-Plan/assets/115490296/0f87b177-f094-4d7a-bb50-5c94539ff314)

![12](https://github.com/krmerdem/Astro-Observer-Plan/assets/115490296/5a5e12a3-bb00-4253-b349-a0bf74d8ea97)

![9](https://github.com/krmerdem/Astro-Observer-Plan/assets/115490296/196ca463-1615-4790-ae70-33f0c8d096f1)

![10](https://github.com/krmerdem/Astro-Observer-Plan/assets/115490296/6076df14-2051-4ce4-8e32-495525a917dc)

The right-click menu is active in the table. When you right-click on an object you want, you can mark the object as main object, comparison object and check object. Additionally, by clicking on the "Show Pecaut and Mamajek Teff-SpT" option, you will see the physical properties and parameters of the object you selected in a tabular form, according to the color indices in the Pecaut and Mamajek Teff-SpT table. There is a more detailed explanation later in the article. Please note that the Pecaut and Mamajek Teff-SpT table is valid for main sequence stars.

![13](https://github.com/krmerdem/Astro-Observer-Plan/assets/115490296/41636e51-1e17-4c16-906c-de8bf0b2238d)

![14](https://github.com/krmerdem/Astro-Observer-Plan/assets/115490296/17814ef0-7800-48b4-846e-b9b14442c386)

In the SIMBAD section, you can filter the results according to color B-V, G-V, U-B, g-r, i-z, J-H, H-K and J-H color indices. In the 2MASS section, you can filter the results according to J-H, H-K, J-K color indices. The reason why we put color indices is that they have an important place in astronomy. It is most commonly used in analysis and is used in the selection of check and comparison stars for observations of binary stars or multiple star systems.

![15](https://github.com/krmerdem/Astro-Observer-Plan/assets/115490296/966ba448-a135-4508-bb00-caa1bebb5939)

For example, when J-H is selected in the 2MASS section, you must enter the J-H value of your main star in the "Index Value" box and then enter a value for a range in the "Range ±" box. For example, let's say the J-H index of our main star is 0.366. When we filter by entering 0.01 in the "Range ±" box, you will only see objects with J-H index between 0.356 and 0.376. These indices and filtering options will help you, but apart from these indices, the characteristics of the main star, the comparison star and the check star, such as their spectral type, object type and whether they show period change or not, whether they show brightness change or not, are also very important. Therefore, do not just stick to this software. We always recommend you analyze in more detail.

When you select a star from the relevant table in the search results, right-click and select "Show Pecaut and Mamajek Teff-SpT", you will see the Pecaut and Mamajek Teff-SpT table for the color indices of the star you selected. For example, you clicked on a star in the simbad catalog in the search results and displayed the Pecaut and Mamajek Teff-SpT table as described. For example, the B-V value in the SIMBAD table is searched among all B-V values in the Pecaut and Mamajek Teff-SpT table and the two closest B-V values are selected. The star parameters for these two selected B-V values are shown in the table that appears. All existing color indices work with the same logic.

The names of the main object, comparison object and check objects you selected are located at the bottom of the window.

![16](https://github.com/krmerdem/Astro-Observer-Plan/assets/115490296/5541e6a9-fc58-4ebc-8472-fb2371f3a082)

## Icons
The icons used in the software are taken from these addresses:

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
