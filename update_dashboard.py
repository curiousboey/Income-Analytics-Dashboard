#!/usr/bin/env python3
"""
Update the dashboard data with manually processed DOCX information.
Since the DOCX files are invoices, I'll estimate hours based on your typical hourly rate.
"""

import json

def update_dashboard_with_new_data():
    """Update the dashboard with the new September and October 2025 data."""
    
    # Your typical hourly rate is around $25-27 (calculated from previous data)
    typical_hourly_rate = 26.0
    
    # New data extracted from DOCX files
    new_data = [
        {
            'month': 'September 2025',
            'hours': 6169.5 / typical_hourly_rate,  # Estimate hours based on earnings
            'amount': 6169.5,
            'received': 0,  # Need to check if any payments received
            'notes': 'Data from 2025 Sept 1-30.docx invoice - House cleaning, Builder\'s cleaning, Office cleaning, Once-over cleaning'
        },
        {
            'month': 'October 2025',
            'hours': 6264.0 / typical_hourly_rate,  # Estimate hours based on earnings
            'amount': 6264.0,
            'received': 0,  # Need to check if any payments received
            'notes': 'Data from 2025 Oct 1-31.docx invoice - House cleaning, Builder\'s cleaning, Office cleaning, Once-over cleaning'
        }
    ]
    
    # Round hours to 2 decimal places
    for item in new_data:
        item['hours'] = round(item['hours'], 2)
    
    print("New data to be added:")
    for item in new_data:
        print(f"{item['month']}: {item['hours']} hours, ${item['amount']}, received ${item['received']}")
    
    return new_data

def update_index_html():
    """Update the index.html file with the new data."""
    
    # Read the current index.html file
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Current workData array in the file (we'll replace this)
    current_data = [
        {'month': 'March 2024', 'hours': 142.25, 'amount': 3556.25, 'received': 0, 'notes': 'Amount to be received: $14,698.67'},
        {'month': 'April 2024', 'hours': 192.58, 'amount': 4814.5, 'received': 1000, 'notes': ''},
        {'month': 'May 2024', 'hours': 213.67, 'amount': 5341.67, 'received': 1200, 'notes': ''},
        {'month': 'June 2024', 'hours': 224.50, 'amount': 5612.5, 'received': 6170, 'notes': ''},
        {'month': 'July 2024', 'hours': 176.0, 'amount': 4400.0, 'received': 2000, 'notes': 'Previous Amount to be received before April= 13,098.67'},
        {'month': 'August 2024', 'hours': 231.0, 'amount': 5775.0, 'received': 3500, 'notes': 'Amount received in April= 5,000 + 11,000= 16,000'},
        {'month': 'September 2024', 'hours': 202.75, 'amount': 5068.75, 'received': 2700, 'notes': 'Total hours April 1-15= 140'},
        {'month': 'October 2024', 'hours': 178.25, 'amount': 4456.25, 'received': 14775, 'notes': 'Total amount April 1-15= 140x25= 3,500'},
        {'month': 'November 2024', 'hours': 176.25, 'amount': 4406.25, 'received': 2000, 'notes': ''},
        {'month': 'December 2024', 'hours': 222.0, 'amount': 5550.0, 'received': 500, 'notes': 'Total amount to be received till April= (13,098.67 + 3,500)- 16,000 = 598.67'},
        {'month': 'January 2025', 'hours': 249.5, 'amount': 6237.5, 'received': 1400, 'notes': ''},
        {'month': 'February 2025', 'hours': 222.75, 'amount': 5568.75, 'received': 16750, 'notes': ''},
        {'month': 'March 2025', 'hours': 236.25, 'amount': 5906.25, 'received': 1600, 'notes': ''},
        {'month': 'April 2025', 'hours': 140.0, 'amount': 3500.0, 'received': 16000, 'notes': ''},
        {'month': 'May 2025', 'hours': 0.0, 'amount': 0.0, 'received': 6000, 'notes': ''},
        {'month': 'June 2025', 'hours': 226.0, 'amount': 6102.0, 'received': 4000, 'notes': ''},
        {'month': 'July 2025', 'hours': 206.75, 'amount': 5582.25, 'received': 3150, 'notes': ''},
        {'month': 'August 2025', 'hours': 202.75, 'amount': 5474.25, 'received': 4240, 'notes': ''}
    ]
    
    # Add new September and October 2025 data
    new_entries = update_dashboard_with_new_data()
    current_data.extend(new_entries)
    
    # Create the JavaScript array string
    js_array = "const workData = [\n"
    for i, item in enumerate(current_data):
        js_array += f"            {{month: '{item['month']}', hours: {item['hours']}, amount: {item['amount']}, received: {item['received']}, notes: '{item['notes']}'}}"
        if i < len(current_data) - 1:
            js_array += ","
        js_array += "\n"
    js_array += "        ];"
    
    # Find and replace the workData array in the HTML file
    import re
    pattern = r'const workData = \[(.*?)\];'
    replacement = js_array
    
    # Use re.DOTALL flag to match across multiple lines
    updated_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    # Write the updated content back to the file
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print("Successfully updated index.html with new data!")
    
    # Calculate and display new totals
    total_hours = sum(item['hours'] for item in current_data)
    total_amount = sum(item['amount'] for item in current_data)
    total_received = sum(item['received'] for item in current_data)
    pending_amount = total_amount - total_received
    
    print(f"\nNew Dashboard Totals:")
    print(f"Total Hours: {total_hours:.1f}")
    print(f"Total Earnings: ${total_amount:,.2f}")
    print(f"Amount Received: ${total_received:,.2f}")
    print(f"Pending Amount: ${pending_amount:,.2f}")

if __name__ == "__main__":
    update_index_html()