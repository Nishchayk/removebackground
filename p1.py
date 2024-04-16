import pandas as pd

parsed_data = []
clean_data = []
dict0 ={}

with open ("test_str.txt","r") as f:
    data = f.read()
    # print(len(data.split("\n")[6]))
    data_len = data.split("\n")
    for i in data_len:
        if len(i) >= 140 and len(i) <= 150:
            lines = i.split("\n")
            header_lines = lines[0]
            convert_to_dataframe = header_lines.split()
            
            for line in convert_to_dataframe:
                if "-" not in line:
                    parsed_data.append(line)
            cli_details = i.strip().split("\n")[0]
            clean_data.append(cli_details)

headers = [header_data for header_data in clean_data[0].split(" ") if len(header_data) != 0]
ap_index = headers.index("ap")
ap_name = headers[ap_index] + " " + headers[ap_index+1]
headers[ap_index] = ap_name
headers.remove(headers[ap_index+1])

cli_detail = clean_data [2:]
for i in cli_detail:
    cleaned_cil = [data for data in i.split(" ") if len(data) != 0]
    for j in range (len(headers)):
        dict0.setdefault(headers[j],[]).append(cleaned_cil[j])

df = pd.DataFrame(dict0)
for i in df["band/ht-mode/bandwidth"]:
    print(i.split("/")[0],i.split("/")[-1])


    


