from datetime import datetime
from config import REPORT_PREVIEW_ROWS

class ReportGenerator:
    def generate_csv_report(self, rows, filename, total_rows, columns):
        """Generate formatted CSV report"""
        report = self._header_section(filename, total_rows)
        report += self._columns_section(columns)
        report += self._data_sample_section(rows, total_rows)
        report += self._footer_section()
        return report
    
    def _header_section(self, filename, total_rows):
        return f"""
{'='*60}
DATA PROCESSING REPORT
{'='*60}

File: {filename}
Processing Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Total Records: {total_rows}

"""
    
    def _columns_section(self, columns):
        section = f"{'='*60}\nCOLUMN INFORMATION\n{'='*60}\n"
        for i, col in enumerate(columns, 1):
            section += f"\n{i}. {col}"
        return section + "\n\n"
    
    def _data_sample_section(self, rows, total_rows):
        section = f"{'='*60}\nDATA SAMPLE (First {REPORT_PREVIEW_ROWS} rows)\n{'='*60}\n\n"
        
        for i, row in enumerate(rows[:REPORT_PREVIEW_ROWS], 1):
            section += f"Row {i}:\n"
            for key, value in row.items():
                section += f"  {key}: {value}\n"
            section += "\n"
        
        if total_rows > REPORT_PREVIEW_ROWS:
            section += f"... and {total_rows - REPORT_PREVIEW_ROWS} more rows\n\n"
        
        return section
    
    def _footer_section(self):
        return f"{'='*60}\nEND OF REPORT\n{'='*60}\n"