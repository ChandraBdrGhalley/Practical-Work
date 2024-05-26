from queue import LifoQueue

backward_history = LifoQueue()
forward_history = LifoQueue()
current_page = None

NoOfVisits = int(input("Enter the number of url history: "))

print("Enter URLs to Visit:")
for i in range(NoOfVisits):
    url = input("URL: ")
    print(f"Visiting {url}")
    backward_history.put(current_page)
    current_page = url
print(f"current page: {current_page}")

while input("Do you want to go back? (yes/no):  ").lower() == 'yes':
    if not backward_history.empty():
        forward_history.put(current_page)
        current_page = backward_history.get()
        print(f"Going back to {current_page}")
    else:
        print("No previous page available")

while input("Do you want to go forward? (yes/no):  ").lower() == 'yes':
    if not backward_history.empty():
        forward_history.put(current_page)
        current_page = backward_history.get()
        print(f"Going forward to {current_page}")
    else:
        print("No forward page available")




