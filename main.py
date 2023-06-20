import csv


with open('64 White Rd - Faults_April_2023 (1).csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=':', quoting=csv.QUOTE_NONE)
    header = next(reader)  # Read the first row as the header

    # Print header

    def format_header():
        for item in header:
            fo
            if item != "":
                return item
    format_header()
print(format_header())
# for fitems in format_header():
#     print(f"{}: ")

    # Print remaining lines
    # for row in reader:
    #     if any(field.strip() for field in row):  # Check if any field is non-empty
    #         for item in row:
    #             print(item)
    #         print()


"""with open('64 White Rd - Faults_April_2023 (1).csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    header = next(reader)     # Read the first row as the header
    for items in header:
        if items != "":
            print(f'{items}\n')
    for row in reader:
        if any(field.strip() for field in row):  # Check if any field is non-empty
            for item in row:
                print(item)"""






"""def print_data(header, data_lines):
        for data in data_lines:
            if any(field.strip() for field in data):  # Check if any field is non-empty
                for i in range(len(header)):
                    print(f'{header[i]}: {data[i]}')
                print()

    data_lines = list(reader)  # Convert the remaining rows into a list
    print_data(header, data_lines)"""


"""def format_data(DAta):
    lines = DAta.split('\n')
    header = lines[0].split('\t')
    data_lines = lines[1:]
    return header, data_lines


def print_data(header, data_lines):
    for data in data_lines:
                if data.strip() != "":
                    fields = data.split('\t')
                    for i in range(len(header)):
                        print(f'{header[i]}: {fields[i]}')
                    print()


header, data_lines = format_data(DAta)
print_data(header, data_lines)"""


"""    for line in reader:
        for field in header:
            data = line[field]
print(f'{field}: {data}')"""





"""    lines = text.split("\n")
    header = lines[0].split()
    data_lines = lines[1:]
print(lines)"""


""" units = []
    buildings = []
    specifications = []
    models = []
    serials = []
    locations = []
    faults = []
    extra_info = []
    serviced = []
    cool_heat_air = []
    gas_type = []
    condition = []
    make = []"""

"""for line in data_lines:
        if line.strip() != "":
            fields = line.split("\t")
            units.append(fields[0])
            buildings.append(fields[1])
            specifications.append(fields[2])
            models.append(fields[3])
            serials.append(fields[4])
            locations.append(fields[5])
            faults.append(fields[6])
            extra_info.append(fields[7])
            serviced.append(fields[8])
            cool_heat_air.append(fields[9])
            gas_type.append(fields[10])
            condition.append(fields[11])
            make.append(fields[12])
print(units)"""


"""with open('64-White-Road.pdf', 'wb') as new_file:
        reader = PyPDF2.PdfReader(file)
        number_of_pages = len(reader.pages)
        writer = PyPDF2.PdfWriter()
        writer.add_page(page)
        with open('FAULT.pdf', 'wb') as new_file:
            writer.write(new_file)"""


"""def Format_data(units, buildings,specifications, models, serials, locations, faults, extra_info, serviced, cool_heat_air, gas_type, condition, make):
    Formatted_data = []
    for i in range(len(units)):
        data = f"{i+1}) Unit: {units[i]}\n"
        data += f"   Building: {buildings[i]}\n"
        data += f"   Specification: {specifications[i]}\n"
        data += f"   Make: {make[i]}\n"
        data += f"   Model: {models[i]}\n"
        data += f"   Serial: {serials[i]}\n"
        data += f"   Location: {locations[i]}\n"
        data += f"   Serviced: {serviced[i]}\n"
        data += f"   Cool, Heat, AirFlow: {cool_heat_air[i]}\n"
        data += f"   Gas Type: {gas_type[i]}\n"
        data += f"   Condition: {condition[i]}\n"
        data += f"   Extra Info: {extra_info[i]}\n"
        data += f"   Fault: {faults[i]}\n"
        
        Formatted_data.append(data)
    return Formatted_data"""



# Example input data
"""input_data = Unit	Building	Specification	Model	Seriel/Ref	Location	Faults	Extra Info	Service Date	Cool, Heat, Airflow	Gas Type	Conditon	Make
												
Ac 06	Back Builing(Paymaster)	Cassette	CS-40U51HE	110287	Boardroom	Faulty Compressor 	This Unit is on the Quotation list for replacement	May 2023	No Heat/Cool	R22a	Bad	Panasonic

units, buildings, specifications, models, serials, locations, faults, extra_info, serviced, cool_heat_air, gas_type, condition, make = format_data(input_data)

Formatted_data = Format_data(units, buildings, specifications, models, serials, locations, faults, extra_info, serviced, cool_heat_air, gas_type, condition, make)"""

# Print the formatted data
#for data in Formatted_data:
#    print(data)


"""def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        firstname = data["firstname"]
        lastname = data["lastname"]
        email = data["email"]
        password = data["password"]
        birthday = data["birthday"]
        gender = ["gender"]
        cat = data["cat"]
        dog = data["dog"]
        cars = data["cars"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([firstname, lastname, email, password, birthday, gender, cat, dog, cars])"""

"""writer = PyPDF2.PdfWriter()
writer.add_page(page)"""

#with open('FAULT.csv', 'wb') as new_file:
    #    writer.write(new_file, )


