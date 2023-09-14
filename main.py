# main.py
from config import truth_list, prediction_list
from my_module import named_entity_recognition

if __name__ == '__main__':
    correct, missed, false_positives = named_entity_recognition(truth_list, prediction_list)
    print(f"Correctly identified entities: {correct}")
    print(f"Missed entities: {missed}")
    print(f"False positive entities: {false_positives}")
