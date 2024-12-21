# 俄罗斯方块游戏 (Tetris)

## 项目说明
这是一个使用 Python 和 Pygame 开发的俄罗斯方块游戏，采用面向对象和状态模式设计，具有完整的游戏功能和用户界面。

## 环境要求
- Python 3.6+
- Pygame 2.0+
- 操作系统：Windows/Mac/Linux

## 项目结构
```
tetris/
├── src/                    # 源代码目录
│   ├── game/              # 游戏核心逻辑
│   │   ├── tetromino.py   # 方块类
│   │   ├── grid.py        # 游戏网格类
│   │   └── game.py        # 游戏主类
│   ├── states/            # 游戏状态
│   │   ├── state.py       # 状态基类
│   │   ├── menu_state.py  # 菜单状态
│   │   ├── play_state.py  # 游戏状态
│   │   └── game_over_state.py  # 结束状态
│   ├── ui/                # 用户界面
│   │   ├── colors.py      # 颜色定义
│   │   └── fonts.py       # 字体管理
│   └── utils/             # 工具函数
│       ├── config.py      # 配置管理
│       └── logger.py      # 日志管理
├── tests/                 # 测试代码目录
├── main.py               # 主程序入口
└── README.md             # 项目说明
```

## 功能特点
1. 基本操作：
   - 左右方向键：移动方块
   - 上方向键：旋转方块
   - 下方向键：加速下落
   - 空格键：直接落地
   - ESC键：返回主菜单

2. 游戏机制：
   - 方块自动下落
   - 方块投影预览
   - 消行计分系统
   - 等级系统
   - 游戏结束判定

3. 技术特点：
   - 状态模式管理游戏状态
   - 完整的日志系统
   - 集中的配置管理
   - 单元测试支持
   - 中文界面支持

## 开发说明
1. 安装依赖：
```bash
pip install -r requirements.txt
```

2. 运行游戏：
```bash
python main.py
```

3. 运行测试：
```bash
python -m pytest tests/
```

## 开发记录
- v1.0.0 (2024-xx-xx)
  - 完成基本游戏功能
  - 实现状态管理系统
  - 添加配置和日志系统
  - 添加单元测试