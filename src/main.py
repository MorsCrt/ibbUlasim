import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import src.lib.models.request.controller as ctrl

def main():
     ctrl.control_list()
     
main()