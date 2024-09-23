from pathlib import Path
from pprint import pprint
from data.data_handler import DataHandler
from model.assigner import MedSocShuffle


def run(frame_dir_str: str = "static/medsoc-new.csv") -> None:
    current_dir = Path(__file__).resolve().parent
    data_handler = DataHandler(frame_dir=current_dir / frame_dir_str)
    people_array = data_handler.get_people_array()

    med_soc_shuffle = MedSocShuffle(people_array)
    assignments = med_soc_shuffle.run()
    pprint(assignments)


if __name__ == "__main__":
    run()
