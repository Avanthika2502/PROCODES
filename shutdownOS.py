import os
shutdown = input("Do you want to shutdown? ( yes / no ): ")
if shutdown == 'no':
    exit()
else :
    os: system("shutdown /s /t 1")
