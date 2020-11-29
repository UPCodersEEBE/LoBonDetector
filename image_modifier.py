from PIL import Image 

from google_annotate import locate_objects_path
from shape_analyzer import check_all_squares, estanteries

image_paths = []


# for filename in os.listdir("resources"):
#     if filename.endswith(".jpg"):
#         image_paths.append(os.path.join("resources",filename))

products_positions = [
            [(0,870,60,990), (30,830,120,920), (80,760,170,860), (150,690,230,780), (200,580,310,710),
            (280,510,390,630), (366,459,467,546),(426,424,504,497), (477,372,570,457), (542,320,623,404),
            (606,277,685,348), (659,241,741,308), (715,193,821,266), (797,150,874,221), (863,105,946,175)],

            [(18,989,85,1075), (61,951,111,1032), (76,917,144,1000), (106,888,167,959), (134,828,218,908),
            (198,775,273,859), (245,716,316,801), (288,668,360,751), (329,622,414,704), (379,572,462,651),
            (430,514,536,602), (505,453,583,542), (555,420,634,498), (601,373,677,451), (653,348,723,427),
            (686,311,776,378), (752,261,832,340), (818,238,867,292), (842,191,934,258)],

            [(115,976,203,1073), (183,927,253,1014), (224,818,341,943), (314,740,416,852), (392,687,469,772),
            (434,651,500,726), (465,588,571,678), (550,537,616,614), (604,477,692,558), (666,432,724,509),
            (710,398,792,471), (764,347,844,411), (815,308,883,375), (863,274,940,325)],

            [(195,1034,253,1081), (231,1002,285,1055), (268,956,320,1015), (299,917,364,978), (341,859,409,927),
            (386,810,454,883), (429,733,529,827), (514,663,588,751), (571,629,626,691), (606,590,672,648),
            (644,538,726,602), (706,480,788,548), (767,420,843,487), (825,370,905,438), (881,336,938,381)],

            [(316,1008,405,1079), (355,953,458,1057), (409,867,510,1005), (459,851,551,943), (496,777,622,901),
            (564,741,654,830), (593,690,705,777), (646,653,734,731), (679,608,781,689), (724,558,834,650), 
            (778,471,911,575), (863,404,979,485)]
]


def get_dims(path):
    width, height = Image.open(path).size
    dims=(width,height)
    return dims

def get_product_slots(path):
    img = Image.open(path)
    for i in range(len(products_positions)):
        for j in range(len(products_positions[i])):
            img.crop(products_positions[i][j]).save('product_slots/%02dx%02d.jpg' % (i,j))

def filter_objects(object_name):
    embotits=['Packaged goods','Food']
    accepted_object=True
    for item in embotits:
        if item in object_name:
            accepted_object=False
    return accepted_object

def map_object_to_pixels(objects, dims):
    ob={}
    i=0
    for object_ in objects:
        if filter_objects(object_.name):
            vertices=[]
            for vertex in object_.bounding_poly.normalized_vertices:
                vertices.append((vertex.x*dims[0],vertex.y*dims[1]))
            ob[object_.name+str(i)]=vertices
            i+=1
    return ob

def analyze_image(path):
    objects=locate_objects_path(path)
    dims=get_dims(path)
    objects_dict=map_object_to_pixels(objects,dims)
    matrix=products_positions
    a,b =check_all_squares(matrix,objects_dict)
    response=estanteries(matrix,a)
    return response