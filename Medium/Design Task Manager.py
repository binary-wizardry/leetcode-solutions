class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.tasks = {}
        self.priorities = []
        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.tasks[taskId] = userId, priority
        heapq.heappush(self.priorities, (-priority, -taskId, userId))

    def edit(self, taskId: int, newPriority: int) -> None:
        userId = self.tasks[taskId][0]
        self.tasks[taskId] = userId, newPriority
        heapq.heappush(self.priorities, (-newPriority, -taskId, userId))

    def rmv(self, taskId: int) -> None:
        del self.tasks[taskId]

    def execTop(self) -> int:
        while self.priorities:
            priority, taskId, userId = heapq.heappop(self.priorities)
            priority, taskId = -priority, -taskId
            check_user, check_priority = self.tasks.get(taskId, (None, None))
            if check_user == userId and check_priority == priority:
                self.rmv(taskId)
                return userId
        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
