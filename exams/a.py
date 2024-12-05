import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load the CSV file
file_path = "exams.csv"  # Replace with your file path
df = pd.read_csv(file_path)

# Calculate the average scores for each subject
average_scores = df[["math score", "reading score", "writing score"]].mean()

# Print the results
print("Average Scores:")
print(f"Math score: {average_scores['math score']:.2f}")
print(f"Reading score: {average_scores['reading score']:.2f}")
print(f"Writing score: {average_scores['writing score']:.2f}")



# Calculate the total score for each student
df['total score'] = df['math score'] + df['reading score'] + df['writing score']

# Identify the top 5 students with the highest total scores
top_5_students = df.nlargest(5, 'total score')
print("Top 5 Students with Highest Total Scores:")
print(top_5_students)


plt.figure(figsize=(10, 6))
df[["math score", "reading score", "writing score"]].boxplot()

# Customize the chart
plt.title("Score Distribution for Each Subject", fontsize=16)
plt.ylabel("Scores", fontsize=12)
plt.xlabel("Subjects", fontsize=12)
plt.grid(True)

# Show the plot
plt.show()

# Calculate total scores
def calculate_below_50_percentage(column):
    return (df[column] < 50).mean() * 100

# Calculate percentages for each subject
subjects = ["math score", "reading score", "writing score"]
below_50_percentages = {subject: calculate_below_50_percentage(subject) for subject in subjects}

# Identify subjects where more than 30% of students scored below 50
subjects_below_threshold = [subject for subject, percentage in below_50_percentages.items() if percentage > 30]

# Print the results
print("Subjects where more than 30% of students scored below 50:")
for subject in subjects_below_threshold:
    print(f"{subject}: {below_50_percentages[subject]:.2f}% of students scored below 50")
else: print("No one scored below 50")
    
if "attendance" not in df.columns:
    print("The dataset must include an 'attendance' column to analyze.")
    exit()

df['total score'] = df['math score'] + df['reading score'] + df['writing score']

# Analyze the relationship between attendance and total score
plt.figure(figsize=(10, 6))
sns.scatterplot(x="attendance", y="total score", data=df, hue="attendance", palette="viridis")

# Customize the plot
plt.title("Relationship Between Attendance and Performance", fontsize=16)
plt.xlabel("Attendance (%)", fontsize=12)
plt.ylabel("Total Score", fontsize=12)
plt.grid(True)

# Show the plot
plt.show()

# Optional: Group data by attendance and calculate average total scores
attendance_performance = df.groupby("attendance")["total score"].mean().sort_index()

# Bar chart to visualize attendance vs. average performance
plt.figure(figsize=(10, 6))
attendance_performance.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Average Performance by Attendance Level", fontsize=16)
plt.xlabel("Attendance", fontsize=12)
plt.ylabel("Average Total Score", fontsize=12)
plt.grid(axis='y')

# Show the plot
plt.tight_layout()
plt.show()