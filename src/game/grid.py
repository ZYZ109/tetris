"""
游戏网格类模块
管理游戏区域、处理方块碰撞检测和消行
"""
import pygame
from ..utils.logger import logger

class Grid:
    def __init__(self, width, height, block_size):
        """初始化游戏网格"""
        self.width = width
        self.height = height
        self.block_size = block_size
        self.cells = [[None] * width for _ in range(height)]
        logger.debug(f"Created grid with dimensions {width}x{height}")
        
    def check_collision(self, piece, dx=0, dy=0, test_y=None):
        """检查碰撞"""
        if test_y is None:
            test_y = piece.y
            
        for i in range(len(piece.shape)):
            for j in range(len(piece.shape[0])):
                if piece.shape[i][j]:
                    new_x = piece.x + j + dx
                    new_y = test_y + i + dy
                    
                    if (new_x < 0 or new_x >= self.width or
                        new_y >= self.height or
                        (new_y >= 0 and self.cells[new_y][new_x])):
                        return True
        return False
        
    def lock_piece(self, piece):
        """锁定方块到网格中"""
        for i in range(len(piece.shape)):
            for j in range(len(piece.shape[0])):
                if piece.shape[i][j]:
                    self.cells[piece.y + i][piece.x + j] = piece.color
        logger.debug("Piece locked into grid")
        
    def clear_lines(self):
        """清除已满的行并返回清除的行数"""
        lines_cleared = 0
        y = self.height - 1
        while y >= 0:
            if all(cell is not None for cell in self.cells[y]):
                lines_cleared += 1
                # 将上面的行都下移一行
                for y2 in range(y, 0, -1):
                    self.cells[y2] = self.cells[y2 - 1][:]
                self.cells[0] = [None] * self.width
            else:
                y -= 1
                
        if lines_cleared > 0:
            logger.info(f"Cleared {lines_cleared} lines")
        return lines_cleared
        
    def draw(self, screen):
        """绘制网格"""
        # 绘制已锁定的方块
        for y in range(self.height):
            for x in range(self.width):
                if self.cells[y][x]:
                    pygame.draw.rect(screen, self.cells[y][x],
                                   (x * self.block_size,
                                    y * self.block_size,
                                    self.block_size - 1,
                                    self.block_size - 1))