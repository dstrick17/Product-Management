import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns  # Import seaborn as sns (standard convention)

# Set a consistent style for all charts
sns.set_style('whitegrid')  # Use Seaborn's whitegrid style (similar to old 'seaborn')

# Chart 1: Weekly Active Users (WAU) - Monthly over 1 year
months = ['Feb 24', 'Mar 24', 'Apr 24', 'May 24', 'Jun 24', 'Jul 24', 
          'Aug 24', 'Sep 24', 'Oct 24', 'Nov 24', 'Dec 24', 'Jan 25', 'Feb 25']
wau = [500, 520, 550, 580, 600, 620, 650, 680, 700, 720, 730, 750, 780]  # Sample data

plt.figure(figsize=(8, 6))
plt.plot(months, wau, marker='o', color='b', linewidth=2)
plt.title('Weekly Active Users (WAU)', fontsize=16)
plt.xlabel('Months', fontsize=12)
plt.ylabel('Number of Active Users', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('wau_chart.png', dpi=300)
plt.close()

# [The rest of your code remains unchanged...]
# Chart 2: Onboarding Completion Rate - Monthly over 1 year
completion_rate = [50, 52, 55, 58, 60, 62, 65, 68, 70, 72, 73, 75, 78]  # Sample %

plt.figure(figsize=(8, 6))
plt.plot(months, completion_rate, marker='o', color='g', linewidth=2)
plt.title('Onboarding Completion Rate', fontsize=16)
plt.xlabel('Time (Months)', fontsize=12)
plt.ylabel('Completion Rate (%)', fontsize=12)
plt.ylim(0, 100)
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('completion_rate_chart.png', dpi=300)
plt.close()

# Chart 3: Time to Onboard - Bar chart with distribution
time_buckets = ['<5 min', '5-10 min', '>10 min']
users = [600, 300, 150]  # Sample user counts after 1 year

plt.figure(figsize=(8, 6))
plt.bar(time_buckets, users, color='orange', edgecolor='black')
plt.title('Time to Onboard', fontsize=16)
plt.xlabel('Time Buckets', fontsize=12)
plt.ylabel('Number of Users', fontsize=12)
plt.tight_layout()
plt.savefig('time_to_onboard_chart.png', dpi=300)
plt.close()

# Chart 4: Funnel Analysis - Onboarding Steps
steps = ['Sign-Up', 'Profile Setup', 'Feature Tour', 'Done']
funnel_data = [1000, 850, 750, 700]  # Sample user counts at each step

plt.figure(figsize=(8, 6))
plt.bar(steps, funnel_data, color='purple', edgecolor='black')
plt.title('Funnel Analysis - Onboarding Steps', fontsize=16)
plt.xlabel('Onboarding Steps', fontsize=12)
plt.ylabel('Number of Users', fontsize=12)
plt.tight_layout()
plt.savefig('funnel_analysis_chart.png', dpi=300)
plt.close()

# Chart 5: Customer Acquisition Cost (CAC) - Monthly over 1 year
cac = [200, 195, 190, 185, 180, 175, 170, 168, 165, 162, 160, 158, 155]  # Sample $ cost

plt.figure(figsize=(8, 6))
plt.plot(months, cac, marker='o', color='r', linewidth=2)
plt.title('Customer Acquisition Cost (CAC)', fontsize=16)
plt.xlabel('Months', fontsize=12)
plt.ylabel('Cost in Dollars ($)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('cac_chart.png', dpi=300)
plt.close()

# Chart 6: Net Promoter Score (NPS) - Quarterly over 1 year
quarters = ['Q1 24', 'Q2 24', 'Q3 24', 'Q4 24', 'Q1 25']
nps = [30, 35, 40, 45, 50]  # Sample scores

plt.figure(figsize=(8, 6))
plt.plot(quarters, nps, marker='o', color='teal', linewidth=2)
plt.title('Net Promoter Score (NPS)', fontsize=16)
plt.xlabel('Time (Quarters)', fontsize=12)
plt.ylabel('NPS Score', fontsize=12)
plt.ylim(-100, 100)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('nps_chart.png', dpi=300)
plt.close()

print("All charts have been saved as PNG files in your current directory!")