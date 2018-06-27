import os

GET_DATA_DIR = "/home/enming/s3-parallel-put"
file_count = -1

def find_file(cur_dir):
    global file_count

    path_prefix = cur_dir

    for ele in os.listdir(cur_dir):
        full_path = path_prefix + '/' + ele
        if os.path.isfile(full_path):
            file_count += 1
        if os.path.isdir(full_path):
            os.chdir(full_path)
            find_file(full_path)
            os.chdir(cur_dir)

    
    

def main():
    cur_dir = os.getcwd()
    if cur_dir != GET_DATA_DIR:
        print "Error Directory!"
        return -1

    find_file(cur_dir)

    print "Totally Get Object: %d" % (file_count)

    return 0




if __name__ == "__main__":
    main()
