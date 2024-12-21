"""
游戏测试模块
包含游戏核心功能的单元测试
"""
import unittest
from src.game.tetromino import Tetromino
from src.game.grid import Grid
from src.utils.config import GameConfig

class TestTetris(unittest.TestCase):
    def setUp(self):
        """测试初始化"""
        self.grid = Grid(GameConfig.GRID_WIDTH, 
                        GameConfig.GRID_HEIGHT, 
                        GameConfig.BLOCK_SIZE)
        self.piece = Tetromino()

    def test_tetromino_rotation(self):
        """测试方块旋转"""
        original_shape = self.piece.shape.copy()
        self.piece.rotate()
        self.assertNotEqual(original_shape, self.piece.shape)
    
    def test_grid_collision(self):
        """测试网格碰撞检测"""
        # 测试左边界碰撞
        self.piece.x = -1
        self.assertTrue(self.grid.check_collision(self.piece))
        
        # 测试右边界碰撞
        self.piece.x = GameConfig.GRID_WIDTH
        self.assertTrue(self.grid.check_collision(self.piece))
        
        # 测试底部碰撞
        self.piece.x = 0
        self.piece.y = GameConfig.GRID_HEIGHT
        self.assertTrue(self.grid.check_collision(self.piece))

    def test_line_clear(self):
        """测试消行功能"""
        # 填充一行
        for x in range(GameConfig.GRID_WIDTH):
            self.grid.cells[GameConfig.GRID_HEIGHT-1][x] = (255, 255, 255)
        
        lines_cleared = self.grid.clear_lines()
        self.assertEqual(lines_cleared, 1)