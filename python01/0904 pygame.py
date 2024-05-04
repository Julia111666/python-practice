# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 00:31:07 2021

@author: zuhan
"""



2pygame.init()

3fpsClock = pygame.time.Clock()


5playSurface = pygame.display.set_mode((600,460))
6pygame.display.set_caption('Snake Game')



8redColour = pygame.Color(255,0,0)

9blackColour = pygame.Color(0,0,0)

10whiteColour = pygame.Color(255,255,255)

11greyColour = pygame.Color(150,150,150)

遊戲結束介面，我們會顯示“Game Over!”和該局遊戲所得分數，相關程式碼如下：



2defgameOver(playSurface,score):

3gameOverFont = pygame.font.SysFont('arial.ttf',54) #遊戲結束字型和大小

4gameOverSurf = gameOverFont.render('Game Over!', True, greyColour) #遊戲結束內容顯示

5gameOverRect = gameOverSurf.get_rect()

6gameOverRect.midtop = (300, 10) #顯示位置

7playSurface.blit(gameOverSurf, gameOverRect)

8scoreFont = pygame.font.SysFont('arial.ttf',54) #得分情況顯示

9scoreSurf = scoreFont.render('Score:'+str(score), True, greyColour)

10scoreRect = scoreSurf.get_rect()

11scoreRect.midtop = (300, 50)

12playSurface.blit(scoreSurf, scoreRect)

13pygame.display.flip() #重新整理顯示介面

14time.sleep(5) #休眠五秒鐘自動退出介面

15pygame.quit()

16sys.exit()