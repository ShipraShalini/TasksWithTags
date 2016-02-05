from datetime import datetime

from src.api.helpers.createmessagestring import createmessagestring
from src.api.helpers.splittags import splittags
from src.common.constants.backendconstatants import *
from src.common.models.models import Task


class ActionClass(object):
    s = Task.search()

    def common_edit(self, task, task_data):
        try:
            task.status = task_data['status']
        except KeyError:
            pass

        try:
            task.task = task_data['task']
        except:
            pass

        try:
            task.tags = splittags(task_data['tags'])
        except:
            pass

        task.save()
        return task


    def create(self, task_data):
        id = str(datetime.now())
        print "id", id
        task = Task(meta={'id': id})
        task.status = STATUS_TODO
        task.date_created = id
        if not task_data['task']:
            raise Exception
        print "task", task.__dict__
        task= self.common_edit(task=task, task_data=task_data)._d_
        return task

    def modify(self,task_data):
        task = self.s.filter('term', taskno= task_data['taskno'])
        task= self.common_edit(task=task, task_data=task_data)
        return task

    def toggle(self,id):
        task =  Task.get(id = id)
        task.status = STATUS_DONE if task.status==STATUS_TODO else STATUS_TODO
        task.save()
        return task


    def delete(self,task_data):
        id = task_data['id']
        task =  Task.get(id = id, ignore=404)
        task.delete()
        message = createmessagestring(TASKDELTED)

        return message


actionclass = ActionClass()