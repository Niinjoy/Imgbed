# from skimage import io
# img_url = "http://cube.rider.biz/visualcube.php?fmt=svg&case=URU'R'&stage=f2l&bg=t&view=trans&cc=grey&co=40&size=512"
# image = io.imread(img_url)
# # io.imshow(image)
# # io.show()
# io.imsave('test.svg',image)

import urllib.request
urllib.request.urlretrieve("http://cube.rider.biz/visualcube.php?fmt=svg&case=URU'R'&stage=f2l&bg=t&view=trans&cc=grey&co=40&size=512", "cubeImg/test2.svg")