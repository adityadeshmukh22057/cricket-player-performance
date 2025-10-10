"""
Cricket Player Performance Analysis
End-to-End Data Analysis Project

This module analyzes cricket player and team performance to identify match-winning factors.
Tools: Python (Pandas, NumPy), Matplotlib, Seaborn
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Set style for better visualizations
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)


class CricketAnalyzer:
    """Main class for analyzing cricket player performance data"""
    
    def __init__(self, data_path):
        """Initialize the analyzer with data path"""
        self.data_path = data_path
        self.df = None
        
    def load_data(self):
        """Load cricket data from CSV file"""
        try:
            self.df = pd.read_csv(self.data_path)
            print(f"Data loaded successfully! Shape: {self.df.shape}")
            print(f"\nColumns: {list(self.df.columns)}")
            return self.df
        except FileNotFoundError:
            print(f"Error: File not found at {self.data_path}")
            return None
    
    def display_basic_info(self):
        """Display basic information about the dataset"""
        if self.df is None:
            print("Please load data first!")
            return
        
        print("\n" + "="*60)
        print("BASIC DATA INFORMATION")
        print("="*60)
        print("\nFirst 5 rows:")
        print(self.df.head())
        print("\nData Info:")
        print(self.df.info())
        print("\nStatistical Summary:")
        print(self.df.describe())
        print("\nMissing Values:")
        print(self.df.isnull().sum())
    
    def analyze_batting_performance(self):
        """Analyze batting performance metrics"""
        if self.df is None:
            print("Please load data first!")
            return
        
        print("\n" + "="*60)
        print("BATTING PERFORMANCE ANALYSIS")
        print("="*60)
        
        # Top run scorers
        top_scorers = self.df.groupby('Player_Name')['Runs'].sum().sort_values(ascending=False).head(10)
        print("\nTop 10 Run Scorers:")
        print(top_scorers)
        
        # Best batting averages (minimum 500 runs)
        batsmen = self.df[self.df['Runs'] > 500].groupby('Player_Name').agg({
            'Runs': 'sum',
            'Average': 'mean',
            'Strike_Rate': 'mean',
            'Centuries': 'sum',
            'Half_Centuries': 'sum'
        }).sort_values('Average', ascending=False).head(10)
        
        print("\nTop 10 Batsmen by Average (min 500 runs):")
        print(batsmen)
        
        # Best strike rates
        aggressive_batsmen = self.df[self.df['Runs'] > 500].groupby('Player_Name')['Strike_Rate'].mean().sort_values(ascending=False).head(10)
        print("\nMost Aggressive Batsmen (by Strike Rate):")
        print(aggressive_batsmen)
    
    def analyze_bowling_performance(self):
        """Analyze bowling performance metrics"""
        if self.df is None:
            print("Please load data first!")
            return
        
        print("\n" + "="*60)
        print("BOWLING PERFORMANCE ANALYSIS")
        print("="*60)
        
        # Top wicket takers
        bowlers = self.df[self.df['Wickets'] > 0]
        top_wicket_takers = bowlers.groupby('Player_Name')['Wickets'].sum().sort_values(ascending=False).head(10)
        print("\nTop 10 Wicket Takers:")
        print(top_wicket_takers)
        
        # Best bowling averages (minimum 30 wickets)
        quality_bowlers = bowlers.groupby('Player_Name').agg({
            'Wickets': 'sum',
            'Bowling_Average': 'mean',
            'Economy': 'mean'
        })
        quality_bowlers = quality_bowlers[quality_bowlers['Wickets'] > 30].sort_values('Bowling_Average').head(10)
        
        print("\nBest Bowlers by Average (min 30 wickets):")
        print(quality_bowlers)
        
        # Most economical bowlers
        economical = bowlers[bowlers['Wickets'] > 30].groupby('Player_Name')['Economy'].mean().sort_values().head(10)
        print("\nMost Economical Bowlers:")
        print(economical)
    
    def analyze_all_rounders(self):
        """Analyze all-rounder performance"""
        if self.df is None:
            print("Please load data first!")
            return
        
        print("\n" + "="*60)
        print("ALL-ROUNDER PERFORMANCE ANALYSIS")
        print("="*60)
        
        # Filter all-rounders (players with both runs and wickets)
        all_rounders = self.df[(self.df['Role'] == 'All-Rounder') | 
                               ((self.df['Runs'] > 500) & (self.df['Wickets'] > 20))]
        
        if len(all_rounders) > 0:
            ar_stats = all_rounders.groupby('Player_Name').agg({
                'Runs': 'sum',
                'Average': 'mean',
                'Wickets': 'sum',
                'Bowling_Average': 'mean',
                'Economy': 'mean'
            }).sort_values('Runs', ascending=False)
            
            print("\nTop All-Rounders:")
            print(ar_stats.head(10))
    
    def analyze_team_performance(self):
        """Analyze team performance and match-winning factors"""
        if self.df is None:
            print("Please load data first!")
            return
        
        print("\n" + "="*60)
        print("TEAM PERFORMANCE ANALYSIS")
        print("="*60)
        
        # Win/Loss analysis by team
        team_performance = self.df.groupby(['Team', 'Match_Result']).size().unstack(fill_value=0)
        team_performance['Win_Percentage'] = (team_performance['Won'] / 
                                              (team_performance['Won'] + team_performance['Lost']) * 100).round(2)
        
        print("\nTeam Win/Loss Record:")
        print(team_performance.sort_values('Win_Percentage', ascending=False))
        
        # Performance comparison in wins vs losses
        print("\nAverage Performance in Winning vs Losing Matches:")
        win_loss_comparison = self.df.groupby('Match_Result').agg({
            'Runs': 'mean',
            'Average': 'mean',
            'Strike_Rate': 'mean',
            'Wickets': 'mean',
            'Economy': 'mean'
        }).round(2)
        print(win_loss_comparison)
    
    def identify_match_winning_factors(self):
        """Identify key factors that contribute to match wins"""
        if self.df is None:
            print("Please load data first!")
            return
        
        print("\n" + "="*60)
        print("MATCH-WINNING FACTORS ANALYSIS")
        print("="*60)
        
        # Compare key metrics between won and lost matches
        won_matches = self.df[self.df['Match_Result'] == 'Won']
        lost_matches = self.df[self.df['Match_Result'] == 'Lost']
        
        print("\nKey Performance Indicators:")
        print(f"\nAverage Runs in Won Matches: {won_matches['Runs'].mean():.2f}")
        print(f"Average Runs in Lost Matches: {lost_matches['Runs'].mean():.2f}")
        
        print(f"\nAverage Strike Rate in Won Matches: {won_matches['Strike_Rate'].mean():.2f}")
        print(f"Average Strike Rate in Lost Matches: {lost_matches['Strike_Rate'].mean():.2f}")
        
        # Bowler performance in winning matches
        won_bowlers = won_matches[won_matches['Wickets'] > 0]
        lost_bowlers = lost_matches[lost_matches['Wickets'] > 0]
        
        if len(won_bowlers) > 0 and len(lost_bowlers) > 0:
            print(f"\nAverage Wickets in Won Matches: {won_bowlers['Wickets'].mean():.2f}")
            print(f"Average Wickets in Lost Matches: {lost_bowlers['Wickets'].mean():.2f}")
            
            print(f"\nAverage Economy in Won Matches: {won_bowlers['Economy'].mean():.2f}")
            print(f"Average Economy in Lost Matches: {lost_bowlers['Economy'].mean():.2f}")
        
        # Role-wise contribution in wins
        print("\nRole-wise Contribution in Winning Matches:")
        role_contribution = won_matches.groupby('Role').agg({
            'Runs': 'mean',
            'Wickets': 'mean'
        }).round(2)
        print(role_contribution)
    
    def create_visualizations(self):
        """Create comprehensive visualizations"""
        if self.df is None:
            print("Please load data first!")
            return
        
        print("\nGenerating visualizations...")
        
        # 1. Top Run Scorers
        plt.figure(figsize=(14, 6))
        top_scorers = self.df.groupby('Player_Name')['Runs'].sum().sort_values(ascending=False).head(10)
        plt.subplot(1, 2, 1)
        top_scorers.plot(kind='barh', color='skyblue')
        plt.xlabel('Total Runs')
        plt.ylabel('Player')
        plt.title('Top 10 Run Scorers', fontsize=14, fontweight='bold')
        plt.gca().invert_yaxis()
        
        # 2. Top Wicket Takers
        plt.subplot(1, 2, 2)
        top_wickets = self.df[self.df['Wickets'] > 0].groupby('Player_Name')['Wickets'].sum().sort_values(ascending=False).head(10)
        top_wickets.plot(kind='barh', color='lightcoral')
        plt.xlabel('Total Wickets')
        plt.ylabel('Player')
        plt.title('Top 10 Wicket Takers', fontsize=14, fontweight='bold')
        plt.gca().invert_yaxis()
        
        plt.tight_layout()
        plt.savefig('visualizations/top_performers.png', dpi=300, bbox_inches='tight')
        print("✓ Saved: visualizations/top_performers.png")
        plt.close()
        
        # 3. Strike Rate vs Average (Batsmen)
        plt.figure(figsize=(10, 6))
        batsmen_data = self.df[self.df['Runs'] > 500]
        scatter = plt.scatter(batsmen_data['Average'], batsmen_data['Strike_Rate'], 
                             c=batsmen_data['Centuries'], s=100, cmap='viridis', alpha=0.6)
        plt.xlabel('Batting Average', fontsize=12)
        plt.ylabel('Strike Rate', fontsize=12)
        plt.title('Batting Average vs Strike Rate (size = Centuries)', fontsize=14, fontweight='bold')
        plt.colorbar(scatter, label='Centuries')
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig('visualizations/batting_analysis.png', dpi=300, bbox_inches='tight')
        print("✓ Saved: visualizations/batting_analysis.png")
        plt.close()
        
        # 4. Bowling Economy vs Average
        plt.figure(figsize=(10, 6))
        bowlers_data = self.df[self.df['Wickets'] > 30]
        if len(bowlers_data) > 0:
            scatter = plt.scatter(bowlers_data['Bowling_Average'], bowlers_data['Economy'], 
                                 c=bowlers_data['Wickets'], s=100, cmap='Reds', alpha=0.6)
            plt.xlabel('Bowling Average', fontsize=12)
            plt.ylabel('Economy Rate', fontsize=12)
            plt.title('Bowling Average vs Economy Rate (size = Wickets)', fontsize=14, fontweight='bold')
            plt.colorbar(scatter, label='Wickets')
            plt.grid(True, alpha=0.3)
            plt.tight_layout()
            plt.savefig('visualizations/bowling_analysis.png', dpi=300, bbox_inches='tight')
            print("✓ Saved: visualizations/bowling_analysis.png")
            plt.close()
        
        # 5. Team Performance Comparison
        plt.figure(figsize=(12, 6))
        team_stats = self.df.groupby('Team')['Runs'].sum().sort_values(ascending=False)
        team_stats.plot(kind='bar', color='teal', alpha=0.7)
        plt.xlabel('Team', fontsize=12)
        plt.ylabel('Total Runs', fontsize=12)
        plt.title('Team-wise Total Runs', fontsize=14, fontweight='bold')
        plt.xticks(rotation=45)
        plt.grid(True, alpha=0.3, axis='y')
        plt.tight_layout()
        plt.savefig('visualizations/team_performance.png', dpi=300, bbox_inches='tight')
        print("✓ Saved: visualizations/team_performance.png")
        plt.close()
        
        # 6. Win/Loss Performance Comparison
        plt.figure(figsize=(14, 6))
        
        plt.subplot(1, 2, 1)
        win_loss_runs = self.df.groupby('Match_Result')['Runs'].mean()
        win_loss_runs.plot(kind='bar', color=['green', 'red'], alpha=0.7)
        plt.xlabel('Match Result', fontsize=12)
        plt.ylabel('Average Runs', fontsize=12)
        plt.title('Average Runs: Won vs Lost', fontsize=14, fontweight='bold')
        plt.xticks(rotation=0)
        plt.grid(True, alpha=0.3, axis='y')
        
        plt.subplot(1, 2, 2)
        win_loss_sr = self.df.groupby('Match_Result')['Strike_Rate'].mean()
        win_loss_sr.plot(kind='bar', color=['green', 'red'], alpha=0.7)
        plt.xlabel('Match Result', fontsize=12)
        plt.ylabel('Average Strike Rate', fontsize=12)
        plt.title('Average Strike Rate: Won vs Lost', fontsize=14, fontweight='bold')
        plt.xticks(rotation=0)
        plt.grid(True, alpha=0.3, axis='y')
        
        plt.tight_layout()
        plt.savefig('visualizations/win_loss_analysis.png', dpi=300, bbox_inches='tight')
        print("✓ Saved: visualizations/win_loss_analysis.png")
        plt.close()
        
        # 7. Role Distribution
        plt.figure(figsize=(10, 6))
        role_counts = self.df['Role'].value_counts()
        colors = plt.cm.Set3(range(len(role_counts)))
        plt.pie(role_counts.values, labels=role_counts.index, autopct='%1.1f%%', 
                colors=colors, startangle=90)
        plt.title('Player Role Distribution', fontsize=14, fontweight='bold')
        plt.axis('equal')
        plt.tight_layout()
        plt.savefig('visualizations/role_distribution.png', dpi=300, bbox_inches='tight')
        print("✓ Saved: visualizations/role_distribution.png")
        plt.close()
        
        # 8. Correlation Heatmap
        plt.figure(figsize=(10, 8))
        numeric_cols = ['Runs', 'Average', 'Strike_Rate', 'Centuries', 'Half_Centuries', 
                       'Wickets', 'Bowling_Average', 'Economy']
        correlation_data = self.df[numeric_cols].corr()
        sns.heatmap(correlation_data, annot=True, fmt='.2f', cmap='coolwarm', 
                    center=0, square=True, linewidths=1)
        plt.title('Performance Metrics Correlation Heatmap', fontsize=14, fontweight='bold')
        plt.tight_layout()
        plt.savefig('visualizations/correlation_heatmap.png', dpi=300, bbox_inches='tight')
        print("✓ Saved: visualizations/correlation_heatmap.png")
        plt.close()
        
        print("\n✓ All visualizations generated successfully!")
    
    def generate_insights(self):
        """Generate key insights from the analysis"""
        if self.df is None:
            print("Please load data first!")
            return
        
        print("\n" + "="*60)
        print("KEY INSIGHTS AND FINDINGS")
        print("="*60)
        
        insights = []
        
        # Best overall player
        player_impact = self.df.groupby('Player_Name').agg({
            'Runs': 'sum',
            'Wickets': 'sum',
            'Average': 'mean',
            'Strike_Rate': 'mean'
        })
        player_impact['Impact_Score'] = (player_impact['Runs'] / 100 + 
                                          player_impact['Wickets'] * 2 + 
                                          player_impact['Average'] / 10)
        best_player = player_impact['Impact_Score'].idxmax()
        insights.append(f"1. Most Impactful Player: {best_player}")
        
        # Match-winning factor
        won_avg_runs = self.df[self.df['Match_Result'] == 'Won']['Runs'].mean()
        lost_avg_runs = self.df[self.df['Match_Result'] == 'Lost']['Runs'].mean()
        run_difference = won_avg_runs - lost_avg_runs
        insights.append(f"2. Teams score {run_difference:.0f} more runs on average in winning matches")
        
        # Best batting team
        team_batting = self.df.groupby('Team')['Runs'].mean().sort_values(ascending=False)
        best_batting_team = team_batting.index[0]
        insights.append(f"3. Best Batting Team: {best_batting_team} (avg: {team_batting.iloc[0]:.2f} runs)")
        
        # Most consistent batsman
        consistent_batsmen = self.df[self.df['Runs'] > 1000].groupby('Player_Name')['Average'].mean().sort_values(ascending=False)
        if len(consistent_batsmen) > 0:
            most_consistent = consistent_batsmen.index[0]
            insights.append(f"4. Most Consistent Batsman: {most_consistent} (avg: {consistent_batsmen.iloc[0]:.2f})")
        
        # Most lethal bowler
        bowlers = self.df[self.df['Wickets'] > 50]
        if len(bowlers) > 0:
            lethal_bowler = bowlers.groupby('Player_Name')['Bowling_Average'].mean().sort_values().index[0]
            insights.append(f"5. Most Lethal Bowler: {lethal_bowler}")
        
        # Strike rate importance
        won_sr = self.df[self.df['Match_Result'] == 'Won']['Strike_Rate'].mean()
        lost_sr = self.df[self.df['Match_Result'] == 'Lost']['Strike_Rate'].mean()
        sr_diff = won_sr - lost_sr
        insights.append(f"6. Teams have {sr_diff:.2f} higher strike rate in winning matches")
        
        # Print all insights
        for insight in insights:
            print(f"\n{insight}")
        
        print("\n" + "="*60)
        return insights


def main():
    """Main function to run the complete analysis"""
    print("="*60)
    print("CRICKET PLAYER PERFORMANCE ANALYSIS")
    print("End-to-End Data Analysis Project")
    print("="*60)
    
    # Initialize analyzer
    analyzer = CricketAnalyzer('data/cricket_data.csv')
    
    # Load data
    df = analyzer.load_data()
    
    if df is not None:
        # Create visualizations directory
        import os
        os.makedirs('visualizations', exist_ok=True)
        
        # Display basic information
        analyzer.display_basic_info()
        
        # Perform analyses
        analyzer.analyze_batting_performance()
        analyzer.analyze_bowling_performance()
        analyzer.analyze_all_rounders()
        analyzer.analyze_team_performance()
        analyzer.identify_match_winning_factors()
        
        # Generate visualizations
        analyzer.create_visualizations()
        
        # Generate insights
        analyzer.generate_insights()
        
        print("\n" + "="*60)
        print("ANALYSIS COMPLETED SUCCESSFULLY!")
        print("="*60)
        print("\nCheck the 'visualizations' folder for generated charts and graphs.")


if __name__ == "__main__":
    main()
