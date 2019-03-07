import os
import fnmatch

from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(

   """Argument spec dictionary, setting required to true, ansible will ensure they are true"""
        argument_spec=dict(ext=dict(type='str', required=True),
                           dir=dict(type='path', required=True),
                           )
    )

    directory = module.params['dir']
    extension = module.params['ext']

    file_count = len([os.path.join(dirpath, f)
                      for dirpath, _, files in os.walk(directory)
                      for f in fnmatch.filter(files, extension)])


    module.exit_json(file_count=file_count,
                     dir=directory,
                     ext=extension,
                     changed=True,
                     )

    if __name__ == '__main__':
        main()