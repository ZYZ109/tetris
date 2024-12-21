"""
字体管理模块
处理游戏中的字体加载和中文显示
包含：
- 字体初始化函数
- 获取字体的工具函数
- 中文字体支持
"""
import pygame

def init_fonts():
    """初始化字体"""
    try:
        # 尝试使用系统中文字体
        font_path = pygame.font.match_font('microsoftyaheimicrosoftyaheiui')
        if not font_path:
            # Windows 系统默认中文字体路径
            font_path = "C:/Windows/Fonts/msyh.ttc"
    except:
        # 如果没有找到中文字体，使用默认字体
        font_path = None
    return font_path

def get_font(size):
    """获取指定大小的字体"""
    font_path = init_fonts()
    try:
        return pygame.font.Font(font_path, size)
    except:
        return pygame.font.Font(None, size) 