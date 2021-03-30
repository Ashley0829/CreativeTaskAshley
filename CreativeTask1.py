SAT_Writing_Test_Config =  [["Setting up ideas", 2.5],
                            ["Strong support", 1.5],
                            ["Relevant information", 3.0],
                            ["Sequencing sentences", 1.5],
                            ["Transitions words and phrases", 4.0],
                            ["Transition sentences", 1.5],
                            ["Introductions and conclusions", 2.5],
                            ["Interpreting graphs and data", 1.5],
                            ["Precise word choice", 1.5],
                            ["Formal vs. casual language", 1.5],
                            ["Frequently confused words", 1.0],
                            ["Concision", 4.0],
                            ["Sentence fragments", 1.5],
                            ["Verb tense and mood", 1.5],
                            ["Modifier placement", 1.5],
                            ["Pronoun clarity", 1.0],
                            ["Pronoun-antecedent agreement", 1.5],
                            ["Confusion with its and their ", 1.5],
                            ["Making nouns possessive", 1.5],
                            ["Subject-verb agreement", 2.0],
                            ["Noun agreement", 1.0],
                            ["Conventional expressions", 1.5],
                            ["Parallel structure", 1.5],
                            ["Logical comparison", 1.5],
                            ["Commas", 1.8],
                            ["Semicolons", 1.8],
                            ["Colons", 1.8],
                            ["Lists and punctuation", 1.5],
                            ["Nonessential elements", 1.5],
                            ["Linking clauses", 2.5]]

#data from Khan Academy SAT Writing practice

Diagnosis_Test_Results = []

test_date = "December 5 2020"
test_name = "The SAT Practice Test#6"

conversion_table = [10, 10, 10, 11, 11, 12, 13, 14, 15, 16, 16, 17, 18, 18, 19, 20, 20, 21, 22, 23, 23, 24, 25, 25, 26, 27, 27, 28, 28, 29, 30, 30, 31, 31, 32, 33, 34, 34, 35, 36, 36, 38, 39, 39, 40]
Diagnosis_Test_Results.append([test_date, test_name, test_result, conversion_table])

test_date = "December 20 2020"
test_name = "The SAT Practice Test#1"

test_result = [0, 0, 0, 1, 3, 0, 1, 2, 2, 1, 0, 3, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0.5, 0, 0, 0, 0, 0, 0, 1]

conversion_table = [10, 10, 10, 10, 11, 12, 13, 13, 14, 15, 16, 16, 17, 18, 19, 19, 20, 21, 21, 22, 23, 23, 24, 25, 25, 26, 26, 27, 28, 28, 29, 30, 30, 31, 32, 32, 33, 34, 34, 35, 36, 37, 38, 39, 40]
Diagnosis_Test_Results.append([test_date, test_name, test_result, conversion_table])

test_date = "December 23 2020"
test_name = "The SAT Practice Test#3"

test_result = [0, 1, 0, 2, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1]

conversion_table = [10, 10, 10, 11, 12, 13, 14, 15, 15, 16, 17, 18, 19, 19, 20, 21, 22, 22, 23, 24, 24, 25, 25, 26, 26, 27, 27, 28, 29, 29, 30, 30, 31, 32, 33, 33, 34, 34, 35, 35, 36, 37, 38, 39, 40]
Diagnosis_Test_Results.append([test_date, test_name, test_result, conversion_table])

test_date = "January 2 2021"
test_name = "The SAT Practice Test#5"

test_result = [1, 0, 1, 2, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]

conversion_table = [10, 10, 10, 10, 11, 12, 13, 13, 14, 15, 16, 16, 17, 18, 18, 19, 20, 20, 21, 22, 23, 23, 24, 25, 25, 26, 27, 28, 28, 29, 30, 30, 31, 32, 32, 33, 34, 34, 35, 36, 37, 38, 39, 40, 40]
Diagnosis_Test_Results.append([test_date, test_name, test_result, conversion_table])


Number_of_Diagnosis_Tests = len(Diagnosis_Test_Results)             # number of diagnosis tests
Length_of_Conversion_Table = len(conversion_table)                  # Number of Questions + 1 - "0" case
Number_of_SAT_Writing_Questions = Length_of_Conversion_Table - 1    # "0" case must be excluded from Conversion Table

def calculate_Weakness(test_config, diagnosis_test_results, weight):

    # number of test topic
    number_of_test_topic = len(test_config)

    # number of diagnosis
    number_of_diagnosis = len(diagnosis_test_results)

    # to apply weight to each element of diagnosis_test_results, it should be normalized
    weight_normalized = normalize_weight(weight)

    # initialize return value
    weakness = [0] * number_of_test_topic

    for index_test_topic in range(0, number_of_test_topic):
        weakness_index_test_topic = 0.0
        # calculate weighted incorrect answer rates (0.0 ~ 1.0) from all the test results of diagnosis_test_results
        for index_diagnosis in range(0, number_of_diagnosis):
            weakness_index_test_topic = weakness_index_test_topic + weight_normalized[index_diagnosis]*diagnosis_test_results[index_diagnosis][2][index_test_topic]
        weakness_index_test_topic = weakness_index_test_topic / test_config[index_test_topic][1]
        weakness[index_test_topic] = weakness_index_test_topic

    return weakness

def calculate_Combined_Conversion_Table(diagnosis_test_results, weight):

    weight_normalized = normalize_weight(weight)

    combined_conversion_table = [0] * Length_of_Conversion_Table

    for test_i in range(0, Number_of_Diagnosis_Tests):
        for table_i in range(0, Length_of_Conversion_Table):
            combined_conversion_table[table_i] = combined_conversion_table[table_i] + weight_normalized[test_i] * diagnosis_test_results[test_i][3][table_i]

    combined_conversion_table = [round(x) for x in combined_conversion_table]

    return combined_conversion_table

def normalize_weight(weight):

    # initialize weight_normalized
    weight_normalized = len(weight)*[0]

    # get weight_sum
    weight_sum = sum(weight)

    # divide each weight by weight_sum
    for index in range(0, len(weight)):
        weight_normalized[index] = weight[index] / weight_sum

    # return
    return weight_normalized

def calculate_Expected_Wrong_Answers(test_config, weakness):

    # number of test topic
    number_of_test_topic = len(test_config)

    # initialize return value
    expected_wrong_answers = [0] * number_of_test_topic

    for index_test_topic in range(0, number_of_test_topic):
        # for each test topic, expected_wrong_answers = Average Number of Questions * weakness
        expected_wrong_answers[index_test_topic] = test_config[index_test_topic][1] * weakness[index_test_topic]

    # return
    return expected_wrong_answers

def convert_test_result_to_Score(test_result, conversion_table):

    total_number_of_questions = len(conversion_table) - 1   # conversion table includes '0', so it should be excluded

    number_of_correct_answers = int(total_number_of_questions - sum(test_result))

    converted_score = 10*conversion_table[number_of_correct_answers]

    # return
    return converted_score

def find_maximum_index(list):

    index_maximum = 0
    maximum_value = list[0]

    for index in range(1, len(list)):
        if list[index] > maximum_value:
            index_maximum = index
            maximum_value = list[index]

    if maximum_value == 0:
        return -1, 0
    else:
        return index_maximum, maximum_value

def find_Study_Priorities(test_config, diagnosis_test_results, weight_method, weight_manual):

