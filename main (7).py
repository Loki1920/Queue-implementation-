#Queue implementation 
queue = []
def enqueue():
  element = int(input("enter element:"))
  queue.append(element)
  print(f'{element} is added')
def dequeue():
  if not queue:
    print("queue is empty")
  else:
    e = queue.pop(0)
    print(f'removed element is :{e}')

def display():
  print(f"queue is {queue}")

while True:
  print("select operation 1. add 2.remove 3. show 4. Quit")
  choice = int(input("enter choice:"))

  if choice==1:
    enqueue()
  elif choice == 2:
    dequeue()
  elif choice==3:
    display()
  elif choice == 4:
    print("Thankyou! ")
    break
  else:
    print("valid operation ")
  