import json

from src.api.helpers.createmessagestring import createmessagestring
from src.common.constants.backendconstatants import *
from src.common.models.models import Task
from src.api.helpers.splittags import splittags


class SearchClass():
    s = Task.search()

    def find(self, tags):
        tags=splittags(tags)
        tasks = self.s.query("terms", tags=tags).execute()
        tasks = tasks._d_
        tasks = tasks['hits']['hits']
        task_list =[]
        for task in tasks:
            task_list.append(task['_source'])
        return task_list

    def findall(self):
        tasks = self.s.query("match_all").execute()
        if tasks:
            task_list =[]
            for task in tasks:
                task_list.append(task._d_)
            return task_list
        else:
            return createmessagestring(NOTASKLISTED)

searchclass = SearchClass()


