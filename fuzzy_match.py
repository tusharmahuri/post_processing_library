from fuzzywuzzy import fuzz
from config import THRESHOLD, TRUTH, PRED


def calculate_fuzzy_matching(truth, pred, threshold):
    # Split the truth string into individual words
    truth_words = truth.lower().split()
    correct = 0
    false_positive = 0
    missed = 0

    for item in pred:
        found_match = False
        for word in truth_words:
            # Calculate the fuzzy match ratio
            match_ratio = fuzz.ratio(item.lower(), word)
            if match_ratio >= threshold:
                found_match = True
                # Printing the match ratio
                print(f"Match ratio for '{item}' and '{word}': {match_ratio}")
                break  # Exit the loop if a match is found
        if found_match:
            correct += 1
        else:
            false_positive += 1

    missed = len(truth_words) - correct
    # Printing the results
    print("Correct:", correct)
    print("False Positive:", false_positive)
    print("Missed:", missed)


if __name__ == '__main__':
    calculate_fuzzy_matching(TRUTH, PRED, THRESHOLD)
