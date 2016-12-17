import scipy.ndimage as ndimage
import scipy.misc as misc
import matplotlib.pyplot as plt
import pylab
import scipy
import numpy 
from scipy import ndimage



def process_object(image, sd):
    objects = misc.imread('objects.png')
    obj_fil = ndimage.gaussian_filter(objects, sd)
    obj_fil = obj_fil[:,:,0]

    thres = obj_fil > obj_fil.mean()
    labeled, n_objects = ndimage.label(thres) 

    count=  "Number of objects is %d " % n_objects
    print count

    c_mass= scipy.ndimage.measurements.center_of_mass(thres, labeled, range(1,n_objects+1))

    for row in c_mass:
        print row
    pylab.imshow(labeled)
    pylab.show()

    return 

def process_circles(image, sd):
    circles = misc.imread('circles.png')
    
    circles = ndimage.gaussian_filter(circles, sd)
    std = numpy.std(circles)
    thres = circles > circles.mean()+ 50
    labeled, n_objects = ndimage.label(thres) 
    count =  "Number of objects is %d " % n_objects
    print count
    c_mass= scipy.ndimage.measurements.center_of_mass(thres, labeled, range(1,n_objects+1))

    for row in c_mass:
        print row
    pylab.imshow(labeled)
    pylab.show()
    return


def process_peppers(image, sd):
    peppers = misc.imread('peppers.png')
    peppers = ndimage.gaussian_filter(peppers, sd)
    peppers = peppers[:,:,0]

    thres = peppers > peppers.mean()
    labeled, n_objects = ndimage.label(thres) 
    count =  "Number of objects is %d " % n_objects
    print count
    c_mass= scipy.ndimage.measurements.center_of_mass(thres, labeled, range(1,n_objects+1))

    for row in c_mass:
        print row
    pylab.imshow(labeled)
    pylab.show()
    return

if __name__ == '__main__':
    process_object('object.png',3)
    process_circles('circles.png', 10)
    process_peppers('peppers.png',6)
    
