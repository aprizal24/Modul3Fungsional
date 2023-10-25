data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

def parse_data(data_str):
    numeric_parts = list(map(int, filter(str.isdigit, data_str.split())))
    return numeric_parts

OutputData = list(map(parse_data, data))

print(OutputData)
