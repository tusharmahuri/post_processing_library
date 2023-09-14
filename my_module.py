def named_entity_recognition(truth_list, prediction_list):
    correct_entities = 0
    missed_entities = 0
    false_positive_entities = 0
    truth_list = [item.lower() for item in truth_list]
    prediction_list = [item.lower() for item in prediction_list]

    for truth_value in truth_list:
        found = False
        for predicted_value in prediction_list:
            if predicted_value in truth_value or truth_value in predicted_value:
                correct_entities += 1
                found = True
                break
        if not found:
            missed_entities += 1

    for predicted_value in prediction_list:
        found = False
        for truth_value in truth_list:
            if predicted_value in truth_value or truth_value in predicted_value:
                found = True
                break
        if not found:
            false_positive_entities += 1

    return correct_entities, missed_entities, false_positive_entities
