import os


def make_diretories(dir):
    dir_path = os.path.join('my_project', subfolder, 'templates', dir)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def make_diretories_templates(dir):
    dir_path = os.path.join('my_project', 'templates', dir)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def make_files(*args):
    for file in args:
        if not os.path.exists(f"my_project/{subfolder}/{file}"):
            with open(f"my_project/{subfolder}/{file}", "x"):
                pass


def make_files_deeper(*args):
    for file in args:
        if not os.path.exists(f"my_project/{subfolder}/templates/{subfolder}/{file}"):
            with open(f"my_project/{subfolder}/templates/{subfolder}/{file}", "x"):
                pass


def make_files_templates(*args):
    for file in args:
        if not os.path.exists(f"my_project/templates/{subfolder}/{file}"):
            with open(f"my_project/templates/{subfolder}/{file}", "x"):
                pass


subfolders = ['settings', 'mainapp', 'authapp']
for subfolder in subfolders:
    dir_path = os.path.join('my_project', subfolder)

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    if subfolder == "mainapp":
        make_diretories("mainapp")
        make_diretories_templates("mainapp")

    if subfolder == "authapp":
        make_diretories("authapp")
        make_diretories_templates("authapp")

    if subfolder == "mainapp" or subfolder == "authapp":
        make_files('__init__.py', 'models.py', 'views.py')
        make_files_deeper('base.html', 'index.html')
        make_files_templates('base.html', 'index.html')

    if subfolder == "settings":
        make_files('__init__.py', 'dev.py', 'prod.py')
