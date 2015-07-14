'''
Created on 2015-07-13

Question: (Towers of Hanoi) Write a program to move the disks from the first tower to the last using Stacks.

'''

class Tower(object):
    
    def __init__(self, identifier):
        self.identifier = identifier
        self.stack = []
        
    def get_identifier(self):
        return self.identifier
    
    def add_disk(self, disk):
        if len(self.stack) == 0:
            self.stack.append(disk)
        else:
            if disk >= self.stack[-1]:
                print('Error placing disk ' + disk)
            else:
                self.stack.append(disk)
    
    # This is the actual worker
    def move_top_to(self, t):
        disk = self.stack.pop()
        t.add_disk(disk)
        print('Move disk ' + str(disk) + ' from Tower ' + str(self.identifier) + ' to Tower ' + str(t.get_identifier()))
        
    def move_disks(self, target_tower, buffer_tower, n):
        if n > 0:
            self.move_disks(buffer_tower, target_tower, n - 1)
            self.move_top_to(target_tower)
            buffer_tower.move_disks(target_tower, self, n - 1)

if __name__ == '__main__':
    t1 = Tower(1)
    t2 = Tower(2)
    t3 = Tower(3)
    for disk in range(5, 0, -1):
        t1.add_disk(disk)
    t1.move_disks(t3, t2, 5)