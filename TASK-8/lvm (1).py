import subprocess
class VolumeGroup:
    """
        VolumeGroup Class will manage Volume Group in LVM(Logical Volume Management)
    """
    def __init__(self,name):
        """ 
            "__init__"  method takes name of Volume Group as a  Argument.
            It creates a variable vg_info , which will contain all inforamation about Volume Group.
            vg_info will have below information -
                > vg_name            --    Volume Group Name
                > vg_access          --    Volume Group Access
                > vg_statuc          --    Volume Group Status
                > vg_internal_number --    Internal Volume Group Number
                > max_lv             --    Maximum Number of Logical Volumes
                > cur_lv             --    Maximum number of Logical Volumes
                > lv_open_count      --    Open Count of All Logical Volumes in This Volume Group
                > max_lv_size        --    Maximum Logical Volume Size
                > max_pv             --    Maximum Number of Physical Volumes
                > cur_pv             --    Current Number of Physical Volumes
                > act_pv             --    Actual Number of Physical Volumes
                > vg_size            --    Size of Volume Group in KiloBytes
                > extent_size        --    Physical Extent Size
                > total_extent       --    Total Number of Physical Extents for This Volume Group
                > allocated_extent   --    Allocated Number of Physical Extents for This Volume Group
                > free_extent        --    free number of physical extents for this volume group
                > vg_uuid            --    UUID of Volume Group
                > volumes            --    List of Physical Volumes
        """
        self.vg_info = {}                     # Initialize vg_info varible
        self.vg_info['vg_name'] = name        # Initialize name in vg_info
        self.vg_info['volumes'] = set()       # Initialize volumes in vg_info
        VolumeGroup.refresh(self)             # Refresh VolumeGroup Information

    @staticmethod
    def refresh(self):
        """
            This is a static method which refreshes all information about Volume Group.
            It doesn't take any argument.
        """
        i=0
        info_name = ("vg_access","vg_status","vg_internal_number","max_lv","cur_lv","lv_open_count","max_lv_size","max_pv","cur_pv","act_pv","vg_size","extent_size","total_extent","allocated_extent","free_extent","vg_uuid")
        # Run "vgdisplay VG --colon" to get information which is stored in info_name variable
        info=subprocess.getoutput("vgdisplay " + self.vg_info['vg_name']+ " --colon").split(":")
        # loop to store Information in "vg_info" variable
        while i+1<len(info):
            self.vg_info[info_name[i]]=info[i+1]
            i+=1
        # Run "pvscan | grep VG" to get Physical Volumes (PVs) which are grouped in this Volume Group
        status,output=subprocess.getstatusoutput("pvscan | grep {0}".format(self.vg_info['vg_name']))
        # Store Physical Volume Names in vg_info variable
        if status == 0:
            volumes=output.split("\n")
            for volume in volumes:
                self.vg_info['volumes'] = self.vg_info['volumes'].union(set([volume.split(" ")[3]]))
        return 0

    def create(self,volumes,force=False):
        """
            "create" method creates Volume Group & it takes volumes list.

            "force" value will be helpful when Volume Group is already exit otherwise it will not impact.

            If "force" value is  True then it will extend volume in pre-created Volume Group otherwise it will not impact on Volume Group
            
            Data Types of Arguments -
                volumes  ---->   list
                force    ---->   bool
        """
        # Run "vgdisplay VG" command to check Volume Group exist or not. If it doesn't exist then code of if block will create New Volume Group.
        if subprocess.getstatusoutput("vgdisplay " + self.vg_info['vg_name'])[0]!=0:
            # this will create Volume Group
            status,output=subprocess.getstatusoutput("vgcreate {0} {1}".format(self.vg_info['vg_name'], " ".join(volumes)))
            print(output)
            if status==0:
                # Refresh Volume Group Information
                VolumeGroup.refresh(self)
                # Return 0 if New Volume is created
                return 0
        # Extend Volume if Volume Group is pre-created
        elif force==True and self.extend(volumes) != 0: 
            # Refresh Volume Group Information
            VolumeGroup.refresh(self)
            # Return 1 if Pre-created volume is extended
            return 1
        elif force==False:
            # Refresh Volume Group Information
            VolumeGroup.refresh(self)
            # Return 2 if Pre-created volume but not extended
            return 2

    def display(self):
        """
            Display Information About Volume Group.
            It doesn't take any argument.
        """
        # Display Information
        print(subprocess.getoutput("vgdisplay {0}".format(self.vg_info['vg_name'])))

    def extend(self,volumes):
        """
            Extend Volume Group size. It takes volumes as a Argument. 

            Data Types of Arguments -
               volumes  ---->   list
        """
        # Extend Volume
        status,output=subprocess.getstatusoutput("vgextend {0} {1}".format(self.vg_info['vg_name'] , " ".join(volumes)))
        print(output)
        if status == 0:
            # Refresh Volume Group Information
            VolumeGroup.refresh(self)
            return 0

    def merge(self,vg):
        """
            Merge another Volume Group into this Volume Group. It takes Volume Group Object Reference.
            
            Data Type of Arguments -
                vg  ---->   VolumeGroup
        """
        # Merge Volume Group
        status,output=subprocess.getstatusoutput("vgmerge {0} {1}".format(self.vg_info['vg_name'] , vg.vg_info['vg_name']))
        print(output)
        if status==0:
            # Remove Volume Group Information which is merged
            vg.__init__(vg.vg_info['vg_name'])
            # Refresh Volume Group Information
            VolumeGroup.refresh(self)
            return 0

    def reduce(self,volume):
        """
            Remove PV volume.
            It takes volume as a Argument.

            Data Type of Arguments - 
                volume  ---->  str
        """
        # Reduce Volume Group Size
        status,output=subprocess.getstatusoutput("vgreduce {0} {1}".format(self.vg_info['vg_name'] , volume))
        print(output)
        if status == 0:
            # Refresh Volume Group Information
            VolumeGroup.refresh(self)
            return 0

    def rename(self,name):
        """
            Rename Volume Group.

            Data Type of Arguments - 
                name  ---->  str
        """
        # Rename Volume Group
        status,output=subprocess.getstatusoutput("vgrename {0} {1}".format(self.vg_info['vg_name'],name))
        print(output)
        if status == 0:
            # Change name in vg_name variable
            self.vg_info['vg_name'] = name
            return 0

    def remove(self):
        """
            Remove Volume Group.
            It doesn't take any argument.
        """
        # Remove Volume Group
        status,output=subprocess.getstatusoutput("vgremove {0} --force".format(self.vg_info['vg_name']))
        print(output)
        if status==0:
            # Re-initialize vg_name
            self.__init__(self.vg_info['vg_name'])
            return 0

    def add(self,vg,volume):
        """
            Add Physical Volume to this Volume Group after split from another Volume Group.
            It takes Volume Group Reference & Physical Volume Name as a Arguments.

            Data Type of Arguments - 
                vg      ---->  VolumeGroup
                volume  ---->  str
        """
        # Split the Volume from another Volume Group('vg') & add that Volume into this Volume Group
        status,output=subprocess.getstatusoutput("vgsplit {0} {1} {2}".format( vg.vg_info['vg_name'] , self.vg_info['vg_name'] , volume))
        print(output)
        if status==0:
            # Refresh 'vg' Volume Group Information
            VolumeGroup.refresh(vg)
            if vg.vg_info['volumes'] == []:
                # If 'vg; have no volume after split then 'vg' will not exist so re-initialize 'vg' information
                vg.__init__(vg.vg_info['vg_name'])
            # Refresh Volume Group Information
            VolumeGroup.refresh(self)
            return 0

class LogicalVolume:
    """
        "LogicalVolume" class manages Logical Volume in LVM(Logical Volume Management)
    """
    def __init__(self,name,vg):
        """
            "__init__"  method takes name of Logical Volume Name & Volume Group object reference as a  Arguments.
            It creates a variable lv_info , which will contain all inforamation about Logical Volume.
            lv_info will have below information -
                > lv_name               --    Logical Volume Name
                > device_name           --    Logical Volume Device Name
                > lv_access             --    Logical Volume Access
                > lv_status             --    Logical Volume Status
                > lv_internal_number    --    Internal Logical Volume Number
                > lv_open_count         --    Open Count of Logical Volume
                > lv_size               --    Logical Volume Size in KiloBytes
                > cur_extent            --    Current Logical Extents Associated to Logical Volume
                > allocated_extent      --    Allocated Logical Extents of Logical Volume
                > allocation_policy     --    Allocation Policy of Vogical Volume
                > lv_read_ahead_sectors --    Read Ahead Sectors of Logical Volume
                > maj_dev_no            --    Major Device Number of Logical Volume
                > min_dev_no            --    Minor Device Number of Logical Volume
                > format_type           --    Format Type of INode Table For Logical Volume
                > mount_point           --    Mount Point of Logical Volume
                > previous_mount_point  --    Previous Mount Point of Logical Volume
        """
        # Intialize lv_info variable
        self.lv_info={}
        # Store name of Logical Volume in lv_info
        self.lv_info['lv_name'] = name
        # Store vg reference in 'vg' variable
        self.vg = vg
        # Store deivce name in lv_info
        self.lv_info['device_name'] = "/dev/{0}/{1}".format(self.vg.vg_info['vg_name'],self.lv_info['lv_name'])
        LogicalVolume.refresh(self)

    @staticmethod
    def refresh(self):
        """
            "refresh" method is a static method which will refresh all information about Logical Volume if any changes occur.
            It doesn't take any argument.
        """
        i=0
        info_name=("lv_access","lv_status","lv_internal_number","lv_open_count","lv_size","cur_extent","allocated_extent","alloc_policy","lv_read_ahead_sectors","maj_dev_no","min_dev_no")
        # Get Information About Logical Volume
        status,output=subprocess.getstatusoutput("lvdisplay {0}/{1} --colon".format(self.vg.vg_info['vg_name'],self.lv_info['lv_name']))
        if status == 0:
            info = output.split(":")
            # Update these Information in lv_info
            while i+2<len(info):
                self.lv_info[info_name[i]]=info[i+2]
                i+=1
        # Check Logical Volume is mounted or not
        status,output = subprocess.getstatusoutput("findmnt {0} | grep '/dev'".format(self.lv_info['device_name']))
        if status == 0:
            # If mounted then update Mount Point Information
            self.lv_info['mount_point'] = output.split(" ")[0]
        # Update Volume Group Information
        VolumeGroup.refresh(self.vg)
        return 0

    def create(self,size,mount_point=False,format_type = "ext4",force=False):
        """
            "create" method creates Logical Volume & it takes Logical Volume Size , Mount Point & Format type.

            By default value of mount_point is False. If you want to mount Logical Volume then give mount_point

            "force" value will be helpful when Logical Volume is already exit otherwise it will not impact.

            If "force" value is  True then it will extend Logical Volume Size & format & it otherwise it's value will not impact on Logical Volume

            Data Type of Arguments -
                size         ---->   str
                mount_point  ---->   In bool only False otherwise str
                format_type  ---->   str
                force        ---->   bool
        """
        # Check Logical Volume is already exist or not
        if subprocess.getstatusoutput("lvdisplay {0}".format(self.lv_info['device_name']))[0] !=0:
            # If Logical Volume doesn't exist then create it
            status,output=subprocess.getstatusoutput("lvcreate --size {0} --name {1} {2} -y".format(size,self.lv_info['lv_name'], self.vg.vg_info['vg_name']))
            print(output)
            if status==0:
                # Format it
                self.format(format_type)
                if mount_point != False:
                    # Mount it
                    self.mount(mount_point)
                # Refresh Logical Volume Information
                LogicalVolume.refresh(self)
                # Return zero (0) if Logical Volume is successfully created
                return 0

        elif force == True:
            print("True")
            # Update Logical Volume Information
            LogicalVolume.refresh(self)
            # Unmount if Logical Volume is mounted
            self.unmount()
            # Format it 
            self.format(format_type)
            if mount_point != False:
                # Mount it
                self.mount(mount_point)
            # Return zero (0) if Logical Volume is successfully created
            return 0

        elif force == False:
            print("False")
            # Check Logical Volume is mounted or not
            status,output = subprocess.getstatusoutput("findmnt {0} | grep '/dev'".format(self.lv_info['device_name']))
            if status == 0:
                # If mounted then update Mount Point Information
                self.lv_info['mount_point'] = output.split(" ")[0]
            # Update All Information 
            LogicalVolume.refresh(self)
            # Return zero (0) if Logical Volume is successfully created
            return 0

    def format(self,format_type="ext4"):
        """
            "format" method formats the Logical Volume.
            It takes format type as argument. By default value of format_type is "ext4"
        """
        # Format Logical Volume
        status,output=subprocess.getstatusoutput("mkfs.{0} {1}".format(format_type , self.lv_info['device_name']))
        print(output)
        if status == 0:
            # if Logical Volume is successfully formated then update lv_info
            self.lv_info['format_type'] = format_type
            # Return zero (0) if Logical Volume is successfully formated
            return 0

    def mount(self,mount_point):
        """
            "mount" method mounts the Logical Volume at given Mount Point.
            It takes Mount Point as argument.
        """
        # Mount Logical Volume
        status,output=subprocess.getstatusoutput("mount {0} {1}".format( self.lv_info['device_name'] , mount_point ))
        print(output)
        if status == 0:
            # if Logical Volume is successfully mounted then update lv_info
            self.lv_info['mount_point'] = mount_point
            # Return zero (0) if Logical Volume is successfully Mounted
            return 0

    def unmount(self):
        """
            "unmount" method unmounts the Logical Volume.
            It doesn't take any argument.
        """
        # Unmount Logical Volume
        status,output=subprocess.getstatusoutput("umount {0}".format(self.lv_info['device_name']))
        print(output)
        if status == 0 and 'mount_point' in self.lv_info:
            # Update previous_mount_point in lv_info
            self.lv_info['previous_mount_point']=self.lv_info['mount_point']
            # Delete 'mount_point' in lv_info
            del self.lv_info['mount_point']
            # Return zero (0) if Logical Volume is successfully unmounted
            return 0

    def extend(self,size):
        """
            "extend" method extends the Logical Volume Size.
            It takes extra volume size as argument (How much size we want to add volume)
        """
        # Extend Logical Volume
        status,output=subprocess.getstatusoutput("lvextend --size +{0} {1}".format(size,self.lv_info['device_name']))
        print(output)
        if status==0:
            # If Logical Volume Successfully extended then update all information
            LogicalVolume.refresh(self)
            # Return zero (0) if Logical Volume is successfully mounted
            return 0

    def reduce(self,size):
        """
            "reduce" method reduces the Logical Volume Size.
            It takes Volume Size (How much Logical Volume Size we want after reduce)
        """
        # Unmount Logical Volume if mounted
        mount_status=self.unmount()
        # Check the ext2/ext3/ext4 family of file systems
        subprocess.run(['e2fsck', '-f' ,self.lv_info['device_name']])
        # If size in float then 'if' block will change size in integer KiB then it will resize2fs because resize doesn't work for float size value
        if "." in size:
            size_type = size[-1]
            types = {"K":0,"M":1,"G":2,"T":3,"P":4,"E":5,"Z":6,"Y":7}
            for stype,times in types.items():
                if stype == size_type:
                    size = int(float(size.rsplit(size_type)[0])*(1024**times))
                    size = str(size) + "K"
        # Resize Logical Volume INode Table
        status,output=subprocess.getstatusoutput("resize2fs {0} {1}".format(self.lv_info['device_name'] , size))
        print(output)
        if status==0:
            # After successfully resized Reduce Logical Volume size
            status,output=subprocess.getstatusoutput("lvreduce --size {0} {1} --force".format( size , self.lv_info['device_name']))
            print(output)
        if mount_status == 0:
            # Mount Logical volume
            self.mount(self.lv_info['previous_mount_point'])
        # Update Logical Volume Information
        LogicalVolume.refresh(self)
        if status==0:
            # Return zero (0) if Logical Volume is successfully reduced
            return 0

    def remove(self):
        """
            It removes Logical Volume & doesn't take any Argument.
        """
        # Unmount if Logical Volume is mounted
        self.unmount()
        # Remove Logical Volume
        status,output=subprocess.getstatusoutput("lvremove {0} --force".format(self.lv_info['device_name']))
        print(output)
        if status == 0:
            # Re-initialize lv_info
            self.__init__(self.lv_info['lv_name'],self.vg)
            # Update Volume Group
            VolumeGroup.refresh(self.vg)
            # Return zero (0) if Logical Volume is successfully removed
            return 0

    def display(self):
        """
            Display Information About Volume Group.
            It doesn't take any argument.
        """
        # Display Logical Volume Information
        print(subprocess.getoutput("lvdisplay {0}".format(self.lv_info['device_name'])))
