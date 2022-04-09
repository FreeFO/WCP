import os
import zipfile


def compress_dir(src_path="./", des_path="./default.zip"):
    if os.path.exists(des_path):
        print("{} is exists, update".format(des_path))
        os.remove(des_path)
    z = zipfile.ZipFile(des_path, 'w', zipfile.ZIP_DEFLATED)
    for dir_path, dir_names, file_names in os.walk(src_path):
        # print("dir_path: {}, dir_names: {}, file_names: {}".format(dir_path, dir_names, file_names))
        fpath = dir_path.replace(src_path, '')
        fpath = fpath and fpath + os.sep or ''
        for filename in file_names:
            z.write(os.path.join(dir_path, filename), fpath + filename)
            print('add file [{}] to zip'.format(filename))
    z.close()
