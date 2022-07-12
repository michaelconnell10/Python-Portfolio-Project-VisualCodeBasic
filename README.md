# 1.-Data-Analysis-Description

Software/Equipment Used: Mac OS, Visual Code Basic, Python

The purpse of this project is to display various skills common to data analysis as a way to show my skills.

The objective is to quantify each score that has been awared on every series of Strictly Come Dancing (except 1, but I will explain this further down) to see if there is a statistical trend between when dances are typically performed during the season.

I hypothesize that there will be a statistical reason of why some dances are performed earlier versus later (that goes beyond the technique of the dance). However, I aim to answer the following questions:
  1. Are certain dances given lower scores due to being performed earlier in the season (Cha-Cha, Salsa) when the average scores across the cast will be        lower?
  2. Do we have any issues where certain dances trend higher because of a lower sample size due to, on average, being performed later?
  3. Does the statistically best celebrity end up winning the series or is this purely a popularity contest disguised as a dancing compeition?

The main language I will be conducting this in will be Python

The "timeline" of the repositories will be as follows:

1. Data Scraping - I will use Python to scrape the Wikipedia pages and then convert the data into .csv
2. Data Cleaning - I will use Python to clean up the data
3. Statistical Analysis - I will conduct this in both Excel and Python utilizing Numpy, Pandas, Matplotlib, and Seaborn
4. Visual Analysis - I will conduct some visual analysis using Tableau Public

At the end of the project, I hope to have displayed the following skills:
- Data Scraping
- Data Cleaning
- Statistical Analysis
- Tableau
- Python

*****Something of note is that I have intentionally missed out the 2020 series (series 18) for 2 reasons.

1. Due to the Covid-19 pandemic, the cast had 4 less contestants (12 down from the usual 16 in modern seasons) and the season was shortened by 4 weeks. This meant that the number of dances performed by each constestant was shorted as well.
2. However, the main reason was that because one of the judges could not travel over from USA, the judging panel was 3 instead of 4 - making the highest possible score 30, instead of 40.
  As such, I made the final decision to leave out this series purely because using the scores out of 30 would affect the precision of the data whether it     increase or decrease the averages and normalizing the scores out of 30 to scores out of 40 would affect the accuracy. And although normalizing the scores   to out of 40 would have given us an idea of what the scores would have been under normal circumstances, we never fully know if that would be the case.
