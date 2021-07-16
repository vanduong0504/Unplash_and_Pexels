import os
import requests
from pexels_api import API


class Pexels:
    def __init__(self, opt):
        self.opt = opt

    def __call__(self):
        print("Image crawler on https://www.pexels.com :3")
        api = API(self.opt.key)
        try:
            os.makedirs(self.opt.dir)
        except FileExistsError:
            pass

        index = 0
        for i in range(1, self.opt.num_page + 1):
            api.search(self.opt.q, page=i, results_per_page=self.opt.per_page)
            photos = api.get_entries()
            print(f"Page {i}: {len(photos)}")
            if not len(photos):
                break
            for photo in photos:
                img = requests.get(photo.landscape).content
                with open(f"{self.opt.dir}/{index}.jpg", "wb+") as f:
                    f.write(img)
                index += 1
