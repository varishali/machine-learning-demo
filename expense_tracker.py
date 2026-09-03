"""
Real-Time Expense Tracker with Dashboard
----------------------------------------
Minor Project - Data Analysis using Python

Features: 
1. Add a new expense (real-time entry)
2. View all expenses
3. View total expenses
4. Category-wise breakdown (table + pie chart)
5. Monthly / Daily trend (line chart)
6. Top spending categories
7. Exit the application

Tools used: Python, Pandas, Matplotlib, CSV (as dastabase)
"""

from operator import index

import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime

FILE_NAME = 'expense.csv'

#--------------- Helper Functions ---------------#

def load_data():
    'load existing expense data'
    if os.path.exists(FILE_NAME):
        df = pd.read_csv(FILE_NAME)
    else:
        df = pd.DataFrame(columns=['Date','Category','Amount','Note'])
        df.to_csv(FILE_NAME, index=False)
    return df

def save_data(df):
    df.to_csv(FILE_NAME, index=False)

#---------------- Core Features ------------------#
def add_expense():
    'Take real-time input from the user and save it to the CSV file'
    print('\n-- Add New Expense --')
    date_input = input('Enter date (DD-MM-YYYY) or press Enter for today : ').strip()

    if date_input == "":
        date_input = datetime.now().strftime('%d-%m-%Y')

    category = input('Enter category (Food/Travel/Shopping/Recharnge/Entertainment/Other) : ').strip().title()

    try:
        amount = float(input('Enter amount spend (RS) : '))
    except ValueError:
        print('Invalid amount. Please enter a number .')
        return

    note = input('Enter a short note (optional) : ').strip()

    df = load_data()
    new_row = {'Date' : date_input , 'Category' : category, 'Amount' : amount, 'Note' : note}
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    save_data(df)

    print(f'Expense of Rs.{amount} added under {category} successfully!\n')

def view_all_expense():
    df = load_data()
    if df.empty:
        print('\nNo Expense recorded Yet.\n')
        return
    print('\n-- All Expense --')
    print(df.to_string(index=False))
    print()

def view_total_expense():
    df = load_data()
    if df.empty:
        print('\nNo Expense recorded Yet.\n')
        return
    total = df['Amount'].sum()
    print(f'\nTotal expense so far : Rs. {total:.2f}\n')

def category_wise_breakdown():
    df = load_data()
    if df.empty:
        print('\nNo expense record Yet.\n')
        return

    summary = df.groupby('Category')['Amount'].sum().sort_values(ascending=False)
    print('\n-- Category-wise Expense Breakdown --')
    print(summary.to_string())

    # Pie Chart
    plt.figure(figsize=(6, 6))
    plt.pie(summary, labels=summary.index, autopct="%1.1f%%", startangle=90)
    plt.title('Expense Breakdown by Category')
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig('category_breakdown.png')
    print("Pie Chart saved as 'category_breakdown.png'")  
    plt.show()

def monthly_trend():
    df = load_data()
    if df.empty:
        print('\nNo expense record yet.\n')
        return

    df['Date'] = pd.to_datetime(df['Date'], format="%d-%m-%Y", errors='coerce')
    df = df.dropna(subset=['Date'])
    df['Month'] = df['Date'].dt.strftime("%b-%Y")

    monthly_summary = df.groupby('Month')['Amount'].sum()

    print('\n-- Month-wise Expense Trend --')
    print(monthly_summary.to_string())
    print()

    plt.figure(figsize=(8, 5))
    monthly_summary.plot(kind='bar', color='skyblue')
    plt.title('Monthly Expense Trend')
    plt.xlabel('Month')
    plt.ylabel('Amount (Rs)')
    plt.tight_layout()
    plt.savefig('Month_trend.png')
    print("Bar chart saved as 'Monthly_trand.png'")
    plt.show()

def top_category():
    df = load_data()
    if df.empty:
        print('\nNo Expense record yet.\n') 
    summary = df.groupby('Category')['Amount'].sum().sort_values(ascending=False)
    top = summary.index[0]
    amount = summary.iloc[0]
    print(f'\nHighest spending category : {top} (Rs.{amount:.2f})\n')


def full_dashboard():
    'show a combined dashboard : pie chart + bar chart together.'
    df = load_data()
    if df.empty:
        print('\nNo Expense record yet.\n')
        return

    df['Date'] = pd.to_datetime(df['Date'], format="%d-%m-%Y", errors='coerce')
    df = df.dropna(subset=['Date'])
    df['Month'] = df['Date'].dt.strftime('%b,%Y') 

    category_summary = df.groupby('Category')['Amount'].sum().sort_values(ascending=False) 
    monthly_summary = df.groupby('Month')['Amount'].sum()
    total = df['Amount'].sum()

    fig, axs = plt.subplots(1, 2, figsize=(12, 5))

    axs[0].pie(category_summary, labels=category_summary.index, autopct='%1.1f%%', startangle=90)
    axs[0].set_title('Category-wise Expenses')

    axs[1].bar(monthly_summary.index, monthly_summary.values, color='orange')
    axs[1].set_title('Monthly Expense Trend')
    axs[1].set_xlabel('Month')
    axs[1].set_ylabel('Amount (Rs)')

    fig.suptitle(f'Expense Dashboard | Total Spend. {total:.2f}', fontsize=14)
    plt.tight_layout()
    plt.savefig('expense_dashboard.png')
    print("\nFull dashboard saved as 'expense_dashboard.png'")
    plt.show()

#------------- Main Menu ----------------
def main():
    while True:
        print("-" * 51)
        print('------  REAL TIME EXPENSE TRACKER DASHBOARD  ------')
        print("-" * 51)
        print('1. Add New Expense')
        print('2. View All Expense')
        print('3. View Total Expense')
        print('4. Category-Wise Breakdown (Pie Chart)')
        print('5. Monthly Trend (Bar Chart)')
        print('6. Top Spending Category')
        print('7. Full Dashboard (Pie + Bar Chart)')
        print('8. Exit')

        choice = input('\nEnter Your Choice (1-8) : ')

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_all_expense()

        elif choice == "3":
            view_total_expense()

        elif choice == "4":
            category_wise_breakdown()

        elif choice == "5":
            monthly_trend()

        elif choice == "6":
            top_category()

        elif choice == "7":
            full_dashboard()

        elif choice == "8":
            print('Thank you for using Expense Tracker. Goodbye!')
            break
        else:
            print('Invalid Choice. Please a number between (1-8).\n')

if __name__ == "__main__":
    main()            


    