### WHAT IS PARTITIONING OF HARD DISK?
It is the concept in which a given hard disk is divided into segments of secondary storage, so that each segment is managed separately. This is also done with a view that if damage is caused to one segment, like in cases of complete deletion of data, the damage is not transferred to the entire disk. It rather remains confined to that particular segment.

### STATIC OR FIXED PARTITION
In this kind, the number of partitions in RAM are fixed , but the size of each partition may be same or may not be so. Click here to learn more about it.

### MAJOR STEPS INVOLVED IN CREATING A PARTITION
Three major steps are involved are:

- Create
- Format
- Mount
#### CREATING
You need to have a harddisk attached.

fdisk -l

This command shows you the list of all attached disks.

In the picture below, you can see I have a harddisk of size 10 GiB attached to my OS named /dev/xvdg.

list of drives
fdisk <drive_name> , In my case fdisk /dev/xvdg

This command creates the partition for you. The ‘n’ in the line 'Command (m for help):n' indicates that we are creating a new partition.

creating the partition
The hard disk is of size 10GB in total, But I want to make use of 3GB so I will input +3G.

w: to save the changes made to the partition.

creating
#### FORMATTING
mkfs.ext4 <drive_name>, In my case mkfs.ext4 /dev/xvdg1

Above command is used to format the partition.

format the partition
#### MOUNTING
Create a new directory , I created /TASK7.

mount /dev/xvdg1 /TASK7

In order to mount the partition to /TASK7.


df -hT

To check the successful mounting of the partition.

list of partitions
cd /TASK7: change the directory.

Within the directory create a file , I created simran.txt.

Now comes our main task which is to increase or decrease the size of the static partition.

For accomplishing this task, we need to first unmount it , using command:

umount /TASK7

Confirm the same using df -hT.

unmounting
e2fsck -f /dev/xvdg1

This command will check errors and will mark file system as clean.

checking file system
RESIZING
resize2fs /dev/xvdg1 5G

The above command resizes my partition to 5GB.

After unmounting you can see that no files exist, but don’t worry your files are safe. It’s not yet visible because once unmounted you need to mount it again.

resizing the partition
For getting your files back along with the increased size of the partition, we need to mount it again:

mount /dev/xvdg1 /TASK7

Now search for your files. Boom! your files are safe and the size has also increased from 3GB to 5GB.

checking for files
Similarly we can decrease the size .

Suppose we want to decrease from 3GB in the initial to 1GB, we need to follow the same steps as above.

Only a small change, during resizing :

resize2fs /dev/xvdg1 1G

You are ready to try the same on your own. Thanks for reading!!
