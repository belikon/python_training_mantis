from model.project import Project
import random

def test_add_project(app):
    test = Project(name = "test", description= "test2")
    old_list = app.project.get_project_list()
    app.project.add_project(test)
    new_list = app.project.get_project_list()
    old_list.append(test)
    assert len(old_list) + 1 == len(new_list)

def test_delite_project(app):
    if len(app.project.get_project_list()) == 0:
        test = Project(name="test", description="test2")
        app.project.add_project(test)
    old_list = app.project.get_project_list()
    project = random.choice(old_list)
    app.project.delete_project(project)
    new_list = app.project.get_project_list()
    assert len(old_list) - 1 == len(new_list)