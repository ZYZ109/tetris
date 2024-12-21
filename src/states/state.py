"""
游戏状态基类模块
定义所有状态的基本接口
"""
from src.utils.logger import logger

class GameState:
    def __init__(self, game):
        self.game = game
        logger.debug(f"Initializing state: {self.__class__.__name__}")
    
    def update(self, dt):
        """更新游戏状态"""
        pass
    
    def draw(self, screen):
        """绘制界面"""
        pass
    
    def handle_event(self, event):
        """处理输入事件"""
        pass