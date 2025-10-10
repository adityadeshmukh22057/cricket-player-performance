# Cricket Player Performance Analysis - User Guide

## Quick Start

This guide will help you get started with the Cricket Player Performance Analysis project.

---

## Installation

### Step 1: Clone the Repository
```bash
git clone <your-repository-url>
cd <repository-directory>
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

Or install packages individually:
```bash
pip install pandas numpy matplotlib seaborn jupyter
```

---

## Running the Analysis

### Method 1: Complete Analysis Script (Recommended)

Run the full analysis with all features:

```bash
python cricket_analysis.py
```

**This will:**
- Load and display dataset information
- Perform batting performance analysis
- Analyze bowling statistics
- Evaluate all-rounder contributions
- Compare team performances
- Identify match-winning factors
- Generate 8 visualizations
- Display key insights

**Output:** Analysis results printed to console + visualizations saved in `visualizations/` folder

---

### Method 2: Interactive Menu (Easy Mode)

Use the interactive menu for simplified access:

```bash
python run_analysis.py
```

**Menu Options:**
1. **Run Complete Analysis** - Full analysis with all features
2. **View Quick Statistics** - Quick summary without visualizations
3. **Generate Visualizations Only** - Create charts without full analysis
4. **Exit** - Close the program

---

### Method 3: Jupyter Notebook (Best for Learning)

Open the interactive notebook:

```bash
jupyter notebook notebooks/cricket_analysis.ipynb
```

**Features:**
- Step-by-step analysis cells
- Inline visualizations
- Editable code blocks
- Markdown documentation
- Interactive exploration

---

## Understanding the Output

### Console Output

The analysis prints several sections:

1. **Basic Data Information**
   - Dataset shape and structure
   - Column names and data types
   - Statistical summary
   - Missing value check

2. **Batting Performance**
   - Top run scorers
   - Best batting averages
   - Most aggressive batsmen
   - Century and half-century statistics

3. **Bowling Performance**
   - Top wicket takers
   - Best bowling averages
   - Most economical bowlers
   - Wicket-taking efficiency

4. **All-Rounder Analysis**
   - Combined contributions
   - Impact scores
   - Value assessment

5. **Team Performance**
   - Win/loss records
   - Team comparisons
   - Win percentages

6. **Match-Winning Factors**
   - Key performance indicators
   - Winning vs losing metrics
   - Role-wise contributions

7. **Key Insights**
   - Most impactful players
   - Critical success factors
   - Performance patterns

### Visualizations Generated

All visualizations are saved in `visualizations/` folder:

1. **top_performers.png**
   - Top 10 run scorers
   - Top 10 wicket takers

2. **batting_analysis.png**
   - Strike rate vs batting average scatter plot
   - Size represents centuries scored

3. **bowling_analysis.png**
   - Economy rate vs bowling average
   - Size represents wickets taken

4. **team_performance.png**
   - Total runs by team (bar chart)

5. **win_loss_analysis.png**
   - Average runs: won vs lost
   - Average strike rate: won vs lost

6. **role_distribution.png**
   - Player roles pie chart

7. **correlation_heatmap.png**
   - Performance metrics correlation matrix

8. **summary_dashboard.png**
   - 4-panel overview of key metrics

---

## Customizing the Analysis

### Using Your Own Data

Replace `data/cricket_data.csv` with your dataset. Ensure it has these columns:

- Player_Name
- Team
- Matches
- Innings
- Runs
- Highest_Score
- Average
- Strike_Rate
- Centuries
- Half_Centuries
- Wickets
- Bowling_Average
- Economy
- Best_Bowling
- Role
- Match_Result

### Modifying the Analysis

Edit `cricket_analysis.py` (examples shown are pseudocode for illustration):

```python
# Example: Change minimum runs threshold for batting analysis
# In the analyze_batting_performance method, modify:
batsmen = self.df[self.df['Runs'] > 1000]  # Changed from 500

# Example: Change top N players displayed
# In the same method, modify:
top_scorers = self.df.groupby('Player_Name')['Runs'].sum().sort_values(ascending=False).head(15)  # Changed from 10
```

### Creating Custom Visualizations

Add new visualization methods to the `CricketAnalyzer` class:

```python
def my_custom_visualization(self):
    """Create a custom visualization"""
    plt.figure(figsize=(10, 6))
    # Your plotting code here
    plt.savefig('visualizations/custom_plot.png', dpi=300, bbox_inches='tight')
```

---

## Working with Jupyter Notebook

### Opening Specific Sections

The notebook is organized into sections:
- Section 1-3: Setup and data loading
- Section 4: Batting analysis
- Section 5: Bowling analysis
- Section 6: Team performance
- Section 7: Match-winning factors
- Section 8: Correlation analysis
- Section 9: Key insights
- Section 10: Conclusion

### Running All Cells

```
Cell → Run All
```

### Running Individual Cells

Click cell, then press `Shift + Enter`

### Modifying Code

All code cells are editable. Make changes and re-run to see results.

---

## Troubleshooting

### Issue: Module not found error
**Solution:** Install missing package
```bash
pip install <package_name>
```

### Issue: File not found error
**Solution:** Ensure you're in the project root directory
```bash
cd <repository-directory>
python cricket_analysis.py
```

### Issue: Visualization not displaying
**Solution:** Check if `visualizations/` folder exists
```bash
mkdir -p visualizations
```

### Issue: Permission denied
**Solution:** Make script executable
```bash
chmod +x run_analysis.py
```

---

## Advanced Usage

### Python Script Integration

Import the analyzer in your own scripts:

```python
from cricket_analysis import CricketAnalyzer

# Create analyzer instance
analyzer = CricketAnalyzer('data/cricket_data.csv')

# Load data
df = analyzer.load_data()

# Run specific analyses
analyzer.analyze_batting_performance()
analyzer.create_visualizations()
analyzer.generate_insights()
```

### Batch Analysis

Analyze multiple datasets:

```python
datasets = ['data/cricket_data.csv', 'data/cricket_data2.csv']

for dataset in datasets:
    analyzer = CricketAnalyzer(dataset)
    analyzer.load_data()
    analyzer.display_basic_info()
    # ... more analysis
```

---

## Interpreting Results

### Batting Metrics
- **Average:** Runs per innings (higher is better)
- **Strike Rate:** Runs per 100 balls (higher = more aggressive)
- **Centuries:** Innings with 100+ runs
- **Half-Centuries:** Innings with 50-99 runs

### Bowling Metrics
- **Wickets:** Total dismissals (higher is better)
- **Bowling Average:** Runs conceded per wicket (lower is better)
- **Economy:** Runs per over (lower is better)

### Key Insights
- **Run Difference:** Average runs scored in wins vs losses
- **Strike Rate Impact:** How aggression affects match outcomes
- **Role Value:** Contribution by player position
- **Team Strength:** Overall performance comparison

---

## Best Practices

1. **Always check data quality** before analysis
2. **Review visualizations** for patterns and outliers
3. **Compare metrics** across different dimensions
4. **Consider context** when interpreting results
5. **Validate findings** with domain knowledge
6. **Document insights** for future reference

---

## Additional Resources

- **README.md** - Project overview and setup
- **FINDINGS.md** - Detailed analysis findings
- **cricket_analysis.py** - Source code with comments
- **notebooks/cricket_analysis.ipynb** - Interactive tutorial

---

## Support

For issues or questions:
1. Check this user guide
2. Review the README.md
3. Examine code comments
4. Open an issue on GitHub

---

**Happy Analyzing! 🏏📊**
