"""
俄罗斯方块游戏主程序入口
创建游戏实例并启动游戏循环
"""
from src.game.game import TetrisGame
from src.utils.logger import logger

def main():
    logger.info("Starting Tetris game...")
    game = TetrisGame()
    game.run()

if __name__ == "__main__":
    main() 