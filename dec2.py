def is_record_safe(record):
    """ This function checks if a record is safe

    A record consists of different levels. A record is considered safe if:
    
    Cond1: The differencies between adjacent levels should be all positive or all negative 
    Cond2: The absolut difference between two adjacent levels is at least 1 and at most 3.
    
    """
    differences_beween_adjacent_levels = [x-y for x,y in zip(record[:-1],record[1:])]
    cond1 = all(diff > 0 for diff in differences_beween_adjacent_levels) or all(diff < 0 for diff in differences_beween_adjacent_levels) 
    cond2 = all(abs(diff) in range(4) for diff in differences_beween_adjacent_levels)

    if cond1 and cond2:
        return True
    return False
 
def count_number_of_save_reports(records):
    res = [is_record_safe(record) for record in records]
    return sum(res)

def count_number_of_save_reports_problem_damper(records):
    all_results = []
    for record in records: 
        result = is_record_safe(record)
        j = 0
        while result == False and j < (len(record)):
            tmp_record = record.copy()
            tmp_record.pop(j)
            result = is_record_safe(tmp_record)
            j = j + 1 
        all_results.append(result)
    return sum(all_results)

if __name__ == "__main__":
    input = []
    with open("input_dec2.txt") as file:
        for line in file:
            clean_line = line.strip().split(" ")
            input.append([int(x) for x in clean_line])

    print(f"Number of safe reports found: {count_number_of_save_reports(input)}")
    print(f"Number of safe reports found when problem damper is used: {count_number_of_save_reports_problem_damper(input)}")

        