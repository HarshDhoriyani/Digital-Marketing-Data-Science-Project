# Let's reconnect the dataset with the code to ensure it runs smoothly
import pandas as pd
# First, reload the dataset (already loaded previously)
data = pd.read_csv("C:\FINLATICS\Digital Marketing\online_advertising_performance_data.csv")

# Execute the code for all the analysis and answers to the questions

import matplotlib.pyplot as plt
import seaborn as sns

# 1. What is the overall trend in user engagement throughout the campaign period?
engagement_trend = data.groupby(['month', 'user_engagement']).size().unstack(fill_value=0)
print("Overall Trend in User Engagement:")
print(engagement_trend)

# 2. How does the size of the ad (banner) impact the number of clicks generated?
banner_clicks = data.groupby('banner')['clicks'].sum().reset_index()
print("\nBanner Size Impact on Clicks:")
print(banner_clicks)

# 3. Which publisher spaces (placements) yielded the highest number of displays and clicks?
placement_performance = data.groupby('placement')[['displays', 'clicks']].sum().reset_index()
top_placements = placement_performance.sort_values(by=['displays', 'clicks'], ascending=False)
print("\nTop Placements by Displays and Clicks:")
print(top_placements)

# 4. Is there a correlation between the cost of serving ads and the revenue generated from clicks?
correlation_cost_revenue = data[['cost', 'revenue']].corr()
print("\nCorrelation between Cost and Revenue:")
print(correlation_cost_revenue)

# 5. What is the average revenue generated per click for Company X during the campaign period?
average_revenue_per_click = data['revenue'].sum() / data['clicks'].sum()
print("\nAverage Revenue per Click:")
print(average_revenue_per_click)

# 6. Which campaigns had the highest post-click conversion rates?
data['conversion_rate'] = data['post_click_conversions'] / data['clicks']
highest_conversion_campaigns = data.groupby('campaign_number')['conversion_rate'].mean().reset_index()
print("\nCampaigns with Highest Post-Click Conversion Rates:")
print(highest_conversion_campaigns.sort_values(by='conversion_rate', ascending=False))

# 7. Are there any specific trends or patterns in post-click sales amounts over time?
sales_trend = data.groupby('day')['post_click_sales_amount'].sum().reset_index()
print("\nTrend in Post-Click Sales Amounts Over Time:")
print(sales_trend)

# 8. How does the level of user engagement vary across different banner sizes?
engagement_banner = data.groupby(['banner', 'user_engagement']).size().unstack(fill_value=0)
print("\nUser Engagement Across Banner Sizes:")
print(engagement_banner)

# 9. Which placement types result in the highest post-click conversion rates?
placement_conversion_rate = data.groupby('placement')['conversion_rate'].mean().reset_index()
top_conversion_placements = placement_conversion_rate.sort_values(by='conversion_rate', ascending=False)
print("\nPlacements with Highest Conversion Rates:")
print(top_conversion_placements)

# 10. Can we identify any seasonal patterns or fluctuations in displays and clicks throughout the campaign period?
displays_clicks_trend = data.groupby(['month'])[['displays', 'clicks']].sum().reset_index()
print("\nSeasonal Patterns in Displays and Clicks:")
print(displays_clicks_trend)

# 11. Is there a correlation between user engagement levels and the revenue generated?
correlation_engagement_revenue = data.groupby('user_engagement')['revenue'].sum().reset_index()
print("\nRevenue Based on User Engagement Levels:")
print(correlation_engagement_revenue)

# 12. Are there any outliers in terms of cost, clicks, or revenue that warrant further investigation?
outliers = data[(data['cost'] > data['cost'].quantile(0.95)) |
                (data['clicks'] > data['clicks'].quantile(0.95)) |
                (data['revenue'] > data['revenue'].quantile(0.95))]
print("\nOutliers in Cost, Clicks, or Revenue:")
print(outliers)

# 13. How does the effectiveness of campaigns vary based on the size of the ad and placement type?
effectiveness = data.groupby(['banner', 'placement'])[['clicks', 'revenue', 'post_click_conversions']].sum().reset_index()
print("\nEffectiveness by Banner Size and Placement Type:")
print(effectiveness)

# 14. Are there any specific campaigns or banner sizes that consistently outperform others in terms of ROI?
data['ROI'] = data['revenue'] / data['cost']
roi_performance = data.groupby(['campaign_number', 'banner'])['ROI'].mean().reset_index()
print("\nCampaigns and Banner Sizes with Highest ROI:")
print(roi_performance.sort_values(by='ROI', ascending=False))

# 15. What is the distribution of post-click conversions across different placement types?
placement_conversion_distribution = data.groupby('placement')['post_click_conversions'].sum().reset_index()
print("\nDistribution of Post-Click Conversions Across Placements:")
print(placement_conversion_distribution)

# 16. Are there any noticeable differences in user engagement levels between weekdays and weekends?
weekday_engagement = data.groupby('day')['user_engagement'].value_counts().unstack(fill_value=0)
print("\nUser Engagement Between Weekdays and Weekends:")
print(weekday_engagement)

# 17. How does the cost per click (CPC) vary across different campaigns and banner sizes?
data['CPC'] = data['cost'] / data['clicks']
cpc_analysis = data.groupby(['campaign_number', 'banner'])['CPC'].mean().reset_index()
print("\nCost per Click (CPC) Across Campaigns and Banner Sizes:")
print(cpc_analysis)

# 18. Are there any campaigns or placements that are particularly cost-effective in terms of generating post-click conversions?
cost_per_conversion = data['cost'] / data['post_click_conversions']
data['cost_per_conversion'] = cost_per_conversion
cost_effective_campaigns = data.groupby(['campaign_number', 'placement'])['cost_per_conversion'].mean().reset_index()
print("\nCost-Effective Campaigns and Placements:")
print(cost_effective_campaigns)

# 19. Can we identify any trends or patterns in post-click conversion rates based on the day of the week?
conversion_rate_by_day = data.groupby('day')['conversion_rate'].mean().reset_index()
print("\nTrends in Post-Click Conversion Rates by Day of the Week:")
print(conversion_rate_by_day)

# 20. How does the effectiveness of campaigns vary throughout different user engagement types in terms of post-click conversions?
engagement_conversion_effectiveness = data.groupby('user_engagement')['post_click_conversions'].sum().reset_index()
print("\nEffectiveness of Campaigns by User Engagement Type:")
print(engagement_conversion_effectiveness)
