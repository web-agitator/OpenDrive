from gclasses import *

def parse_arguments():
    parser = argparse.ArgumentParser()
    s = Sanitize()
    parser.add_argument("-l", "--listening", action="store_true",help="File listenig")
    parser.add_argument("-p","--path",type=s.check_path, help= "Enter the path of the folder to backup ")
    parser.add_argument("-m", "--mail",type=s.check_mail, help="Receive an email when the backup is complete")
    args = parser.parse_args()
    return parser.parse_args()

def main():
    args = parse_arguments()
    g = Gopen()
    drive = g.auth()
    if args.listening:
        drive = g.auth()
        file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
        for file1 in file_list:
            print('title: %s, id: %s' % (file1['title'], file1['id']))
            if  args.path:
                title = str(datetime.datetime.now())
                folderid = g.mkdr(title,drive)
                path =(args.path)
                files = []
                for root, dirs, files in os.walk(path, topdown=False):
                    for name in files:
                        file = (os.path.join(root, name))
                        print(file)
                        g.uploadfile(drive,file,folderid)
                        print ("All files have been uploaded")
                        if args.mail:
                            email = (args.mail)
                            a.push(to_addr_list = [email])
                            print("Email correctly sent")
                        else:
                            print("Error")
if __name__ == '__main__':
    main()
