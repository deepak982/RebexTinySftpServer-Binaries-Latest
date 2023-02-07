# def preview(Filename,r):
#     import os
#     import pysftp as sftp
#     import subprocess
#     import platform

#     home_dir = os.path.expanduser('~')
#     download_dir = os.path.join(home_dir, 'Downloads')
#     os_name = platform.system()

#     cnopts = sftp.CnOpts()
#     cnopts.hostkeys = None
#     with sftp.Connection(host='192.168.1.39', username='tester', password='password',port=2222,cnopts=cnopts) as sftp:
#         dir = sftp.listdir('jnp')
#         for item in dir:
#             if Filename == item:
#                 if r == 'admin':
#                     File_Path=os.path.join(download_dir,Filename)
#                     sftp.get(f'jnp/{Filename}',localpath=File_Path)
#                     if os_name == 'Windows':
#                         subprocess.Popen(f"start Microsoftedge {File_Path}",shell=True)
#                     else:
#                         subprocess.Popen(f"open Microsoftedge {File_Path}",shell=True)
#                     break

#                 elif r == 'Standard':
#                     File_Path=os.path.join(download_dir,Filename)
#                     sftp.get(f'jnp/{Filename}',localpath=File_Path)
#                     if os_name == 'Windows':
#                         subprocess.Popen(f"start Microsoftedge {File_Path}",shell=True)
#                     else:
#                         subprocess.Popen(f"open Microsoftedge {File_Path}",shell=True)
#                     break

#                 elif r=='Rh_operator':
#                     File_Path=os.path.join(download_dir,Filename)
#                     sftp.get(f'jnp/{Filename}',localpath=File_Path)
#                     if os_name == 'Windows':
#                         subprocess.Popen(f"start Microsoftedge {File_Path}",shell=True)
#                     else:
#                         subprocess.Popen(f"open Microsoftedge {File_Path}",shell=True)
#                     break
                
#                 elif r=='Rp_operator':
#                     File_Path=os.path.join(download_dir,Filename)
#                     sftp.get(f'jnp/{Filename}',localpath=File_Path)
#                     if os_name == 'Windows':
#                         subprocess.Popen(f"start Microsoftedge {File_Path}",shell=True)
#                     else:
#                         subprocess.Popen(f"open Microsoftedge {File_Path}",shell=True)
#                     break

#                 else:
#                     print("Unknown User Type")
#                     break

# preview("count.mp4",'admin')

# Time Stamp
# Find Limit


def open_file(File_Path):
    import subprocess
    import platform
    os_name = platform.system()
    if os_name == 'Windows':
        subprocess.Popen(f"start Microsoftedge {File_Path}", shell=True)
    else:
        subprocess.Popen(f"open Microsoftedge {File_Path}", shell=True)

def preview(Filename, r):
    import os
    import pysftp as sftp
    home_dir = os.path.expanduser('~')
    download_dir = os.path.join(home_dir, 'Downloads')
    
    cnopts = sftp.CnOpts()
    cnopts.hostkeys = None
    with sftp.Connection(host='192.168.1.39', username='tester', password='password', port=2222, cnopts=cnopts) as sftp:
        dir = sftp.listdir('jnp')
        if Filename in dir:
            if r in ['admin', 'Standard', 'Rh_operator', 'Rp_operator']:
                File_Path = os.path.join(download_dir, Filename)
                sftp.get(f'jnp/{Filename}', localpath=File_Path)
                open_file(File_Path)
            else:
                print("Unknown User Type")
        else:
            print(f"{Filename} not found in jnp directory")

preview('abcd.txt','admin')