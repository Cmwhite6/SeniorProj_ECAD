from vpython import *





# Specify the file as a file name.

# See http://en.wikipedia.org/wiki/STL_(file_format)
# Text .stl file starts with a header that begins with the word "solid".
# Binary .stl file starts with a header that should NOT begin with the word "solid",
# but this rule seems not always to be obeyed.


def stl_to_triangles(fileinfo): # specify file
    # Accept a file name or a file descriptor; make sure mode is 'rb' (read binary)
    fd = open(fileinfo, mode='rb')
    text = fd.read()
    tris = [] # list of triangles to compound
    if False: # prevent executing code for binary file
        pass
    # The following code for binary files must be updated:
#    if chr(0) in text: # if binary file
#        text = text[84:]
#        L = len(text)
#        N = 2*(L//25) # 25/2 floats per point: 4*3 float32's + 1 uint16
#        triPos = []
#        triNor = []
#        n = i = 0
#        while n < L:
#            triNor[i] = fromstring(text[n:n+12], float32)
#            triPos[i] = fromstring(text[n+12:n+24], float32)
#            triPos[i+1] = fromstring(text[n+24:n+36], float32)
#            triPos[i+2] = fromstring(text[n+36:n+48], float32)
#            colors = fromstring(text[n+48:n+50], uint16)
#            if colors != 0:
#                print '%x' % colors
#            if triNor[i].any():
#                triNor[i] = triNor[i+1] = triNor[i+2] = norm(vector(triNor[i]))
#            else:
#                triNor[i] = triNor[i+1] = triNor[i+2] = \
#                    norm(cross(triPos[i+1]-triPos[i],triPos[i+2]-triPos[i]))
#            n += 50
#            i += 3
    else:
        fd.seek(0)
        fList = fd.readlines()
    
        # Decompose list into vertex positions and normals
        vs = []
        for line in fList:
            FileLine = line.split( )
            if FileLine[0] == b'facet':
                N = vec(float(FileLine[2]), float(FileLine[3]), float(FileLine[4]))
            elif FileLine[0] == b'vertex':
                vs.append( vertex(pos=vec(float(FileLine[1]), float(FileLine[2]), float(FileLine[3])), normal=N, color=color.white) )
                if len(vs) == 3:
                    tris.append(triangle(vs=vs))
                    vs = []
                    
    return compound(tris)

if __name__ == '__main__':
    man = stl_to_triangles('STLbot.stl')
    man.pos = vec(-200,0,0)
    man.color = color.cyan
    part = stl_to_triangles('Part1.stl')
    part.size *= 200
    part.pos = vec(250,0,0)
    part.color = color.orange