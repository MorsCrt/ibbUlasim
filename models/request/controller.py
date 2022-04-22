import check_list


def control_list():
    if check_list.check_empty():
        print("Links File Empty! First Run")
    diff = check_list.check_diff()
    if not diff:
        print("Database Up-Date!")

control_list()