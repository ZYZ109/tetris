"""
游戏结束状态模块
处理游戏结束时的显示和交互
"""
import pygame
from .state import GameState
from ..ui.colors import *
from ..ui.fonts import get_font
from ..utils.config import GameConfig
from ..utils.logger import logger

class GameOverState(GameState):
    def __init__(self, game):
        super().__init__(game)
        self.font_big = get_font(GameConfig.FONT_BIG)
        self.font_small = get_font(GameConfig.FONT_MEDIUM)
        self.score = 0
        logger.info("Game over state initialized")
        
    def draw(self, screen):
        screen.fill(BLACK)
        
        # 绘制游戏结束文本
        game_over_text = self.font_big.render("游戏结束!", True, WHITE)
        text_rect = game_over_text.get_rect(center=(self.game.width // 2, self.game.height // 3))
        screen.blit(game_over_text, text_rect)
        
        # 绘制最终分数
        score_text = self.font_small.render(f"最终得分: {self.score}", True, WHITE)
        score_rect = score_text.get_rect(center=(self.game.width // 2, self.game.height // 2))
        screen.blit(score_text, score_rect)
        
        # 绘制重新开始提示
        restart_text = self.font_small.render("按空格键重新开始", True, WHITE)
        restart_rect = restart_text.get_rect(center=(self.game.width // 2, self.game.height * 2 // 3))
        screen.blit(restart_text, restart_rect)
    
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                logger.info(f"Game over - Final score: {self.score}")
                self.game.change_state('playing')