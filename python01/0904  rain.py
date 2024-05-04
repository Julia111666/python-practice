# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 00:35:54 2021

@author: 
"""

import random
import pygame
PANEL_width = 1600
PANEL_highly = 1000
FONT_PX = 15
pygame.init()
# 建立一個可是視窗
winSur = pygame.display.set_mode((PANEL_width, PANEL_highly))
font = pygame.font.SysFont("123.ttf", 25)
bg_suface = pygame.Surface((PANEL_width, PANEL_highly), flags=pygame.SRCALPHA)
pygame.Surface.convert(bg_suface)
bg_suface.fill(pygame.Color(0, 0, 0, 28))
winSur.fill((0, 0, 0))
# 數位版
# texts = [font.render(str(i), True, (0, 255, 0)) for i in range(10)]
#texts = [
  #font.render(str(letter[i]), True, (0, 255, 0)) for i in range(26)
#]
# 字母版
letter = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c',
     'v', 'b', 'n', 'm']
texts = [
  font.render(str(letter[i]), True, (0, 255, 0)) for i in range(26)
]
texts = [font.render(str(i), True, (0, 255, 0)) for i in range(2)]
# 按螢幕的寬頻計算可以在畫板上放幾列座標並生成一個列表
column = int(PANEL_width / FONT_PX)
drops = [0 for i in range(column)]
while True:
  # 從佇列中獲取事件
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      exit()
    elif event.type == pygame.KEYDOWN:
      chang = pygame.key.get_pressed()
      if (chang[32]):
        exit()
  # 將暫停一段給定的毫秒數
  pygame.time.delay(40)
  # 重新編輯影象第二個引數是坐上角座標
  winSur.blit(bg_suface, (0, 0))
  for i in range(len(drops)):
    text = random.choice(texts)
    # 重新編輯每個座標點的影象
    winSur.blit(text, (i * FONT_PX, drops[i] * FONT_PX))
    drops[i] += 1
    if drops[i] * 10 > PANEL_highly or random.random() > 0.95:
      drops[i] = 0
  pygame.display.flip()
  