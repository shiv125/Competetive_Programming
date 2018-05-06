class PointDistance:
	def findPoint(self,xA,yA,xB,yB):
		for i in range(-100,101):
			for j in range(-100,101):
				if (i-xA)**2+(j-yA)**2>(i-xB)**2+(j-yB)**2:
					return i,j
