class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if not k % 2:
            return -1
        n = length = 1
        reminders, reminder = set(), n % k
        while reminder:
            if reminder in reminders:
                return -1
            else:
                reminders.add(reminder)
                n = n * 10 + 1
                length += 1
                reminder = n % k
        return length
