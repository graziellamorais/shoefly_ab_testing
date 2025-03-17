# Ad Click Analysis Project  

## 📌 **Project Overview**  
This project analyzes an A/B test conducted to compare the effectiveness of two different ads, **Ad A** and **Ad B**. The goal is to identify which ad generated higher user engagement (click-through rate) and to determine if the engagement patterns varied by day of the week.

---

## 📂 **Project Structure**  
├── ad_clicks.csv # Dataset containing user interactions with ads
├── ad_click_analysis.ipynb # Jupyter Notebook with the analysis code
├── README.md # Project documentation


---

## 📝 **Objective**  
1. Analyze the total number of views from different ad platforms.  
2. Calculate the percentage of users who clicked on each ad.  
3. Compare the performance of **Ad A** vs. **Ad B** based on click-through rates.  
4. Analyze click patterns over the course of the week.  
5. Recommend which ad the company should use based on the results.  

---

## 📊 **Methodology**  
1. **Data Cleaning:**  
   - Handled missing values and inconsistencies.  
   - Created a new column `is_click` to identify if the ad was clicked.  

2. **Performance by Platform:**  
   - Grouped data by `utm_source` to calculate total views and click rates.  
   - Used a pivot table to reshape the data.  

3. **A/B Test Performance:**  
   - Grouped data by `experimental_group` to calculate the click-through rate.  
   - Compared the performance of Ad A and Ad B using percentage-based analysis.  

4. **Day of the Week Analysis:**  
   - Grouped data by `day` and `is_click` for each ad group.  
   - Created pivot tables to calculate daily click rates.  
   - Merged the results for side-by-side comparison.  

---

## 💡 **Key Findings**  
✅ **Ad A outperformed Ad B** on most days of the week:  
- Ad A had higher click rates on **Monday, Wednesday, Thursday, Friday, and Sunday**.  
- Ad B only performed better on **Tuesday and Saturday**, but the difference was small.  

✅ **Highest Performance:**  
- Ad A peaked on **Thursday (40.52%)** and **Friday (39.84%)**.  
- Ad B peaked on **Tuesday (37.82%)** and **Saturday (35.59%)**.  

✅ **Recommendation:**  
- The company should **go with Ad A** since it demonstrated more consistent and higher engagement across the week.  
- Further testing could explore why Ad B performed better on Tuesday and Saturday.  

---

## 🚀 **Technologies Used**  
- **Python**  
- **Pandas**  
