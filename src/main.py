from utils import *
from db_utils import *

get_all_election_data()

files = get_all_data_file_names('../data/json/raw/')

data = load_json_data('../data/json/raw/' + files[-1])

save_to_db(data, get_generated_date(data))