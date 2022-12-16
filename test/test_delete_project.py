from model.project import Project
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def test_delite_project(app):
    if len(app.project.get_project_list()) == 0:
        test = Project(name = random_string("name=", 5), description= random_string("desc=", 7))
        app.project.add_project(test)
    old_list = app.project.get_project_list()
    project = random.choice(old_list)
    app.project.delete_project(project)
    new_list = app.project.get_project_list()
    assert len(old_list) - 1 == len(new_list)
    old_list.remove(project)
    assert sorted(old_list, key=Project.ret_name) == sorted(new_list, key=Project.ret_name)

def test_soap_delite_project(app):
    if len(app.project.get_project_list()) == 0:
        test = Project(name = random_string("name=", 5), description= random_string("desc=", 7))
        app.project.add_project(test)
    old_list = app.soap.get_project_list()
    project = random.choice(old_list)
    app.project.delete_project(project)
    new_list = app.soap.get_project_list()
    assert len(old_list) - 1 == len(new_list)
    old_list.remove(project)
    assert sorted(old_list, key=Project.ret_name) == sorted(new_list, key=Project.ret_name)