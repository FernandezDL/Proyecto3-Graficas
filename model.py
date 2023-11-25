from OpenGL.GL import * 
import glm
from numpy import array, float32
import pygame
from obj import Obj

class Model(object):
    def __init__(self, filename, translate=(0,0,0), rotation=(0,0,0), scale=(1,1,1)):
        model = Obj(filename)
        
        data = []
        untransformedVerts = []
        texCoords = []
        normals = []

        for face in model.faces:
            vertCount = len(face)
            v0 = model.vertices[face[0][0]-1]
            v1 = model.vertices[face[1][0]-1]
            v2 = model.vertices[face[2][0]-1]
            
            if vertCount == 4:
                v3 = model.vertices[face[3][0]-1]
                
            vt0 = model.texcoords[face[0][1]-1]
            vt1 = model.texcoords[face[1][1]-1]
            vt2 = model.texcoords[face[2][1]-1]
            
            if vertCount == 4:
                vt3 = model.texcoords[face[3][1]-1]

            vn0 = model.normals[face[0][2]-1]
            vn1 = model.normals[face[1][2]-1]
            vn2 = model.normals[face[2][2]-1]

            if vertCount == 4:
                vn3 = model.normals[face[3][2]-1]
                
            untransformedVerts.append(v0)
            untransformedVerts.append(v1)
            untransformedVerts.append(v2)
            if vertCount == 4:
                untransformedVerts.append(v0)
                untransformedVerts.append(v2)
                untransformedVerts.append(v3)
            
            texCoords.append([vt0[0],vt0[1]])
            texCoords.append([vt1[0],vt1[1]])
            texCoords.append([vt2[0],vt2[1]])

            if vertCount==4:
                texCoords.append([vt0[0],vt0[1]])
                texCoords.append([vt2[0],vt2[1]])
                texCoords.append([vt3[0],vt3[1]])

            normals.append(vn0)
            normals.append(vn1)
            normals.append(vn2)

            if vertCount == 4:
                normals.append(vn0)
                normals.append(vn2)
                normals.append(vn3)
        
        for i in range(0,len(untransformedVerts),3):
            for item in untransformedVerts[i]:
                data.append(item)
            for item in texCoords[i]:
                data.append(item)
            for item in normals[i]:
                data.append(item) 
            
            for item in untransformedVerts[i+1]:
                data.append(item)
            for item in texCoords[i+1]:
                data.append(item)
            for item in normals[i+1]:
                data.append(item) 
            
            for item in untransformedVerts[i+2]:
                data.append(item)
            for item in texCoords[i+2]:
                data.append(item)
            for item in normals[i+2]:
                data.append(item) 

        self.vertBuffer = array(data, dtype = float32)
        self.VBO = glGenBuffers(1)
        self.VAO = glGenVertexArrays(1)
        
        self.translate = glm.vec3(translate)
        self.rotation = glm.vec3(rotation)
        self.scale = glm.vec3(scale)
        
    def loadTexture(self, textureName):
        self.textureSurface = pygame.image.load(textureName)
        self.textureData    = pygame.image.tostring(self.textureSurface, "RGB", True)
        self.textureBuffer  = glGenTextures(1)

    def getModelMatrix(self):
        identity = glm.mat4(1)
        
        translateMat = glm.translate(identity, self.translate)
        
        #rotation
        pitch = glm.rotate(identity, glm.radians(self.rotation.x), glm.vec3(1,0,0))
        yaw =   glm.rotate(identity, glm.radians(self.rotation.y), glm.vec3(0,1,0))
        roll =  glm.rotate(identity, glm.radians(self.rotation.z), glm.vec3(0,0,1))
        rotationMat = pitch * yaw * roll
        
        scaleMat = glm.scale(identity, self.scale)
        
        return translateMat * rotationMat * scaleMat
    
    def render(self):
        
        glBindBuffer(GL_ARRAY_BUFFER, self.VBO)
        glBindVertexArray(self.VAO)

        glBufferData( GL_ARRAY_BUFFER,
                     self.vertBuffer.nbytes,
                     self.vertBuffer,
                     GL_STATIC_DRAW)
        # atributo de posiciones
        glVertexAttribPointer(0,
                              3,
                              GL_FLOAT,
                              GL_FALSE,
                              4 * 8,
                              ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)
        
        # atributos de coordenadas de textura
        glVertexAttribPointer(1,
                              2,
                              GL_FLOAT,
                              GL_FALSE,
                              4 * 8,
                              ctypes.c_void_p(4*3))
    
        glEnableVertexAttribArray(1)

        # atributos de normales
        glVertexAttribPointer(2,
                              3,
                              GL_FLOAT,
                              GL_FALSE,
                              4 * 8,
                              ctypes.c_void_p(4*5))
    
        glEnableVertexAttribArray(2)

        # Activar textura
        glActiveTexture( GL_TEXTURE0 )
        glBindTexture( GL_TEXTURE_2D, self.textureBuffer)
        glTexImage2D(GL_TEXTURE_2D,
                    0,
                    GL_RGB,
                    self.textureSurface.get_width(),
                    self.textureSurface.get_height(),
                    0,
                    GL_RGB,
                    GL_UNSIGNED_BYTE,
                    self.textureData)
        glGenerateTextureMipmap(self.textureBuffer) 

        glDrawArrays(GL_TRIANGLES, 0, int(len(self.vertBuffer) / 8))