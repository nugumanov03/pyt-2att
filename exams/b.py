import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset from a CSV file
file_path = "exams.csv"  # Replace with the path to your CSV file
df = pd.read_csv(file_path)

# Define the subjects
subjects = ["math score", "reading score", "writing score"]

# Plot a pie chart for each subject
for subject in subjects:
    plt.figure(figsize=(8, 8))
    
    # Define score ranges for distribution
    bins = [0, 50, 70, 85, 100]
    labels = ['<50', '50-70', '70-85', '85-100']
    score_distribution = pd.cut(df[subject], bins=bins, labels=labels).value_counts()
    
    # Plot pie chart
    score_distribution.plot(kind='pie', autopct='%1.1f%%', startangle=90, colormap="viridis", legend=False)
    plt.title(f"Score Distribution for {subject.capitalize()}", fontsize=16)
    plt.ylabel("")  # Remove y-axis label
    plt.tight_layout()
    
    # Show the chart
    plt.show()
