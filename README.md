# Module 9 Challenge - Surfs Up!

## Overview of Surfs Up!
W. Avy wants to expand on the surf shop location weather data. Specifically, he wants to see the temperature data for Oahu in June and December in order to determine if the surf-and-ice-cream shop will be a sustainable year-round business.


## Analysis Tools

- Jupiter Notebook 6.3.0

- Python 3.7.10

- SQLite 3.36.0

- SQLAlchemy 1.4.7


## Results - Key Differences in Temperature

Figures 1 and 2 display the summary statistics for Oahu temperatures in June and December respectively:
Figure 1: [Oahu Temperatures Summary Statistics - June](https://github.com/pmoores/surfs_up/blob/main/Resources/Oahu%20Temperatures%20Summary%20Stats%20-%20June.png)
Figure 2: [Oahu Temperatures Summary Statistics - December](https://github.com/pmoores/surfs_up/blob/main/Resources/Oahu%20Temperatures%20Summary%20Stats%20-%20Dec.png)

The average temperature for each month is higher in June (75) vs. December (71).

The temperature ranges for each month (June: 64 to 85; December: 56 to 83) show that December reaches lower temperatures, but both months have similar highs. 

The standard deviations for both months are similar (June: 3.26 vs. Dec: 3.75), meaning the distribution of data is similar within each range.


## Summary

The results of the temperature analysis for Oahu in June and December show that, in terms of temperature, both months are ideal for a surf-and-ice-cream shop: 

 - The average temperatures are similar and ideal for outdoor beach activities

-  The temperatures for both months have similar distributions so the 'everyday temperature' works for outdoor beach activities

Two additional queries can be performed to gather more weather data June and December:

1. Gather summary statistics for precipitation data (mean, range, std dev)

2. Gather summary statistics from 2 other months that are spread six months apart (e.g. January and July) and compare these to the June and December statistics for an even more accurate annual weather picture of Oahu.



## Attachments

- [SurfsUp_Challenge.ipynb](https://github.com/pmoores/surfs_up/blob/main/SurfsUp_Challenge.ipynb)

- [hawaii.sqlite](https://github.com/pmoores/surfs_up/blob/main/hawaii.sqlite)

