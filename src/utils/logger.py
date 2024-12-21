"""
日志工具模块
提供统一的日志记录功能
"""
import logging

def setup_logger():
    """初始化日志配置"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger(__name__)

logger = setup_logger() 