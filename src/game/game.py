"""
游戏主类模块
负责管理游戏状态、处理游戏主循环、初始化游戏环境
"""
import pygame
from src.utils.config import GameConfig
from src.utils.logger import logger
from .grid import Grid
from src.states import MenuState, PlayState, GameOverState

class TetrisGame:
    def __init__(self):
        self.block_size = GameConfig.BLOCK_SIZE
        self.grid_width = GameConfig.GRID_WIDTH
        self.grid_height = GameConfig.GRID_HEIGHT
        self.width = GameConfig.SCREEN_WIDTH
        self.height = GameConfig.SCREEN_HEIGHT
        
        logger.info("Initializing game...")
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('俄罗斯方块')
        
        self.grid = Grid(self.grid_width, self.grid_height, self.block_size)
        self.clock = pygame.time.Clock()
        
        # 初始化状态
        self.states = {
            'menu': MenuState(self),
            'playing': PlayState(self),
            'game_over': GameOverState(self)
        }
        self.current_state = self.states['menu']
        logger.info("Game initialized successfully")
        
    def change_state(self, state_name):
        logger.debug(f"Changing state to: {state_name}")
        self.current_state = self.states[state_name]
        # 如果切换到游戏状态，重置游戏
        if state_name == 'playing':
            self.grid = Grid(self.grid_width, self.grid_height, self.block_size)
            self.states['playing'].reset_game()
        
    def run(self):
        running = True
        while running:
            dt = self.clock.tick(GameConfig.FPS)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.current_state.handle_event(event)
            
            self.current_state.update(dt)
            self.current_state.draw(self.screen)
            pygame.display.flip()
        
        logger.info("Game closing...")
        pygame.quit()