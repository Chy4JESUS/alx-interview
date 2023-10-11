#!/usr/bin/python3
"""Lockboxes """

def canUnlockAll(container):
  """
  Determine if all the boxes in the container
  can be opened.
  """

  if type(container) is not list or container is None:
    return False
  
  container_size = len(container)

  box_status = ['opened']
  for box in range(1, container_size):
    box_status.append('closed')


  for box_no in range(0, container_size):
    if box_no == 0 or box_status[box_no] == 'opened':
      for key in container[box_no]:
        if key < container_size and box_status[key] == 'closed':
          # use the key to loop through the key box number in the container
          for k in container[key]:
            if k < container_size:
              box_status[k] = 'opened'
        if key < container_size:
          box_status[key] = 'opened'

  return 'closed' not in box_status 
