import ctypes
import platform
import os

class SysInfo:

    def __init__(self):

        self.totalRam, self.availRam = self.ram()
        self.totalRam = self.totalRam / (1048576)
        self.availRam = self.availRam / (1048576)



    def ram(self):
    
        try:
            kernel32 = ctypes.windll.kernel32
            c_ulong = ctypes.c_ulong
        
            class MEMORYSTATUS(ctypes.Structure):
                _fields_ = [
                ('dwLength', c_ulong),
                ('dwMemoryLoad', c_ulong),
                ('dwTotalPhys', c_ulong),
                ('dwAvailPhys', c_ulong),
                ('dwTotalPageFile', c_ulong),
                ('dwAvailPageFile', c_ulong),
                ('dwTotalVirtual', c_ulong),
                ('dwAvailVirtual', c_ulong)
            ]

            memoryStatus = MEMORYSTATUS()
            memoryStatus.dwLength = ctypes.sizeof(MEMORYSTATUS)
            kernel32.GlobalMemoryStatus(ctypes.byref(memoryStatus))
            return (memoryStatus.dwTotalPhys, memoryStatus.dwAvailPhys)



        def get_free_space(self, folder, format="GB"):

            try:

                fConstants = {"GB": 1073741824,
                      "MB": 1048576,
                      "KB": 1024,
                      "B": 1
                  }
                if platform.system() == 'Windows':
                    free_bytes = ctypes.c_ulonglong(0)
                    ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(folder), None, None, ctypes.pointer(free_bytes))
                    #return (int(free_bytes.value/fConstants[format.upper()]), format)
                    return (int(free_bytes.value/1073741824), format)
                else:
                    return (int(os.statvfs(folder).f_bfree*os.statvfs(folder).f_bsize/fConstants[format.upper()]), format)
 


if __name__ == "__main__":
    sys = SysInfo()
    print "System Memory : %dMb total" % sys.totalRam
    print "Available System Memory  : %dMb free" % sys.availRam
    byteformat = "GB"
    drive = raw_input("Enter Drive:")
    space,size = sys.get_free_space(drive+":", byteformat)

    print(space,size)

            # except Exception as e:
            #     raise e