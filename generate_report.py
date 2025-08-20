import pandas as pd
from fpdf import FPDF

# Function to read data from CSV
def read_data(file_path):
    data = pd.read_csv(file_path)
    return data

# Function to analyze data
def analyze_data(data):
    summary = {
        'Total Students': len(data),
        'Average Score': data['Score'].mean(),
        'Highest Score': data['Score'].max(),
        'Lowest Score': data['Score'].min(),
    }
    return summary

# Function to generate PDF report
def generate_pdf_report(summary, data, output_file):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, 'Student Score Report', ln=True, align='C')

    # Summary
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"Total Students: {summary['Total Students']}", ln=True)
    pdf.cell(0, 10, f"Average Score: {summary['Average Score']:.2f}", ln=True)
    pdf.cell(0, 10, f"Highest Score: {summary['Highest Score']}", ln=True)
    pdf.cell(0, 10, f"Lowest Score: {summary['Lowest Score']}", ln=True)

    # Add a line break
    pdf.ln(10)

    # Table header
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(60, 10, 'Name', 1)
    pdf.cell(60, 10, 'Score', 1)
    pdf.ln()

    # Table rows
    pdf.set_font("Arial", size=12)
    for index, row in data.iterrows():
        pdf.cell(60, 10, row['Name'], 1)
        pdf.cell(60, 10, str(row['Score']), 1)
        pdf.ln()

    # Save the PDF
    pdf.output(output_file)

# Main function
def main():
    input_file = 'data.csv'
    output_file = 'report.pdf'

    # Read and analyze data
    data = read_data(input_file)
    summary = analyze_data(data)

    # Generate PDF report
    generate_pdf_report(summary, data, output_file)
    print(f"Report generated: {output_file}")

if __name__ == "__main__":
    main()