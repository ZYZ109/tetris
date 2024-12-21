"""
游戏运行状态模块
处理主要的游戏逻辑，包括：
- 方块移动和旋转
- 游戏分数计算
- 等级系统
- 游戏界面绘制
"""
import pygame
from .state import GameState
from ..ui.colors import *
from ..ui.fonts import get_font
from ..game.tetromino import Tetromino
from ..game.grid import Grid
from ..utils.config import GameConfig
from ..utils.logger import logger

class PlayState(GameState):
    def __init__(self, game):
        super().__init__(game)
        logger.info("Initializing play state")
        self.reset_game()
        
    def reset_game(self):
        """重置游戏状态"""
        logger.debug("Resetting game state")
        self.current_piece = Tetromino()
        self.next_piece = Tetromino()
        self.current_piece.x = self.game.grid_width // 2 - len(self.current_piece.shape[0]) // 2
        self.current_piece.y = 0
        self.fall_time = 0
        self.fall_speed = GameConfig.FALL_SPEED
        self.score = 0
        self.level = 1
        self.lines_cleared = 0
        self.game.grid = Grid(self.game.grid_width, self.game.grid_height, self.game.block_size)
        
    def update(self, dt):
        self.fall_time += dt
        
        if self.fall_time >= self.fall_speed:
            if not self.game.grid.check_collision(self.current_piece, 0, 1):
                self.current_piece.y += 1
            else:
                self.game.grid.lock_piece(self.current_piece)
                lines = self.game.grid.clear_lines()
                if lines > 0:
                    self.handle_line_clear(lines)
                
                self.current_piece = self.next_piece
                self.next_piece = Tetromino()
                self.current_piece.x = self.game.grid_width // 2 - len(self.current_piece.shape[0]) // 2
                
                if self.game.grid.check_collision(self.current_piece):
                    logger.info(f"Game Over! Final score: {self.score}")
                    self.game.states['game_over'].score = self.score
                    self.game.change_state('game_over')
            self.fall_time = 0
            
    def handle_line_clear(self, lines):
        """处理消行得分"""
        self.lines_cleared += lines
        # 计算得分：一次消除的行数越多，单行得分越高
        line_scores = [100, 300, 500, 800]  # 1-4行的得分
        self.score += line_scores[lines-1] * self.level
        
        # 每消除10行升一级
        if self.lines_cleared >= self.level * 10:
            self.level_up()
            
        logger.info(f"Cleared {lines} lines. Score: {self.score}, Level: {self.level}")
            
    def level_up(self):
        """升级处理"""
        self.level += 1
        # 提高下落速度
        self.fall_speed = max(GameConfig.FALL_SPEED - (self.level - 1) * 50, 100)
        logger.info(f"Level up! New level: {self.level}")
            
    def draw(self, screen):
        screen.fill(BLACK)
        
        # 绘制游戏区域边框
        pygame.draw.rect(screen, WHITE, 
                        (0, 0, self.game.block_size * self.game.grid_width, 
                         self.game.block_size * self.game.grid_height), 1)
        
        # 绘制网格和当前方块
        self.game.grid.draw(screen)
        self.current_piece.draw_ghost(screen, self.game.grid, self.game.block_size)
        self.current_piece.draw(screen, self.game.block_size)
        
        # 绘制下一个方块预览
        self.draw_next_piece(screen)
        
        # 绘制分数
        self.draw_score(screen)
        
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if not self.game.grid.check_collision(self.current_piece, -1, 0):
                    self.current_piece.x -= 1
            elif event.key == pygame.K_RIGHT:
                if not self.game.grid.check_collision(self.current_piece, 1, 0):
                    self.current_piece.x += 1
            elif event.key == pygame.K_DOWN:
                if not self.game.grid.check_collision(self.current_piece, 0, 1):
                    self.current_piece.y += 1
            elif event.key == pygame.K_UP:
                self.current_piece.try_rotate(self.game.grid)
            elif event.key == pygame.K_SPACE:
                self.hard_drop()
            elif event.key == pygame.K_ESCAPE:
                logger.info("Returning to menu")
                self.game.change_state('menu')
                
    def hard_drop(self):
        """直接落地"""
        drop_distance = 0
        while not self.game.grid.check_collision(self.current_piece, 0, 1):
            self.current_piece.y += 1
            drop_distance += 1
            
        self.game.grid.lock_piece(self.current_piece)
        lines = self.game.grid.clear_lines()
        if lines > 0:
            self.handle_line_clear(lines)
            
        self.current_piece = self.next_piece
        self.next_piece = Tetromino()
        self.current_piece.x = self.game.grid_width // 2 - len(self.current_piece.shape[0]) // 2
        
        if self.game.grid.check_collision(self.current_piece):
            logger.info(f"Game Over! Final score: {self.score}")
            self.game.states['game_over'].score = self.score
            self.game.change_state('game_over')
            
    def draw_next_piece(self, screen):
        """绘制下一个方块预览"""
        preview_x = self.game.block_size * (self.game.grid_width + 1)
        preview_y = self.game.block_size * 3
        
        # 绘制预览区域标题
        font = get_font(GameConfig.FONT_SMALL)
        text = font.render("下一个:", True, WHITE)
        text_rect = text.get_rect(x=preview_x, y=self.game.block_size * 1.5)
        screen.blit(text, text_rect)
        
        # 绘制下一个方块
        for i in range(len(self.next_piece.shape)):
            for j in range(len(self.next_piece.shape[0])):
                if self.next_piece.shape[i][j]:
                    pygame.draw.rect(screen, self.next_piece.color,
                                   (preview_x + self.game.block_size * j,
                                    preview_y + self.game.block_size * i,
                                    self.game.block_size - 1,
                                    self.game.block_size - 1))

    def draw_score(self, screen):
        """绘制分数和等级"""
        font = get_font(GameConfig.FONT_SMALL)
        
        score_text = font.render(f"分数: {self.score}", True, WHITE)
        screen.blit(score_text, (self.game.block_size * (self.game.grid_width + 1),
                                self.game.block_size * 7))
        
        level_text = font.render(f"等级: {self.level}", True, WHITE)
        screen.blit(level_text, (self.game.block_size * (self.game.grid_width + 1),
                                self.game.block_size * 9))