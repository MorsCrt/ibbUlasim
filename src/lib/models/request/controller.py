import src.lib.models.request.check_list as check_list
from src.lib.models.dataprocessing.pandasop import PandasOperations

def control_list():
    if check_list.check_empty():
        print("Links File Empty! First Run")
    diff = check_list.check_diff()
    if diff:
        print("Database Updating")
        PandasOperations(diff)
    else:
        print("Database Update")
        
