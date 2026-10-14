
import plotly.express as px
import pandas as pd

# Student Mathematics marks
data = {
    "Student": [
        "S1", "S2", "S3", "S4", "S5",
        "S6", "S7", "S8", "S9", "S10"
    ],
    "Mathematics": [
        78, 85, 67, 90, 73,
        81, 69, 94, 76, 88
    ]
}

df = pd.DataFrame(data)

# Create interactive bar chart
fig = px.bar(
    df,
    x="Student",
    y="Mathematics",
    title="Students' Mathematics Examination Marks",
    labels={
        "Student": "Student",
        "Mathematics": "Marks"
    },
    text="Mathematics"
)

fig.update_traces(
    textposition="outside",
    hovertemplate=(
        "Student: %{x}<br>"
        "Mathematics Marks: %{y}<extra></extra>"
    )
)

fig.update_layout(
    xaxis_title="Student",
    yaxis_title="Mathematics Marks",
    yaxis=dict(range=[0, 105])
)

# Display interactive chart
fig.show()

# Display highest and lowest marks
highest = df.loc[df["Mathematics"].idxmax()]
lowest = df.loc[df["Mathematics"].idxmin()]

print(
    f"Highest Marks: {highest['Student']} - "
    f"{highest['Mathematics']}"
)

print(
    f"Lowest Marks: {lowest['Student']} - "
    f"{lowest['Mathematics']}"
)
