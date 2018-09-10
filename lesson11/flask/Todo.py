#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Todo:
    def __init__(self):
        self.taskList = []
        self.__fileLocation__ = "./todo.txt"
        self.__loadTask__()

    def addTodo(self, thing):
        self.taskList.append(thing)
        self.__saveTodo__()
        return True

    def removeTodo(self, thing):
        if not thing in self.taskList:
            return False
        else:
            self.taskList.remove(thing)
            self.__saveTodo__()
            return True

    def searchTodo(self, thing):
        for todo in self.taskList:
            if thing in todo:
                return todo
        return None

    def getAllToto(self):
        return self.taskList

    def __loadTask__(self):
        file = open(self.__fileLocation__, 'r')
        # 换行符
        self.taskList = []
        for task in file.readlines():
            self.taskList.append(task.replace('\n', ''))

    def __saveTodo__(self):
        file = open(self.__fileLocation__, 'w')
        file.write('\n'.join(self.taskList))
        file.close()
