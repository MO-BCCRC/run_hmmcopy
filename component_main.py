from kronos.utils import ComponentAbstract
import os


class Component(ComponentAbstract):
    
    """
    Runs HMMcopy using R package 
    """

    def __init__(self, component_name="run_hmmcopy", 
                 component_parent_dir=None, seed_dir=None):
        
        self.version = "1.0.1"

        ## initialize ComponentAbstract
        super(Component, self).__init__(component_name, 
                                        component_parent_dir, seed_dir)

    def make_cmd(self, chunk=None):
        path = os.path.join(self.seed_dir, 'hmmcopy.R')

        cmd = ' '.join([self.requirements['R'], '--no-save', '--args'])

 #        if self.args.mode == [True, False]:
 #            normal_copy = 'NULL'
 #            tumour_copy = self.args.tumour_copy
 #        elif self.args.mode == [False, True]:
 #            tumour_copy = self.args.normal_copy
 #            normal_copy= 'NULL'
 #        elif self.args.mode == [True, True]:
 #            tumour_copy = self.args.tumour_copy
 #            normal_copy = self.args.normal_copy
 #        else:
 #            raise Exception('mode shouldn\'t have 2 False flags')
        if self.args.normal_copy:
            normal_copy = self.args.normal_copy
        else:
            normal_copy = 'NULL'

        if self.args.normal_table:
            normal_table = self.args.normal_table
        else:
            normal_table = 'NULL'

        if self.args.normal_table_out:
            normal_table_out = self.args.normal_table_out
        else:
            normal_table_out = 'NULL'

        cmd_args = [self.args.tumour_copy, self.args.tumour_table, 
                    normal_copy, normal_table,
                    self.args.segments,self.args.obj_file,
                    self.args.sample_id, normal_table_out,
                    self.args.tumour_table_out, '<', path]
        return cmd, cmd_args

## To run as stand alone
def _main():
    m = Component()
    m.args = component_ui.args
    m.run()

if __name__ == '__main__':
    import component_ui
    _main()

