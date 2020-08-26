from OpenGL.GL import *
import pygame

textureSurface = pygame.image.load('../images/original-image.png'), pygame.image.load('../images/dilation.png'), pygame.image.load('../images/result-image.png')
textureSurface = pygame.transform.rotate(textureSurface[0],180),pygame.transform.rotate(textureSurface[1],180),pygame.transform.rotate(textureSurface[2],180)
textureData = pygame.image.tostring(textureSurface[0], "RGBA"), pygame.image.tostring(textureSurface[1], "RGBA"), pygame.image.tostring(textureSurface[2], "RGBA")
width = textureSurface[0].get_width(), textureSurface[1].get_width(), textureSurface[2].get_width()
height = textureSurface[0].get_height(), textureSurface[1].get_height(), textureSurface[2].get_height()


class Texture:
    def __init__(self, texture=False,n1=0,n2=0):

        self.n1=n1
        self.n2=n2

        self.vertices = [
            [5, -n1-0.5, -1],
            [0, -n1-0.5, -1],
            [0, -n1, 0],
            [5, -n1, 0]
        ]

        self.surfaces = (
            (0, 1, 2, 3),
        )
        self.colors = (
            (105 / 255, 210 / 255, 231 / 255),
            (167 / 255, 219 / 255, 216 / 255),
            (224 / 255, 228 / 255, 204 / 255),
            (243 / 255, 134 / 255, 48 / 255)
        )
        self.vertices_texture = (
            (0.0, 0.0),
            (1.0, 0.0),
            (1.0, 1.0),
            (0.0, 1.0),
        )
        self.texture = texture
        self.center = [0, 0, 0]

    def draw(self):

        if self.texture:
            glEnable(GL_TEXTURE_2D)
            glColor3f(1, 1, 1)
            glBindTexture(GL_TEXTURE_2D, self.id)

        glBegin(GL_QUADS)

        if self.texture:
            for surface in self.surfaces:
                for x, vertex in enumerate(surface):
                    glTexCoord2fv(self.vertices_texture[x])
                    glVertex3fv(self.vertices[vertex])
        else:
            for surface in self.surfaces:
                for x, vertex in enumerate(surface):
                    glColor3fv(self.colors[x])
                    glVertex3fv(self.vertices[vertex])
        glEnd()

        if self.texture:
            glDisable(GL_TEXTURE_2D)

    def set_vertices(self,imageNumber):
        if(imageNumber==1):
            self.vertices = [[2+self.n1,-self.n2-2,0],[self.n1-2,-self.n2-2,0],[self.n1-2,0.5-self.n2-2,1],[2+self.n1,0.5-self.n2-2,1]]
        elif(imageNumber==2):
            self.vertices = [[7+self.n1,-self.n2+1-0.5,-1],[self.n1+2,-self.n2+1-0.5,-1],[self.n1+2,-self.n2+1,0],[7+self.n1,-self.n2+1,0]]

    def rotate(self):
        glPushMatrix()
        glRotatef(25, 1, 0, 0)
        glPopMatrix()

    def loadTexture(self, file):

        glEnable(GL_TEXTURE_2D)
        id = [0,1]
        self.id = glGenTextures(1)

        if file == 0:
            glBindTexture(GL_TEXTURE_2D, self.id)
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width[file], height[file], 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData[file])
        if file == 1:
            glBindTexture(GL_TEXTURE_2D, self.id)
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width[file], height[file], 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData[file])        
        if file == 2:
            glBindTexture(GL_TEXTURE_2D, self.id)
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width[file], height[file], 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData[file])        

        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

        glDisable(GL_TEXTURE_2D)