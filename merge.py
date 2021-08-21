import os
import sys
import glob
import shutil


class merge_folder:
    def __init__(self, folders_, output_):
        print(f"List of folders to merge: {folders_}")
        print(f"Output folder: {output_}")
        self.folders = folders_
        self.output = output_
        try:
            os.makedirs(self.output)
        except FileExistsError:
            pass

    def __call__(self):
        count = 0
        for folder in self.folders:
            # path = os.path.join("data", folder)
            for image in glob.glob(folder + "/*.jpg"):
                shutil.copy(image, f"{self.output}/{count}.jpg")
                count += 1


if __name__ == '__main__':
    _, *folders, output = sys.argv
    print("Begin to merge folders :3")
    merge = merge_folder(folders, output)
    merge()
    print("Done!!")
