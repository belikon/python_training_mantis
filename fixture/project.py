from model.project import Project

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    project_cache = None

    def add_project(self, project):
        wd = self.app.wd
        self.go_to_projects_page()
        self.create_new_project()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.name)
        if project.description is not None:
            wd.find_element_by_name("description").click()
            wd.find_element_by_name("description").clear()
            wd.find_element("name", "description").send_keys(project.description)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.project_cache = None

    def create_new_project(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()

    def go_to_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.go_to_projects_page()
            self.project_cache = []
            for element in wd.find_elements_by_xpath("//table[@class='width100']")[1].find_elements_by_css_selector(".row-1, .row-2"):
                cells = element.find_elements_by_tag_name("td")
                name = cells[0].text
                status = cells[1].text
                view_status = cells[3].text
                description = cells[4].text
                self.project_cache.append(Project(name=name, description=description, status=status, view_status=view_status))
        return list(self.project_cache)

    def select_project_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//table[@class='width100']")[1].find_elements_by_tag_name("a")[index].click()

    def delete_project(self, project):
        wd = self.app.wd
        self.go_to_projects_page()
        wd.find_element_by_link_text(project.name).click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()

