from todoist_api_python.api import TodoistAPI
import json
import pprint
import fixed

api = TodoistAPI(fixed.TODOIST_API)
pp = pprint.PrettyPrinter(indent=4)


def listing_todoist_projects():
    try:
        projects = api.get_projects()
        pp.pprint(projects)
        return projects
    except Exception as error:
        print(error)


def create_todoist_project(name):
    try:
        project = api.add_project(name=name)
        pp.pprint(project)
    except Exception as error:
        print(error)


def create_todoist_task(content, project_id):
    try:
        task = api.add_task(content=content, project_id=project_id)
        print(task)
    except Exception as error:
        print(error)


def projects_dictionary_list_creation():
    projects = listing_todoist_projects()
    projects_list = []
    for project in projects:
        new_project = {
            "name": project.name,
            "id": project.id
        }
        projects_list.append(new_project)
        pp.pprint(projects_list)
    return projects_list

