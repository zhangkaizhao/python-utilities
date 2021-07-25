with open('modules.txt') as f:
    module_names = [m.strip() for m in f.readlines()]

with open('module.py.tmpl') as f:
    template = f.read()

for module_name in module_names:
    file_content = template.format(module_name=module_name)
    exec(file_content)
