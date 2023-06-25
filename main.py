import csv
from docx import Document

with open('64 White Rd - Faults_April_2023 (1).csv') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    data_lines = list(reader)

def format_data(_header, _data_lines):
    formatted_data = []
    for data in _data_lines:
        if any(data):
            formatted_row = ""
            for j in range(len(_header)):
                formatted_row += f'{_header[j]}: {data[j]}\n'
            formatted_data.append(formatted_row)
    return formatted_data

def write_to_doc(file_name, data):
    doc = Document()
    for row in data:
        doc.add_paragraph(row)
    doc.save(file_name)

Formatted_data = format_data(header, data_lines)
write_to_doc('formatted_data.docx', Formatted_data)
