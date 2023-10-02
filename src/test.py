from utils import *


# get_all_election_data()

files = get_all_data_file_names('../data/json/raw/')

data = load_json_data("../data/json/raw/" + files[0])

for item in data["Groups"]:
    print(item["Name"])

