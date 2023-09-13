import warnings
from fuzzywuzzy import fuzz
from config import FUZZY_THRESHOLD, TRUTH_STRING, PREDS_LIST

# Filter out the warning about the slow pure-python SequenceMatcher
warnings.filterwarnings("ignore", category=UserWarning, module="fuzzywuzzy")


def compare_strings(truth, preds):
    # Convert truth and preds to lowercase
    truth = truth.lower()
    preds = [pred.lower() for pred in preds]

    # Initialize counts for correct, false positives, and missed entities
    correct_count = 0
    false_positives = 0
    missed_count = 0

    # Split truth and preds strings into lists of entities
    truth_entities = truth.split()

    for pred in preds:
        print(pred)
        pred_entities = pred.split()
        print(pred_entities)

        # Exact match comparison
        for entity in truth_entities.copy():
            if entity in pred_entities:
                correct_count += 1
                truth_entities.remove(entity)  # Remove matched entity from truth
                pred_entities.remove(entity)  # Remove matched entity from prediction

        # Fuzzy match comparison
        for pred_entity in pred_entities.copy():
            match_found = False
            for truth_entity in truth_entities.copy():
                ratio = fuzz.ratio(pred_entity, truth_entity)
                if ratio >= FUZZY_THRESHOLD:
                    correct_count += 1
                    match_found = True
                    truth_entities.remove(truth_entity)  # Remove matched entity from truth
                    pred_entities.remove(pred_entity)  # Remove matched entity from prediction
                    break
            if not match_found:
                false_positives += 1

    # Calculate missed count as the remaining truth entities
    missed_count = len(truth_entities)

    return correct_count, false_positives, missed_count


if __name__ == '__main__':
    correct, false_positives, missed = compare_strings(TRUTH_STRING, PREDS_LIST)
    print(f"Correct: {correct}, False Positives: {false_positives}, Missed: {missed}")
