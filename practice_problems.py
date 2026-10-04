"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.

Example:
Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False
"""

def has_duplicates(product_ids):
    """ Takes a list of product IDs. Returns True if duplicates are found and False if the list contains no duplicates"""
    
    #Convert the list to a set to remove duplicates
    product_ids_set = set(product_ids)
    
    #If values are removed from the list when it's converted to a set, there were duplicates
    if len(product_ids) > len(product_ids_set):
        return True  #duplicates found
    else:
        return False  #no duplicates 

print("Question 1:\n")

product_ids_duplicates = [10, 20, 30, 20, 40]
print(product_ids_duplicates, "\nContains duplicates:", has_duplicates(product_ids_duplicates), "\n")

product_ids_no_duplicates = [1, 2, 3, 4, 5]
print(product_ids_no_duplicates, "\nContains duplicates:", has_duplicates(product_ids_no_duplicates), "\n")


"""
A list and a set work well for this task. Once the original list is converted to a set, their lengths can be compared to get the number of duplicates. Larger lists will take longer to convert to a set, but this conversion is still fast in Python. Additionally, finding the lengths of the list and set is a fast operation, since Python stores lengths in a built-in attribute.
"""


"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.
Implement a class that supports add_task(task) and remove_oldest_task().

Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"
"""
class Task:
    def __init__(self, name):
        self.name = name
        self.next = None

class TaskQueue:

    def __init__(self):
        self.front = None
        self.rear = None

    def __str__(self):
        """ Prints the contents of the queue when the print functon is used on a TaskQueue object """

        #Start with the first task in the queue
        current_task = self.front

        #Check if the queue is empty
        if not current_task:
            return "The queue is empty."

        #iterate through the queue and print each task name
        print("\nCurrent queue:")
        
        while current_task:
            print("- ", current_task.name)
            current_task = current_task.next
        
        return ""

    def add_task(self, task):

        #Create a new Task object using the provided task
        new_task = Task(task)

        #If the queue is empty, make the new task the front and rear of the queue.
        if not self.front:
            self.front = new_task
            self.rear = new_task

        #Otherwise, place the new task at the rear of the queue
        else:
            self.rear.next = new_task
            self.rear = new_task

        print("New task added:", new_task.name)

    
    def remove_oldest_task(self):
        """ Removes the oldest task from the queue """

        #Check if the queue is empty
        if not self.front:
            print("The queue is empty.")
            return

        #Always remove tasks from the front of the queue
        removed_task = self.front
        self.front = self.front.next

        #Change the front to the next task in the queue
        if not self.front:
            self.rear = None
        
        print(removed_task.name, "was removed from the queue.")
        return


print("Question 2:\n")

#Initialize the queue
task_queue = TaskQueue()

#Add tasks to the queue
task_queue.add_task("Write")
task_queue.add_task("Review")
task_queue.add_task("Print")

print(task_queue)

#Remove a task
task_queue.remove_oldest_task()

print(task_queue)

"""
A queue fits this task because the order of the list of tasks must be maintained, and the tasks must always be removed from the front of the line. The main operations are adding and removing items from the queue. Both operations are fast and predictable, since items are always added to the end and always removed from the front. 
"""


"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.

Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2
"""
from random import randint

class UniqueTracker:
    def __init__(self):
        
        self.integers = set()

    
    def add(self, value):
        """ Adds the supplied integer to the integers set """
        
        self.integers.add(value)
        
        print(value)  #print the value for testing purposes

    
    def get_unique_count(self):
        """ Returns the length of the integers set """
        
        return len(self.integers)
        

print("Question 3:\n")

tracker = UniqueTracker()

#Feed 5 random integers between 1 - 5 to the UniqueTracker class
counter = 0

while counter < 5:
    tracker.add(randint(1, 5))
    counter += 1

#Print the list and its unique count 
print("Unique integers:", tracker.get_unique_count(), "\n")

#Add more integers
counter = 0

while counter < 5:
    tracker.add(randint(6, 10))
    counter += 1

#Show updated list and the new number of unique integers
print("Unique integers:", tracker.get_unique_count(), "\n")


"""
A set works well for this task because it only requires returning the number of unique values seen, rather than storing all values in a specific order. The main operations involve adding integers and getting the length of the list, which are both relatively fast in Python, even for large sets.
"""

