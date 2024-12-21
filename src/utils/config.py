"""
游戏配置模块
存储游戏的常量和配置项
"""
class GameConfig:
    # 窗口设置
    BLOCK_SIZE = 30
    GRID_WIDTH = 10
    GRID_HEIGHT = 20
    SCREEN_WIDTH = BLOCK_SIZE * (GRID_WIDTH + 8)
    SCREEN_HEIGHT = BLOCK_SIZE * GRID_HEIGHT

    # 游戏设置
    FPS = 60
    FALL_SPEED = 500
    
    # 字体设置
    FONT_BIG = 48
    FONT_MEDIUM = 36
    FONT_SMALL = 28 