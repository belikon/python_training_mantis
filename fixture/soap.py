from suds.client import Client
from suds import WebFault
from model.project import  Project

class SoapHelper:
    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(self.app.baseUrl + "/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self):
        username = self.app.config['web']['username']
        password = self.app.config['web']['password']
        soap_project_list = []
        client = Client(self.app.baseUrl + "/api/soap/mantisconnect.php?wsdl")
        try:
            result = client.service.mc_projects_get_user_accessible(username, password)
            for soap_list in result:
                name = soap_list['name']
                description = soap_list['description']
                status = soap_list['status']['name']
                view_status = soap_list['view_state']['name']
                soap_project_list.append(Project(name=name, description=description, status=status, view_status=view_status))
            return soap_project_list
        except WebFault:
            return False
