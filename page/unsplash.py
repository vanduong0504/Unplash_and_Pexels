import os
import requests


class Unsplash:
    def __init__(self, opt):
        self.opt = opt

    def __call__(self):
        print("Image crawler on https://api.unsplash.com :3")
        try:
            os.makedirs(self.opt.dir)
        except FileExistsError:
            pass

        index = 0
        for i in range(1, self.opt.num_page + 1):
            r = requests.get(f"https://api.unsplash.com/search/photos?client_id={self.opt.key}"
                             f"&query={self.opt.q}&page={i}&per_page={self.opt.per_page}")
            photos = r.json()['results']
            print(f"Page {i}: {len(photos)}")
            if not len(photos):
                break

            for photo in photos:
                img = requests.get(photo['urls']['regular']).content
                with open(f"{self.opt.dir}/{index}.jpg", "wb+") as f:
                    f.write(img)
                index += 1
