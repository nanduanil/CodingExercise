# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 22:38:31 2017
Change the input and the output folder

Usage:
Export files from the camera using playmemories
Export the files into a folder and map it to 'inputFolder'
Map the output folder to 'outputFolder'
Run!!

Working:
Checks the first jpg file in a folder.
Creates the new folder name based on this files date in exif data.
Copies all the files in this folder to the newly created folder.

If not image files are present in a folder, then the contents of this folder are marked for manual review.
"""
import exifread,os,time,shutil,glob,datetime

def log(logFolder,logString):
    now = datetime.datetime.now()
    file = open(logFolder+"\\" + "sonyPicImport_" + str(now.date())+".txt",'a+')
    logString = str(now.time()) + "  - " + logString + "\n"
    file.writelines(logString) 
    file.close()
    
inputFolder = "C:\\Users\\nandu\\Desktop\\Pictures\\sonyPicImport\\sony_pics_new"
outputFolder = "C:\\Users\\nandu\\Desktop\\Pictures\\sonyPicImport\\sony_modified"
statusFolder = "C:\\Users\\nandu\\Desktop\\Pictures\\sonyPicImport"
now = datetime.datetime.now()
outputCSVPath = statusFolder + "\\outputStatus_" + str(now.date())+".csv"
csvOut = {}

if(not os.path.isdir(inputFolder)):
    print('Input folder is not present', inputFolder)
    exit()
if(not os.path.isdir(outputFolder)):
    os.makedirs(outputFolder)
    
dirlist = os.listdir(inputFolder)

for curDir in dirlist:
    curDirPath = inputFolder + "\\" + curDir 
    listJPG_Files = glob.glob(curDirPath + "\\*.jpg")
    newFolder = ''
    try:
            
        if(len(listJPG_Files) > 0):
            samplePhoto = listJPG_Files[0]
            #samplePhoto = "C:\\Users\\nandu\\Desktop\\sony pics new\\9-3-2017\\DSC02655.JPG"    
            # Open image file for reading (binary mode)
            f = open(samplePhoto, 'rb')
            
            # Return Exif tags
            photoTags = exifread.process_file(f)
            exifImageDate = photoTags["EXIF DateTimeOriginal"]
            
            imageDate = time.strptime(str(exifImageDate),"%Y:%m:%d %H:%M:%S")
            newFolder = str(imageDate.tm_year)+"-"+str(imageDate.tm_mon).zfill(2)+"-"+str(imageDate.tm_mday).zfill(2)
            logEntry = curDir + ": "+newFolder
            csvStatus = "Done, "
        else:
            newFolder = "manual_" + curDir
            logEntry = curDir + ": no jpeg for reference"
            csvStatus = "Manual,No jpeg for reference"
               
        newFolderPath = outputFolder + "\\" + newFolder
        #if(not os.path.isdir(newFolderPath)):
        #    os.makedirs(newFolderPath)
        log(statusFolder,logEntry) 
        shutil.copytree(curDirPath,newFolderPath)
    except FileExistsError as fe:
        logEntry = curDir + ": "+str(fe)
        log(outputFolder,logEntry) 
        csvStatus = "Error," +str(fe)

    except (Exception,WindowsError) as e:
        logEntry = curDir + ": "+str(e)
        log(statusFolder,logEntry) 
        csvStatus = "Error,"+str(e)
    
    csvOut[newFolder] = curDir.ljust(10,' ') +","+newFolder+"," + csvStatus
    
    
fileCSV = open(outputCSVPath,'a+')
for line in sorted(csvOut):
  fileCSV.write("%s\n" % csvOut[line])        
fileCSV.close()     
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            