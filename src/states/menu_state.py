"""
游戏菜单状态模块
处理游戏开始菜单的显示和交互
"""
import pygame
from .state import GameState
from ..ui.colors import *
from ..ui.fonts import get_font
from ..utils.config import GameConfig
from ..utils.logger import logger

class MenuState(GameState):
    def __init__(self, game):
        super().__init__(game)
        self.font_big = get_font(GameConfig.FONT_BIG)
        self.font_small = get_font(GameConfig.FONT_SMALL)
        logger.info("Menu state initialized")
    
    def draw(self, screen):
        screen.fill(BLACK)
        
        # 绘制标题
        title = self.font_big.render("俄罗斯方块", True, WHITE)
        title_rect = title.get_rect(center=(self.game.width // 2, self.game.height // 3))
        screen.blit(title, title_rect)
        
        # 绘制提示
        start_text = self.font_small.render("按空格键开始游戏", True, WHITE)
        start_rect = start_text.get_rect(center=(self.game.width // 2, self.game.height * 3 // 5))
        screen.blit(start_text, start_rect)
        
        # 绘制操作说明
        controls = [
            "方向键左右：移动方块",
            "方向键上：旋转方块",
            "方向键下：加速下落",
            "空格键：直接落地",
            "ESC键：返回主菜单"
        ]
        
        for i, text in enumerate(controls):
            control_text = self.font_small.render(text, True, WHITE)
            rect = control_text.get_rect(
                center=(self.game.width // 2, self.game.height * 2 // 3 + i * 35)
            )
            screen.blit(control_text, rect)
    
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                logger.info("Starting new game from menu")
                self.game.change_state('playing')