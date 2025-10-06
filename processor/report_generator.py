from datetime import datetime

def generate_report(rows, filename, total_rows, columns):
    report = f"""
{'='*60}
DATA PROCESSING REPORT
{'='*60}

File: {filename}
Processing Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Total Records: {total_rows}

{'='*60}
COLUMN INFORMATION
{'='*60}
"""
    for i, col in enumerate(columns, 1):
        report += f"\n{i}. {col}"
    
    report += f"\n\n{'='*60}\nDATA SAMPLE (First 5 rows)\n{'='*60}\n\n"
    
    for i, row in enumerate(rows[:5], 1):
        report += f"Row {i}:\n"
        for key, value in row.items():
            report += f"  {key}: {value}\n"
        report += "\n"
    
    if total_rows > 5:
        report += f"... and {total_rows - 5} more rows\n\n"
    
    report += f"{'='*60}\nEND OF REPORT\n{'='*60}\n"
    return report
