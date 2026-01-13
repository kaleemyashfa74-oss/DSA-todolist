# Urgent To-Do List using Stack (LIFO)
# Stack is following the Last In First Out rule

stack = []

def push(task):
    # adding new task to stack
    stack.append(task)
    print("Task added:", task)

def pop_task():
    # taking last task out from stack
    if len(stack) == 0:
        print("Stack is empty")
    else:
        done = stack.pop()
        print("Completed task:", done)

def view_top():
    # displaying top task without taking it out
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Top task:", stack[-1])

def display_all():
    # all tasks in stack will be displayed
    if len(stack) == 0:
        print("No tasks available")
    else:
        print("All tasks:")
        for t in stack:
            print("-", t)

# testing the program
push("Submit assignment")
push("Prepare for quiz")
push("Send email")

view_top()
display_all()
pop_task()
display_all()
