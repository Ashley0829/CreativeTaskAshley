#----------------------------------------------------------------------------------------------------
# Define Global Lists and Variables
#----------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------
# SAT_Writing_Test_Config = list of 30 elements - [Test Topics, Average Number of Questions]
# Source: from the KhanAcademy.org (https://www.khanacademy.org/mission/sat/tips-and-planning)
#  - Test Topics : SAT Writing and Language Test question guides (30 guides)
#  - Average Number of Questions : median of the range values, which is provided in "What's on the test" of each guide
#---------------------------------------------------------------------------------------------------
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

#-------------------------------------------------------------------------------------------------
# Diagnosis Test Results : list of element - [test_date, test_name, test_result, conversion_table]
#-------------------------------------------------------------------------------------------------
# test_date : diagnostic test date
# test_name : name of diagnostic test set
# test_result : list of the number of incorrect answers, each element represents the 30 test topics
# conversion_table : list of numbers which converts raw score to SAT Writing Scores, which is available at the "Scoring Your SAT Practice Test".
Diagnosis_Test_Results = []

# Diagnosis Test Result #1 (using the CollegeBoard's The SAT Practice Test #6)
test_date = "December 5 2020"
test_name = "The SAT Practice Test#6"
# my real test results
test_result = [0, 1, 3, 1, 3, 1, 0, 0, 2, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 3, 0, 0, 1]
# source: SAT Practice Test #6: Worksheets, RAW SCORE CONVERSION TABLE1, CollegeBoard
conversion_table = [10, 10, 10, 11, 11, 12, 13, 14, 15, 16, 16, 17, 18, 18, 19, 20, 20, 21, 22, 23, 23, 24, 25, 25, 26, 27, 27, 28, 28, 29, 30, 30, 31, 31, 32, 33, 34, 34, 35, 36, 36, 38, 39, 39, 40]
Diagnosis_Test_Results.append([test_date, test_name, test_result, conversion_table])

# Diagnosis Test Result #2 (using the CollegeBoard's The SAT Practice Test #1)
test_date = "December 20 2020"
test_name = "The SAT Practice Test#1"
# my real test results
test_result = [0, 0, 0, 1, 3, 0, 1, 2, 2, 1, 0, 3, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0.5, 0, 0, 0, 0, 0, 0, 1]
# source: SAT Practice Test #1: Worksheets, RAW SCORE CONVERSION TABLE1, CollegeBoard
conversion_table = [10, 10, 10, 10, 11, 12, 13, 13, 14, 15, 16, 16, 17, 18, 19, 19, 20, 21, 21, 22, 23, 23, 24, 25, 25, 26, 26, 27, 28, 28, 29, 30, 30, 31, 32, 32, 33, 34, 34, 35, 36, 37, 38, 39, 40]
Diagnosis_Test_Results.append([test_date, test_name, test_result, conversion_table])

# Diagnosis Test Result #3 (using the CollegeBoard's The SAT Practice Test #3)
test_date = "December 23 2020"
test_name = "The SAT Practice Test#3"
# my real test results
test_result = [0, 1, 0, 2, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1]
# source: SAT Practice Test #3: Worksheets, RAW SCORE CONVERSION TABLE1, CollegeBoard
conversion_table = [10, 10, 10, 11, 12, 13, 14, 15, 15, 16, 17, 18, 19, 19, 20, 21, 22, 22, 23, 24, 24, 25, 25, 26, 26, 27, 27, 28, 29, 29, 30, 30, 31, 32, 33, 33, 34, 34, 35, 35, 36, 37, 38, 39, 40]
Diagnosis_Test_Results.append([test_date, test_name, test_result, conversion_table])

# Diagnosis Test Result #4 (using the CollegeBoard's The SAT Practice Test #5)
test_date = "January 2 2021"
test_name = "The SAT Practice Test#5"
# my real test results
test_result = [1, 0, 1, 2, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
# source: SAT Practice Test #3: Worksheets, RAW SCORE CONVERSION TABLE1, CollegeBoard
conversion_table = [10, 10, 10, 10, 11, 12, 13, 13, 14, 15, 16, 16, 17, 18, 18, 19, 20, 20, 21, 22, 23, 23, 24, 25, 25, 26, 27, 28, 28, 29, 30, 30, 31, 32, 32, 33, 34, 34, 35, 36, 37, 38, 39, 40, 40]
Diagnosis_Test_Results.append([test_date, test_name, test_result, conversion_table])

# More Diagnosis Tests Results can be easily added by append() to the list - Diagnostic_Test_Results as below
# Diagnostic_Test_Results = [ [test_date1, test_name1, test_result1, conversion_table1],
#                             [test_date2, test_name2, test_result2, conversion_table2]
#                             [test_date3, test_name3, test_result3, conversion_table3]
#                              .....
#                             [test_dateN, test_nameN, test_resultN, conversion_tableN]]

#-----------------------------------------------------------------------------------------------
# Other Variables
#-----------------------------------------------------------------------------------------------
Number_of_Diagnosis_Tests = len(Diagnosis_Test_Results)             # number of diagnosis tests
Length_of_Conversion_Table = len(conversion_table)                  # Number of Questions + 1 - "0" case
Number_of_SAT_Writing_Questions = Length_of_Conversion_Table - 1    # "0" case must be excluded from Conversion Table


#-----------------------------------------------------------------------------------------------------------------------
# Procedure - calculate_Weakness(test_config, diagnosis_test_results, weight)
# input :   test_config = list of elements - [Test Topics, Average Number of Questions]
#           diagnosis_test_results = list of elements - [test_date, test_name, test_result, conversion_table]
#           weight = weight values for each element of diagnosis_test_results
# output :  weakness = list of weighted incorrect answer rates (0~1.0) for each test topic question
#-----------------------------------------------------------------------------------------------------------------------
def calculate_Weakness(test_config, diagnosis_test_results, weight):

    # number of test topic
    number_of_test_topic = len(test_config)

    # number of diagnosis
    number_of_diagnosis = len(diagnosis_test_results)

    # to apply weight to each element of diagnosis_test_results, it should be normalized
    weight_normalized = normalize_weight(weight)

    # initialize return value : using reference: https://stackoverflow.com/questions/8528178/list-of-zeros-in-python
    weakness = [0] * number_of_test_topic

    for index_test_topic in range(0, number_of_test_topic):
        weakness_index_test_topic = 0.0
        # calculate weighted incorrect answer rates (0.0 ~ 1.0) from all the test results of diagnosis_test_results
        for index_diagnosis in range(0, number_of_diagnosis):
            weakness_index_test_topic = weakness_index_test_topic + weight_normalized[index_diagnosis]*diagnosis_test_results[index_diagnosis][2][index_test_topic]
        weakness_index_test_topic = weakness_index_test_topic / test_config[index_test_topic][1]
        weakness[index_test_topic] = weakness_index_test_topic

    # return
    return weakness

#-----------------------------------------------------------------------------------------------------------------------
# Procedure - calculate_Combined_Conversion_Table(diagnosis_test_results, weight)
# input :   diagnosis_test_results = list of elements - [test_date, test_name, test_result, conversion_table]
#           weight = weight values for each element of diagnosis_test_results
# output :  combined_conversion_table = combination of conversion tables (from diagnosis_test_results) with weight
#-----------------------------------------------------------------------------------------------------------------------
def calculate_Combined_Conversion_Table(diagnosis_test_results, weight):

    # normalize weight
    weight_normalized = normalize_weight(weight)

    # initialize return value : using reference: https://stackoverflow.com/questions/8528178/list-of-zeros-in-python
    combined_conversion_table = [0] * Length_of_Conversion_Table

    # calculate combined conversion table using normalized weight
    for test_i in range(0, Number_of_Diagnosis_Tests):
        for table_i in range(0, Length_of_Conversion_Table):
            combined_conversion_table[table_i] = combined_conversion_table[table_i] + weight_normalized[test_i] * diagnosis_test_results[test_i][3][table_i]

    # round each value of combined_conversion_table to integer by using round()
    # using reference : https://stackoverflow.com/questions/35651470/rounding-a-list-of-floats-into-integers-in-python
    combined_conversion_table = [round(x) for x in combined_conversion_table]

    # return
    return combined_conversion_table

#-----------------------------------------------------------------------------------------------------------------------
# Procedure - normalize_weight(weight)
# input :   weight = unnormalized weight values (i.e., sum of weight is not 1.0)
# output :  weight_normalized = weight / sum_of_weight (i.e., sum of normalized weight is 1.0)
#-----------------------------------------------------------------------------------------------------------------------
def normalize_weight(weight):

    # initialize weight_normalized
    weight_normalized = len(weight)*[0]

    # get weight_sum
    weight_sum = sum(weight)  # reference: https://stackoverflow.com/questions/11344827/summing-elements-in-a-list

    # divide each weight by weight_sum
    for index in range(0, len(weight)):
        weight_normalized[index] = weight[index] / weight_sum

    # return
    return weight_normalized

#-----------------------------------------------------------------------------------------------------------------------
# Procedure - calculate_Expected_Wrong_Answers(test_config, weakness)
# input :   test_config = list of elements - [Test Topics, Average Number of Questions]
#           weakness = list of incorrect answer rates (0.0 ~ 1.0) for each test topic question
# output :  expected_wrong_answers = list of expected total incorrect answers for each test topic based on weakness
#-----------------------------------------------------------------------------------------------------------------------
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

#-----------------------------------------------------------------------------------------------------------------------
# Procedure - convert_test_result_to_Score(test_result, conversion_table)
# input :   test_result = list of the number of incorrect answers, each element represents the 30 test topics
#           conversion_table  = list of converting number (raw score to SAT Writing Scores)
# output :  converted_score = converted SAT scores
#-----------------------------------------------------------------------------------------------------------------------
def convert_test_result_to_Score(test_result, conversion_table):

    # total number of questions
    total_number_of_questions = len(conversion_table) - 1   # conversion table includes '0', so it should be excluded

    # calculate number of correct answers
    # sum of list : reference: https://stackoverflow.com/questions/11344827/summing-elements-in-a-list
    # number_of_correct_answers will be used as index for conversion table, so it should be floor to integer by int()
    number_of_correct_answers = int(total_number_of_questions - sum(test_result))

    # apply the conversion equation of the SAT Practice Test Worksheets to get converted scores
    # using equation of "SAT Practice Test : Worksheets, RAW SCORE CONVERSION TABLE1, CollegeBoard"
    converted_score = 10*conversion_table[number_of_correct_answers]

    # return
    return converted_score

#-----------------------------------------------------------------------------------------------------------------------
# Procedure - find_maximum_index(list)
# input  :  list = list of numbers (i.e., correct answers, expected wrong answers, and etc.)
# output :  index and value for maximum element, if maximum value is 0 return -1, 0
#-----------------------------------------------------------------------------------------------------------------------
def find_maximum_index(list):

    # initialize index_maximum as zero and maximum value as list[0]
    index_maximum = 0
    maximum_value = list[0]

    # find maximum value and index
    for index in range(1, len(list)):
        if list[index] > maximum_value:
            index_maximum = index
            maximum_value = list[index]

    # if maximum_value is zero, return -1 as index_maximum, otherwise return index_maximum
    if maximum_value == 0:
        return -1, 0
    else:
        return index_maximum, maximum_value

#-----------------------------------------------------------------------------------------------------------------------
# Procedure - find_Study_Priorities(test_config, diagnosis_test_results, weight_method, weight_manual)
# input :   test_config = list of elements - [Test Topics, Average Number of Questions]
#           diagnosis_test_results = list of elements - [test_date, test_name, test_result, conversion_table]
#           weight_method = weight method for analyzing diagnosis_test_results
#           weight_manual = weight values for each element of diagnosis_test_results
# output :  study_priority = list of [achievable score, index, expected wrong answers for question topic],
#                            sorted by expected wrong answers in descending order
#-----------------------------------------------------------------------------------------------------------------------
def find_Study_Priorities(test_config, diagnosis_test_results, weight_method, weight_manual):

    # number of tests
    number_of_tests = len(diagnosis_test_results)

    #---------------------------------------------------------------
    # STEP 1: determine weight according to input - "weight_method"
    #---------------------------------------------------------------
    weight = number_of_tests*[0]

    # 1: equivalent weight
    if weight_method == 1:
        for i in range(0, number_of_tests):
            weight[i] = 1

    # 2: time_forgetting
    elif weight_method == 2:
        for i in range(0, number_of_tests):
            weight[i] = i/(number_of_tests-1)

    # 3: usd manual weight
    elif weight_method == 3:
        for i in range(0, number_of_tests):
            weight[i] = weight_manual[i]

    # otherwise return -1 => terminate procedure because weight_method is unknown
    else:
        return -1

    #-------------------------------------------------------------------------------------------------------------------
    # STEP 2: make combined_conversion_table, which combines all the conversion tables of test_result using weight
    #-------------------------------------------------------------------------------------------------------------------
    combined_conversion_table = calculate_Combined_Conversion_Table(diagnosis_test_results, weight)

    #-------------------------------------------------------------------------------------------------------------------
    # STEP 3: calculate weakness - list of incorrect answer rates (0.0 ~ 1.0) for each test topic question using weight
    #         i.e., probability of incorrect answer for each test topic
    #-------------------------------------------------------------------------------------------------------------------
    weakness = calculate_Weakness(test_config, diagnosis_test_results, weight)

    #-------------------------------------------------------------------------------------------------------------------
    # STEP 4: calculate expected wrong_answers - list of expected incorrect answers for each test topic using weakness
    #-------------------------------------------------------------------------------------------------------------------
    expected_wrong_answers = calculate_Expected_Wrong_Answers(SAT_Writing_Test_Config, weakness)

    #-------------------------------------------------------------------------------------------------------------------
    # STEP 5: build study_priority list - sequence of topics, which maximizes SAT scores with same studying time
    #-------------------------------------------------------------------------------------------------------------------
    # initialize study_priority,
    # - the first row : current expected score
    # - each row : expected score, test topic for study, expected wrong answers from previous test results
    study_priority = []
    expected_score = convert_test_result_to_Score(expected_wrong_answers, combined_conversion_table)
    study_priority.append([expected_score, -1, 0])

    # number of test topic
    number_of_test_topic = len(expected_wrong_answers)

    # find study_priority by rearranging the index in descending order of expected wrong answers
    for index in range (0, number_of_test_topic):

        # find index which has maximum expected wrong answers, i.e. maximum improvable test topic
        index_maximum, maximum_value = find_maximum_index(expected_wrong_answers)

        # if index_maximum is -1, there is no more test topic to study => terminate finding index
        if index_maximum == -1 :
            break

        # add index_maximum to study_priority and replace the value of expected_wrong_answers as zero
        expected_wrong_answers[index_maximum] = 0
        expected_score = convert_test_result_to_Score(expected_wrong_answers, combined_conversion_table)
        study_priority.append([expected_score, index_maximum, maximum_value])

    # return
    return study_priority

#-------------------------------------------------------------------------------------
# Main program
#-------------------------------------------------------------------------------------

#-----------------------------------------------------
# [Step 1] Get inputs : weight_method, weight_manual
#-----------------------------------------------------
weight_method = 0
weight_manual = Number_of_Diagnosis_Tests*[1]
print("=====================================================================================================")
print(" Welcome to SAT Writing Study Adviser based on your {} diagnosis test results!".format(Number_of_Diagnosis_Tests))
print("=====================================================================================================")
print(" At first, determine Weight for {} test results".format(Number_of_Diagnosis_Tests))
weight_method = int(input(' Select your choice  : 1) Equivalent,  2) Time-forgetting, 3) Manual Input ? '))
if weight_method == 3:
    # see https://www.geeksforgeeks.org/python-get-a-list-as-input-from-user/
    weight_manual = list(map(float, input("Input {} numbers for weight_manual : ".format(Number_of_Diagnosis_Tests)).strip().split()))[:Number_of_Diagnosis_Tests]
    print(" your weight_manual is - ", weight_manual)

# terminate program if weight_method is unknown with message, reference:  https://stackoverflow.com/questions/285289/exit-codes-in-python
import sys
if weight_method < 1 or weight_method > 3 :
    print("Weight option was unknown... Run again program with correct weight option!")
    sys.exit(0)

#-------------------------------------------------------------------------------------
# [Step 2] Execute find_Study_Priority procedure using weight_method, weight_manual
#-------------------------------------------------------------------------------------
Study_Priority = find_Study_Priorities(SAT_Writing_Test_Config, Diagnosis_Test_Results, weight_method, weight_manual)

#--------------------------------
# [Step 3-1] Print result as text
#--------------------------------
print("=====================================================================================================")
print(" The SAT Writing Study Adviser recommends that your studying sequence should be ...")
print("=====================================================================================================")

achievable_score_figure = []
incorrect_answers_figure = []
study_topic_figure = []

for item in Study_Priority:
    if item[1] == -1 :
        print("  Current    Score: {:3d}".format(item[0]))
        achievable_score_figure.append(item[0])
        incorrect_answers_figure.append(0)
        study_topic_figure.append("")
    else :
        print("  Achievable Score: {:3d} <= {:.1f} incorrect answers could be improved by studying the topic '{}' ".format(item[0], item[2], SAT_Writing_Test_Config[item[1]][0]))
        achievable_score_figure.append(item[0])
        incorrect_answers_figure.append(item[2])
        study_topic_figure.append(SAT_Writing_Test_Config[item[1]][0])

#-------------------------------------
# [Step 3-2] Display result as figure
#-------------------------------------
# for figure, see
# https://matplotlib.org/3.1.1/gallery/ticks_and_spines/ticklabels_rotation.html
# https://matplotlib.org/3.1.1/gallery/ticks_and_spines/ticklabels_rotation.html#sphx-glr-gallery-ticks-and-spines-ticklabels-rotation-py
# https://pythondata.com/visualizing-data-overlaying-charts/
import matplotlib.pyplot as plt #to install matplotlib, see 'https://matplotlib.org/3.3.3/users/installing.html'
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

# ax1: create bars
ax1.bar(study_topic_figure, incorrect_answers_figure)

# add title and axis name
plt.title("The SAT Writing Study Adviser : Efficient Study Sequences to Improve Your Scores!")
plt.xlabel('Question Topics')
ax1.set_ylabel('Raw Scores needs to be Improved')
ax1.set_ylim(0, 5.0)

# options
plt.setp(ax1.get_xticklabels(), rotation = 90)  # rotate xticks 90 degree
plt.subplots_adjust(bottom = 0.30)

# ax2: create line charts
ax2.plot(study_topic_figure, achievable_score_figure, 'r*-')
ax2.set_ylabel('Achievable SAT Writing Score')
ax2.set_ylim(200, 430.0)
ax2.grid(True)    # turn on grid #2

# place a text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
textstr = ''
if weight_method == 1:
    textstr = "Weight : 1) Equivalent"
elif weight_method == 2:
    textstr = "Weight : 2) Time-forgetting"
elif weight_method == 3:
    textstr = "Weight : 3) Manual Input"
ax1.text(0.05, 0.95, textstr, transform=ax1.transAxes, fontsize=14, verticalalignment='top', bbox=props)

# show plot
plt.show()