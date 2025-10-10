#!/usr/bin/env python3
"""
Quick Start Script for Cricket Performance Analysis

This script provides a simple interface to run the cricket analysis.
"""

import sys
import os

def print_menu():
    """Display main menu"""
    print("\n" + "="*60)
    print("CRICKET PLAYER PERFORMANCE ANALYSIS")
    print("="*60)
    print("\nChoose an option:")
    print("1. Run Complete Analysis")
    print("2. View Quick Statistics")
    print("3. Generate Visualizations Only")
    print("4. Exit")
    print("\n" + "="*60)

def run_complete_analysis():
    """Run the complete analysis"""
    print("\nRunning complete analysis...")
    os.system('python3 cricket_analysis.py')

def quick_stats():
    """Display quick statistics"""
    import pandas as pd
    
    df = pd.read_csv('data/cricket_data.csv')
    
    print("\n" + "="*60)
    print("QUICK STATISTICS")
    print("="*60)
    
    print(f"\nTotal Players: {df['Player_Name'].nunique()}")
    print(f"Total Teams: {df['Team'].nunique()}")
    print(f"Total Matches: {df['Matches'].sum()}")
    
    print(f"\nTop Run Scorer: {df.groupby('Player_Name')['Runs'].sum().idxmax()}")
    print(f"Top Wicket Taker: {df[df['Wickets'] > 0].groupby('Player_Name')['Wickets'].sum().idxmax()}")
    
    won_matches = df[df['Match_Result'] == 'Won']
    lost_matches = df[df['Match_Result'] == 'Lost']
    
    print(f"\nAvg Runs (Won): {won_matches['Runs'].mean():.2f}")
    print(f"Avg Runs (Lost): {lost_matches['Runs'].mean():.2f}")
    print(f"Run Difference: {won_matches['Runs'].mean() - lost_matches['Runs'].mean():.2f}")
    
    print("\n" + "="*60)

def generate_visualizations():
    """Generate visualizations only"""
    print("\nGenerating visualizations...")
    from cricket_analysis import CricketAnalyzer
    
    analyzer = CricketAnalyzer('data/cricket_data.csv')
    analyzer.load_data()
    
    import os
    os.makedirs('visualizations', exist_ok=True)
    
    analyzer.create_visualizations()
    print("\n✓ Visualizations generated successfully!")

def main():
    """Main function"""
    while True:
        print_menu()
        
        try:
            choice = input("\nEnter your choice (1-4): ").strip()
            
            if choice == '1':
                run_complete_analysis()
            elif choice == '2':
                quick_stats()
            elif choice == '3':
                generate_visualizations()
            elif choice == '4':
                print("\nThank you for using Cricket Performance Analysis!")
                print("Goodbye!\n")
                sys.exit(0)
            else:
                print("\n❌ Invalid choice! Please enter 1, 2, 3, or 4.")
        
        except KeyboardInterrupt:
            print("\n\nExiting...")
            sys.exit(0)
        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("Please try again.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
