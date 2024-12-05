import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "exams.csv"  # Replace with the path to your CSV file
df = pd.read_csv(file_path)

# Calculate average scores for students based on test preparation course status
test_prep_group = df.groupby('test preparation course')[['math score', 'reading score', 'writing score']].mean()

# Visualize the relationship using a bar chart
test_prep_group.plot(kind='bar', figsize=(10, 6), color=['#1f77b4', '#ff7f0e', '#2ca02c'])
plt.title("Average Scores by Test Preparation Course", fontsize=16)
plt.xlabel("Test Preparation Course Status", fontsize=12)
plt.ylabel("Average Score", fontsize=12)
plt.xticks(rotation=0)
plt.legend(title="Subjects")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Show the plot
plt.show()
