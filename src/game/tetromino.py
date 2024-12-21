"""
俄罗斯方块类模块
定义方块的形状、颜色、移动和旋转等基本操作
"""
import random
import pygame
from ..ui.colors import *
from ..utils.logger import logger

# 定义方块形状
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]],  # J
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]]   # Z
]

# 定义方块颜色
SHAPE_COLORS = [CYAN, YELLOW, MAGENTA, BLUE, GREEN, RED, RED]

class Tetromino:
    def __init__(self, shape_idx=None):
        """初始化方块"""
        if shape_idx is None:
            shape_idx = random.randint(0, len(SHAPES) - 1)
        self.shape = [row[:] for row in SHAPES[shape_idx]]
        self.color = SHAPE_COLORS[shape_idx]
        self.x = 0
        self.y = 0
        logger.debug(f"Created new tetromino with shape index {shape_idx}")
        
    def rotate(self):
        """旋转方块"""
        # 转置矩阵
        self.shape = [[self.shape[y][x] for y in range(len(self.shape))]
                     for x in range(len(self.shape[0]) - 1, -1, -1)]
        
    def try_rotate(self, grid):
        """尝试旋转，如果不能旋转则返回原位置"""
        original_shape = [row[:] for row in self.shape]
        self.rotate()
        if grid.check_collision(self):
            self.shape = original_shape
            return False
        return True
        
    def draw(self, screen, block_size):
        """绘制方块"""
        for i in range(len(self.shape)):
            for j in range(len(self.shape[0])):
                if self.shape[i][j]:
                    pygame.draw.rect(screen, self.color,
                                   ((self.x + j) * block_size,
                                    (self.y + i) * block_size,
                                    block_size - 1,
                                    block_size - 1))
                    
    def draw_ghost(self, screen, grid, block_size):
        """绘制方块的投影"""
        ghost_y = self.y
        while not grid.check_collision(self, 0, 1, ghost_y):
            ghost_y += 1
            
        ghost_color = (self.color[0] // 2, self.color[1] // 2, self.color[2] // 2)
        for i in range(len(self.shape)):
            for j in range(len(self.shape[0])):
                if self.shape[i][j]:
                    pygame.draw.rect(screen, ghost_color,
                                   ((self.x + j) * block_size,
                                    (ghost_y + i) * block_size,
                                    block_size - 1,
                                    block_size - 1))