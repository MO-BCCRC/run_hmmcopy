"""
component_params.py
"""

input_files  = {
                 'tumour_copy' : '__REQUIRED__',
                 'tumour_table' : '__REQUIRED__',
                 'normal_copy' : None,
                 'normal_table' : '__REQUIRED__',
                }

output_files = {
                 'obj_file' : '__REQUIRED__',
                 'segments': '__REQUIRED__',
                 'normal_table_out' : '__REQUIRED__',
                 'tumour_table_out':'__REQUIRED__',
                }

input_params = {
                'mode' : '__REQUIRED__',
                'sample_id' : '__REQUIRED__',
                }

return_value = []
