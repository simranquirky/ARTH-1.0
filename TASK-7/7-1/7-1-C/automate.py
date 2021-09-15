import os
import getpass
import subprocess as sp
from lvm import VolumeGroup,LogicalVolume

while True:
            print("---------Welcome TO LVM (Logical Volume Management) Automation---------")
            print("\n")
            print("""
                  1).  Manage Volume Groups
                  2).  Manage Logical Volumes
                  3).  Exit 
                  """)
            print("\n")
            
            
            # Take Choice of User
            ch=int(input("Enter your Choice : "))
            if ch == 1:
                # Ask to User on which Volume Group he/she want to perform tasks/operations & Create VolumeGroup Class to Manage that Volume Group
                vg_name = VolumeGroup(input("Volume Group Name :")) 
                while True:
                    print("Volume Group -------> {0}".format(vg_name.vg_info['vg_name']))
                    print("""
                              A). Create Volume Group
                              B). Display Volume Group Information
                              C). Extend Volume Group Size
                              D). Merge two Volume Groups
                              E). Reduce Volume Group Size
                              F). Rename Volume Group
                              G). Remove Volume Group
                              H). Add Volume From Another Volume Group
                              I). Exit
                              """)
                    print("\n")
                    # Take Input that what operation user would like to perform
                    ch=input("What do you want to do => ")
                    if ch == 'A':
                        print("Create")
                        # Take list of Volume
                        volumes=[volume.replace(" ","") for volume in input("Enter volumes : ").split(",")]
                        print(volumes)
                        # Create Volume Group
                        vg_name.create(volumes)
                    elif ch == 'B':
                        # Display Volume Group Information
                        vg_name.display()
                    elif ch == 'C':
                        print("Extend")
                        # Take Volumes List
                        volumes=[volume.replace(" ","") for volume in input("Enter volumes : ").split(",")]
                        # Extend Volume
                        vg_name.extend(volumes)
                    elif ch == 'D':
                        print("Merge")
                        # Take Volume Group which will be merged
                        vg = VolumeGroup(input("Merged Volume Group :"))
                        # Merge Volume Group
                        vg_name.merge(vg)
                        # Delete Reference of Merged Volume Group
                        del vg
                    elif ch == 'E':
                        print("Reduce")
                        # Reduce Volume Group . For this take input Volume
                        vg_name.reduce(input("Enter volume name (which we want to remove from Volume Group) : "))
                    elif ch == 'F':
                        print("Rename")
                        # Rename VOlume Group . Take New Volume Group Name
                        vg_name.rename(input("New Volume Group Name : "))
                    elif ch == 'G':
                        print("Remove")
                        # Remove Volume Group
                        vg_name.remove()
                    elif ch == 'H':
                        print("Add")
                        # Split Volume form Another Volume Group 
                        vg_name.add(VolumeGroup(input("Enter Volume Group : ")),input("Volume Name : "))
                    elif ch == 'I':
                        break
            elif ch == 2:
                lv_name = LogicalVolume(input("Enter Logical Volume Name : "),VolumeGroup(input("Enter Volume Group Name : ")))
                while True:
                    print("Logical Volume   ----->  {0}".format(lv_name.lv_info['lv_name']))
                    print("Volume Group     ----->  {0}".format(lv_name.vg.vg_info['vg_name']))
                    print("""
                              A). Create Logical Volume
                              B). Format Logical Volume
                              C). Mount Logical Volume
                              D). Unmount Logical Volume
                              E). Extend Logical Volume
                              F). Reduce Logical Volume
                              G). Remove Logical Volume
                              H). Display Logical Volume
                              I). Exit
                        """)
                    print("\n")
                    ch=input("What do you want to do => ")
                    if ch == 'A':
                        # Create Logical Volume
                        print("Create")
                        lv_name.create(input("Enter Logical Volume Size : "))
                    elif ch == 'B':
                        print("Format")
                        # Format Logical Volume
                        lv_name.format(input("Format Type : "))
                    elif ch == 'C':
                        print("Mount")
                        # Mount Logical Volume
                        lv_name.mount(input("Mount Point : "))
                    elif ch == 'D':
                        print("Unmount")
                        # Unmount Logical Volume
                        lv_name.unmount()
                    elif ch == 'E':
                        print("Extend")
                        # Extend Logical Volume
                        lv_name.extend(input("Extend Volume Size : "))
                    elif ch == 'F':
                        print("Reduce")
                        # Reduce Logical Volume
                        lv_name.reduce(input("Volume Size After Reducing : "))
                    elif ch == 'G':
                        print("Remove")
                        # Remove Logical Volume
                        lv_name.remove()
                    elif ch == 'H':
                        print("Display")
                        # Display Logical Volume Information
                        lv_name.display()
                    elif ch == 'I':
                        print("Exit")
                        break
            elif ch == 3:
                break
