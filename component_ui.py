"""
component_ui.py

Note the places you need to change to make it work for you. 
They are marked with keyword 'TODO'.
"""

import argparse

#==============================================================================
# make a UI 
#==============================================================================
parser = argparse.ArgumentParser(prog='run_hmmcopy', 
                                 description = """
                                 brief description of your component goes here.""")

parser.add_argument(
                     "--tumour_copy", 
                    required = True, 
                    help= """
                    The corrected tumour wig
                    """)

parser.add_argument(
                     "--normal_copy",
                    default = None,
                    help= """
                    The corrected normal wig
                    """)

parser.add_argument(
                     "--outfile",
                    required = True,
                    help= """
                    The hmmcopy output file
                    """)
                    

## parse the argument parser.
args, unknown = parser.parse_known_args()
